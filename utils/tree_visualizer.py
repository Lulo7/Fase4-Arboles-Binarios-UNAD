import matplotlib.pyplot as plt


class TreeVisualizer:

    @staticmethod
    def draw_tree(ax, root):

        ax.clear()
        ax.set_title(
            "Binary Search Tree",
            fontsize=13,
            fontweight="bold",
            color="#00BCD4",
            pad=15
        )

        ax.set_facecolor("#162638")
        ax.axis("off")

        if root is None:
            ax.text(
                0.5, 0.5,
                "Empty Tree",
                color="white",
                ha="center",
                va="center",
                fontsize=14,
                transform=ax.transAxes
            )
            return

        def calculate_positions(node, depth=0, position=0):

            if node is None:
                return

            calculate_positions(
                node.left,
                depth + 1,
                position - 1
            )

            calculate_positions(
                node.right,
                depth + 1,
                position + 1
            )

        positions = {}

        def assign_positions(node, depth=0, x=0):

            if node is None:
                return x

            x = assign_positions(node.left, depth + 1, x)

            positions[node.value] = (x, -depth)

            x += 1

            x = assign_positions(node.right, depth + 1, x)

            return x

        assign_positions(root)

        def draw_connections(node):

            if node is None:
                return

            x, y = positions[node.value]

            for child in (node.left, node.right):

                if child is not None:
                    child_x, child_y = positions[child.value]

                    ax.plot(
                        [x, child_x],
                        [y, child_y],
                        color="#00BCD4",
                        linewidth=2,
                        zorder=1
                    )

                    draw_connections(child)

        draw_connections(root)

        for value, (x, y) in positions.items():

            ax.scatter(
                x, y,
                s=1100,
                color="#087F95",
                edgecolors="#00BCD4",
                linewidths=2,
                zorder=2
            )

            ax.text(
                x, y,
                str(value),
                color="white",
                ha="center",
                va="center",
                fontsize=10,
                fontweight="bold",
                zorder=3
            )

        max_x = max(x for x, y in positions.values())
        min_x = min(x for x, y in positions.values())

        ax.set_xlim(min_x - 1, max_x + 1)
        ax.set_ylim(-4.5, 1)

    @staticmethod
    def draw_traversal(ax, values, title):

        ax.clear()
        ax.set_title(
            title,
            fontsize=12,
            fontweight="bold",
            color="#00BCD4",
            pad=12
        )

        ax.set_facecolor("#162638")
        ax.axis("off")

        if not values:

            ax.text(
                0.5, 0.5,
                "No nodes available",
                color="white",
                ha="center",
                va="center",
                transform=ax.transAxes
            )
            return

        count = len(values)

        for index, value in enumerate(values):

            x = index

            if index < count - 1:

                ax.plot(
                    [x, x + 1],
                    [0, 0],
                    color="#00BCD4",
                    linewidth=2
                )

            ax.scatter(
                x, 0,
                s=650,
                color="#087F95",
                edgecolors="#00BCD4",
                linewidths=2,
                zorder=2
            )

            ax.text(
                x, 0,
                str(value),
                color="white",
                ha="center",
                va="center",
                fontsize=9,
                fontweight="bold",
                zorder=3
            )

        ax.set_xlim(-0.7, count - 0.3)
        ax.set_ylim(-1, 1)