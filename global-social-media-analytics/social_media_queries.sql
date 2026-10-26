-- Global Social Media Analytics: MySQL 8 practice queries.
-- The included seed data is synthetic; do not report its results as original-project findings.
USE social_media_demo;

-- 1. Most active users by combined posts and comments.
WITH post_counts AS (SELECT user_id, COUNT(*) AS posts_count FROM Posts GROUP BY user_id),
comment_counts AS (SELECT user_id, COUNT(*) AS comments_count FROM Comments GROUP BY user_id)
SELECT u.user_id, u.username, COALESCE(p.posts_count,0) AS posts_count,
       COALESCE(c.comments_count,0) AS comments_count,
       COALESCE(p.posts_count,0)+COALESCE(c.comments_count,0) AS total_activity
FROM Users u LEFT JOIN post_counts p ON p.user_id=u.user_id
LEFT JOIN comment_counts c ON c.user_id=u.user_id
ORDER BY total_activity DESC,u.username LIMIT 10;

-- 2. Most liked posts and creators.
SELECT p.post_id,u.username AS creator,p.content,COUNT(l.like_id) AS like_count
FROM Posts p JOIN Users u ON u.user_id=p.user_id LEFT JOIN Likes l ON l.post_id=p.post_id
GROUP BY p.post_id,u.username,p.content ORDER BY like_count DESC,p.post_id LIMIT 10;

-- 3. Countries ranked by average likes per post.
WITH post_likes AS (
 SELECT p.post_id,u.country,COUNT(l.like_id) AS like_count
 FROM Posts p JOIN Users u ON u.user_id=p.user_id LEFT JOIN Likes l ON l.post_id=p.post_id
 GROUP BY p.post_id,u.country
)
SELECT country,COUNT(*) AS post_count,ROUND(AVG(like_count),2) AS avg_likes_per_post
FROM post_likes GROUP BY country ORDER BY avg_likes_per_post DESC,post_count DESC LIMIT 15;

-- 4. Trending hashtags by distinct tagged posts.
SELECT h.hashtag_text,COUNT(DISTINCT ph.post_id) AS tagged_posts
FROM Hashtags h JOIN Post_hashtags ph ON ph.hashtag_id=h.hashtag_id
GROUP BY h.hashtag_id,h.hashtag_text ORDER BY tagged_posts DESC,h.hashtag_text;

-- 5. Most followed users.
SELECT u.user_id,u.username,COUNT(f.follower_id) AS follower_count
FROM Users u LEFT JOIN Followers f ON f.followed_user_id=u.user_id
GROUP BY u.user_id,u.username ORDER BY follower_count DESC,u.username LIMIT 10;

-- 6. Monthly posting trend.
SELECT DATE_FORMAT(created_at,'%Y-%m') AS month,COUNT(*) AS post_count
FROM Posts GROUP BY DATE_FORMAT(created_at,'%Y-%m') ORDER BY month;

-- 7. Registered users who have never published a post.
SELECT u.user_id,u.username,u.country FROM Users u
WHERE NOT EXISTS (SELECT 1 FROM Posts p WHERE p.user_id=u.user_id) ORDER BY u.username;

-- 8. Like and comment counts for every post, including zero-engagement posts.
WITH like_counts AS (SELECT post_id,COUNT(*) AS like_count FROM Likes GROUP BY post_id),
comment_counts AS (SELECT post_id,COUNT(*) AS comment_count FROM Comments GROUP BY post_id)
SELECT p.post_id,u.username AS creator,COALESCE(l.like_count,0) AS like_count,
       COALESCE(c.comment_count,0) AS comment_count
FROM Posts p JOIN Users u ON u.user_id=p.user_id
LEFT JOIN like_counts l ON l.post_id=p.post_id
LEFT JOIN comment_counts c ON c.post_id=p.post_id
ORDER BY like_count+comment_count DESC,p.post_id;
