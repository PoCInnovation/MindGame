#! /bin/bash -

############################################################
# Default variables                                        #
############################################################
COLOR_RED="\e[1;31m"
COLOR_GREEN="\e[1;32m"
COLOR_YELLOW="\e[1;33m"
COLOR_BLUE="\e[1;34m"
COLOR_PURPLE="\e[1;35m"
COLOR_CYAN="\e[1;36m"
COLOR_RESET="\e[0m"

PATH_PYTHON=`python -c "import sys; print(sys.executable)"`
PATH_ENVRC=`pwd`/.env
CONDA_ENV=${PWD##*/}

BUCKET_NAME="mindgame"
DVC_REMOTE="s3://$BUCKET_NAME/storage"
AWS_PROFILE="$BUCKET_NAME"

############################################################
# Help                                                     #
############################################################
Help()
{
   # Display Help
   echo "Script to execute after the git clone of the project"
   echo "IT MUST BE LAUNCHED FROM THE PROJECT TOP DIRECTORY"
   echo
   echo "usage: bash .AI/init.sh [--help] [python_path]"
   echo "options:"
   echo "	--help          Print this Help."
   echo "   python_path     Optional path to python interpreter."
   echo "                   Defaults to: $PATH_PYTHON"
   echo
}

############################################################
############################################################
# Main program                                             #
############################################################
############################################################


############################################################
# Process the input options. Add options as needed.        #
############################################################
while test $# -gt 0
do
    case "$1" in
        --help) # Display Help
			Help
			exit 0
            ;;
        --*) # Bad option used
			echo "bad option $1"
			echo
			Help
			exit 1
            ;;
        *) # Setting up python path
			PATH_PYTHON=$1
			echo "Python path for this script has been set to: $PATH_PYTHON"
            ;;
    esac
    shift
done


echo -e $COLOR_YELLOW ".AI/init.sh" $COLOR_RESET "Welcome to our project initilizer"
echo -e "    Variables:"
echo -e "\t" $COLOR_BLUE "PATH_PYTHON=" $COLOR_RESET  $PATH_PYTHON
echo -e "\t" $COLOR_BLUE "PATH_ENVRC=" $COLOR_RESET  $PATH_ENVRC
echo -e "\t" $COLOR_BLUE "CONDA_ENV=" $COLOR_RESET  $CONDA_ENV
echo -e "\t" $COLOR_BLUE "DVC_REMOTE=" $COLOR_RESET  $DVC_REMOTE
echo -e "\t" $COLOR_BLUE "AWS_PROFILE=" $COLOR_RESET  $AWS_PROFILE
echo -e "\t" $COLOR_BLUE "CI=" $COLOR_RESET  $CI


############################################################
# CONDA Environment                                        #
############################################################

echo -e $COLOR_YELLOW "INIT: " $COLOR_RESET "Testing your conda environment..."

if [[ "$CI" ]]
then
    echo -e $COLOR_PURPLE "Skipping test because we are in Github actions" $COLOR_RESET
elif [ -z "$CONDA_DEFAULT_ENV" ]
then
    echo -e $COLOR_RED "No conda environment" $COLOR_RESET
	echo "You can create one by executing the folowing command:"
    echo -e $COLOR_YELLOW "conda create -n $CONDA_ENV python=3.8" "\n" "conda activate $CONDA_ENV" $COLOR_RESET
	exit 1

elif [ "$CONDA_DEFAULT_ENV" == "$CONDA_ENV" ]
then
    echo -e $COLOR_GREEN "Good conda environment" $COLOR_RESET

# elif [ "$CONDA_DEFAULT_ENV" == "base" ]
else
    echo -e $COLOR_RED "Conda environment is not active" $COLOR_RESET

	echo "If necessary, you can create your environment with:"
    echo -e $COLOR_YELLOW "conda create -n $CONDA_ENV python=3.8" $COLOR_RESET

	echo "Activate your environment with:"
    echo -e $COLOR_YELLOW "conda activate $CONDA_ENV" $COLOR_RESET
	exit 1
fi


############################################################
# aws cli                                                  #
############################################################

echo -e $COLOR_YELLOW "INIT: " $COLOR_RESET "Verifying if aws cli is installed"

if [[ "$CI" ]]
then
    echo -e $COLOR_PURPLE "Skipping test because we are in Github actions" $COLOR_RESET
elif aws --version;
then
    echo -e $COLOR_GREEN "aws is installed !" $COLOR_RESET
else
    echo -e $COLOR_RED "ERROR: aws is not installed, please follow the steps in Setup.md" $COLOR_RESET
	exit 1
fi


echo -e $COLOR_YELLOW "INIT: " $COLOR_RESET "Verifying that aws cli is configured"
if [[ "$CI" ]]
then
    echo -e $COLOR_PURPLE "Skipping test because we are in Github actions" $COLOR_RESET
elif [[ $(aws configure get aws_access_key_id) ]]; then
    echo -e $COLOR_GREEN "aws is configured !" $COLOR_RESET
elif [[ $(aws configure get aws_access_key_id --profile $AWS_PROFILE) ]]; then
    echo -e $COLOR_GREEN "aws is configured !" $COLOR_RESET
else
    echo -e $COLOR_RED "ERROR: aws is not configured, please run:" $COLOR_RESET
	echo -e $COLOR_YELLOW "aws configure --profile $AWS_PROFILE" $COLOR_RESET
	echo "Think of then adding your AWS_PROFILE environment variable to conda"
	echo -e $COLOR_YELLOW "conda env config vars set AWS_PROFILE=$AWS_PROFILE" $COLOR_RESET
	echo -e $COLOR_YELLOW "conda activate $CONDA_ENV" $COLOR_RESET
	exit 1
fi


############################################################
# DVC                                                      #
############################################################

echo -e $COLOR_YELLOW "INIT: " $COLOR_RESET "Verifying that DVC remote is setup"

if [[ "$CI" ]]
then
    echo -e $COLOR_PURPLE "Skipping test because we are in Github actions" $COLOR_RESET
elif [[ $(dvc remote list | grep s3-remote) ]]; then
    echo -e $COLOR_GREEN "DVC remote is already setup!" $COLOR_RESET
else
	echo -e $COLOR_RED "ERROR: " $COLOR_RESET "DVC remote is not yet setup"

	echo "Add dvc remote with:"
	echo -e $COLOR_YELLOW "dvc remote add -f s3-remote $DVC_REMOTE" $COLOR_RESET
	exit 1
fi


echo -e $COLOR_YELLOW "INIT: " $COLOR_RESET "Pulling DVC data !"
echo "Please synchronize your data with:"
echo -e $COLOR_YELLOW "dvc pull -r s3-remote" $COLOR_RESET


echo -e $COLOR_GREEN "PROJECT IS FULLY INITIALIZED <3" $COLOR_RESET
