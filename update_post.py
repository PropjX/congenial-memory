import praw 
import time
reddit=praw.Reddit(client_id="*********", client_secret="************",username="Upper-Connection-714",password="*******",user_agent="*********")
while True:
    time.sleep(10)
    submission = reddit.submission(id="********")
    ratio = submission.upvote_ratio
    ups = round((ratio * submission.score) / (2 * ratio - 1)) if ratio != 0.5 else round(submission.score / 2)
    downs = ups - submission.score
    edited_body = str(ups) + ' upvotes,' + '\n\n' + str(downs) + ' downvotes' + "\n\n" "and " + \
                  str(submission.num_comments) + ' comments!'
    submission.edit(edited_body)
