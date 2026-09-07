# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateADConnectorOfficeSiteRequest(DaraModel):
    def __init__(
        self,
        access_attribute: str = None,
        ad_hostname: str = None,
        backup_dchostname: str = None,
        backup_dns: str = None,
        bandwidth: int = None,
        cen_id: str = None,
        cen_owner_id: int = None,
        cidr_block: str = None,
        desktop_access_type: str = None,
        dns_address: List[str] = None,
        domain_name: str = None,
        domain_password: str = None,
        domain_user_name: str = None,
        enable_admin_access: bool = None,
        enable_internet_access: bool = None,
        mfa_enabled: bool = None,
        office_site_name: str = None,
        protocol_type: str = None,
        region_id: str = None,
        specification: int = None,
        sub_domain_dns_address: List[str] = None,
        sub_domain_name: str = None,
        v_switch_id: List[str] = None,
        verify_code: str = None,
    ):
        # The access attribute of the office network (workspace).
        self.access_attribute = access_attribute
        # The hostname of the domain controller. The hostname must comply with Windows hostname naming conventions.
        self.ad_hostname = ad_hostname
        # The hostname of the backup domain controller.
        self.backup_dchostname = backup_dchostname
        # The DNS address of the backup domain controller.
        self.backup_dns = backup_dns
        # The peak Internet bandwidth, in Mbit/s. Valid values: 0 to 200.    
        # If you do not set this parameter or set it to 0, the Internet access feature is not enabled. Settings take effect immediately.
        self.bandwidth = bandwidth
        # The instance ID of the Cloud Enterprise Network (CEN).
        self.cen_id = cen_id
        # The Alibaba Cloud account ID of the Cloud Enterprise Network (CEN) instance owner.
        # 
        # - If CenId is not specified, or the specified CenId belongs to the current Alibaba Cloud account, you do not need to specify this parameter.
        # - If the specified CenId belongs to another Alibaba Cloud account, specify the Alibaba Cloud account ID of that account.
        self.cen_owner_id = cen_owner_id
        # The IPv4 CIDR block of the office network VPC. The system uses automatic creation to provision a VPC based on the specified IPv4 CIDR block. Use one of the following CIDR blocks or their subnets as the IPv4 CIDR block:
        # 
        # - `10.0.0.0/12` (valid mask range: 12 to 24 bits)
        # - `172.16.0.0/12` (valid mask range: 12 to 24 bits)
        # - `192.168.0.0/16` (valid mask range: 16 to 24 bits)
        self.cidr_block = cidr_block
        # The access method allowed when connecting to cloud computers.
        # 
        # > The VPC connection method depends on the Alibaba Cloud PrivateLink service, which is free of charge. If this parameter is set to `VPC` or `Any`, the system automatically activates the PrivateLink service for you.
        self.desktop_access_type = desktop_access_type
        # The IP address of the DNS server corresponding to the enterprise AD. Currently, only one IP address is supported.
        # 
        # This parameter is required.
        self.dns_address = dns_address
        # The domain name of the enterprise AD. The same domain name can be registered only once.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The password of the domain administrator. The password can be up to 64 characters in length.
        self.domain_password = domain_password
        # The username of the domain administrator. The username can be up to 64 characters in length.
        # 
        # > Use the sAMAccountName format for the username. Do not use the userPrincipalName format.
        self.domain_user_name = domain_user_name
        # Specifies whether to grant local administrator permissions to users who use cloud computers.
        self.enable_admin_access = enable_admin_access
        # Specifies whether public network access is enabled. This parameter indicates whether the feature is active.
        self.enable_internet_access = enable_internet_access
        # Specifies whether to enable multi-factor authentication (MFA).
        self.mfa_enabled = mfa_enabled
        # The name of the office network. The name must be 2 to 255 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). The name must start with a letter or Chinese character and cannot start with `http://` or `https://`.    
        # Default value: null.
        self.office_site_name = office_site_name
        # The protocol type.
        self.protocol_type = protocol_type
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The AD Connector specification.
        self.specification = specification
        # The DNS address of the enterprise AD subdomain. If `SubDomainName` is specified but this parameter is not, the subdomain DNS is considered the same as the parent domain DNS.
        self.sub_domain_dns_address = sub_domain_dns_address
        # The domain name of the enterprise AD subdomain.
        self.sub_domain_name = sub_domain_name
        # The list of vSwitch IDs.
        self.v_switch_id = v_switch_id
        # The verification code. If the specified CenId belongs to another Alibaba Cloud account, you must first call [SendVerifyCode](https://help.aliyun.com/document_detail/436847.html) to obtain the verification code.
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_attribute is not None:
            result['AccessAttribute'] = self.access_attribute

        if self.ad_hostname is not None:
            result['AdHostname'] = self.ad_hostname

        if self.backup_dchostname is not None:
            result['BackupDCHostname'] = self.backup_dchostname

        if self.backup_dns is not None:
            result['BackupDns'] = self.backup_dns

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type

        if self.dns_address is not None:
            result['DnsAddress'] = self.dns_address

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password

        if self.domain_user_name is not None:
            result['DomainUserName'] = self.domain_user_name

        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access

        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access

        if self.mfa_enabled is not None:
            result['MfaEnabled'] = self.mfa_enabled

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.specification is not None:
            result['Specification'] = self.specification

        if self.sub_domain_dns_address is not None:
            result['SubDomainDnsAddress'] = self.sub_domain_dns_address

        if self.sub_domain_name is not None:
            result['SubDomainName'] = self.sub_domain_name

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessAttribute') is not None:
            self.access_attribute = m.get('AccessAttribute')

        if m.get('AdHostname') is not None:
            self.ad_hostname = m.get('AdHostname')

        if m.get('BackupDCHostname') is not None:
            self.backup_dchostname = m.get('BackupDCHostname')

        if m.get('BackupDns') is not None:
            self.backup_dns = m.get('BackupDns')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')

        if m.get('DnsAddress') is not None:
            self.dns_address = m.get('DnsAddress')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')

        if m.get('DomainUserName') is not None:
            self.domain_user_name = m.get('DomainUserName')

        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')

        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')

        if m.get('MfaEnabled') is not None:
            self.mfa_enabled = m.get('MfaEnabled')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        if m.get('SubDomainDnsAddress') is not None:
            self.sub_domain_dns_address = m.get('SubDomainDnsAddress')

        if m.get('SubDomainName') is not None:
            self.sub_domain_name = m.get('SubDomainName')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')

        return self

