/* task10, https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true */
select s.hacker_id, h.name, sum(score) as total_score
from (select hacker_id, challenge_id, max(score) as score from submissions group by hacker_id, challenge_id) s
join hackers h on s.hacker_id = h.hacker_id
group by s.hacker_id, h.name
having sum(score) > 0
order by total_score desc, s.hacker_id;