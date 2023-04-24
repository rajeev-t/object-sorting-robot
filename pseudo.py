# Code for robot's maneuvering, sensing, and decision-making
# Written by: Rajeev Thimmareddy and Joseph Tai

# Import Dependencies

# Create Variables

# Ask for Sorting Input - Color or Mass?

# Steps:

    # As long as limit switch is engaged, robot carrys out these actions:

        # 1. Base rotates to initial position (unsorted), if not already at it

        # 2. Four bar moves to desired location

        # 3. Once at location, suction engages

        # 4. Four bar retracts to rotatable location

        # 5a. IF color sorted, base rotates to assigned location based on color sensor input

        # 5b. IF mass sorted, base rotates to assigned location based on load cell delta

        # 6. Once rotated, four bar moves front till IR sensor engaged

            # a. At the same time, suction disengages

        # 7. Four bar retracts to rotatable location

        # 8. Base rotates back to initial position and loop continues