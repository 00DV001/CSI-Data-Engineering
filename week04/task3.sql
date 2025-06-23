/* task3, https://www.hackerrank.com/challenges/weather-observation-station-19/problem */
select ROUND(SQRT(POWER(min(LAT_N)-max(LAT_N),2)+POWER(min(LONG_W)-max(LONG_W),2)),4) from station;