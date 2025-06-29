/* task8, https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true */
select h.hacker_id, h.name
from hackers h 
join submissions sb on h.hacker_id = sb.hacker_id
join challenges ch on sb.challenge_id = ch.challenge_id
join difficulty df on ch.difficulty_level = df.difficulty_level
where sb.score = df.score
group by h.hacker_id, h.name
having count(*) > 1
order by count(*) desc, h.hacker_id asc;