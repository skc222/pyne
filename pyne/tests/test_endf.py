import warnings
import StringIO

import numpy as np
from numpy.testing import assert_array_equal

from pyne.endf import Library
from pyne.rxdata import DoubleSpinDict

import nose 
from nose.tools import assert_equal

new_library = StringIO.StringIO(
""" $Rev:: 532      $  $Date:: 2011-12-05#$                             1 0  0    0
 1.002000+3 1.996800+0          1          0          0          0 128 1451    1
 0.000000+0 0.000000+0          0          0          0          6 128 1451    2
 1.000000+0 1.500000+8          1          0         10          7 128 1451    3
 0.000000+0 0.000000+0          0          0        211         17 128 1451    4
  1-H -  2 LANL       EVAL-FEB97 WEBDubois,Q.W.Alle,H.N.Casnowck   128 1451    5
 CH97,CH99            DIST-DEC06                       20111222    128 1451    6
----ENDF/B-VII.1      MATERIAL  128                                128 1451    7
-----INCIDENT NEUTRON DATA                                         128 1451    8
------ENDF-6 FORMAT                                                128 1451    9
                                                                   128 1451   10
 ****************************************************************  128 1451   11
                                                                   128 1451   12
 Lorem ipsum dolor sit amet, consectetur adipiscing elit.          128 1451   13
 Integer nec odio. Praesent libero. Sed cursus ante dapibus        128 1451   14
 diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet.       128 1451   15
 Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed        128 1451   16
 augue semper porta.                                               128 1451   17
                                                                   128 1451   18
 ************************ C O N T E N T S ************************ 128 1451   19
                                1        451         27          0 128 1451   20
                                2        151         31          0 128 1451   21
                                3          1          1          0 128 1451   22
                                3          2          1          0 128 1451   23
                                3          3          1          0 128 1451   24
                                3         16          1          0 128 1451   25
                                3        102          1          0 128 1451   26
                                4          2          1          0 128 1451   27
 0.000000+0 0.000000+0          0          0          0          0 128 1  099999
 0.000000+0 0.000000+0          0          0          0          0 128 0  0    0
 1.876876+3 1.776576+0          0          0          1          0 128 2151    1
 5.513700+4 1.000000+0          0          0          1          0 128 2151    2
 1.700000+3 1.000000+5          2          2          0          0 128 2151    3
 3.500000+0 5.101200-1          0          0          3          0 128 2151    4
 1.357310+2 0.000000+0          0          0          2          0 128 2151    5
 3.000000+0 0.000000+0          5          0         24          3 128 2151    6
 0.000000+0 0.000000+0 0.000000+0 1.000000+0 0.000000+0 0.000000+0 128 2151    7
 1.700000+3 1.261820+3 0.000000+0 2.078520-1 1.000000-2 0.000000+0 128 2151    8
 2.000000+3 3.271100+3 0.000000+0 6.088000-1 2.000000-2 0.000000+0 128 2151    9
 3.000000+3 5.288900+3 0.000000+0 3.120000-1 3.000000-2 0.000000+0 128 2151   10
 4.000000+0 0.000000+0          5          0         24          3 128 2151   11
 0.000000+0 0.000000+0 0.000000+0 1.000000+0 0.000000+0 0.000000+0 128 2151   12
 1.710000+3 7.762320+3 0.000000+0 2.172160-1 3.000000-2 0.000000+0 128 2151   13
 2.010000+3 6.766400+3 0.000000+0 4.179600-1 2.000000-2 0.000000+0 128 2151   14
 3.010000+3 2.780300+3 0.000000+0 6.204500-1 1.000000-2 0.000000+0 128 2151   15
 1.357310+2 0.000000+0          1          0          4          0 128 2151   16
 2.000000+0 0.000000+0          5          0         24          3 128 2151   17
 0.000000+0 0.000000+0 0.000000+0 1.000000+0 0.000000+0 0.000000+0 128 2151   18
 1.720000+3 1.176160+3 0.000000+0 4.489400-1 8.000000-2 0.000000+0 128 2151   19
 2.020000+3 7.177600+3 0.000000+0 8.497500-1 7.000000-2 0.000000+0 128 2151   20
 3.020000+3 2.202500+3 0.000000+0 9.524900-1 6.000000-2 0.000000+0 128 2151   21
 3.000000+0 0.000000+0          5          0         24          3 128 2151   22
 0.000000+0 0.000000+0 0.000000+0 2.000000+0 0.000000+0 0.000000+0 128 2151   23
 1.730000+3 6.265820+3 0.000000+0 4.422380-1 9.000000-2 0.000000+0 128 2151   24
 2.030000+3 5.274100+3 0.000000+0 9.438200-1 7.000000-2 0.000000+0 128 2151   25
 3.030000+3 8.282900+3 0.000000+0 2.557800-1 4.000000-2 0.000000+0 128 2151   26
 4.000000+0 0.000000+0          5          0         24          3 128 2151   27
 0.000000+0 0.000000+0 0.000000+0 2.000000+0 0.000000+0 0.000000+0 128 2151   28
 1.740000+3 7.762320+3 0.000000+0 9.938540-1 2.000000-2 0.000000+0 128 2151   29
 2.040000+3 6.766400+3 0.000000+0 3.943100-1 5.000000-2 0.000000+0 128 2151   30
 3.040000+3 2.780300+3 0.000000+0 8.958300-1 4.000000-2 0.000000+0 128 2151   31
 0.000000+0 0.000000+0          0          0          0          0 128 2  099999
 0.000000+0 0.000000+0          0          0          0          0 128 0  0    0
 1.989875+3 1.998644+0          0          0          0          0 128 3  1    1
 0.000000+0 0.000000+0          0          0          0          0 128 3  099999
 1.012000+3 1.231241+0          0          0          0          0 128 3  2    1
 0.000000+0 0.000000+0          0          0          0          0 128 3  099999
 1.123123+3 1.123113+0          0          0          0          0 128 3  3    1
 0.000000+0 0.000000+0          0          0          0          0 128 3  099999
 7.984533+3 1.125535+0          1          0          0          0 128 3 16    1
 0.000000+0 0.000000+0          0          0          0          0 128 3  099999
 1.948720+3 1.145243+0          0          0          0          0 128 3102    1
 0.000000+0 0.000000+0          0          0          0          0 128 3  099999
 0.000000+0 0.000000+0          0          0          0          0 128 0  0    0
 1.983232+3 1.934732+0          0          2          0          0 128 4  2    1
 0.000000+0 0.000000+0          0          0          0          0 128 4  099999
 0.000000+0 0.000000+0          0          0          0          0 128 0  0    0
 0.000000+0 0.000000+0          0          0          0          0   0 0  0    0
 0.000000+0 0.000000+0          0          0          0          0  -1 0  0    0
 $Rev:: 512      $  $Date:: 2006-12-05#$                             1 0  0    0
 1.003100+3 2.098312+0          1          0          0          1 131 1451    1
 0.564324+0 1.123121+0          0          0          0          6 131 1451    2
 1.905018+0 2.401998+7          1          0         10          7 131 1451    3
 0.109590+0 0.123112+0          0          0         90          8 131 1451    4
  1-H -  3 LANL       EVAL-NOV01 W.P.Pike                          131 1451    5
PRC  42, 438 (1990)   DIST-DEC06                       20111222    131 1451    6
----ENDF/B-VII.1      MATERIAL  131                                131 1451    7
-----INCIDENT NEUTRON DATA                                         131 1451    8
------ENDF-6 FORMAT                                                131 1451    9
                                                                   131 1451   10
*** Mauris massa. Vestibulum lacinia arcu eget nulla. Class *****  131 1451   11
aptent taciti sociosqu ad litora torquent per conubia nostra, per  131 1451   12
inceptos himenaeos. Curabitur sodales ligula in libero. Sed        131 1451   13
*****************************************************************  131 1451   14
                                                                   131 1451   15
                                1        451         21          1 131 1451   16
                                2        151         22          1 131 1451   17
                                3          1          1          1 131 1451   18
                                3          2          1          1 131 1451   19
                                3         16          1          1 131 1451   20
                                4          2          1          1 131 1451   21
 0.000000+0 0.000000+0          0          0          0          0 131 1  099999
 0.000000+0 0.000000+0          0          0          0          0 131 0  0    0
 1.212311+3 2.898897+0          0          0          1          0 131 2151    1
 5.513700+4 1.000000+0          0          0          1          0 131 2151    2
 1.700000+3 1.000000+5          2          1          0          0 131 2151    3
 3.500000+0 5.101200-1          0          0          3          0 131 2151    4
 1.357310+2 0.000000+0          0          0         18          3 131 2151    5
 1.800000+3          6 1.000000+0 2.078520-1 1.000000-2 0.000000+0 131 2151    6
 2.100000+3          7 2.000000+0 6.088000-1 2.000000-2 0.000000+0 131 2151    7
 3.100000+3          8 3.000000+0 3.120000-1 3.000000-2 0.000000+0 131 2151    8
 1.357310+2 0.000000+0          1          0         18          3 131 2151    9
 1.810000+3          9 4.000000+0 4.489400-1 8.000000-2 0.000000+0 131 2151   10
 2.110000+3         10 5.000000+0 8.497500-1 7.000000-2 0.000000+0 131 2151   11
 3.110000+3         11 6.000000+0 9.524900-1 6.000000-2 0.000000+0 131 2151   12
 1.100000+5 2.000000+7          2          1          0          0 131 2151   13
 2.000000+0 5.101200-1          0          0          3          0 131 2151   14
 1.357310+2 0.000000+0          2          0         18          3 131 2151   15
 1.801000+3          0 1.100000+0 3.078520-1 1.000000-2 0.000000+0 131 2151   16
 2.101000+3          1 2.100000+0 7.088000-1 2.000000-2 0.000000+0 131 2151   17
 3.101000+3          2 3.100000+0 2.120000-1 3.000000-2 0.000000+0 131 2151   18
 1.357310+2 0.000000+0          1          0         18          3 131 2151   19
 1.812000+3          3 4.100000+0 5.489400-1 8.000000-2 0.000000+0 131 2151   20
 2.112000+3          4 5.100000+0 9.497500-1 7.000000-2 0.000000+0 131 2151   21
 3.112000+3          5 6.100000+0 0.524900-1 6.000000-2 0.000000+0 131 2151   22
 0.000000+0 0.000000+0          0          0          0          0 131 2  099999
 0.000000+0 0.000000+0          0          0          0          0 131 0  0    0
 1.304918+3 2.582082+0          0          0          0          0 131 3  1    1
 0.000000+0 0.000000+0          0          0          0          0 131 3  099999
 1.001200+3 2.912396+0          0          0          0          0 131 3  2    1
 0.000000+0 0.000000+0          0          0          0          0 131 3  099999
 1.001900+3 2.988596+0          0          0          0          0 131 3 16    1
 0.000000+0 0.000000+0          0          0          0          0 131 3  099999
 0.000000+0 0.000000+0          0          0          0          0 131 0  0    0
 1.001900+3 2.989116+0          0          1          0          0 131 4  2    1
 0.000000+0 0.000000+0          0          0          0          0 131 4  099999
 0.000000+0 0.000000+0          0          0          0          0 131 0  0    0
 0.000000+0 0.000000+0          0          0          0          0   0 0  0    0
 0.000000+0 0.000000+0          0          0          0          0  -1 0  0    0
 $Rev:: 512      $  $Date:: 2006-12-05#$                             1 0  0    0
 4.019200+3 6.192500+0          1          0          0          1 419 1451    1
 0.123000+0 0.063200+0          0          0          0          6 419 1451    2
 1.000230+0 8.100130+6          1          0         10          7 419 1451    3
 0.001200+0 0.001600+0          0          0         47         10 419 1451    4
  4-Be-  7 LANL       EVAL-JUN04 E.N.Trix                          419 1451    5
                      DIST-DEC06                       20111222    419 1451    6
----ENDF/B-VII.1      MATERIAL  419                                419 1451    7
-----INCIDENT NEUTRON DATA                                         419 1451    8
------ENDF-6 FORMAT                                                419 1451    9
                                                                   419 1451   10
 ***************************************************************** 419 1451   11
dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh.       419 1451   12
Aenean quam. In scelerisque sem at dolor. Maecenas mattis. Sed     419 1451   13
convallis tristique sem.                                           419 1451   14
 ***************************************************************** 419 1451   15
                                1        451         22          1 419 1451   16
                                2        151         11          1 419 1451   17
                                3          2          1          1 419 1451   18
                                3        600          1          1 419 1451   19
                                3        650          1          1 419 1451   20
                                3        800          1          1 419 1451   21
                                4          2          2          1 419 1451   22
 0.000000+0 0.000000+0          0          0          0          0 419 1  099999
 0.000000+0 0.000000+0          0          0          0          0 419 0  0    0
 1.212311+3 2.898897+0          0          0          1          0 419 2151    1
 5.513700+4 1.000000+0          0          1          1          0 419 2151    2
 1.700000+3 1.000000+5          2          1          0          0 419 2151    3
 3.500000+0 5.101200-1          0          0         11          2 419 2151    4
 1.000000+3 1.100000+3 1.200000+3 1.300000+3 1.400000+3 1.500000+3 419 2151    5
 1.600000+3 1.700000+3 1.800000+3 1.900000+3 2.000000+3            419 2151    6
 1.419000+2 0.000000+0          0          0          2          0 419 2151    7
 0.000000+0 0.000000+0          0          1         17          0 419 2151    8
 4.190000+2 4.200000+2 4.210000+2 4.220000+2 4.230000+2 0.000000+0 419 2151    9
 2.000000+3 2.100000+3 2.200000+3 2.300000+3 2.400000+3 2.500000+3 419 2151   10
 2.600000+3 2.700000+3 2.800000+3 2.900000+3 3.000000+3            419 2151   11
 0.000000+0 0.000000+0          0          0          0          0 419 2  099999
 0.000000+0 0.000000+0          0          0          0          0 419 0  0    0
 4.284918+3 6.292347+0          0          0          0          0 419 3  2    1
 0.000000+0 0.000000+0          0          0          0          0 419 3  099999
 4.193742+3 6.287192+0          0          0          0          0 419 3600    1
 0.000000+0 0.000000+0          0          0          0          0 419 3  099999
 4.192847+3 6.874398+0          0          0          0          0 419 3650    1
 0.000000+0 0.000000+0          0          0          0          0 419 3  099999
 4.897498+3 6.287322+0          0          0          0          0 419 3800    1
 0.000000+0 0.000000+0          0          0          0          0 419 3  099999
 0.000000+0 0.000000+0          0          0          0          0 419 0  0    0
 4.898421+3 6.768123+0          0          1          0          0 419 4  2    1
 2.123124+6 8.123142-6 2.123212+6 8.231231-6-2.231211+6 8.123421-6 419 4  2    2
 0.000000+0 0.000000+0          0          0          0          0 419 4  099999
 0.000000+0 0.000000+0          0          0          0          0 419 0  0    0
 0.000000+0 0.000000+0          0          0          0          0   0 0  0    0
 0.000000+0 0.000000+0          0          0          0          0  -1 0  0    0
""")

library = Library(new_library)


def test_mats():
    for mat_id in library.mats:
        assert_in(mat_id, [128, 131, 419])


def test_get():
    obs = library.get(419, 4, 2)

    exp = np.array([4.898421e+3, 6.768123e+0, 0, 
                    1, 0, 0, 2.123124e+6, 8.123142e-6, 
                    2.123212e+6, 8.231231e-6,
                    -2.231211e+6, 8.123421e-6])    
    badkey = library.get(111, 1, 1)
    assert_array_equal(exp, obs)
    assert_equal(badkey, False)


def test_unresolved_resonances_a():
    # Case A (ENDF Manual p.70)
    
    obs = library.mat131['data']['unresolved']
    # print obs
    # assert(1==2)

    obs_D = obs[0][2][3.5,1,10]['D']
    exp_D = 2.110000e3

    obs_GNO = obs[0][2][3.5,1,10]['GNO']
    exp_GNO = 8.497500e-1
    
    new_obs = obs[1][2][2,2,1]

    new_obs_D = new_obs['D']
    new_exp_D = 2.101000e3

    new_obs_GNO = new_obs['GNO']
    new_exp_GNO = 7.088000e-1

    assert_array_equal(exp_D, obs_D)
    assert_array_equal(exp_GNO, obs_GNO)

    assert_array_equal(new_exp_D, new_obs_D)
    assert_array_equal(new_exp_GNO, new_obs_GNO)


def test_unresolved_resonances_b():
    # Case B (ENDF Manual p. 70)
    obs = library.mat419['data']['unresolved'][0][2]

    obs_ES = obs[3.5,0,419]['ES']
    exp_ES = 100 * np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) 

    obs_419_GF = obs[3.5,0,419]['GF']
    exp_419_GF = np.array([2.000000e3, 2.100000e3, 2.200000e3, 2.300000e3, 2.400000e3, 2.500000e3,
                        2.600000e3, 2.700000e3, 2.800000e3, 2.900000e3, 3.000000e3])
    
    assert_array_equal(exp_ES, obs_ES)
    assert_array_equal(exp_419_GF, obs_419_GF)


def test_unresolved_resonances_c():
    # Case C (ENDF Manual p. 70)

    obs = library.mat128['data']['unresolved'][0][2][3.5,1,4]

    obs_ES = obs['ES']
    exp_ES = np.array([1.74e3, 2.04e3, 3.04e3])

    obs_D = obs['D']
    exp_D = np.array([7.762320e3, 6.766400e3, 2.780300e3])

    assert_array_equal(exp_ES, obs_ES)
    assert_array_equal(exp_D, obs_D)

    
def test_DoubleSpinDict():
    subject = DoubleSpinDict({(3.499999999998, 2, 1):{'A':'a', 'B':'b'},
                              (2.000000000012, 3, 4):{'C':'c', 'D':'d'}})
    subject.update({(3.500000000011,8,9):{'E':'e', 'F':'f'}})
    
    obs = subject[(3.48, 8, 9)]
    exp = {'E':'e', 'F':'f'}
    assert_equal(exp, obs)


if __name__ == "__main__":
    nose.main()
