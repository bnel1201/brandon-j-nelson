---
aliases:
- /math/2021/01/31/Empirical Beam Hardening Correction for X-Ray Grating Interferometry
categories:
- math
date: '2021-01-31'
hide: false
layout: post
title: Empirical Beam Hardening Correction for X-Ray Grating Interferometry (EBHC-GI)
toc: true

---

Recently, my first first-author manuscript related to my thesis work on x-ray phase contrast was published. The paper summarizes artifacts experienced while using a tabletop x-ray phase contrast micro-CT system. While the focus of the paper is limited to grating-based x-ray phase contrast systems, the empirical methods used to solve the beam hardening problem are quite generalizable. I first learned about these interpolation-based empirical corrections from researching previous x-ray corrections that are referenced in the paper, but along the way I enjoyed digging more into the math of solving least squares problems and how they are implemented. The following tutorials document some of my explorations and provide background to the paper.

## Manuscript Citation and Links

- **Nelson, B.J.**, Leng, S., Shanblatt, E.R., McCollough, C.H. and Koenig, T. (2021), Empirical beam hardening and ring artifact correction for x‐ray grating interferometry (EBHC‐GI). Med Phys. <https://doi.org/10.1002/mp.14672>
  - [pre-peer reviewed version](../assets/EBHC-GI.pdf)

## Related Tutorials

- [solving interpolation problems with Vandermonde Matrices](2021-01-27-Vandermonde Interpolation.ipynb)
- [performing matrix inversion via LU decomposition](2021-01-28-LU Solving.ipynb)
- [using interpolation to fix image artifacts in CT](2021-01-29-Vandermonde Matrices in Beam Hardening Corrections.ipynb)
  - this tutorial is built upon the previous two but is most related to the paper
