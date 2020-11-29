sudo amazon-linux-extras install epel

sudo yum -y install bzip2-devel       \
                    gcc               \
                    git               \
                    openssl-devel     \
                    postgresql-devel  \
                    python-devel      \
                    python-setuptools \
                    readline-devel    \
                    sqlite-devel      \
                    zlib-devel

python -m pip install --upgrade pip setuptools wheel

pyenv install 3.6.12

pip install pandas==1.1.1 psycopg2-binary==2.8 -t .

zip -r psycopg2-binary-2.8.zip .

aws s3 cp psycopg2-binary-2.8.zip s3://emp.s3.bucket/psycopg2-binary-2.8.zip
