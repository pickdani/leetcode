SELECT
    Customers.name as Customers
FROM
    Customers
WHERE
    Customers.Id NOT IN
    (
        SELECT
            Orders.CustomerId
        FROM Orders
    );