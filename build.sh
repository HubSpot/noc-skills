#!/bin/bash

version=0.1

rpmbuilddir="$(pwd)/rpmbuild-$(date +%s)"


# Create RPM build structure
echo "Creating RPM build structure"
mkdir ./RPMs
mkdir ${rpmbuilddir}
for d in BUILD RPMS SOURCES SPECS; do
    mkdir ${rpmbuilddir}/${d}
done

# Create Web source archive
echo "Creating NocSkillsWeb tarball"
tar -zcvf ${rpmbuilddir}/SOURCES/noc-skills-web-${version}.tar.gz NocSkillsWeb/* resources/*

# Run the NocSkillsWeb build
echo "Running NocSkillsWeb rpmbuild"
rpmbuild -ba --define "_topdir ${rpmbuilddir}" --define "version ${version}" noc-skills-web.spec

if [ $? -eq 0 ]; then
    echo "Copying noc-skills-web RPM to dist directory"
    cp ${rpmbuilddir}/RPMS/noarch/noc-skills-web-${version}-1.noarch.rpm ./RPMs/
else
    echo "[FAILURE] noc-skills-web RPM build failed"
    exit 1
fi

# Create API source archive
echo "Creating NocSkillsAPI tarball"
tar -zcvf ${rpmbuilddir}/SOURCES/noc-skills-api-${version}.tar.gz NocSkillsAPI/*

# Run the NocSkillsAPI build
echo "Running NocSkillsAPI rpmbuild"
rpmbuild -ba --define "_topdir ${rpmbuilddir}" --define "version ${version}" noc-skills-api.spec

if [ $? -eq 0 ]; then
    echo "Copying noc-skills-api RPM to dist directory"
    cp ${rpmbuilddir}/RPMS/noarch/noc-skills-api-${version}-1.noarch.rpm ./RPMs/
else
    echo "[FAILURE] noc-skills-api RPM build failed"
    exit 1
fi

# Create the Mongo source archive
echo "Creating NocSkillsMongo tarball"
tar -zcvf ${rpmbuilddir}/SOURCES/noc-skills-mongo-${version}.tar.gz NocSkillsMongo/*

# Run the NocSkillsMongo build
echo "Running the NocSkillsMongo build"
rpmbuild -ba --define "_topdir ${rpmbuilddir}" --define "version ${version}" noc-skills-mongo.spec

if [ $? -eq 0 ]; then
    echo "Copying mongo-skills-mongo RPM to dist directory"
    cp ${rpmbuilddir}/RPMS/noarch/noc-skills-mongo-${version}-1.noarch.rpm ./RPMs/
else
    echo "[FAILURE] noc-skills-mongo RPM build failed"
    exit 1
fi

rm -rf ${rpmbuilddir}