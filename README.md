Ghertil Search Algorithm for Transport Network Project

Overview

The Ghertil Search Algorithm is a Python-based solution designed to optimize route searches in transport networks. This project aims to improve efficiency and accuracy in identifying the shortest or most optimal paths in complex networks, such as urban transit systems or logistics chains.

Features

- Optimized Pathfinding: Leverages advanced graph traversal techniques to find the shortest or most efficient routes.
- Scalability: Capable of handling large transport networks with thousands of nodes and edges.
- Customizable Metrics: Supports different criteria for optimization, such as distance, time, or cost.
- Dynamic Updates: Allows real-time updates to the network topology.
- Visual Representation: Generates a graphical representation of the network and the computed routes.

 Prerequisites

- Python 3.8 or later
- Required Python libraries:
  - `networkx`
  - `matplotlib`
  - `numpy`
  - `pandas`

To install the dependencies, run:



Usage

1. Define your transport network in a CSV file (e.g., `network.csv`) with the following format:

   ```csv
   Source,Target,Weight
   A,B,10
   B,C,15
   A,C,20
   ```

   - **Source**: Starting node of the edge
   - **Target**: Ending node of the edge
   - **Weight**: Cost or distance between the nodes

2. Run the algorithm:

   ```bash
   python main.py --input network.csv --start A --end C
   ```

   - Replace `network.csv` with the path to your network file.
   - Use `--start` and `--end` to specify the source and destination nodes.

3. View results:

   - Shortest path: Displayed in the console.
   - Visualization: Saved as an image file (e.g., `output.png`).

## Example Output

**Command:**

```bash
python main.py --input network.csv --start A --end C
```

**Output:**

```
Shortest path from A to C: A -> B -> C
Total cost: 25
```

**Visualization:**

- A graph highlighting the shortest path is saved as `output.png`.

## Configuration

- Modify `config.py` to adjust settings such as:
  - Default input file
  - Visualization styles
  - Logging levels

## Contributing

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ``
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

##

## Contact

For questions or support, please contact Ghertil Abdelmalek at [malikghertil10@gmail.com](mailto\:malikghertil10@gmail.com).

