SELECT
    request_at as Day,
    round((sum(Trips.status = "cancelled_by_driver") +
           sum(Trips.status = "cancelled_by_client"))
          / count(status), 2) as "Cancellation Rate"
FROM
    Trips
JOIN users users1
    ON Trips.client_id = users1.users_id
JOIN users users2
    ON Trips.driver_id = users2.users_id
WHERE
    users1.banned = "No" and users2.banned = "No"
    AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY
    Day;