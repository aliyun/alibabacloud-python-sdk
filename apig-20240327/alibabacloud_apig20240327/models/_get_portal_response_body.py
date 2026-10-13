# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetPortalResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPortalResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetPortalResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetPortalResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        name: str = None,
        portal_domain_config: List[main_models.HiMarketPortalDomainConfig] = None,
        portal_id: str = None,
        portal_setting_config: main_models.HiMarketPortalSettingConfig = None,
        region_id: str = None,
    ):
        # The creation time in ISO 8601 (RFC 3339) format in the UTC time zone, such as 2026-05-15T10:00:00Z.
        self.created_at = created_at
        # The portal description, which is the Description property of the portal resource.
        self.description = description
        # The portal name, which is the Name property of the portal resource.
        self.name = name
        # The list of portal domain name configurations. The list element is named domainConfig.
        self.portal_domain_config = portal_domain_config
        # The portal ID, which is the primary ID of the portal resource and points to the same portal as the portalId request parameter.
        self.portal_id = portal_id
        # The portal settings, including whether to enable username and password authentication, whether to automatically approve developer registrations, and whether to automatically approve subscription requests.
        self.portal_setting_config = portal_setting_config
        # The region ID, which is the RegionId property of the portal resource.
        self.region_id = region_id

    def validate(self):
        if self.portal_domain_config:
            for v1 in self.portal_domain_config:
                 if v1:
                    v1.validate()
        if self.portal_setting_config:
            self.portal_setting_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        result['portalDomainConfig'] = []
        if self.portal_domain_config is not None:
            for k1 in self.portal_domain_config:
                result['portalDomainConfig'].append(k1.to_map() if k1 else None)

        if self.portal_id is not None:
            result['portalId'] = self.portal_id

        if self.portal_setting_config is not None:
            result['portalSettingConfig'] = self.portal_setting_config.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.portal_domain_config = []
        if m.get('portalDomainConfig') is not None:
            for k1 in m.get('portalDomainConfig'):
                temp_model = main_models.HiMarketPortalDomainConfig()
                self.portal_domain_config.append(temp_model.from_map(k1))

        if m.get('portalId') is not None:
            self.portal_id = m.get('portalId')

        if m.get('portalSettingConfig') is not None:
            temp_model = main_models.HiMarketPortalSettingConfig()
            self.portal_setting_config = temp_model.from_map(m.get('portalSettingConfig'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

