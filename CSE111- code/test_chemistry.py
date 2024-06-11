from chemistry import get_name, get_atomic_mass, \
        parse_formula, molar_mass, FormulaError
from pytest import approx
import pytest


def test_names():
    """Test the chemistry.get_name function."""
    # TODO: write this function.
    assert get_name("Ac") == "Actinium"
    assert get_name("Ag") == "Silver"
    assert get_name("Al") == "Aluminum"
    assert get_name("Am") == "Americium"
    assert get_name("Ar") == "Argon"
    assert get_name("As") == "Arsenic"
    assert get_name("At") == "Astatine"
    assert get_name("Au") == "Gold"
    assert get_name("B") == "Boron"
    assert get_name("Ba") == "Barium"
    assert get_name("Be") == "Beryllium"
    assert get_name("Bh") == "Bohrium"
    assert get_name("Bi") == "Bismuth"
    assert get_name("Bk") == "Berkelium"
    assert get_name("Br") == "Bromine"
    assert get_name("C") == "Carbon"
    assert get_name("Ca") == "Calcium"
    assert get_name("Cd") == "Cadmium"
    assert get_name("Ce") == "Cerium"
    assert get_name("Cf") == "Californium"
    assert get_name("Cl") == "Chlorine"
    assert get_name("Cm") == "Curium"
    assert get_name("Cn") == "Copernicium"
    assert get_name("Co") == "Cobalt"
    assert get_name("Cr") == "Chromium"
    assert get_name("Cs") == "Cesium"
    assert get_name("Cu") == "Copper"
    assert get_name("Db") == "Dubnium"
    assert get_name("Ds") == "Darmstadtium"
    assert get_name("Dy") == "Dysprosium"
    assert get_name("Er") == "Erbium"
    assert get_name("Es") == "Einsteinium"
    assert get_name("Eu") == "Europium"
    assert get_name("F") == "Fluorine"
    assert get_name("Fe") == "Iron"
    assert get_name("Fl") == "Flerovium"
    assert get_name("Fm") == "Fermium"
    assert get_name("Fr") == "Francium"
    assert get_name("Ga") == "Gallium"
    assert get_name("Gd") == "Gadolinium"
    assert get_name("Ge") == "Germanium"
    assert get_name("H") == "Hydrogen"
    assert get_name("He") == "Helium"
    assert get_name("Hf") == "Hafnium"
    assert get_name("Hg") == "Mercury"
    assert get_name("Ho") == "Holmium"
    assert get_name("Hs") == "Hassium"
    assert get_name("I") == "Iodine"
    assert get_name("In") == "Indium"
    assert get_name("Ir") == "Iridium"
    assert get_name("K") == "Potassium"
    assert get_name("Kr") == "Krypton"
    assert get_name("La") == "Lanthanum"
    assert get_name("Li") == "Lithium"
    assert get_name("Lr") == "Lawrencium"
    assert get_name("Lu") == "Lutetium"
    assert get_name("Lv") == "Livermorium"
    assert get_name("Mc") == "Moscovium"
    assert get_name("Md") == "Mendelevium"
    assert get_name("Mg") == "Magnesium"
    assert get_name("Mn") == "Manganese"
    assert get_name("Mo") == "Molybdenum"
    assert get_name("Mt") == "Meitnerium"
    assert get_name("N") == "Nitrogen"
    assert get_name("Na") == "Sodium"
    assert get_name("Nb") == "Niobium"
    assert get_name("Nd") == "Neodymium"
    assert get_name("Ne") == "Neon"
    assert get_name("Nh") == "Nihonium"
    assert get_name("Ni") == "Nickel"
    assert get_name("No") == "Nobelium"
    assert get_name("Np") == "Neptunium"
    assert get_name("O") == "Oxygen"
    assert get_name("Og") == "Oganesson"
    assert get_name("Os") == "Osmium"
    assert get_name("P") == "Phosphorus"
    assert get_name("Pa") == "Protactinium"
    assert get_name("Pb") == "Lead"
    assert get_name("Pd") == "Palladium"
    assert get_name("Pm") == "Promethium"
    assert get_name("Po") == "Polonium"
    assert get_name("Pr") == "Praseodymium"
    assert get_name("Pt") == "Platinum"
    assert get_name("Pu") == "Plutonium"
    assert get_name("Ra") == "Radium"
    assert get_name("Rb") == "Rubidium"
    assert get_name("Re") == "Rhenium"
    assert get_name("Rf") == "Rutherfordium"
    assert get_name("Rg") == "Roentgenium"
    assert get_name("Rh") == "Rhodium"
    assert get_name("Rn") == "Radon"
    assert get_name("Ru") == "Ruthenium"
    assert get_name("S") == "Sulfur"
    assert get_name("Sb") == "Antimony"
    assert get_name("Sc") == "Scandium"
    assert get_name("Se") == "Selenium"
    assert get_name("Sg") == "Seaborgium"
    assert get_name("Si") == "Silicon"
    assert get_name("Sm") == "Samarium"
    assert get_name("Sn") == "Tin"
    assert get_name("Sr") == "Strontium"
    assert get_name("Ta") == "Tantalum"
    assert get_name("Tb") == "Terbium"
    assert get_name("Tc") == "Technetium"
    assert get_name("Te") == "Tellurium"
    assert get_name("Th") == "Thorium"
    assert get_name("Ti") == "Titanium"
    assert get_name("Tl") == "Thallium"
    assert get_name("Tm") == "Thulium"
    assert get_name("Ts") == "Tennessine"
    assert get_name("U") == "Uranium"
    assert get_name("V") == "Vanadium"
    assert get_name("W") == "Tungsten"
    assert get_name("Xe") == "Xenon"
    assert get_name("Y") == "Yttrium"
    assert get_name("Yb") == "Ytterbium"
    assert get_name("Zn") == "Zinc"
    assert get_name("Zr") == "Zirconium"


def test_atomic_masses():
    """Test the chemistry.get_atomic_mass function."""
    # TODO: write this function.
    assert get_atomic_mass("Ac") == 227
    assert get_atomic_mass("Ag") == 107.8682
    assert get_atomic_mass("Al") == 26.9815386
    assert get_atomic_mass("Am") == 243
    assert get_atomic_mass("Ar") == 39.948
    assert get_atomic_mass("As") == 74.9216
    assert get_atomic_mass("At") == 210
    assert get_atomic_mass("Au") == 196.966569
    assert get_atomic_mass("B") == 10.811
    assert get_atomic_mass("Ba") == 137.327
    assert get_atomic_mass("Be") == 9.012182
    assert get_atomic_mass("Bh") == 272
    assert get_atomic_mass("Bi") == 208.9804
    assert get_atomic_mass("Bk") == 247
    assert get_atomic_mass("Br") == 79.904
    assert get_atomic_mass("C") == 12.0107
    assert get_atomic_mass("Ca") == 40.078
    assert get_atomic_mass("Cd") == 112.411
    assert get_atomic_mass("Ce") == 140.116
    assert get_atomic_mass("Cf") == 251
    assert get_atomic_mass("Cl") == 35.453
    assert get_atomic_mass("Cm") == 247
    assert get_atomic_mass("Cn") == 285
    assert get_atomic_mass("Co") == 58.933195
    assert get_atomic_mass("Cr") == 51.9961
    assert get_atomic_mass("Cs") == 132.9054519
    assert get_atomic_mass("Cu") == 63.546
    assert get_atomic_mass("Db") == 268
    assert get_atomic_mass("Ds") == 281
    assert get_atomic_mass("Dy") == 162.5
    assert get_atomic_mass("Er") == 167.259
    assert get_atomic_mass("Es") == 252
    assert get_atomic_mass("Eu") == 151.964
    assert get_atomic_mass("F") == 18.9984032
    assert get_atomic_mass("Fe") == 55.845
    assert get_atomic_mass("Fl") == 289
    assert get_atomic_mass("Fm") == 257
    assert get_atomic_mass("Fr") == 223
    assert get_atomic_mass("Ga") == 69.723
    assert get_atomic_mass("Gd") == 157.25
    assert get_atomic_mass("Ge") == 72.64
    assert get_atomic_mass("H") == 1.00794
    assert get_atomic_mass("He") == 4.002602
    assert get_atomic_mass("Hf") == 178.49
    assert get_atomic_mass("Hg") == 200.59
    assert get_atomic_mass("Ho") == 164.93032
    assert get_atomic_mass("Hs") == 270
    assert get_atomic_mass("I") == 126.90447
    assert get_atomic_mass("In") == 114.818
    assert get_atomic_mass("Ir") == 192.217
    assert get_atomic_mass("K") == 39.0983
    assert get_atomic_mass("Kr") == 83.798
    assert get_atomic_mass("La") == 138.90547
    assert get_atomic_mass("Li") == 6.941
    assert get_atomic_mass("Lr") == 262
    assert get_atomic_mass("Lu") == 174.9668
    assert get_atomic_mass("Lv") == 293
    assert get_atomic_mass("Mc") == 288
    assert get_atomic_mass("Md") == 258
    assert get_atomic_mass("Mg") == 24.305
    assert get_atomic_mass("Mn") == 54.938045
    assert get_atomic_mass("Mo") == 95.96
    assert get_atomic_mass("Mt") == 276
    assert get_atomic_mass("N") == 14.0067
    assert get_atomic_mass("Na") == 22.98976928
    assert get_atomic_mass("Nb") == 92.90638
    assert get_atomic_mass("Nd") == 144.242
    assert get_atomic_mass("Ne") == 20.1797
    assert get_atomic_mass("Nh") == 284
    assert get_atomic_mass("Ni") == 58.6934
    assert get_atomic_mass("No") == 259
    assert get_atomic_mass("Np") == 237
    assert get_atomic_mass("O") == 15.9994
    assert get_atomic_mass("Og") == 294
    assert get_atomic_mass("Os") == 190.23
    assert get_atomic_mass("P") == 30.973762
    assert get_atomic_mass("Pa") == 231.03588
    assert get_atomic_mass("Pb") == 207.2
    assert get_atomic_mass("Pd") == 106.42
    assert get_atomic_mass("Pm") == 145
    assert get_atomic_mass("Po") == 209
    assert get_atomic_mass("Pr") == 140.90765
    assert get_atomic_mass("Pt") == 195.084
    assert get_atomic_mass("Pu") == 244
    assert get_atomic_mass("Ra") == 226
    assert get_atomic_mass("Rb") == 85.4678
    assert get_atomic_mass("Re") == 186.207
    assert get_atomic_mass("Rf") == 267
    assert get_atomic_mass("Rg") == 280
    assert get_atomic_mass("Rh") == 102.9055
    assert get_atomic_mass("Rn") == 222
    assert get_atomic_mass("Ru") == 101.07
    assert get_atomic_mass("S") == 32.065
    assert get_atomic_mass("Sb") == 121.76
    assert get_atomic_mass("Sc") == 44.955912
    assert get_atomic_mass("Se") == 78.96
    assert get_atomic_mass("Sg") == 271
    assert get_atomic_mass("Si") == 28.0855
    assert get_atomic_mass("Sm") == 150.36
    assert get_atomic_mass("Sn") == 118.71
    assert get_atomic_mass("Sr") == 87.62
    assert get_atomic_mass("Ta") == 180.94788
    assert get_atomic_mass("Tb") == 158.92535
    assert get_atomic_mass("Tc") == 98
    assert get_atomic_mass("Te") == 127.6
    assert get_atomic_mass("Th") == 232.03806
    assert get_atomic_mass("Ti") == 47.867
    assert get_atomic_mass("Tl") == 204.3833
    assert get_atomic_mass("Tm") == 168.93421
    assert get_atomic_mass("Ts") == 294
    assert get_atomic_mass("U") == 238.02891
    assert get_atomic_mass("V") == 50.9415
    assert get_atomic_mass("W") == 183.84
    assert get_atomic_mass("Xe") == 131.293
    assert get_atomic_mass("Y") == 88.90585
    assert get_atomic_mass("Yb") == 173.054
    assert get_atomic_mass("Zn") == 65.38
    assert get_atomic_mass("Zr") == 91.224



def test_parse():
    """Test the chemistry.parse_formula function."""
    # TODO: write this function.
    assert parse_formula("O3") == {'O': 3}
    assert parse_formula("H2O") == {"H":2, "O":1}
    assert parse_formula("C6H12O6") == {"C": 6, "H": 12, "O":6}
    assert parse_formula("PO4H2(CH2)12CH3") == {"P":1, "O":4, "H":29, "C":13}
    assert parse_formula("L")
    assert parse_formula("4H")
    assert parse_formula("H2L4")
    assert parse_formula("-H")
    assert parse_formula("(H2O")
    assert parse_formula("H2)O3")



def test_molar_mass():
    """Test the chemistry.molar_mass function."""
    # TODO: write this function.
    assert molar_mass(parse_formula("H2O")) == 18.01528
    assert molar_mass(parse_formula("C6H6")) == 78.11184
    assert molar_mass(parse_formula("PO4H2(CH2)12CH3")) == approx(280.34072, 0.01)

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=no", "test_chemistry.py"])
