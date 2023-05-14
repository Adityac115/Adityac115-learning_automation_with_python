#!/bin/bash 


#############################
#
#
# Author : Aditya
#
#
#
############################


if [ ${#@} -lt 2  ]; then
	echo "usage: $0 [your github token] [REST expression] "
	exit 1;
fi



GIT_TOKEN=$1
GIT_API_URL=$2
GIT_LINK=https://api.github.com$GIT_API_URL
GIT_HEADER_ACCEPT="Accept: application/vnd.github+json"

temp="basename $0"
TMPFILE="mktemp /tmp/${temp}.XXXXXX" || exit 1

curl -s -L  -H $GIT_HEADER_ACCEPT   -H "Authorization: Bearer $GIT_TOKEN"  -H "X-GitHub-Api-Version: 2022-11-28"  $GIT_LINK 

