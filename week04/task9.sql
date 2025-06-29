/* task9, https://www.hackerrank.com/challenges/harry-potter-and-wands/problem */
select w.id, wp.age, w.coins_needed, w.power
from wands w 
join wands_property wp
on w.code = wp.code
where wp.is_evil = 0
and w.coins_needed = (select min(w2.coins_needed) from wands w2 
                      join wands_property wp2 
                      on w2.code = wp2.code 
                      where wp2.age = wp.age 
                      and w2.power = w.power 
                      and wp2.is_evil = 0)
order by w.power desc, wp.age desc;