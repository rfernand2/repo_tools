# install ODBC 17 driver for XT
sudo -i # enter root mode

apt-get update \
    && apt-get install -y curl \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc 

# add dev files for odbc (specifically sql.h)
# (as root)
apt-get install -y unixodbc-dev \
    # Install Common Dependencies
    && apt-get update  \
    && apt-get install -y --no-install-recommends libmlx4-1 libmlx5-1 librdmacm1 libibverbs1 libmthca1 libdapl2 dapl2-utils \
        openssh-client openssh-server iproute2 \
    && apt-get install -y build-essential bzip2 git wget cpio  \
    && apt-get clean -y 
exit  # from root

# install XT in xt_shared environment
conda create -y -n xt_shared python=3.10
conda activate xt_shared
pip install xtlib==0.0.326
conda deactivate

