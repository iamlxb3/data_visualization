def centre_points_plot(csv_path):
    """
    Check merged points and diameters
    Draw spheres for centre points
    df example:
    sid, x, y, z, diameter
    1.2.392.200036.9116.2.6.1.3268.2060189434.1491..., -70.063, 29.013,  -517.5, 7.188
    """
    df = pd.read_csv(csv_path)
    data_dict = collections.defaultdict(lambda: collections.defaultdict(lambda: []))
    xmin = 0
    ymin = 0
    zmin = 0
    xmax = 0
    ymax = 0
    zmax = 0
    for i, row in df.iterrows():
        # initialize data_dict[sid]
        sid = row[0]
        color = tuple(np.random.uniform(0, 1, 3))
        # data_dict[sid]['centre_points'] = []
        # data_dict[sid]['sphere_points'] = []
        # data_dict[sid]['color'] = []
        # data_dict[sid]['marker'] = []


        # add centre points
        array = row.values[1:-1]
        array = array.astype(float).reshape(1, -1)
        data_dict[sid]['centre_points'].append(array)
        data_dict[sid]['centre_color'].append(color)
        data_dict[sid]['centre_marker'].append('D')
        #

        # add sphere points
        x, y, z = row.values[1:-1].astype(float)

        # get the min max x,y,z
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y
        if z < zmin:
            zmin = z
        if z < zmax:
            zmax = z
        #

        diameter = row[-1]
        radius = diameter / 2
        layer = 6 # how many layers you want to generate (half sphere)
        layer_point_num = 12 # how many points to create in 1 layer
        degree_unit = 360. / layer_point_num
        gap = radius / layer
        for i in range(layer + 1):
            layer_gap = i * gap
            if radius - layer_gap <= 1e-6:
                layer_gap = radius
            z_up = z + layer_gap
            z_down = z - layer_gap
            layer_radius = np.sqrt(radius**2 - layer_gap**2)
            for i in range(layer_point_num):
                degree = i * degree_unit
                x_layer = x + layer_radius * math.cos(math.radians(degree))
                y_layer = y + layer_radius * math.sin(math.radians(degree))
                # print("degree: ", degree)
                # print("radius: ", radius)
                # print("layer_gap: ", layer_gap)
                # print("layer_radius: ", layer_radius)
                # print("x_layer: ", x_layer)
                # print("y_layer: ", y_layer)
                data_dict[sid]['sphere_points'].append(np.array([[x_layer, y_layer, z_up]]))
                data_dict[sid]['sphere_color'].append(color)
                data_dict[sid]['sphere_marker'].append('.')
                data_dict[sid]['sphere_points'].append(np.array([[x_layer, y_layer, z_down]]))
                data_dict[sid]['sphere_color'].append(color)
                data_dict[sid]['sphere_marker'].append('.')

    # get the min, max point
    min_max_data = [np.array([[xmin, ymin, zmin]]), np.array([[xmax, ymax, zmax]])]
    min_max_color = ['w', 'w']
    min_max_marker =  ['.', '.']
    #

    for sid, data_dict in data_dict.items():
        centre_points = data_dict['centre_points']
        sphere_points = data_dict['sphere_points']
        data = (centre_points + sphere_points + min_max_data)
        color = data_dict['centre_color'] + data_dict['sphere_color'] + min_max_color
        marker = data_dict['centre_marker'] + data_dict['sphere_marker'] + min_max_marker
        hyp.plot(data, marker=marker, title=sid, color=color, show=False, save_path='lungnodule/{}.png'.format(sid))
        print("{} done".format(sid))
