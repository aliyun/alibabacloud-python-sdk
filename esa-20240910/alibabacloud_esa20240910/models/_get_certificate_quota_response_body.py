# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetCertificateQuotaResponseBody(DaraModel):
    def __init__(
        self,
        quota: int = None,
        quota_usage: int = None,
        request_id: str = None,
        site_count: int = None,
        site_usage: List[main_models.GetCertificateQuotaResponseBodySiteUsage] = None,
        type: str = None,
    ):
        # Free certificate quota.
        self.quota = quota
        # Usage of free certificate quota.
        self.quota_usage = quota_usage
        # Request ID.
        self.request_id = request_id
        # Number of sites.
        self.site_count = site_count
        # List of site usage details.
        self.site_usage = site_usage
        # Certificate Quota type.
        self.type = type

    def validate(self):
        if self.site_usage:
            for v1 in self.site_usage:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.quota is not None:
            result['Quota'] = self.quota

        if self.quota_usage is not None:
            result['QuotaUsage'] = self.quota_usage

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_count is not None:
            result['SiteCount'] = self.site_count

        result['SiteUsage'] = []
        if self.site_usage is not None:
            for k1 in self.site_usage:
                result['SiteUsage'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('QuotaUsage') is not None:
            self.quota_usage = m.get('QuotaUsage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteCount') is not None:
            self.site_count = m.get('SiteCount')

        self.site_usage = []
        if m.get('SiteUsage') is not None:
            for k1 in m.get('SiteUsage'):
                temp_model = main_models.GetCertificateQuotaResponseBodySiteUsage()
                self.site_usage.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetCertificateQuotaResponseBodySiteUsage(DaraModel):
    def __init__(
        self,
        site_id: str = None,
        site_name: str = None,
        site_usage: int = None,
    ):
        # Site ID.
        self.site_id = site_id
        # Site name.
        self.site_name = site_name
        # Site usage.
        self.site_usage = site_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.site_usage is not None:
            result['SiteUsage'] = self.site_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('SiteUsage') is not None:
            self.site_usage = m.get('SiteUsage')

        return self

