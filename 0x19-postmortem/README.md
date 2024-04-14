Issue summary:
Mars, 12, 2023 6:00 pm (WAT)

- Impact : a local web server for a large bakery shop was responding very slow and many users complained about it.

Root Cause:
The root cause was identified as a problem in the load balancer setting that made uneven distribution of traffic to the servers.

Timeline:
Mars, 12, 2023 6:00 pm (WAT) the issue was detected from the users.

6:10 => engineering team was notified of the problem.

6:25 => first investigating focused on database and servers

6:40 => misleading assumption that the database is the problem

6:55 => by more investigations found that the load balancer was the problem for different distribution between servers

7:15 => load balancer setting was adjusted to distribute traffic evenly

Root cause and resolution:
The misconfiguration in the load balancer setting led to different distribution in traffic that made overload on a certain server while leaving the other servers without any job to do
That caused a slow time response 

To solve the problem the load balancer was adjusted to evenly distribute the traffic between all the servers

Correction and prevention measures:
-regular review on the load balancer
-or implement an automated monitoring for the load balancer
