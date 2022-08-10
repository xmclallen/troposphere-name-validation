set -o verbose

#build the image
docker build -t troposphere-test .

############################################################################
#
# run the test
#
############################################################################

docker run --name ubuntu_bash --rm -i -t troposphere-test python -m unittest test.py
