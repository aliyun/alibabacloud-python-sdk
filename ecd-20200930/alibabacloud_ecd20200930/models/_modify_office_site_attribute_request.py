# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyOfficeSiteAttributeRequest(DaraModel):
    def __init__(
        self,
        authority_host: str = None,
        client_id: str = None,
        client_secret: str = None,
        desktop_access_type: str = None,
        domain_name: str = None,
        enable_admin_access: bool = None,
        need_verify_login_risk: bool = None,
        need_verify_zero_device: bool = None,
        office_site_id: str = None,
        office_site_name: str = None,
        region_id: str = None,
        tenant_id: str = None,
        v_switch_id: List[str] = None,
    ):
        self.authority_host = authority_host
        self.client_id = client_id
        self.client_secret = client_secret
        # The method for connecting to cloud computers.
        # 
        # > VPC connections use Alibaba Cloud PrivateLink, a free service. If you set this parameter to VPC or Any, PrivateLink is automatically activated.
        self.desktop_access_type = desktop_access_type
        self.domain_name = domain_name
        # Specifies whether to grant cloud computer users local administrative permissions.
        self.enable_admin_access = enable_admin_access
        # Specifies whether to enable two-factor authentication. This parameter is applicable to only office sites that use convenience accounts. If enabled, the system performs a security check during logon. If the system detects a risk, it sends a verification code to the email address that is associated with the account. The user must enter the correct verification code to log on.
        self.need_verify_login_risk = need_verify_login_risk
        # Specifies whether to enable device verification. This feature is available only for office sites that use convenience accounts.
        self.need_verify_zero_device = need_verify_zero_device
        # The ID of the office site.
        # 
        # This parameter is required.
        self.office_site_id = office_site_id
        # The name of the office site. The name must be 2 to 255 characters long. The name must start with a letter or a Chinese character, and cannot start with http\\:// or https\\://. It can contain digits, colons (:), underscores (_), and hyphens (-).<br>
        # This parameter is optional.<br>
        self.office_site_name = office_site_name
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the regions where Elastic Desktop Service is available.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.tenant_id = tenant_id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authority_host is not None:
            result['AuthorityHost'] = self.authority_host

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_secret is not None:
            result['ClientSecret'] = self.client_secret

        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access

        if self.need_verify_login_risk is not None:
            result['NeedVerifyLoginRisk'] = self.need_verify_login_risk

        if self.need_verify_zero_device is not None:
            result['NeedVerifyZeroDevice'] = self.need_verify_zero_device

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_name is not None:
            result['OfficeSiteName'] = self.office_site_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorityHost') is not None:
            self.authority_host = m.get('AuthorityHost')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientSecret') is not None:
            self.client_secret = m.get('ClientSecret')

        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')

        if m.get('NeedVerifyLoginRisk') is not None:
            self.need_verify_login_risk = m.get('NeedVerifyLoginRisk')

        if m.get('NeedVerifyZeroDevice') is not None:
            self.need_verify_zero_device = m.get('NeedVerifyZeroDevice')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteName') is not None:
            self.office_site_name = m.get('OfficeSiteName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

