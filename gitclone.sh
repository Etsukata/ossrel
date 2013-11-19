#!/bin/sh

URLS=(
# Kernel/VM
    "git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git"
    "git://git.qemu.org/qemu.git"
    "git://git.fedorahosted.org/virt-manager.git"
    "git://libvirt.org/libvirt.git"
# DataBase
    "https://github.com/basho/riak.git"
    "https://github.com/mongodb/mongo.git"
    "git://git.postgresql.org/git/postgresql.git"
# Language
    "https://github.com/python/cpython.git"
    "https://github.com/ruby/ruby.git"
    "https://github.com/erlang/otp.git"
    "https://github.com/ocaml/ocaml.git"
    "git://perl5.git.perl.org/perl.git"
# OpenStack
    "https://github.com/openstack/nova.git"
)

for url in ${URLS[@]}
do
    BASE=$(basename $url)
    DIR=$(echo $BASE | sed -e "s/\.git//")
    git clone $url repos/$DIR
done
