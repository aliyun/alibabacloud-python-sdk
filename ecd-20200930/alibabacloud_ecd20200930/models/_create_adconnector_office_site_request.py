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
        self.access_attribute = access_attribute
        # The domain controller hostname.
        # The hostname must comply with Windows hostname naming conventions.
        self.ad_hostname = ad_hostname
        # The hostname of the backup domain controller.
        self.backup_dchostname = backup_dchostname
        # The DNS address of the backup domain controller.
        self.backup_dns = backup_dns
        # The peak public bandwidth, specified in Mbit/s. The value can range from 0 to 200.<br>
        # If you omit this parameter or set it to 0, internet access is disabled.<br>
        self.bandwidth = bandwidth
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The ID of the Alibaba Cloud account that owns the Cloud Enterprise Network (CEN) instance.
        # 
        # - If you do not specify `CenId`, or the specified CEN instance belongs to your Alibaba Cloud account, you do not need to specify this parameter.
        # 
        # - If the specified CEN instance belongs to another Alibaba Cloud account, you must specify that account\\"s ID.
        self.cen_owner_id = cen_owner_id
        # The IPv4 CIDR block for the office site\\"s VPC. The system uses this IPv4 CIDR block to automatically create a VPC. We recommend that you use one of the following CIDR blocks or their subnets:
        # 
        # - `10.0.0.0/12` (The subnet mask length must be 12 to 24 bits.)
        # 
        # - `172.16.0.0/12` (The subnet mask length must be 12 to 24 bits.)
        # 
        # - `192.168.0.0/16` (The subnet mask length must be 16 to 24 bits.)
        self.cidr_block = cidr_block
        # The method for connecting to cloud desktops.
        # 
        # > VPC connections are established using Alibaba Cloud PrivateLink, which is a free service. If you set this parameter to `VPC` or `Any`, PrivateLink is automatically enabled.
        self.desktop_access_type = desktop_access_type
        # An array that contains the IP address of the DNS server for the enterprise AD. You can specify only one IP address.
        # 
        # This parameter is required.
        self.dns_address = dns_address
        # The domain name for the enterprise AD. Each domain name must be unique.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The domain administrator\\"s password. The password cannot exceed 64 characters in length.
        self.domain_password = domain_password
        # The domain administrator\\"s username. The username cannot exceed 64 characters in length.
        # 
        # > Use the sAMAccountName, not the userPrincipalName.
        self.domain_user_name = domain_user_name
        # Specifies whether to grant local administrator permissions to cloud desktop users. Default: true.
        self.enable_admin_access = enable_admin_access
        # This parameter is deprecated. Use the `Bandwidth` parameter to manage internet access.
        self.enable_internet_access = enable_internet_access
        # Specifies whether to enable multi-factor authentication (MFA).
        self.mfa_enabled = mfa_enabled
        # The name of the office site. The name must be 2 to 255 characters in length. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`. The name can contain digits, colons (:), underscores (_), and hyphens (-).<br>
        # This parameter is empty by default.<br>
        self.office_site_name = office_site_name
        # The protocol type.
        self.protocol_type = protocol_type
        # The ID of the region. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the regions supported by Elastic Desktop Service (EDS).
        # 
        # This parameter is required.
        self.region_id = region_id
        # The AD Connector type.
        self.specification = specification
        # The DNS address of the enterprise AD child domain. If you specify `SubDomainName` but not this parameter, the DNS address of the child domain is considered the same as that of the parent domain.
        self.sub_domain_dns_address = sub_domain_dns_address
        # The domain name of the enterprise AD child domain.
        self.sub_domain_name = sub_domain_name
        # The list of vSwitch IDs.
        self.v_switch_id = v_switch_id
        # The verification code. If the `CenId` that you specify belongs to another Alibaba Cloud account, you must first call the [SendVerifyCode](https://help.aliyun.com/document_detail/436847.html) operation to obtain the verification code.
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

