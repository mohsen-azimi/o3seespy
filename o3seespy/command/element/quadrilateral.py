from o3seespy.command.element.base_element import ElementBase


class Quad(ElementBase):
    """
    The Quad Element Class
    
    This command is used to construct a FourNodeQuad element object which uses a bilinear isoparametric formulation.

  
     
    """
    op_type = 'quad'

    def __init__(self, osi, ele_nodes, thick, otype, mat, pressure, rho, b1, b2):
        """
        Initial method for Quad

        Parameters
        ----------
        ele_nodes: listi
            A list of four element nodes in counter-clockwise order
        thick: float
            Element thickness
        otype: str
            String representing material behavior. the type parameter can be either ``'planestrain'`` or
            ``'planestress'``
        mat: obj
            Tag of ndmaterial
        pressure: float
            Surface pressure (optional, default = 0.0)
        rho: float
            Element mass density (per unit volume) from which a lumped element mass matrix is computed (optional,
            default=0.0)
        b1: float
            Constant body forces defined in the isoparametric domain (optional, default=0.0)
        b2: float
            Constant body forces defined in the isoparametric domain (optional, default=0.0)
        """
        self.ele_nodes = [x.tag for x in ele_nodes]
        self.thick = float(thick)
        self.otype = otype
        self.mat = mat
        self.pressure = float(pressure)
        self.rho = float(rho)
        self.b1 = float(b1)
        self.b2 = float(b2)
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, *self.ele_nodes, self.thick, self.otype, self.mat.tag, self.pressure, self.rho, self.b1, self.b2]
        self.to_process(osi)


class ShellMITC4(ElementBase):
    """
    The ShellMITC4 Element Class
    
    This command is used to construct a ShellMITC4 element object, which uses a bilinear isoparametric formulation in
    combination with a modified shear interpolation to improve thin-plate bending performance.

    
    """
    op_type = 'ShellMITC4'

    def __init__(self, osi, ele_nodes, sec):
        """
        Initial method for ShellMITC4

        Parameters
        ----------
        ele_nodes: listi
            A list of four element nodes in counter-clockwise order
        sec: obj
            Tag associated with previously-defined sectionforcedeformation object. currently must be either a
            ``'platefibersection'``, or ``'elasticmembraneplatesection'``
        """
        self.ele_nodes = [x.tag for x in ele_nodes]
        self.sec = sec
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, *self.ele_nodes, self.sec.tag]
        self.to_process(osi)


class ShellDKGQ(ElementBase):
    """
    The ShellDKGQ Element Class
    
    This command is used to construct a ShellDKGQ element object, which is a quadrilateral shell element based on the
    theory of generalized conforming element.

    
    """
    op_type = 'ShellDKGQ'

    def __init__(self, osi, ele_nodes, sec):
        """
        Initial method for ShellDKGQ

        Parameters
        ----------
        ele_nodes: listi
            A list of four element nodes in counter-clockwise order
        sec: obj
            Tag associated with previously-defined sectionforcedeformation object. currently can be a
            ``'platefibersection'``, a ``'elasticmembraneplatesection'`` and a ``'layeredshell'`` section
        """
        self.ele_nodes = [x.tag for x in ele_nodes]
        self.sec = sec
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, *self.ele_nodes, self.sec.tag]
        self.to_process(osi)


class ShellDKGT(ElementBase):
    """
    The ShellDKGT Element Class
    
    This command is used to construct a ShellDKGT element object, which is a triangular shell element based on the
    theory of generalized conforming element.

    
    """
    op_type = 'ShellDKGT'

    def __init__(self, osi, ele_nodes, sec):
        """
        Initial method for ShellDKGT

        Parameters
        ----------
        ele_nodes: listi
            A list of three element nodes in clockwise or counter-clockwise order
        sec: obj
            Tag associated with previously-defined sectionforcedeformation object. currently can be a
            ``'platefibersection'``, a ``'elasticmembraneplatesection'`` and a ``'layeredshell'`` section
        """
        self.ele_nodes = [x.tag for x in ele_nodes]
        self.sec = sec
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, *self.ele_nodes, self.sec.tag]
        self.to_process(osi)


class ShellNLDKGQ(ElementBase):
    """
    The ShellNLDKGQ Element Class
    
    This command is used to construct a ShellNLDKGQ element object accounting for the geometric nonlinearity of large
    deformation using the updated Lagrangian formula, which is developed based on the ShellDKGQ element.

    
    """
    op_type = 'ShellNLDKGQ'

    def __init__(self, osi, ele_nodes, sec):
        """
        Initial method for ShellNLDKGQ

        Parameters
        ----------
        ele_nodes: listi
            A list of four element nodes in counter-clockwise order
        sec: obj
            Tag associated with previously-defined sectionforcedeformation object. currently can be a
            ``'platefibersection'``, a ``'elasticmembraneplatesection'`` and a ``'layeredshell'`` section
        """
        self.ele_nodes = [x.tag for x in ele_nodes]
        self.sec = sec
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, *self.ele_nodes, self.sec.tag]
        self.to_process(osi)


class ShellNLDKGT(ElementBase):
    """
    The ShellNLDKGT Element Class
    
    This command is used to construct a ShellNLDKGT element object accounting for the geometric nonlinearity of large
    deformation using the updated Lagrangian formula, which is developed based on the ShellDKGT element.

    
    """
    op_type = 'ShellNLDKGT'

    def __init__(self, osi, ele_nodes, sec):
        """
        Initial method for ShellNLDKGT

        Parameters
        ----------
        ele_nodes: listi
            A list of three element nodes in clockwise or counter-clockwise order around the element
        sec: obj
            Tag associated with previously-defined sectionforcedeformation object. currently can be a
            ``'platefibersection'``, a ``'elasticmembraneplatesection'`` and a ``'layeredshell'`` section
        """
        self.ele_nodes = [x.tag for x in ele_nodes]
        self.sec = sec
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, *self.ele_nodes, self.sec.tag]
        self.to_process(osi)


class ShellNL(ElementBase):
    """
    The ShellNL Element Class
    
    
    """
    op_type = 'ShellNL'

    def __init__(self, osi, ele_nodes, sec):
        """
        Initial method for ShellNL

        Parameters
        ----------
        ele_nodes: listi
            A list of nine element nodes, input is the typical, firstly four corner nodes counter-clockwise, then
            mid-side nodes counter-clockwise and finally the central node
        sec: obj
            Tag associated with previously-defined sectionforcedeformation object. currently can be a
            ``'platefibersection'``, a ``'elasticmembraneplatesection'`` and a ``'layeredshell'`` section
        """
        self.ele_nodes = [x.tag for x in ele_nodes]
        self.sec = sec
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, *self.ele_nodes, self.sec.tag]
        self.to_process(osi)


class BbarQuad(ElementBase):
    """
    The BbarQuad Element Class
    
    This command is used to construct a four-node quadrilateral element object, which uses a bilinear isoparametric
    formulation along with a mixed volume/pressure B-bar assumption. This element is for plane strain problems only.

    
    """
    op_type = 'bbarQuad'

    def __init__(self, osi, ele_nodes, thick, mat):
        """
        Initial method for BbarQuad

        Parameters
        ----------
        ele_nodes: listi
            A list of four element nodes in counter-clockwise order
        thick: float
            Element thickness
        mat: obj
            Tag of ndmaterial
        """
        self.ele_nodes = [x.tag for x in ele_nodes]
        self.thick = float(thick)
        self.mat = mat
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, *self.ele_nodes, self.thick, self.mat.tag]
        self.to_process(osi)


class EnhancedQuad(ElementBase):
    """
    The EnhancedQuad Element Class
    
    This command is used to construct a four-node quadrilateral element, which uses a bilinear isoparametric formulation
    with enhanced strain modes.

    
    """
    op_type = 'enhancedQuad'

    def __init__(self, osi, ele_nodes, thick, otype, mat):
        """
        Initial method for EnhancedQuad

        Parameters
        ----------
        ele_nodes: listi
            A list of four element nodes in counter-clockwise order
        thick: float
            Element thickness
        otype: str
            String representing material behavior. valid options depend on the ndmaterial object and its available
            material formulations. the type parameter can be either ``'planestrain'`` or ``'planestress'``
        mat: obj
            Tag of ndmaterial
        """
        self.ele_nodes = [x.tag for x in ele_nodes]
        self.thick = float(thick)
        self.otype = otype
        self.mat = mat
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, *self.ele_nodes, self.thick, self.otype, self.mat.tag]
        self.to_process(osi)


class SSPquad(ElementBase):
    """
    The SSPquad Element Class
    
    This command is used to construct a SSPquad element object.

    
    """
    op_type = 'SSPquad'

    def __init__(self, osi, ele_nodes, mat, otype, thick, b1, b2):
        """
        Initial method for SSPquad

        Parameters
        ----------
        ele_nodes: listi
            A list of four element nodes in counter-clockwise order
        mat: obj
            Unique integer tag associated with previously-defined ndmaterial object
        otype: str
            String to relay material behavior to the element, can be either ``'planestrain'`` or ``'planestress'``
        thick: float
            Thickness of the element in out-of-plane direction
        b1: float
            Constant body forces in global x- and y-directions, respectively (optional, default = 0.0)
        b2: float
            Constant body forces in global x- and y-directions, respectively (optional, default = 0.0)
        """
        self.ele_nodes = [x.tag for x in ele_nodes]
        self.mat = mat
        self.otype = otype
        self.thick = float(thick)
        self.b1 = float(b1)
        self.b2 = float(b2)
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, *self.ele_nodes, self.mat.tag, self.otype, self.thick, self.b1, self.b2]
        self.to_process(osi)
