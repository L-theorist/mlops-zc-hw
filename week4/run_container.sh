docker run -it --name my_app --rm -e AWS_DEFAULT_REGION="eu-west-3" -v ~/.aws/credentials:/root/.aws/credentials:ro my_predictor_image
