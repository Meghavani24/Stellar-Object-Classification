The data consists of 100,000 observations of space taken by the SDSS (Sloan Digital Sky Survey). Every data point is described by 17 feature columns and 1 class column which identifies it to be either a star, galaxy, or quasar 
Features in the dataset:
obj_ID = Object Identifier, the unique value that identifies the object in the image catalog used by the CAS.
alpha = Right Ascension angle (at J2000 epoch).
delta = Declination angle (at J2000 epoch).
u = Ultraviolet filter in the photometric system.
g = Green filter in the photometric system.
r = Red filter in the photometric system.
i = Near Infrared filter in the photometric system.
z = Infrared filter in the photometric system.
run_ID = Run Number used to identify the specific scan.
rereun_ID = Rerun Number to specify how the image was processed.
cam_col = Camera column to identify the scanline within the run.
field_ID = Field number to identify each field.
spec_obj_ID = Unique ID used for optical spectroscopic objects (this means that 2 different observations with the same spec_obj_ID must share the output class).
class = Object class (galaxy, star, or quasar object).
redshift = Redshift value based on the increase in wavelength.
plate = Plate ID, identifies each plate in SDSS.
MJD = Modified Julian Date, used to indicate when a given piece of SDSS data was taken.
fiber_ID = Fiber ID that identifies the fiber that pointed the light at the focal plane in each observation.
