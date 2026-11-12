USE mi_db_1;
SELECT * FROM usuarios;

SELECT employee_id, full_name, job_title, department, business_unit, gender, ethnicity, age, annual_salary, bonus 
FROM usuarios 
LIMIT 10;

SELECT department, COUNT(*) AS total_empleados, ROUND(AVG(annual_salary), 2) AS salario_promedio
FROM usuarios
GROUP BY department;