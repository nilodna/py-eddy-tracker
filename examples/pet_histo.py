"""
Parameter Histogram
===================

"""
from matplotlib import pyplot as plt
from py_eddy_tracker.observations.tracking import TrackEddiesObservations
import py_eddy_tracker_sample
from numpy import arange

a = TrackEddiesObservations.load_file(
    py_eddy_tracker_sample.get_path("eddies_med_adt_allsat_dt2018/Anticyclonic.zarr")
)
c = TrackEddiesObservations.load_file(
    py_eddy_tracker_sample.get_path("eddies_med_adt_allsat_dt2018/Cyclonic.zarr")
)
kwargs_a = dict(label="Anticyclonic", color="r")
kwargs_c = dict(label="Cyclonic", color="b")

# Plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(a["amplitude"], histtype="step", bins=arange(0.0005, 1, 0.002), **kwargs_a)
ax.hist(c["amplitude"], histtype="step", bins=arange(0.0005, 1, 0.002), **kwargs_c)
ax.set_xlabel("Amplitude (m)")
ax.set_xlim(0, 0.5)
ax.legend()
ax.grid()

fig = plt.figure()
ax = fig.add_subplot(111)
bins = arange(0, 200, 1)
ax.hist(a["radius_s"] / 1000.0, histtype="step", bins=bins, **kwargs_a)
ax.hist(c["radius_s"] / 1000.0, histtype="step", bins=bins, **kwargs_c)
ax.set_xlabel("Speed_radius (km)")
ax.set_xlim(0, 150)
ax.legend()
ax.grid()

fig = plt.figure()
ax = fig.add_subplot(111)
bins = arange(0, 100, 1)
ax.hist(a["speed_average"] * 100.0, histtype="step", bins=bins, **kwargs_a)
ax.hist(c["speed_average"] * 100.0, histtype="step", bins=bins, **kwargs_c)
ax.set_xlabel("speed_average (cm/s)")

ax.set_xlim(0, 50)
ax.legend()
ax.grid()
