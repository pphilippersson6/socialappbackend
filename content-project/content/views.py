from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            email=serializer.validated_data['email']
            password=serializer.validated_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            return Response({'success':'true', 'message':'user created successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            users=User.objects.get(username=username)
        refresh = RefreshToken.for_user(user)
        return Response({
            'Success': True,
            'Code': 200,
            'Details': {
                "user_id":users.id,
                'email': users.email,
                'username': users.username,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=HTTP_200_OK)
    else:
        # Authentication failed
        return Response({
            'Success': False,
            'Code': 401,
            'message': 'Invalid email or password.'
        }, status=HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            title=serializer.validated_data['title']
            content=serializer.validated_data['content']
            user=request.user
            print(user)
            post = Post.objects.create(title=title, content=content, user=user)
            return Response({'success':'true', 'message':'post created successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# like post
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request):
    if request.method == 'POST':
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            user=request.user
            post=serializer.validated_data['post']
            like = Like.objects.create(user=user, post=post)
            return Response({'success':'true', 'message':'post liked successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# comment post
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_post(request):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            user=request.user
            post=serializer.validated_data['post']
            content=serializer.validated_data['content']
            comment = Comment.objects.create(user=user, post=post, content=content)
            return Response({'success':'true', 'message':'post commented successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request):
    if request.method == 'POST':
        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            followed_user_id = serializer.validated_data['followed_user']
            followed_user = get_object_or_404(User, id=followed_user_id.id)

            if user == followed_user:
                return Response({'succsess': 'false','message':'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
            #if user follow exists
            if Follow.objects.filter(user=user, followed_user=followed_user).exists():
                return Response({'success': 'false', 'message':'You are already following this user'}, status=status.HTTP_400_BAD_REQUEST)

            follow = Follow.objects.create(user=user, followed_user=followed_user)

            # return count
            follower_count = Follow.objects.filter(followed_user=followed_user).count()

            return Response({'success': 'true', 'message': 'followed successfully', 'follower_count': follower_count}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# following
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def following(request):
    if request.method == 'GET':
        user=request.user
        following = Follow.objects.filter(user=user)
        serializer = FollowListSerializer(following, many=True)
        return Response({'following':serializer.data}, status=status.HTTP_200_OK)
    
# followers
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def followers(request):
    if request.method == 'GET':
        user=request.user
        followers = Follow.objects.filter(followed_user=user)
        serializer = FollowListSerializer(followers, many=True)
        return Response({'followers':serializer.data}, status=status.HTTP_200_OK)
    
# posts
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def posts(request):
    if request.method == 'GET':
        user=request.user
        posts = Post.objects.filter(user=user)
        serializer = PostListSerializer(posts, many=True)
        return Response({'posts':serializer.data}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def all_posts(request):
    if request.method == 'GET':
        user=request.user
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response({'posts':serializer.data}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def view_post(request, id):
    if request.method == 'GET':
        user=request.user
        posts = Post.objects.get(id=id)
        serializer = PostListSerializer(posts)
        return Response({'posts':serializer.data}, status=status.HTTP_200_OK)
    
# edit post
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def edit_post(request, id):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            title=serializer.validated_data['title']
            content=serializer.validated_data['content']
            user=request.user
            post = Post.objects.filter(id=id, user=user).update(title=title, content=content)
            return Response({'success':'true', 'message':'post updated successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# delete post
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, id):
    if request.method == 'DELETE':
        try:
            user=request.user
            post = Post.objects.filter(id=id, user=user).delete()
            return Response({'success':'true', 'message':'post deleted successfully'},status=status.HTTP_200_OK)
        except:
            return Response({'success':'false', 'message':'post not found'},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow(request):
    if request.method == 'POST':
        followed_user_id = request.data.get('followed_user')
        followed_user = get_object_or_404(User, id=followed_user_id)
        user = request.user

        # Check if the user is trying to unfollow themselves
        if user == followed_user:
            return Response({'success': 'false','message':'You cannot unfollow yourself'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the follow relationship exists
        follow_relationship = Follow.objects.filter(user=user, followed_user=followed_user)
        if follow_relationship.exists():
            follow_relationship.delete()

            # Count the followers of the unfollowed user
            follower_count = Follow.objects.filter(followed_user=followed_user).count()

            return Response({'success': 'true', 'message': 'unfollowed successfully', 'follower_count': follower_count}, status=status.HTTP_200_OK)
        else:
            return Response({'success': 'false', 'message': 'You are not following this user'}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    if request.method == 'POST':
        user = request.user
        post = get_object_or_404(Post, pk=post_id)

        
        if Like.objects.filter(user=user, post=post).exists():
            return Response({'success': 'false', 'message': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)
        # Create the like
        Like.objects.create(user=user, post=post)

        # Count likes 
        like_count = Like.objects.filter(post=post).count()

        return Response({'success': 'true', 'message': 'Post liked successfully', 'like_count': like_count}, status=status.HTTP_201_CREATED)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, post_id):
    if request.method == 'POST':
        user = request.user
        post = get_object_or_404(Post, pk=post_id)

        
        like = Like.objects.filter(user=user, post=post)
        if like.exists():
            like.delete()

            like_count = Like.objects.filter(post=post).count()
            return Response({'success': 'true', 'message': 'Post unliked successfully', 'like_count': like_count}, status=status.HTTP_200_OK)
        else:
            return Response({'success': 'false', 'message': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:

        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        print(type(token))

        token.blacklist()

        return Response({'success': 'Successfully logged out'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)