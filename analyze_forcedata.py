import matplotlib.pyplot as plt

def read_data(file_path):
    times = []
    values = []
    start_time = None

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split('\t')
            if len(parts) >= 2:
                try:
                    # Extracting time and value while removing unwanted characters
                    time = float(parts[0].replace(' s', ''))
                    value = parts[1].replace(' N', '').strip()

                    # Initialize start_time with the first valid time value
                    if start_time is None:
                        start_time = time

                    # Check if the value is a number
                    try:
                        float_value = float(value)
                        times.append(time - start_time)
                        values.append(abs(float_value))
                    except ValueError:
                        continue

                except ValueError:
                    # Skip lines that don't have proper numeric values
                    continue

    return times, values

def plot_data(file_paths):
    plt.figure(figsize=(5, 5))

    for path in file_paths:
        times, values = read_data(path)
        plt.plot(times, values, label=path.split('/')[-1])  # Label each line with the file name

    plt.xlabel('Time (s)')
    plt.ylabel('Force (N)')
    plt.title('Combined Line Chart of Data')
    plt.legend()
    plt.show()

file_paths = [
    # '/Users/yxc/Desktop/1/big/anal_data/F_line0.txt',
    # '/Users/yxc/Desktop/1/big/anal_data/layer1_big.txt',
    # '/Users/yxc/Desktop/1/middle/anal_data/layer1_middle.txt',
    # '/Users/yxc/Desktop/1/small/anal_data/layer1_small.txt',
    # '/Users/yxc/Desktop/1/compare/layer1_big.txt',
    # '/Users/yxc/Desktop/1/compare/layer1_middle.txt',
    # '/Users/yxc/Desktop/1/compare/layer1_small.txt'
    # '/Users/yxc/Desktop/1/big/anal_data/F_line0.txt',
    # '/Users/yxc/Desktop/1/middle/anal_data/F_line0.txt',
    # '/Users/yxc/Desktop/1/small/anal_data/F_line0.txt',
    # '/Users/yxc/Desktop/1/components/Fx_S.txt',
    # '/Users/yxc/Desktop/1/components/Fx_M.txt',
    # '/Users/yxc/Desktop/1/components/Fx_B.txt',
    # '/Users/yxc/Desktop/1/components/Fy_S.txt',
    # '/Users/yxc/Desktop/1/components/Fy_M.txt',
    # '/Users/yxc/Desktop/1/components/Fy_B.txt',
    '/Users/yxc/Desktop/1/force data/Fx.txt',
]

plot_data(file_paths)
# plot_boxplot(file_paths)