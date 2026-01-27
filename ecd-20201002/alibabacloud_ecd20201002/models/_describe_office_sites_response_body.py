# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20201002 import models as main_models
from darabonba.model import DaraModel

class DescribeOfficeSitesResponseBody(DaraModel):
    def __init__(
        self,
        office_sites: List[main_models.DescribeOfficeSitesResponseBodyOfficeSites] = None,
        request_id: str = None,
    ):
        # The office networks.
        self.office_sites = office_sites
        self.request_id = request_id

    def validate(self):
        if self.office_sites:
            for v1 in self.office_sites:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OfficeSites'] = []
        if self.office_sites is not None:
            for k1 in self.office_sites:
                result['OfficeSites'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.office_sites = []
        if m.get('OfficeSites') is not None:
            for k1 in m.get('OfficeSites'):
                temp_model = main_models.DescribeOfficeSitesResponseBodyOfficeSites()
                self.office_sites.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeOfficeSitesResponseBodyOfficeSites(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        biz_type: int = None,
        desktop_access_type: str = None,
        desktop_vpc_endpoint: str = None,
        office_site_id: str = None,
        office_site_type: str = None,
        provider_id: str = None,
        sso_service_url: str = None,
    ):
        # aliuid
        self.ali_uid = ali_uid
        # biztype
        self.biz_type = biz_type
        self.desktop_access_type = desktop_access_type
        self.desktop_vpc_endpoint = desktop_vpc_endpoint
        self.office_site_id = office_site_id
        self.office_site_type = office_site_type
        self.provider_id = provider_id
        self.sso_service_url = sso_service_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.desktop_access_type is not None:
            result['DesktopAccessType'] = self.desktop_access_type

        if self.desktop_vpc_endpoint is not None:
            result['DesktopVpcEndpoint'] = self.desktop_vpc_endpoint

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.office_site_type is not None:
            result['OfficeSiteType'] = self.office_site_type

        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id

        if self.sso_service_url is not None:
            result['SsoServiceUrl'] = self.sso_service_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('DesktopAccessType') is not None:
            self.desktop_access_type = m.get('DesktopAccessType')

        if m.get('DesktopVpcEndpoint') is not None:
            self.desktop_vpc_endpoint = m.get('DesktopVpcEndpoint')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('OfficeSiteType') is not None:
            self.office_site_type = m.get('OfficeSiteType')

        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')

        if m.get('SsoServiceUrl') is not None:
            self.sso_service_url = m.get('SsoServiceUrl')

        return self

