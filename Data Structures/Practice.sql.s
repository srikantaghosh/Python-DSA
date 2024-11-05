/*Each employee has an ID and a name, and manager_id references the emp_id of their manager.
 Write a query to find the names of employees who earn more than their manager.
 */

SELECT emp_id AS Employee_Id,
emp_name AS Employee_Name

From Employee e
JOIN Employee m
ON e.manager_id = m.emp_id
AND e.salary > m.salary

/*
Write a query to find the cumulative total sales amount for each day. The result should include sale_date and 
cumulative_amount, with cumulative_amount representing the running total of sales up to that day.
*/

SELECT sale_date,
       SUM(amount) OVER (ORDER BY sale_date) AS cumulative_amount
FROM Sales;

/*
Write a query to find the top three highest spending customers based on the total amount spent across all orders.
The output should include customer_id and total_amount.
*/

SELECT distinct customer_id
from orders
where 1=1
group by 1
qualify rank() over(order by sum(amount) desc) <