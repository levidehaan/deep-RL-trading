import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec

# Fixing random state for reproducibility
np.random.seed(19680801)


data = [203.40307009, 223.4719321 , 228.1811464 , 254.3000196 ,
       256.55447703, 268.62005099, 278.6640559 , 294.83409517,
       296.64767794, 302.76017963, 301.45127903, 293.0361667 ,
       299.31591779, 287.78210914, 285.3634384 , 261.54946461,
       248.48695054, 240.38665203, 229.18516501, 241.18335408,
       238.22147727, 214.69316241, 206.2772102 , 211.28277884,
       210.1978592 , 198.84497848, 211.90666287, 228.71646184,
       215.2043186 , 222.32752717, 226.64012093, 239.55712854,
       242.58614692, 247.57977383, 253.28069437, 280.2509976 ,
       277.07017473, 279.26628783, 297.40729132, 286.35984194,
       279.5437468 , 278.47154621, 271.13044467, 279.08587477,
       270.12762561, 265.53016023, 254.83969597, 233.85129703,
       224.00862936, 192.914501  , 184.49629277, 172.69893599,
       175.14651349, 137.34202626, 127.73680515, 131.61483061,
       115.12536537, 125.28615641, 125.03662307, 123.8816043 ,
       109.15423017, 113.66353036, 109.35840505, 141.34330573,
       128.39787194, 155.07143395, 165.45205592, 180.15569572,
       193.04399272, 190.80957038, 220.10037852, 233.95383564,
       222.61386259, 247.794505  , 254.89901252, 268.86363577,
       242.9821494 , 255.10837134, 266.04911105, 256.55794488,
       247.84440951, 243.16125581, 257.26939399, 240.93883651,
       236.98868582, 246.64517713, 199.89879925, 239.55931563,
       243.39699964, 275.78222886, 272.14166625, 276.36548878,
       283.06350142, 264.36186198, 248.96703844, 215.86000036,
       207.83471661, 192.9080875 , 206.19436642, 193.76045265,
       203.17002384, 214.49884266, 228.66798781, 252.92618863,
       288.71932001, 302.72840614, 311.712534  , 314.26709087,
       308.49737644, 306.28010978, 301.1755718 , 253.51856372,
       283.94919301, 300.62662516, 318.27789819, 310.93779404,
       312.94470261, 315.59557886, 336.21670544, 325.74129146,
       317.12054094, 301.71189308, 305.77937651, 284.25892521,
       264.93562991, 242.0229735 , 223.25514339, 245.71426268,
       264.09899971, 267.39689507, 270.9914839 , 276.86934585,
       258.58708868, 246.98456092, 232.77001674, 212.52996244,
       211.48908228, 170.73943592, 158.55812211, 150.19766322,
       123.76822961, 135.40913793, 129.05790121, 129.82495537,
       150.09378712, 168.73497518, 176.19206204, 185.00936467,
       198.2303017 , 222.43043822, 203.74355168, 225.903195  ,
       220.13895899, 213.17510348, 183.08026084, 188.95096485,
       156.94235182, 156.43510276, 165.83146335, 168.80000741,
       172.49241669, 179.28444218, 185.13939887, 185.98809131,
       185.06863913, 190.42525303, 190.80002953, 192.47019449,
       199.35610114, 199.00185583, 201.43243897, 193.4187208 ,
       203.01568558, 203.50664869, 193.64186012, 201.38467444,
       200.60118337, 200.94822473, 202.23246191, 197.63847832]
dt = 1
t = np.arange(0, len(data), dt)
nse = np.random.randn(len(t))
r = np.exp(-t / 0.05)

cnse = np.convolve(nse, r) * dt
cnse = cnse[:len(t)]
s = 0.1 * np.sin(2 * np.pi * t) + cnse

plt.subplot(211)
plt.plot(t, data)
plt.subplot(212)
t2 = np.arange(0, 40)
plt.plot(t2, data[:40])

plt.show()
