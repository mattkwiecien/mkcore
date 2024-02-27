# Steps needed to be done to build an mpi4py ready conda branch at NERSC 
# Add to .bash_profile
export LD_LIBRARY_PATH=/opt/cray/pe/mpt/7.7.10/gni/mpich-gnu-abi/8.2/lib:$LD_LIBRARY_PATH 

module load python 

# Create a base mpi env
conda create -n mpi python=3.10 -y 
conda activate mpi
conda install -c conda-forge  "mpich=4.0.3=external_*" mpi4py 

# Clone the env into whatever env you want to create
conda create --clone mpi --name tjpcov

# Install the rest of your dependencies
conda install -c conda-forge scipy numpy Jinja2 pyyaml pytest pyccl>=2.5.0 sacc>=0.7 camb healpy h5py