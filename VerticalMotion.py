"""
Author: Jacob Miletti

This program uses functions to model the vertical motion of an object thrown
straight up into the air. It takes a user inputted number for the initial vertical speed
and outputs the time to peak, maximum height, and total flight time of the object.

"""


def time_to_peak(vertical_speed, gravity=-32):
    """Return the time it takes an object to reach its maximum height."""
    return -vertical_speed / gravity


def maximum_height(vertical_speed, gravity=-32, initial_height=0):
    """Return the object's maximum height above the ground."""
    time = time_to_peak(vertical_speed, gravity)
    return 0.5 * gravity * time**2 + vertical_speed * time + initial_height


def total_flight_time(vertical_speed, gravity=-32):
    """Return the flight time when the object lands at its launch height."""
    return 2 * time_to_peak(vertical_speed, gravity)


def main():
    vertical_speed = float(input("Enter the initial vertical speed (ft/s): "))

    print(f"Time to peak: {time_to_peak(vertical_speed):.2f} seconds")
    print(f"Maximum height: {maximum_height(vertical_speed):.2f} feet")
    print(f"Total flight time: {total_flight_time(vertical_speed):.2f} seconds")


if __name__ == "__main__":
    main()
