import src.main as main
import time

if __name__ == "__main__":
    output_file = "data/test.out"
    with open(output_file, "w") as out_file:
        for i in range(1, 11):
            file_path = f"data/test{i}.in"
            values, A, B = main.read_example_in(file_path)

            start_time = time.time()
            max_value, lcs = main.highest_val_longest_common_sequence(A, B, values)
            end_time = time.time()

            run_time = end_time - start_time

            out_file.write(f"Test case {i}:\n")
            out_file.write(f"Length of A: {len(A)}, Length of B: {len(B)}\n")
            out_file.write(f"Max Value: {max_value}\n")
            out_file.write(f"Longest Common Sequence: {lcs}\n")
            out_file.write(f"Runtime: {run_time:.6f} seconds\n\n")