from manim import *

class LineChartExample(Scene):
    def construct(self):
        # Your vector data
        data = [1, 3, 2, 5, 4, 6, 7, 5, 6]

        # Create a set of points based on the data
        points = [
            np.array([x, y, 0]) 
            for x, y in enumerate(data)
        ]
        # Convert points to a line plot
        line_plot = VMobject()
        line_plot.set_points_as_corners(points)

        # Styling the plot
        line_plot.set_color(BLUE)
        line_plot.set_stroke(width=2)

        # Create axes for reference
        axes = Axes(
            x_range=[0, len(data)-1, 1],
            y_range=[min(data)-1, max(data)+1, 1],
            axis_config={"color": GREY}
        )
        
        # Add labels to the axes
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        print("xd")
        # Display the plot and axes on the scene
        self.play(Create(axes), Create(axes_labels))
        self.play(Create(line_plot))
        self.wait(2)
