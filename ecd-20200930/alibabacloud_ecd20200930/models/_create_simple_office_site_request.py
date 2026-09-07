# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateSimpleOfficeSiteRequest(DaraModel):
    def __init__(
        self,
        access_attribute: str = None,
        account_type: str = None,
        authority_host: str = None,
        bandwidth: int = None,
        cen_id: str = None,
        cen_owner_id: int = None,
        cidr_block: str = None,
        client_id: str = None,
        client_secret: str = None,
        cloud_box_office_site: bool = None,
        desktop_access_type: str = None,
        domain_name: str = None,
        eid: str = None,
        enable_admin_access: bool = None,
        enable_internet_access: bool = None,
        need_verify_zero_device: bool = None,
        office_site_name: str = None,
        region_id: str = None,
        tenant_id: str = None,
        v_switch_id: List[str] = None,
        verify_code: str = None,
        vpc_type: str = None,
    ):
        # The access attribute of the office network (workspace).
        self.access_attribute = access_attribute
        # The account type.
        self.account_type = account_type
        # The authority URL of the identity authentication service.
        self.authority_host = authority_host
        # The peak Internet bandwidth. Valid values: 10 to 200. Unit: Mbit/s.
        # You can specify this parameter when `EnableInternetAccess` is set to `true`.
        self.bandwidth = bandwidth
        # The instance ID of the Cloud Enterprise Network (CEN) instance.
        # 
        # > To connect to cloud desktops over a VPC connection, add the office network to a CEN instance. The CEN instance is the one that the on-premises network connects to by using a VPN or Express Connect circuit.
        self.cen_id = cen_id
        # The Alibaba Cloud account ID to which the CEN instance belongs.
        # 
        # - If CenId is not specified or the specified CEN instance belongs to the current Alibaba Cloud account, you do not need to specify this parameter.
        # - If the specified CEN instance belongs to another Alibaba Cloud account, specify the Alibaba Cloud account ID of that account.
        self.cen_owner_id = cen_owner_id
        # The IPv4 CIDR block of the VPC for the office network. This parameter is required for advanced office networks. The system uses automatic creation of a VPC based on the specified IPv4 CIDR block. Use one of the following CIDR blocks or their subnets:
        # 
        # - `10.0.0.0/12` (valid mask range: 12 to 24 bits)
        # - `172.16.0.0/12` (valid mask range: 12 to 24 bits)
        # - `192.168.0.0/16` (valid mask range: 16 to 24 bits)
        self.cidr_block = cidr_block
        # The client ID registered with the identity provider application.
        self.client_id = client_id
        # The client secret registered with the identity provider application.
        self.client_secret = client_secret
        # Specifies whether the office network is a CloudBox office network.
        self.cloud_box_office_site = cloud_box_office_site
        # The access method allowed when connecting to cloud desktops.
        # 
        # > The VPC connection method depends on the Alibaba Cloud PrivateLink service, which is free of charge. If this parameter is set to `VPC` or `Any`, the system automatically activates the PrivateLink service.
        self.desktop_access_type = desktop_access_type
        # The domain name of the enterprise AD.
        self.domain_name = domain_name
        # The enterprise ID (EID).
        self.eid = eid
        # Specifies whether to grant local administrator permissions to users who use cloud desktops.
        self.enable_admin_access = enable_admin_access
        # Specifies whether to enable public network access.
        self.enable_internet_access = enable_internet_access
        # Specifies whether to enable trusted device verification.
        self.need_verify_zero_device = need_verify_zero_device
        # The name of the office network. The name must be 2 to 255 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). The name must start with a letter or Chinese character and cannot start with `http://` or `https://`.
        self.office_site_name = office_site_name
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The tenant ID of the identity provider.
        self.tenant_id = tenant_id
        # The ID of the vSwitch in the VPC. This parameter is required when you create a CloudBox office network.
        self.v_switch_id = v_switch_id
        # The verification code. If the specified CEN instance belongs to another Alibaba Cloud account, call [SendVerifyCode](https://help.aliyun.com/document_detail/335132.html) to obtain the verification code first.
        self.verify_code = verify_code
        # The type of the office network.
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_attribute is not None:
            result['AccessAttribute'] = self.access_attribute

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.authority_host is not None:
            result['AuthorityHost'] = self.authority_host

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.cloud_box_office_site is not None:
            result['CloudBoxOfficeSite'] = self.cloud_box_office_site

        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.eid is not None:
            result['Eid'] = self.eid

        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access

        if self.enable_internet_access is not None:
            result['EnableInternetAccess'] = self.enable_internet_access

        if self.need_verify_zero_device is not None:
            result['NeedVerifyZeroDevice'] = self.need_verify_zero_device

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code

        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessAttribute') is not None:
            self.access_attribute = m.get('AccessAttribute')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('AuthorityHost') is not None:
            self.authority_host = m.get('AuthorityHost')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('CloudBoxOfficeSite') is not None:
            self.cloud_box_office_site = m.get('CloudBoxOfficeSite')

        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Eid') is not None:
            self.eid = m.get('Eid')

        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')

        if m.get('EnableInternetAccess') is not None:
            self.enable_internet_access = m.get('EnableInternetAccess')

        if m.get('NeedVerifyZeroDevice') is not None:
            self.need_verify_zero_device = m.get('NeedVerifyZeroDevice')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')

        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')

        return self

