"""Unit tests for the Vector interface"""

__author__ = "Garth N. Wells (gnw20@cam.ac.uk)"
__date__ = "2011-03-01"
__copyright__ = "Copyright (C) 2011 Garth N. Wells"
__license__  = "GNU LGPL Version 2.1"

import unittest
from dolfin import *

class AbstractBaseTest(object):
    count = 0
    def setUp(self):
        if self.backend != "default":
            parameters.linear_algebra_backend = self.backend
        type(self).count += 1
        if type(self).count == 1:
            # Only print this message once per class instance
            print "\nRunning:",type(self).__name__

    #def assemble_matrices(self, use_backend=False):
    #    " Assemble a pair of matrices, one (square) MxM and one MxN"
    #    mesh = UnitSquare(3,3)
    #
    #    V = FunctionSpace(mesh, "Lagrange", 2)
    #    W = FunctionSpace(mesh, "Lagrange", 1)
    #
    #    v = TestFunction(V)
    #    u = TrialFunction(V)
    #    s = TrialFunction(W)

    #    # Forms
    #    a = dot(grad(u),grad(v))*dx
    #    b = v*s*dx

    #    if use_backend:
    #        if self.backend == "uBLAS":
    #            backend = globals()[self.backend+self.sub_backend+'Factory_instance']()
    #        else:
    #            backend = globals()[self.backend+'Factory_instance']()
    #        return assemble(a, backend=backend), assemble(b, backend=backend)
    #    else:
    #        return assemble(a), assemble(b)

    #def assemble_vectors(self):
    #    mesh = UnitSquare(3,3)
    #
    #    V = FunctionSpace(mesh, "Lagrange", 2)
    #    W = FunctionSpace(mesh, "Lagrange", 1)

    #    v = TestFunction(V)
    #    t = TestFunction(W)

    #    return assemble(v*dx), assemble(t*dx)


    def test_create_empty_vector(self):
        v0 = Vector()
        self.assertEqual(v0.size(), 0)

    def test_create_vector(self):
        n = 301
        v1 = Vector(n)
        self.assertEqual(v1.size(), n)

    def test_copy_vector(self):
        n = 301
        v0 = Vector(n)
        v1 = Vector(v0)
        self.assertEqual(v0.size(), n)
        del v0
        self.assertEqual(v1.size(), n)

    def test_assign_and_copy_vector(self):
        n = 301
        v0 = Vector(n)
        v0[:] = 1.0
        self.assertEqual(v0.sum(), n)
        v1 = Vector(v0)
        del v0
        self.assertEqual(v1.sum(), n)

    def test_zero(self):
        v0 = Vector(301)
        v0.zero()
        self.assertEqual(v0.sum(), 0.0)

    def test_apply(self):
        v0 = Vector(301)
        v0.apply("insert")
        v0.apply("add")

    def test_str(self):
        v0 = Vector(13)
        tmp = v0.str(False)
        tmp = v0.str(True)

    def test_resize(self):
        m, n = 301, 409
        v0 = Vector()
        v0.resize(m)
        self.assertEqual(v0.size(), m)
        v0.resize(n)
        self.assertEqual(v0.size(), n)

    def test_resize_range(self):
        n = 301
        local_range = MPI.local_range(n)
        v0 = Vector()
        v0.resize(local_range)
        self.assertEqual(v0.local_range(), local_range)

    def test_size(self):
        n = 301
        v0 = Vector(301)
        self.assertEqual(v0.size(), n)

    def test_local_size(self):
        n = 301
        local_range = MPI.local_range(n)
        v0 = Vector()
        v0.resize(local_range)
        self.assertEqual(v0.local_size(), local_range[1] - local_range[0])

    def test_owns_index(self):
        m, n = 301, 25
        v0 = Vector(m)
        local_range = v0.local_range()
        in_range = local_range[0] <= n < local_range[1]
        self.assertEqual(v0.owns_index(n), in_range)

    #def test_get_local(self):

    #def test_set(self):

    #def test_add(self):

    def test_get_local(self):
        from numpy import empty
        n = 301
        v0 = Vector(n)
        data = empty((v0.local_size()), dtype='d')
        v0.get_local(data)

    def test_set_local(self):
        from numpy import zeros
        n = 301
        v0 = Vector(n)
        data = zeros((v0.local_size()), dtype='d')
        v0.set_local(data)

    def test_add_local(self):
        from numpy import zeros
        n = 301
        v0 = Vector(n)
        data = zeros((v0.local_size()), dtype='d')
        v0.add_local(data)

    #def test_gather(self):

    def test_axpy(self):
        n = 301
        v0 = Vector(n)
        v0[:] = 1.0
        v1 = Vector(v0)
        v0.axpy(2.0, v1)
        self.assertEqual(v0.sum(), 2*n + n)

    def test_abs(self):
        n = 301
        v0 = Vector(n)
        v0[:] = -1.0
        v0.abs()
        self.assertEqual(v0.sum(), n)

    def test_inner(self):
        n = 301
        v0 = Vector(n)
        v0[:] = 2.0
        v1 = Vector(n)
        v1[:] = 3.0
        self.assertEqual(v0.inner(v1), 6*n)

    def test_norm(self):
        n = 301
        v0 = Vector(n)
        v0[:] = -2.0
        self.assertEqual(v0.norm("l1"), 2.0*n)
        self.assertEqual(v0.norm("l2"), sqrt(4.0*n))
        self.assertEqual(v0.norm("linf"), 2.0)

    def test_min(self):
        v0 = Vector(301)
        v0[:] = 2.0
        self.assertEqual(v0.min(), 2.0)

    def test_max(self):
        v0 = Vector(301)
        v0[:] = -2.0
        self.assertEqual(v0.max(), -2.0)

    def test_sum(self):
        n = 301
        v0 = Vector(n)
        v0[:] = -2.0
        self.assertEqual(v0.sum(), -2.0*n)

    def test_sum_entries(self):
        from numpy import zeros
        n = 301
        v0 = Vector(n)
        v0[:] = -2.0
        entries = zeros(5, dtype='I')
        self.assertEqual(v0.sum(entries), -2.0)
        entries[0] = 2
        entries[1] = 1
        entries[2] = 236
        entries[3] = 123
        entries[4] = 97
        self.assertEqual(v0.sum(entries), -2.0*5)

    def test_scalar_mult(self):
        n = 301
        v0 = Vector(n)
        v0[:] = -1.0
        v0 *= 2.0
        self.assertEqual(v0.sum(), -2.0*n)

    def test_vector_element_mult(self):
        n = 301
        v0 = Vector(n)
        v1 = Vector(n)
        v0[:] = -2.0
        v1[:] =  3.0
        v0 *= v1
        self.assertEqual(v0.sum(), -6.0*n)

    def test_scalar_divide(self):
        n = 301
        v0 = Vector(n)
        v0[:] = -1.0
        v0 /= -2.0
        self.assertEqual(v0.sum(), 0.5*n)

    def test_vector_add(self):
        n = 301
        v0 = Vector(n)
        v1 = Vector(n)
        v0[:] = -1.0
        v1[:] =  2.0
        v0 += v1
        self.assertEqual(v0.sum(), n)

    def test_vector_subtract(self):
        n = 301
        v0 = Vector(n)
        v1 = Vector(n)
        v0[:] = -1.0
        v1[:] =  2.0
        v0 -= v1
        self.assertEqual(v0.sum(), -3.0*n)

    def test_vector_assignment(self):
        m, n = 301, 345
        v0 = Vector(m)
        v1 = Vector(n)
        v0[:] = -1.0
        v1[:] =  2.0
        v0 = v1
        self.assertEqual(v0.sum(), 2.0*n)

# A DataTester class that test the acces of the raw data through pointers
# This is only available for uBLAS and MTL4 backends
class DataTester(AbstractBaseTest):
    def test_vector_data(self):
        # Test for ordinary Vector
        v = Vector(301)
        array = v.array()
        data = v.data()
        self.assertTrue((data == array).all())

        # Test for down_casted Vector
        v = down_cast(v)
        data = v.data()
        self.assertTrue((data==array).all())

class DataNotWorkingTester(AbstractBaseTest):
    def test_vector_data(self):
        v = Vector(301)
        self.assertRaises(RuntimeError, v.data)

        v = down_cast(v)
        def no_attribute():
            v.data()
        self.assertRaises(AttributeError,no_attribute)


if MPI.num_processes() <= 1:
    class uBLASSparseTester(DataTester, unittest.TestCase):
        backend     = "uBLAS"
        sub_backend = "Sparse"

    class uBLASDenseTester(DataTester, unittest.TestCase):
        backend     = "uBLAS"
        sub_backend = "Dense"

    if has_la_backend("MTL4"):
        class MTL4Tester(DataTester, unittest.TestCase):
            backend    = "MTL4"

if has_la_backend("PETSc"):
    class PETScTester(DataNotWorkingTester, unittest.TestCase):
        backend    = "PETSc"

if has_la_backend("Epetra"):
    class EpetraTester(DataNotWorkingTester, unittest.TestCase):
        backend    = "Epetra"

if __name__ == "__main__":
    # Turn of DOLFIN output
    logging(False)

    print ""
    print "Testing DOLFIN Vector class"
    print "------------------------------------------------"
    unittest.main()