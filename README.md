# RPM files for LBRY

[![Copr build status](https://copr.fedorainfracloud.org/coprs/jonny/LBRY/package/lbrynet/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/jonny/LBRY/package/lbrynet/)

Built on Fedora Copr at https://copr.fedorainfracloud.org/coprs/jonny/LBRY/

## How to build the RPM locally

Make srpm:
```
$ make -f .copr/Makefile srpm outdir=. spec=./lbrynet.spec
```

Make rpm:
```
$ mock --rebuild --enable-network ./lbrynet-${VERSION}.src.rpm
```
