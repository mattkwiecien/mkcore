#!/usr/bin/env bash
# Script by Jack O'Donnell

# coadd_id=74346222
# DES_dir=/Users/matt/Data/DES/des_cutouts/COADD_OBJECT_ID_$coadd_id

img_id=39627775673373754
legacyhalos_dir=/Users/matt/Repos/desi-donuts/data/output/3962/$img_id

red=$legacyhalos_dir/*custom-image-z.fits.fz
green=$legacyhalos_dir/*custom-image-r.fits.fz
blue=$legacyhalos_dir/*custom-image-g.fits.fz

echo $red
echo $green
echo $blue

# ds9 -scale log -rgb \
#     -red $red -cmap value 7.4267 0.20847 \
#     -green $green -cmap value 4.62541 0.205212 \
#     -blue $blue -cmap value 6.87 0.176 \
#     -frame first -frame delete \
#     -lock frame wcs "$@"
ds9 -rgb \
    -red $red -cmap value 7.4267 0.20847 \
    -green $green -cmap value 4.62541 0.205212 \
    -blue $blue -cmap value 6.87 0.176 \
    -frame first -frame delete \
    -lock frame wcs "$@"
