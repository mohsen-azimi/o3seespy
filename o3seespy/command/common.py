from o3seespy.base_model import OpenSeesObject
from o3seespy.opensees_instance import OpenSeesInstance


def set_node_mass(osi, node, x_mass, y_mass, rot_mass):
    op_type = 'mass'
    parameters = [node.tag, x_mass, y_mass, rot_mass]
    osi.to_process(op_type, parameters)


class Mass(OpenSeesObject):
    op_base_type = "mass"
    op_type = None

    def __init__(self, osi, node, x_mass, y_mass, rot_mass=None):
        if osi.ndf > 2 and rot_mass is None:
            rot_mass = 0.0
        self.node = node
        self.x_mass = x_mass
        self.y_mass = y_mass
        self.rot_mass = rot_mass
        self._parameters = [self.node.tag, self.x_mass, self.y_mass]
        if self.rot_mass is not None:
            self._parameters.append(self.rot_mass)
        self.to_process(osi)


def set_equal_dof(osi, node_1, node_2, dof):
    op_type = 'equalDOF'
    parameters = [node_1.tag, node_2.tag,  dof]
    osi.to_process(op_type, parameters)


def set_equal_dofs(osi, node_1, node_2, dofs):
    op_type = 'equalDOF'
    parameters = [node_1.tag, node_2.tag,  *dofs]
    osi.to_process(op_type, parameters)


def set_equal_dofs_mixed(osi, node_1, node_2, num_dof, rcdofs):  # TODO: validate
    op_type = 'equalDOF_Mixed'
    parameters = [node_1.tag, node_2.tag,  num_dof, *rcdofs]
    osi.to_process(op_type, parameters)


class EqualDOF(OpenSeesObject):
    op_base_type = "equalDOF"
    op_type = None

    def __init__(self, osi, node_1, node_2, dofs):
        self.node_1 = node_1
        self.node_2 = node_2
        self.dofs = dofs
        self._parameters = [self.node_1.tag, self.node_2.tag, *self.dofs]
        self.to_process(osi)


def set_rigid_diaphragm(osi, r_node, cnodes, perp_dir):
    cnode_tags = [x.tag for x in cnodes]
    op_type = 'rigidDiaphragm'
    parameters = [perp_dir, r_node.tag,  *cnode_tags]
    osi.to_process(op_type, parameters)


def set_rigid_link(osi, r_node, c_node, rtype):
    """
    Create a multi-point constraint between nodes.

    Parameters
    ----------
    r_node: Node
        Master node
    c_node: Node
        Slave node
    rtype: str
        Either 'bar' or 'beam'

    Returns
    -------

    """
    op_type = 'rigidLink'
    parameters = [rtype, r_node.tag, c_node.tag]
    osi.to_process(op_type, parameters)


class Fix1DOF(OpenSeesObject):
    op_base_type = "fix"
    op_type = None

    def __init__(self, osi, node, x):
        """
        Create a homogeneous SP constraint.

        Parameters
        ----------
        osi: OpenSeesInstance
        node: OpenSeesObject.node.Node()
        x: int
            Fixity in x-direction
        """
        self.node = node
        self.x = x
        self._parameters = [self.node.tag, self.x]
        self.to_process(osi)


class Fix2DOF(OpenSeesObject):
    op_base_type = "fix"
    op_type = None

    def __init__(self, osi, node, x, y):
        """
        Create a homogeneous SP constraint.

        Parameters
        ----------
        osi: OpenSeesInstance
        node: OpenSeesObject.node.Node()
        x: int
            Fixity in x-direction
        y: int
            Fixity in y-direction
        """
        self.node = node
        self.x = x
        self.y = y
        self._parameters = [self.node.tag, self.x, self.y]
        self.to_process(osi)


class Fix3DOF(OpenSeesObject):
    op_base_type = "fix"
    op_type = None

    def __init__(self, osi, node, x, y, z_rot):
        """
        Create a homogeneous SP constraint.

        Parameters
        ----------
        osi: OpenSeesInstance
        node: OpenSeesObject.node.Node()
        x: int
            Fixity in x-direction
        y: int
            Fixity in y-direction
        z_rot: int
            Fixity in rotation about z-axis
        """
        self.node = node
        self.x = x
        self.y = y
        self.z_rot = z_rot
        self._parameters = [self.node.tag, self.x, self.y, self.z_rot]
        self.to_process(osi)


class Fix6DOF(OpenSeesObject):
    op_base_type = "fix"
    op_type = None

    def __init__(self, osi, node, x, y, z, x_rot, y_rot, z_rot):
        """
        Create a homogeneous SP constraint.

        Parameters
        ----------
        osi: OpenSeesInstance
        node: OpenSeesObject.node.Node()
        x: int
            Fixity in x-direction
        y: int
            Fixity in y-direction
        z: int
            Fixity in z-direction
        x_rot: int
            Fixity in rotation about x-axis
        y_rot: int
            Fixity in rotation about y-axis
        z_rot: int
            Fixity in rotation about z-axis
        """
        self.node = node
        self.x = x
        self.y = y
        self.z = z
        self.x_rot = x_rot
        self.y_rot = y_rot
        self.z_rot = z_rot
        self._parameters = [self.node.tag, self.x, self.y, self.z, self.x_rot, self. y_rot, self.z_rot]
        self.to_process(osi)


class Fix(OpenSeesObject):
    op_base_type = "fix"
    op_type = None

    def __init__(self, osi, node, fixities):
        """
        Create a homogeneous SP constraint.

        """
        self.node = node
        self.fixities = fixities
        self._parameters = [self.node.tag, *self.fixities]
        self.to_process(osi)


class Load(OpenSeesObject):
    op_base_type = "load"
    op_type = None

    def __init__(self, osi, node, load_values):
        self.node = node
        self.load_values = load_values

        self._parameters = [self.node.tag, *self.load_values]
        self.to_process(osi)


class EleLoad2DPoint(OpenSeesObject):
    op_base_type = "eleLoad"
    op_type = None

    def __init__(self, osi, ele, p_y, x, p_x=None):
        """
        Type of load is 'beamPoint'

        x: float
            Position of load as a fraction of element length from node i
        """
        self.ele_tag = ele.tag
        self.x = float(x)
        self.p_y = float(p_y)
        self.p_x = p_x

        self._parameters = ['-ele', self.ele_tag, '-type', '-beamPoint', self.p_y, self.x]
        if self.p_x is not None:
            self._parameters.append(float(self.p_x))
        self.to_process(osi)


class EleLoad2DUniform(OpenSeesObject):
    op_base_type = "eleLoad"
    op_type = None

    def __init__(self, osi, ele, w_y, w_x=None):
        """
        ltype: 'beamUniform'
        """
        self.ele_tag = ele.tag
        self.w_y = float(w_y)
        self.w_x = w_x

        self._parameters = ['-ele', self.ele_tag, '-type', '-beamUniform', self.w_y]
        if self.w_x is not None:
            self._parameters.append(float(self.w_x))
        self.to_process(osi)


class SP(OpenSeesObject):
    op_base_type = "sp"
    op_type = None

    def __init__(self, osi, node, dof, dof_values):
        self.node = node
        self.dof = int(dof)
        self.dof_values = dof_values

        self._parameters = [self.node.tag, self.dof, *self.dof_values]
        self.to_process(osi)


def analyze(osi, num_inc=1, dt=0.1, dt_min=None, dt_max=None, jd=None):
    op_type = 'analyze'
    if dt_min is None:
        parameters = [int(num_inc), float(dt)]
    else:
        parameters = [int(num_inc), float(dt), dt_min, dt_max, jd]
    # opy.analyze(*parameters)
    return osi.to_process(op_type, parameters)
    # if osi.state in [1, 3]:
    #     para = []
    #     for i, e in enumerate(parameters):
    #         if isinstance(e, str):
    #             e = "'%s'" % e
    #         para.append(str(e))
    #         if i > 40:  # avoid verbose print output
    #             break
    #     p_str = ', '.join(para)
    #     osi.to_process('opy.analyze(%s)' % p_str)
    # return 0


def get_node_disp(osi, node, dof):
    op_type = 'nodeDisp'
    parameters = [node.tag, dof]
    # p_str = ', '.join([str(x) for x in parameters])
    return osi.to_process(op_type, parameters)


def get_all_node_disps(osi, dof):
    tags = get_node_tags(osi)
    disps = []
    for tag in tags:
        disps.append(osi.to_process('nodeDisp', [tag, dof]))  # very slow
    return disps


def get_node_vel(osi, node, dof):
    op_type = 'nodeVel'
    parameters = [node.tag, dof]
    return osi.to_process(op_type, parameters)


def get_node_accel(osi, node, dof):
    op_type = 'nodeAccel'
    parameters = [node.tag, dof]
    return osi.to_process(op_type, parameters)


def gen_reactions(osi):
    op_type = 'reactions'
    parameters = []
    return osi.to_process(op_type, parameters)


def get_node_reaction(osi, node, dof):
    op_type = 'nodeReaction'
    parameters = [node.tag, dof]
    return osi.to_process(op_type, parameters)

def get_node_reactions(osi, node):
    op_type = 'nodeReaction'
    parameters = [node.tag]
    return osi.to_process(op_type, parameters)


def get_ele_response(osi, ele, arg, extra_args=None):
    params = [ele.tag, arg]
    if extra_args is not None:
        params += extra_args
    return osi.to_process('eleResponse', params)


def remove_sp(osi, node, dof, pattern=None):
    op_type = 'remove'
    parameters = ['sp', node.tag, dof]
    if pattern is not None:
        parameters.append(pattern.tag)
    # p_str = ', '.join([str(x) for x in parameters])
    return osi.to_process(op_type, parameters)


def remove_load_pattern(osi, load_pattern):
    op_type = 'remove'
    parameters = ['loadPattern', load_pattern.tag]
    return osi.to_process(op_type, parameters)


def remove(osi, o3_obj):
    """Generic remover"""
    op_type = 'remove'
    parameters = [o3_obj.op_base_type, o3_obj.tag]
    return osi.to_process(op_type, parameters)


def set_parameter(osi, value, eles=None, ele_range=None, args=None):
    op_type = 'setParameter'
    parameters = ['-val', value]
    if eles is not None:
        ele_tags = [x.tag for x in eles]
        parameters += ['-ele', *ele_tags]
    elif ele_range is not None:
        ele_tags = [x.tag for x in ele_range]
        parameters += ['-eleRange', *ele_tags]
    else:
        raise ValueError("'eles or ele_range must not be None in set_parameter")
    if args:
        parameters += [*args]
    else:
        raise ValueError("'args' can not be None in set_parameter")
    # p_str = ', '.join([str(x) for x in parameters])
    return osi.to_process(op_type, parameters)


def set_time(osi, time):
    osi.to_process('setTime', [time])


def get_time(osi):
    return osi.to_process('getTime', [])


def wipe_analysis(osi):
    osi.to_process('wipeAnalysis', [])


def wipe(osi):
    osi.to_process('wipe', [])


def load_constant(osi, time=None):
    params = []
    if time is not None:
        params += ['-time', time]
    osi.to_process('loadConst', params)


def update_material_stage(osi, material, stage):
    parameters = ['-material', material.tag, '-stage', stage]
    osi.to_process("updateMaterialStage", parameters)


def get_eigen(osi, solver='genBandArpack', n=1):
    parameters = [f'-{solver}', n]
    return osi.to_process("eigen", parameters)


def get_pid(osi):
    """Get the processor ID of the calling processor."""
    return osi.to_process('getPID', [])


def get_np(osi):
    """Get total number of processors."""
    return osi.to_process('getNP', [])


def get_num_threads(osi):
    """return the total number of threads available"""
    return osi.to_process('getNumThread', [])


def get_node_dofs(osi, node):
    """Returns the DOF numbering of a node."""
    return osi.to_process('nodeDOFs', node.tag)


def get_node_tags(osi, mesh=None):
    """Returns the OpenSEES numbering of the nodes."""
    params = []
    if mesh is not None:
        params += ['-mesh', mesh.tag]
    return osi.to_process('getNodeTags', params)


def get_ele_tags(osi, mesh=None):
    """Returns the OpenSEES numbering of the elements."""
    params = []
    if mesh is not None:
        params += ['-mesh', mesh.tag]
    return osi.to_process('getEleTags', params)


def get_node_coords(osi, node, ndm=None):

    if ndm is not None:
        pms = [ndm]
    else:
        pms = []
    return osi.to_process('nodeCoord', [node.tag, *pms])


def get_all_node_coords(osi, ndm=None):
    tags = get_node_tags(osi)
    coords = []
    if ndm is not None:
        pms = [ndm]
    else:
        pms = []
    for tag in tags:
        coords.append(osi.to_process('nodeCoord', [tag, *pms]))  # very slow
    return coords


def get_all_ele_node_tags(osi):
    ele_tags = get_node_tags(osi)
    node_tags = []
    for tag in ele_tags:
        node_tags.append(osi.to_process('eleNodes', [tag]))
    return node_tags


def get_all_ele_node_tags_as_dict(osi):
    ele_tags = get_node_tags(osi)
    node_tags = {}
    for tag in ele_tags:
        tags = osi.to_process('eleNodes', [tag])
        if tags is not None:
            if len(tags) not in node_tags:
                node_tags[len(tags)] = []
            node_tags[len(tags)].append(tags)
    return node_tags
