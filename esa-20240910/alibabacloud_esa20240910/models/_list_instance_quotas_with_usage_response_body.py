# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListInstanceQuotasWithUsageResponseBody(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        quotas: List[main_models.ListInstanceQuotasWithUsageResponseBodyQuotas] = None,
        request_id: str = None,
        status: str = None,
    ):
        # The plan ID.[](~~2850189~~)
        self.instance_id = instance_id
        # The quotas and their actual usage in the plan.
        self.quotas = quotas
        # The request ID.
        self.request_id = request_id
        # The plan status. Valid values:
        # 
        # *   online: The plan is in service.
        # *   offline: The plan has expired within an allowable period. In this state, the plan is unavailable.
        # *   disable: The plan is released.
        self.status = status

    def validate(self):
        if self.quotas:
            for v1 in self.quotas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['Quotas'] = []
        if self.quotas is not None:
            for k1 in self.quotas:
                result['Quotas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.quotas = []
        if m.get('Quotas') is not None:
            for k1 in m.get('Quotas'):
                temp_model = main_models.ListInstanceQuotasWithUsageResponseBodyQuotas()
                self.quotas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListInstanceQuotasWithUsageResponseBodyQuotas(DaraModel):
    def __init__(
        self,
        quota_name: str = None,
        quota_value: str = None,
        site_usage: List[main_models.ListInstanceQuotasWithUsageResponseBodyQuotasSiteUsage] = None,
        usage: str = None,
    ):
        # The quota name.
        self.quota_name = quota_name
        # The quota value.
        self.quota_value = quota_value
        # The usage of the quota in each website associated with the plan.
        self.site_usage = site_usage
        # The quota usage.
        self.usage = usage

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
        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        if self.quota_value is not None:
            result['QuotaValue'] = self.quota_value

        result['SiteUsage'] = []
        if self.site_usage is not None:
            for k1 in self.site_usage:
                result['SiteUsage'].append(k1.to_map() if k1 else None)

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        if m.get('QuotaValue') is not None:
            self.quota_value = m.get('QuotaValue')

        self.site_usage = []
        if m.get('SiteUsage') is not None:
            for k1 in m.get('SiteUsage'):
                temp_model = main_models.ListInstanceQuotasWithUsageResponseBodyQuotasSiteUsage()
                self.site_usage.append(temp_model.from_map(k1))

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

class ListInstanceQuotasWithUsageResponseBodyQuotasSiteUsage(DaraModel):
    def __init__(
        self,
        site_id: int = None,
        site_name: str = None,
        site_usage: str = None,
    ):
        # The website ID.
        self.site_id = site_id
        # The website name.
        self.site_name = site_name
        # The quota usage of the website.
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

