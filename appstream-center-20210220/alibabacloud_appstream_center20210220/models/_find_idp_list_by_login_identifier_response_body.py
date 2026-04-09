# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_appstream_center20210220 import models as main_models
from darabonba.model import DaraModel

class FindIdpListByLoginIdentifierResponseBody(DaraModel):
    def __init__(
        self,
        idp_infos: List[main_models.FindIdpListByLoginIdentifierResponseBodyIdpInfos] = None,
        office_site_info: main_models.FindIdpListByLoginIdentifierResponseBodyOfficeSiteInfo = None,
        pop_region_config: Dict[str, str] = None,
        profile_region: str = None,
        request_id: str = None,
        tenant_alias_info: main_models.FindIdpListByLoginIdentifierResponseBodyTenantAliasInfo = None,
    ):
        self.idp_infos = idp_infos
        self.office_site_info = office_site_info
        self.pop_region_config = pop_region_config
        self.profile_region = profile_region
        self.request_id = request_id
        self.tenant_alias_info = tenant_alias_info

    def validate(self):
        if self.idp_infos:
            for v1 in self.idp_infos:
                 if v1:
                    v1.validate()
        if self.office_site_info:
            self.office_site_info.validate()
        if self.tenant_alias_info:
            self.tenant_alias_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IdpInfos'] = []
        if self.idp_infos is not None:
            for k1 in self.idp_infos:
                result['IdpInfos'].append(k1.to_map() if k1 else None)

        if self.office_site_info is not None:
            result['OfficeSiteInfo'] = self.office_site_info.to_map()

        if self.pop_region_config is not None:
            result['PopRegionConfig'] = self.pop_region_config

        if self.profile_region is not None:
            result['ProfileRegion'] = self.profile_region

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tenant_alias_info is not None:
            result['TenantAliasInfo'] = self.tenant_alias_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.idp_infos = []
        if m.get('IdpInfos') is not None:
            for k1 in m.get('IdpInfos'):
                temp_model = main_models.FindIdpListByLoginIdentifierResponseBodyIdpInfos()
                self.idp_infos.append(temp_model.from_map(k1))

        if m.get('OfficeSiteInfo') is not None:
            temp_model = main_models.FindIdpListByLoginIdentifierResponseBodyOfficeSiteInfo()
            self.office_site_info = temp_model.from_map(m.get('OfficeSiteInfo'))

        if m.get('PopRegionConfig') is not None:
            self.pop_region_config = m.get('PopRegionConfig')

        if m.get('ProfileRegion') is not None:
            self.profile_region = m.get('ProfileRegion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TenantAliasInfo') is not None:
            temp_model = main_models.FindIdpListByLoginIdentifierResponseBodyTenantAliasInfo()
            self.tenant_alias_info = temp_model.from_map(m.get('TenantAliasInfo'))

        return self

class FindIdpListByLoginIdentifierResponseBodyTenantAliasInfo(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        tenant_alias: str = None,
    ):
        self.access_type = access_type
        self.tenant_alias = tenant_alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.tenant_alias is not None:
            result['TenantAlias'] = self.tenant_alias

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('TenantAlias') is not None:
            self.tenant_alias = m.get('TenantAlias')

        return self

class FindIdpListByLoginIdentifierResponseBodyOfficeSiteInfo(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        office_site_id: str = None,
        provider_id: str = None,
        region_id: str = None,
        sso_service_url: str = None,
    ):
        self.access_type = access_type
        self.office_site_id = office_site_id
        self.provider_id = provider_id
        self.region_id = region_id
        self.sso_service_url = sso_service_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['AccessType'] = self.access_type

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sso_service_url is not None:
            result['SsoServiceUrl'] = self.sso_service_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SsoServiceUrl') is not None:
            self.sso_service_url = m.get('SsoServiceUrl')

        return self



class FindIdpListByLoginIdentifierResponseBodyIdpInfos(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        cookies: str = None,
        idp_id: str = None,
        idp_name: str = None,
        idp_name_en: str = None,
        idp_provider: str = None,
        jump_switch: str = None,
        sso_protocol: str = None,
        sso_service_url: str = None,
    ):
        self.account_type = account_type
        self.cookies = cookies
        self.idp_id = idp_id
        self.idp_name = idp_name
        self.idp_name_en = idp_name_en
        self.idp_provider = idp_provider
        self.jump_switch = jump_switch
        self.sso_protocol = sso_protocol
        self.sso_service_url = sso_service_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.cookies is not None:
            result['Cookies'] = self.cookies

        if self.idp_id is not None:
            result['IdpId'] = self.idp_id

        if self.idp_name is not None:
            result['IdpName'] = self.idp_name

        if self.idp_name_en is not None:
            result['IdpNameEN'] = self.idp_name_en

        if self.idp_provider is not None:
            result['IdpProvider'] = self.idp_provider

        if self.jump_switch is not None:
            result['JumpSwitch'] = self.jump_switch

        if self.sso_protocol is not None:
            result['SsoProtocol'] = self.sso_protocol

        if self.sso_service_url is not None:
            result['SsoServiceUrl'] = self.sso_service_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')

        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')

        if m.get('IdpName') is not None:
            self.idp_name = m.get('IdpName')

        if m.get('IdpNameEN') is not None:
            self.idp_name_en = m.get('IdpNameEN')

        if m.get('IdpProvider') is not None:
            self.idp_provider = m.get('IdpProvider')

        if m.get('JumpSwitch') is not None:
            self.jump_switch = m.get('JumpSwitch')

        if m.get('SsoProtocol') is not None:
            self.sso_protocol = m.get('SsoProtocol')

        if m.get('SsoServiceUrl') is not None:
            self.sso_service_url = m.get('SsoServiceUrl')

        return self

