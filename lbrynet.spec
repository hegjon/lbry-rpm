%global debug_package %{nil}

Name:    lbrynet
Version: 0.106.0
Release: 1%{?dist}
Summary: A decentralized peer-to-peer protocol for publishing and accessing digital content

License: MIT
URL:     https://github.com/lbryio/lbry-sdk

Source0: https://github.com/lbryio/lbry-sdk/releases/download/v%{version}/lbrynet-linux.zip


%description
LBRY is a decentralized peer-to-peer protocol for publishing and accessing \
digital content. It utilizes the LBRY blockchain as a global namespace and \
database of digital content. Blockchain entries contain searchable content \
metadata, identities, rights and access rules. LBRY also provides a data \
network that consists of peers (seeders) uploading and downloading data from \
other peers, possibly in exchange for payments, as well as a distributed hash \
table used by peers to discover other peers.


%prep
%setup -c

%build
#no build, pre-compiled binary

%install
install -dD -m 755 %{buildroot}%{_bindir}
install -m 755 lbrynet %{buildroot}%{_bindir}/lbrynet

%files
%{_bindir}/lbrynet

%changelog
* Wed Dec 29 2021 Jonny Heggheim <hegjon@gmail.com> - 0.106.0-1
- Initial package
