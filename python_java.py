
import subprocess

def call_java_program(input_data):
    try:
        # Compile the Java program
        subprocess.run(["javac", "ComplexLogic.java"], check=True)

        # Run the Java program and capture output
        process = subprocess.run(
            ["java", "ComplexLogic"],
            input=input_data,
            text=True,
            capture_output=True
        )

        if process.returncode == 0:
            print("Output from Java Program:")
            print(process.stdout)
        else:
            print("Error in Java Program:")
            print(process.stderr)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_data = "25 30"  # Example inputs for Java program
    call_java_program(input_data)




