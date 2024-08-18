![team work](teamwork.png)
##Issue Summary:
* Duration of Outage: The outage lasted for 2 hours and 15 minutes, from 10:30 AM to 12;45PM (UTC)on August 15, 2024.

* Impact: The outage affected our e-commerce platform, resulting in significant slowdowns and partial unavailability of the checkout service. Approximately 70% of users experienced delayed responses, with 40% being completely unable to complete transactions.

* Root Cause: The issue was caused by an unoptimized database query that led to excessive CPU utilization on the primary database server, which then cascaded into a broader system slowdown.

#TimeLine:
* 10:30 AM - The issue was detected through monitoring alerts indicating high CPU usage on the database server.

* 10:35 AM - The engineering team notified and began investigating the database performance.

* 10:45 AM - The initial assumption was that the issue was related to a recent deployment; rollback was initiated.

* 11:00 AM - Rollback completed, but the issue persisted, leading to further investigation into the database.

* 11:15 AM - Escalation to the database administration team to analyze query logs and server performance.

* 11:30 AM - Misleading investigation into network latency as a potential cause, which was ruled out after testing.

* 11:45 AM - Database query optimization was identified as the root cause; the problematic query was isolated.
* 12:00 PM - Query optimization applied, and database performance began to stabilize.
* 12:30 PM - Monitoring confirmed a significant reduction in CPU utilization, and services began to recover.
* 12:45 PM - Full service restored, with the platform operating at normal performance levels.

##Root Cause and Resolution:

#Root Cause:
The root cause of the outage was a poorly optimized SQL query that was deployed as part of a new feature release. The query led to excessive CPU usage on the database server, which resulted in delayed responses across the system. The query was intended to aggregate data for a new report feature, but it was not properly indexed, leading to a full table scan that overwhelmed the database.

#Resolution:
The resolution involved identifying the problematic query through database performance logs and query analysis. Once identified, the query was optimized by adding the necessary indexes and modifying the query structure to improve efficiency. After the optimization was applied, the CPU usage on the database server dropped significantly, allowing the system to recover and return to normal operation.

##Corrective and Preventative Measures:
#Improvements/Fixes:
* Query Review Process: Implement a more rigorous query review process before deployment, including performance testing on production-like environments.
* Monitoring Enhancements: Add specific monitoring for slow queries and high CPU usage on the database server to detect similar issues more rapidly in the future.
* Documentation: Update the deployment checklist to include query optimization checks, especially for new features involving large datasets.
