from testlibrary import N
import testlibrary as TL
from random import randint
import sys

localhost1 = 'http://13.124.80.116:8000/'
localhost2 = 'http://13.124.80.116:8001/'
localhost3 = 'http://localhost:8000/'

if len(sys.argv) is 1:
    localhost = localhost1
elif len(sys.argv) is 2:
    localhost = localhost3
else:
    localhost = localhost2

TL.test_start('BackEnd')

#####################################################
print('1. POST signup')
link = localhost + 'signup/'

for i in range(1, N+1):
    print('1-{0}. test{0} SignUp'.format(i), end=' ')
    unickname = "test{0}nickname".format(i)
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    TL.signup_post_test(link, unickname, uname, upwd)

#####################################################
print('2. POST login')
link = localhost + 'login/'

for i in range(1, N+1):
    print('2-{0}. test{0} SignIn'.format(i), end=' ')
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    TL.login_post_test(link, uname, upwd)

#####################################################
print('3. POST feed')
link = localhost + 'feed/'

scopes = ['Public','Friends Only','Private','Hidden']
# number of feed of each user
NF = [0]
# total number of Feed
F = 0

for i in range(1, N+1):
    M = randint(1, 4) # number of feed for ith user
    #M = 4
    print('3-{0}. user test{0} will post {1} feed'.format(i,M))
    NF.append(M)
    F += M
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    for j in range(1, M+1):
        print('posting feed{0}: '.format(j), end=' ')
        contents = 'Backend - contents of POST {0}-{1} feed: 종강하고싶다{1}{1}'.format(i,j)
        scope = scopes[0] #global or private, will be changed by i%4 later
        TL.feed_post_test(link, contents, scope, uname, upwd)

#####################################################
print('4. GET feed')
link = localhost + 'feed/'
feedlist = [0]

for i in range(1, N+1):
    print('4-{0}. user test{0} will get feed'.format(i), end=' ')
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    feedlist.append(TL.feed_get_test(link, uname, upwd))

#####################################################
print('5. GET feed/<id>')
sum = 0

for i in range(1, N+1):
    print('5-{0}. user test{0} will get feed by id'.format(i))
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    # see own's all post and (other's) one global post, one private post
    #if i != N:
    #    limit += 2
    #print('{0} sum: {1}'.format(i,sum))
    for j in feedlist[i]:
        print('getting {0} feed: '.format(j), end=' ')
        link = localhost + 'feed/' + str(j) + '/'
        seen = True
        #if i != N and (sum+j) == limit-1:
        #    seen = False # other user's private feed
        TL.feed_id_get_test(link, uname, upwd, seen)

#####################################################
print('6. POST feed/<id>/reply')

# number of reply of each feed
NfR = [0]
#total number of reply
R = 0

for i in range(1, N+1):
    print('6-{0}. user test{0} will post {1} reply(replies)'.format(i, NF[i]))
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    for j in feedlist[i]:
        print('posting reply(my feed){0}: '.format(j), end=' ')
        link = localhost + 'feed/' + str(j) + '/reply/'
        contents = 'contents of POST {0}-{1} reply: 아무것도 안하고 싶다'.format(i,j)
        TL.feed_reply_post_test(link, contents, uname, upwd)
    '''for j in range(1, N+1):
        if i==j: continue
        R += 1
        print('posting reply(other user\'s feed){0}: '.format(j), end=' ')
        link = localhost + 'feed/' + str(j) + '/reply/'
        contents = 'contents of POST {0}-{1} reply: 아무것도 안하고 싶다{1}{1}'.format(i, j)
        TL.feed_reply_post_test(link, contents, uname, upwd)'''


#####################################################
print('7. GET feed/<id>/reply')
sum = 0
R = 0

for i in range(1, N+1):
    print('7-{0}. user test{0} will get {1} reply(replies)'.format(i, NF[i]))
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    for j in feedlist[i]:
        print('getting all replies of feed{0}: '.format(j), end=' ')
        link = localhost + 'feed/' + str(j) + '/reply/'
        replylist = TL.feed_reply_get_test(link, uname, upwd)
        for k in replylist:
            print('getting 1 reply of id {0}: '.format(k), end=' ')
            link = localhost + 'reply/' + str(k)
            TL.reply_get_test(link, uname, upwd)
            
#####################################################
print('8. POST feed/<id>/likes')
sum = 0

for i in range(1, N+1):
    print('8-{0}. user test{0} will post likes to {1} feeds '.format(i, NF[i]))
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    for j in feedlist[i]:
        print('post like to feed{0}: '.format(j), end=' ')
        link = localhost + 'feed/' + str(j) + '/likes/'
        TL.feed_likes_post_test(link, uname, upwd)
            
#####################################################
print('9. GET feed/<id>/likes')
sum = 0

for i in range(1, N+1):
    print('9-{0}. user test{0} will get likes to {1} feeds '.format(i, NF[i]))
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    sum += NF[i-1]
    for j in feedlist[i]:
        print('get like to feed{0}: '.format(j), end=' ')
        link = localhost + 'feed/' + str(j) + '/likes/'
        TL.feed_likes_get_test(link, uname, upwd)
            
#####################################################
print('10. delete feed/<id>/likes')
sum = 0

for i in range(1, N+1):
    print('10-{0}. user test{0} will delete likes to {1} feeds '.format(i, NF[i]))
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    for j in feedlist[i]:
        print('delete like to feed{0}: '.format(j), end=' ')
        link = localhost + 'feed/' + str(j) + '/likes/'
        TL.feed_likes_delete_test(link, uname, upwd)
                                
#####################################################
print('11. POST feed/<id>/dislikes')
sum = 0

for i in range(1, N+1):
    print('11-{0}. user test{0} will post dislikes to {1} feeds '.format(i, NF[i]))
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    for j in feedlist[i]:
        print('post dislike to feed{0}: '.format(j), end=' ')
        link = localhost + 'feed/' + str(j) + '/dislikes/'
        TL.feed_likes_post_test(link, uname, upwd)
            
#####################################################
print('12. GET feed/<id>/dislikes')
sum = 0

for i in range(1, N+1):
    print('12-{0}. user test{0} will get dislikes to {1} feeds '.format(i, NF[i]))
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    for j in feedlist[i]:
        print('get dislike to feed{0}: '.format(j), end=' ')
        link = localhost + 'feed/' + str(j) + '/dislikes/'
        TL.feed_likes_get_test(link, uname, upwd)
        
#####################################################
print('13. delete feed/<id>/dislikes')
sum = 0

for i in range(1, N+1):
    print('13-{0}. user test{0} will delete dislikes to {1} feeds '.format(i, NF[i]))
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    for j in feedlist[i]:
        print('delete dislike to feed{0}: '.format(j), end=' ')
        link = localhost + 'feed/' + str(j) + '/dislikes/'
        TL.feed_dislikes_delete_test(link, uname, upwd)
        
#####################################################
print('14. make new chat chat/user/<username>')
chatlist = [0]

for i in range(1, (N+1)//2):
    print('14-{0}. user test{1} makes new chat with test{2}'.format(i,2*i-1, 2*i))
    uname = "test{0}".format(2*i-1)
    upwd = "test{0}passwd".format(2*i-1)
    link = localhost + 'chat/user/test{0}/'.format(2*i)
    chatlist.append(TL.chat_new_chat_test(link, uname, upwd))
                
#####################################################
print('15. post chat chat/<id>')

for i in range(1, (N+1)//2):
    print('15-{0}. user test{1} chat to test{2} in room{3}'.format(i,2*i-1, 2*i,chatlist[i]))
    uname = "test{0}".format(2*i-1)
    upwd = "test{0}passwd".format(2*i-1)
    link = localhost + 'chat/{0}/'.format(chatlist[i])
    contents = "asdf"
    TL.chat_post_chat_test(link, contents, uname, upwd)
        
#####################################################
print('16. get prev chat chat/<id>')

for i in range(1, (N+1)//2):
    print('16-{0}. user test{1} get prev chat from room{2}'.format(i,2*i,chatlist[i]))
    uname = "test{0}".format(2*i)
    upwd = "test{0}passwd".format(2*i)
    link = localhost + 'chat/{0}/'.format(chatlist[i])
    TL.chat_get_prev_chat_test(link, uname, upwd)

#####################################################
print('17. get all chat chat/<id>/all')

for i in range(1, (N+1)//2):
    print('17-{0}. user test{1} get all chat from room{2}'.format(i,2*i,chatlist[i]))
    uname = "test{0}".format(2*i)
    upwd = "test{0}passwd".format(2*i)
    link = localhost + 'chat/{0}/all/'.format(chatlist[i])
    TL.chat_get_all_chat_test(link, uname, upwd)    
        
#####################################################
print('18. hashtag post and get hashtag/<tagname>')

for i in range(1, N+1):
    print('18-{0}, user test{1}'.format(i, i))
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    feedlink = localhost + 'feed/'
    hashtaglink = localhost + 'hashtag/hashtag{0}'.format(i)
    contents = 'asdf #hashtag{0} asdf'.format(i)
    scope = 'Public'
    TL.post_feed_get_hashtag_test(feedlink, hashtaglink, contents, scope, uname, upwd)

#####################################################
print('19. get all hashtags')

for i in range(1, N+1):
    print('19-{0}, user test{0} will get hashtags'.format(i))
    uname = 'test{0}'.format(i)
    upwd = 'test{0}passwd'.format(i)
    uhashtag = 'hashtag{0}'.format(i) 
    link = localhost + 'hashtag/'
    TL.get_hashtag_test(link, uhashtag, uname, upwd)

#####################################################
print('20. make multichat')

for i in range(1, N+1):
    print('20-{0}, user test{0} will make multichat room'.format(i))
    uname = 'test{0}'.format(i)
    upwd = 'test{0}passwd'.format(i)
    link = localhost + 'multichat/'
    TL.enter_multichat_test(link, uname, upwd)

######################################################
print('21. enter multichat')

for i in range(1, N+1):
    print('21-{0}, user test{0} will enter multichat room'.format(i))
    uname = 'test{0}'.format(i)
    upwd = 'test{0}passwd'.format(i)
    link = localhost + 'multichat/enter/1/'
    TL.enter_multichat_test(link, uname, upwd)

######################################################
print('22. post chat multichat')

for i in range(1, N+1):
    print('22-{0}, user test{0} will enter multichat room'.format(i))
    uname = 'test{0}'.format(i)
    upwd = 'test{0}passwd'.format(i)
    link = localhost + 'multichat/1/'
    contents = 'asdf'
    TL.post_multichat_test(link, contents, uname, upwd)

#####################################################
print('23. get prev chat multichat')

for i in range(1, N+1):
    print('23-{0}. user test{1} get prev chat from multichat'.format(i,i))
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    link = localhost + 'multichat/1/'
    TL.get_prev_multichat_test(link, uname, upwd)

####################################################
print('24. get all multichat')

for i in range(1, N+1):
    print('24-{0}. user test{1} get all chat from multichat'.format(i,i))
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    link = localhost + 'multichat/1/all/'
    TL.get_all_multichat_test(link, uname, upwd)    
        
#####################################################
print('25. get all multichat room')

for i in range(1, N+1):
    print('25-{0}. user test{1} get all chat from multichat'.format(i,i))
    uname = "test{0}".format(i)
    upwd = "test{0}passwd".format(i)
    link = localhost + 'multichat/'
    TL.get_all_multichat_room_test(link, uname, upwd)    
        
#####################################################
print('26. post markdownfeed')

for i in range(1, N+1):
    print('26-{0}, user test{0} post markdown feed'.format(i))
    uname = 'test{0}'.format(i)
    upwd = 'test{0}passwd'.format(i)
    link = localhost + 'feed/'
    contents = 'asdf'
    scope = scopes[0]
    TL.markdown_feed_post_test(link, contents, scope, uname, upwd)

#####################################################
print('27. change password')

for i in range(1, N+1):
    print('27-{0}, user test{0} change password'.format(i))
    uname = 'test{0}'.format(i)
    upwd = 'test{0}passwd'.format(i)
    npwd = 'test{0}'.format(i)
    link = localhost + 'users/password/'
    TL.change_password_test(link, npwd, uname, upwd)

#####################################################
print('28. change nickname')

for i in range(1, N+1):
    print('28-{0}, user test{0} change nickname'.format(i))
    uname = 'test{0}'.format(i)
    upwd = 'test{0}'.format(i)
    link = localhost+'users/profile/'
    nickname = 'test{0}nickname'.format(i)
    TL.change_nickname_test(link, nickname, uname, upwd)

#####################################################
print('29. get nickname')

for i in range(1, N+1):
    print('29-{0}, user test{0} get nickname'.format(i))
    uname = 'test{0}'.format(i)
    upwd = 'test{0}'.format(i)
    link = localhost+'users/profile/'.format(i)
    nickname = 'test{0}nickname'.format(i)
    TL.get_nickname_test(link, nickname, uname, upwd)

#print('8. profile')

#for i in range(1, N+1):
    #link = localhost + 'profile'
    #pass

TL.test_end()
