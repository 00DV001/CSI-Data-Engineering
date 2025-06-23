/* task1, https://www.hackerrank.com/challenges/weather-observation-station-8/problem?isFullScreen=true */
select city from station where (lower(city) like 'a%'
or lower(city) like 'e%'
or lower(city) like 'i%'
or lower(city) like 'o%'
or lower(city) like 'u%')
and
(lower(city) like '%a'
or lower(city) like '%e'
or lower(city) like '%i'
or lower(city) like '%o'
or lower(city) like '%u');