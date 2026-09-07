# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyADConnectorOfficeSiteRequest(DaraModel):
    def __init__(
        self,
        ad_hostname: str = None,
        backup_dchostname: str = None,
        backup_dns: str = None,
        dns_address: List[str] = None,
        domain_name: str = None,
        domain_password: str = None,
        domain_user_name: str = None,
        mfa_enabled: bool = None,
        ouname: str = None,
        office_site_id: str = None,
        office_site_name: str = None,
        region_id: str = None,
        sub_domain_dns_address: List[str] = None,
        sub_domain_name: str = None,
    ):
        # The hostname of the domain controller. The hostname must comply with Windows hostname naming conventions.
        self.ad_hostname = ad_hostname
        # The hostname of the backup domain controller.
        self.backup_dchostname = backup_dchostname
        # The DNS address of the backup domain controller.
        self.backup_dns = backup_dns
        # The IP address of the DNS server corresponding to the enterprise AD. Currently, only one IP address can be specified.
        self.dns_address = dns_address
        # The domain name of the enterprise AD. The same domain name can be registered only once.
        self.domain_name = domain_name
        # The password of the domain administrator. The password can be up to 64 characters in length.
        self.domain_password = domain_password
        # The username of the domain administrator. The username can be up to 64 characters in length.
        # 
        # > Use sAMAccountName for the username. Do not use userPrincipalName.
        self.domain_user_name = domain_user_name
        # Specifies whether to enable multi-factor authentication (MFA).
        self.mfa_enabled = mfa_enabled
        # The organizational unit (OU) of the AD domain. You can call [ListUserAdOrganizationUnits](https://help.aliyun.com/document_detail/311259.html) to obtain the value.
        self.ouname = ouname
        # The office network ID.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The office network name. The name must be 2 to 255 characters in length. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`. The name can contain digits, colons (:), underscores (_), or hyphens (-).
        self.office_site_name = office_site_name
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The DNS address of the enterprise AD subdomain. Currently, only one address can be specified. If `SubDomainName` is specified but this parameter is not, the subdomain DNS defaults to the same value as the parent domain.
        self.sub_domain_dns_address = sub_domain_dns_address
        # The domain name of the enterprise AD subdomain.
        self.sub_domain_name = sub_domain_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_hostname is not None:
            result['AdHostname'] = self.ad_hostname

        if self.backup_dchostname is not None:
            result['BackupDCHostname'] = self.backup_dchostname

        if self.backup_dns is not None:
            result['BackupDns'] = self.backup_dns

        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password

        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name

        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled

        if self.ouname is not None:
            result['OUName'] = self.ouname

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address

        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdHostname') is not None:
            self.ad_hostname = m.get('AdHostname')

        if m.get('BackupDCHostname') is not None:
            self.backup_dchostname = m.get('BackupDCHostname')

        if m.get('BackupDns') is not None:
            self.backup_dns = m.get('BackupDns')

        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')

        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')

        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')

        if m.get('OUName') is not None:
            self.ouname = m.get('OUName')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')

        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')

        return self

