# Global Social Media Analytics

## Overview
A MySQL 8 project exploring social-media activity, post popularity, country-level engagement, follower networks, and hashtag usage.

## Files
- `social_media_schema.sql` — demo schema and small fictional seed records.
- `social_media_queries.sql` — eight analytical queries using joins, CTEs, grouping, aggregates, `NOT EXISTS`, and date functions.
- `.github/workflows/social-media-sql-check.yml` — automated MySQL 8 execution and seed-data checks.

## Run locally
Use a disposable MySQL 8 database and run:

```bash
mysql -u root -p < social_media_schema.sql
mysql -u root -p < social_media_queries.sql
```

The schema creates and selects `social_media_demo`.

## Questions covered
1. Which users have the highest combined posting and commenting activity?
2. Which posts have the most likes?
3. How does average likes per post vary by creator country?
4. Which hashtags appear on the most distinct posts?
5. Which users have the most followers?
6. How does post volume change by month?
7. Which registered users have not published a post?
8. What are the like and comment counts for every post, including zero-engagement posts?

## Data and interpretation
The seed records are synthetic examples added to make the query structure reproducible. They are not the original dataset and their results must not be described as original-project findings. The source presentation contained repeated slides with the same “most active users” objective; the repaired presentation replaces those repeated objectives with distinct analysis topics but still needs a final visual review before presenting.

## Validation
The new GitHub Actions workflow runs the schema and queries in MySQL 8 and checks that seed data loaded. Check the Actions tab for the actual run result. Passing the workflow confirms that the SQL runs against this synthetic schema; it does not validate real-world conclusions.
