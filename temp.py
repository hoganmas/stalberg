# translating DeriveModelFromActors (C++) to python

# RANDOM STUFF
left = right = up = down = forward = backward = 0
adjacencies = [left, right, up, down, forward, backward]


constraints = set()
position_to_option = {}

# Empty tile can be adjacent to Empty tile in all directions
for adjacency in adjacencies:
    constraints += [None, adjacency, None]


# Set relative origin the location of first actor
origin = input_actors[0].position
min_position = max_position = [0, 0, 0]

# Iterate through each actor
for actor in input_actors:
    
    # Assert that actor is static
    if actor is not static:
        continue

    # Get mesh
    mesh = actor.mesh

    # Check if mesh exists
    if mesh is None:
        continue

    # Get the grid posiiton
    current_grid_position = round((actor.position - origin) / tile_size)

    # Check if we already covered this position
    if current_grid_position in position_to_option:
        continue
    
    # Update min/max grid positions
    min_position = min(current_grid_position, min_position)
    max_position = max(current_grid_position, max_position)


    # Obtain rotation of the actor
    rotation = 0
    if mesh not in ignore_rotation_assets:
        rotation = sanitize_rotator(actor.rotation)
    
    # Create new option from the mesh, rotation, and scale of the object 
    # Add this option to our set
    current_option = [mesh, rotation, actor.scale]
    position_to_option[current_grid_position] = current_option


# At this point, we fully propogated position_to_option
# alongside the min and max positions in our grid

position_to_option_with_border = {}

# We normalize each position in our map to be > the min_position
# NOTE: this uses one-indexing (because the border is at index 0)
for position, option in position_to_option:
    position_to_option[position - min_position + 1] = option

# Clear our position_to_option
position_to_option = {}

# NOTE: for a grid that is N-wide, then max_position - min_position = N - 1
# We include border options within our grid, so we add 3 to get our final resolution
resolution_with_border = max_position - min_position + 3


# For each non-empty position in our grid
for position, option in position_to_option_with_border:

    dict position_to_adjacency = get_adjacent_positions(position, resolution_with_border)

    for adj_position, adjacency in position_to_adjacency:
        
        if adj_position in position_to_option_with_border:
            adj_option = position_to_option_with_border[adj_position]
            constraints += [option, adjacency, adj_option]

        # ... (there are also other edge cases here)


# Clear our position_to_option_with_border
position_to_option_with_border = {}




