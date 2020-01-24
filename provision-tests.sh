#!/bin/bash

orig_dir=$(pwd)
OUTDIR="./test-data"

mkdir -p "$OUTDIR"

while read line; do
	words=( $line )
	repo_url="${words[0]}"
	repo_name="${words[1]}"
	version="${words[2]}"
	dest="./${OUTDIR}/${repo_name}"
	if [[ ! -d "${dest}/.git" ]]; then
		git clone "$repo_url" "$dest"
	fi
	cd "$dest"
	git checkout "$version"
	cd "$orig_dir"
done < ./test-repositories.list
