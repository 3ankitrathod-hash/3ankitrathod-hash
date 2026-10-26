# Global Social Media Analytics

## Overview
A SQL-focused project about social-media activity, post popularity, country-level engagement, follower networks, and hashtag usage.

## Files
- `social_media_schema.sql` — MySQL 8 demo schema with small synthetic records.
- `social_media_queries.sql` — eight example analytical queries.
- `GLOBAL_SOCIAL_MEDIA_ANALYTICS_Repaired.pptx` — repaired presentation copy is available separately; the original presentation is not overwritten.

## SQL concepts
JOINs, LEFT JOIN, GROUP BY, ORDER BY, CTEs, aggregate functions, NOT EXISTS, and date functions.

## Run locally
Open MySQL 8 and run `social_media_schema.sql`, then execute queries from `social_media_queries.sql`.

## Important distinction
The SQL seed records are synthetic examples added to make the query structure reproducible. They are not the original dataset, and their output must not be described as the original project's findings. The source presentation had repeated slides with the same “most active users” objective; the repaired presentation replaces those repeated objectives with distinct analysis topics. It still needs a final visual review before presenting.

## Validation status
The schema and query files have been reviewed for structure, but a MySQL server was not available in this environment for an end-to-end SQL execution test.
