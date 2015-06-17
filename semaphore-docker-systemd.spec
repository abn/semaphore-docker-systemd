%define debug_package %{nil}

Name:           semaphore-docker-systemd		
Version:	    0.0.1
Release:	    1%{?dist}
Summary:	    systemd wrapper for dockerized semaphore deployment

Group:		    Application/Internet
License:	    MIT
URL:		    https://github.com/abn/semaphore-docker-systemd
Source0:	    semaphore.service
Source1:        semaphore.redis.service
Source2:        semaphore.mongo.service

BuildRequires:	systemd-units
Requires:	    systemd coreutils docker

%description
systemd wrapper

%install
install -d %{buildroot}/%{_unitdir}
install %{SOURCE0} %{buildroot}/%{_unitdir}
install %{SOURCE1} %{buildroot}/%{_unitdir}
install %{SOURCE2} %{buildroot}/%{_unitdir}

%pre
install -d -m 750 /var/lib/semaphore/
install -d -m 750 /var/lib/semaphore/mongo
chconf -Rt svirt_sandbox_file_t /var/lib/semaphore/mongo

%post
%systemd_post semaphore.redis.service
%systemd_post semaphore.mongo.service
%systemd_post semaphore.service

%preun
%systemd_preun semaphore.service
%systemd_preun semaphore.mongo.service
%systemd_preun semaphore.redis.service

%postun
%systemd_postun_with_restart semaphore.service
%systemd_postun_with_restart semaphore.mongo.service
%systemd_postun_with_restart semaphore.redis.service

%clean
rm -rf %{buildroot}

%files
%{_unitdir}/semaphore.service
%{_unitdir}/semaphore.mongo.service
%{_unitdir}/semaphore.redis.service

%changelog
* Wed Jun 17 2015 Arun Babu Neelicattu <arun.neelicattu@gmail.com> - 0.0.1-1
- Initial specfile


