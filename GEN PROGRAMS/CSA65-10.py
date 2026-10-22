schema = """
Table: Student
Columns: student_id, name, department, marks
"""

prompt = """
Display students scoring above 80 marks.
Sort results by marks in descending order.
"""

query = """
SELECT name, marks
FROM Student
WHERE marks > 80
ORDER BY marks DESC;
"""

print("Schema:", schema)
print("Requirement:", prompt)
print("Generated SQL Query:")
print(query)
