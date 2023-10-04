name = ""
identity = 0
job_title = ""
salary = 0

# OPen and load the file
with open("hr_system.txt", "r") as file:
    # Read and display each line
    for line in file:
        line = line.strip()

        # Divide the parts
        parts = line.split()

        name = parts[0]
        identity = parts[1]
        job_title = parts[2]
        salary = float(parts[3])

        paycheck_amount = (salary / 12) / 2  # Payments every 2 weeks in a yr

        if job_title == "Engineer":
            paycheck_amount += 1000

        print(f"Name: {name}, ({identity}), {job_title} - {paycheck_amount:.2f}")
