Name:           puppet-sysctl
Version:        XXX
Release:        XXX
Summary:        This modules allows you to configure sysctl.
License:        GPL-2.0

URL:            https://github.com/duritong/puppet-sysctl

Source0:        https://github.com/duritong/puppet-sysctl/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet >= 2.7.0

%description
This modules allows you to configure sysctl.

%prep
%setup -q -n %{name}-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/sysctl/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/sysctl/



%files
%{_datadir}/openstack-puppet/modules/sysctl/


%changelog

