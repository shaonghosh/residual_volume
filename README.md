# Residual Volume

## Introduction 
This small script is inspired from the youtube video by user: 3Blue1Brown (https://www.youtube.com/watch?v=zwAD6dRSVyI&frags=pl%2Cwn).
The video discusses visualization of hypercubes in dimensions greater than 3 with hyper-spheres in their vertices with diameters
equal to the side of the hyper-cubes. This act will create a 'gap' in the hyper-cube that allows us to put another hyper-sphere
with its center coinciding with the center of the hyper-cube. It was illustrated in the video how the radius of this central
hyper-sphere will depend on the dimensionality of the space. Specifically, the radius of the central hyper-sphere gets larger
for higher dimensions. 

## Residual volume computation

This observation led me to wonder how much of the volume is actually available for the central hyper-sphere. Since we are putting
the hyper-spheres in each vertices of the hyper-cube, if we extend the hyper-cube to a hyper-lattice, we can imagine each hyper-sphere
being shared by 2^N of adjacent hyper-cubes where N is the number of dimensions. Thus a single hyper-cube will get 1/(2^N)th 
share of each hyper-sphere from each of the 2^N hyper-spheres in its 2^N vertices. Thus, the total volume of the hyper-spheres 
enclosed within the hyper-cube is same a that of a single hyper-cube in the vertices. Now if we are to put a hyper-sphere at the
center of the hyper-cube, the largest radius of this non-overlapping hyper-sphere that we can put given by N^(1/2) - 1, where
the sides of the hyper-cube are 2 units and the radius of the hyper-spheres is 1 unit. We define the residual volume as,
Volume of the hyper-cube - volume of one hyper-sphere at the vertex - volume of the hyper-sphere at the center.

## Observation 

It was observed that this residual volume gets larger with increasing dimensionality of the space until D<6, and then the 
residual volume gets lower and beyond D>6.5 the residual volume is negative, meaning the volume of the hyper-cube is smaller than the
volume of the combined volume occupied by the hyper-spheres. It was also observed that the difference between the volumes of the hyper-cube and the central hyper-sphere follows the same trend. 
However, when we plot the fractional residual volume, which is the residual volume divided by the volume of the hyper-cube, and the fraction difference between the hyper-cube's volume and the hyper-sphere's volume then we note the following:
The fractional difference between the volume of the hyper-cube and the hyper-sphere is a monotonically decreasing function of the dimensionality. This implies that with increasing dimesionality, the hyper-sphere contains greater and greater volume fraction of the hyper-cube. This is corollary to the point made in the video, namely, the "proportion of the inner-sphere lying inside the box decreases exponentially towards zero as the dimension keeps increasing".
What is interesting though is that the fractional residual volume peaks somewhere between D=4 and D=5, where close to 40% of the hyper-cube is still empty. This means that while the central hyper-sphere keeps increasing in volume, up to D of 4.4 or so, the volume of the other spheres in the vertices contributes lesser and lesser to the volume enclosed by the hyper-cube (as shown by the dotted black curve, which depicts the ratio of the the volume contributions from the hyper-spheres at the vertices and the volume of the hyper-cube), until at about D=4.4 the central hyper-sphere completely takes over this contribution.
