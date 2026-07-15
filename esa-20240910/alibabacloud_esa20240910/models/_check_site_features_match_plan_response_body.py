# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CheckSiteFeaturesMatchPlanResponseBody(DaraModel):
    def __init__(
        self,
        is_passed: bool = None,
        request_id: str = None,
        un_passed_site_quotas: List[main_models.CheckSiteFeaturesMatchPlanResponseBodyUnPassedSiteQuotas] = None,
    ):
        # Indicates whether the features of the current site are compatible with the target instance.
        self.is_passed = is_passed
        # The request ID.
        self.request_id = request_id
        # The information about site quotas that do not meet the requirements.
        self.un_passed_site_quotas = un_passed_site_quotas

    def validate(self):
        if self.un_passed_site_quotas:
            for v1 in self.un_passed_site_quotas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_passed is not None:
            result['IsPassed'] = self.is_passed

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UnPassedSiteQuotas'] = []
        if self.un_passed_site_quotas is not None:
            for k1 in self.un_passed_site_quotas:
                result['UnPassedSiteQuotas'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsPassed') is not None:
            self.is_passed = m.get('IsPassed')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.un_passed_site_quotas = []
        if m.get('UnPassedSiteQuotas') is not None:
            for k1 in m.get('UnPassedSiteQuotas'):
                temp_model = main_models.CheckSiteFeaturesMatchPlanResponseBodyUnPassedSiteQuotas()
                self.un_passed_site_quotas.append(temp_model.from_map(k1))

        return self

class CheckSiteFeaturesMatchPlanResponseBodyUnPassedSiteQuotas(DaraModel):
    def __init__(
        self,
        current_quota_value: str = None,
        dest_quota_value: str = None,
        quota_name: str = None,
    ):
        # The quota value of the current site.
        self.current_quota_value = current_quota_value
        # The quota value of the target instance.
        self.dest_quota_value = dest_quota_value
        # The quota name.
        self.quota_name = quota_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_quota_value is not None:
            result['CurrentQuotaValue'] = self.current_quota_value

        if self.dest_quota_value is not None:
            result['DestQuotaValue'] = self.dest_quota_value

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentQuotaValue') is not None:
            self.current_quota_value = m.get('CurrentQuotaValue')

        if m.get('DestQuotaValue') is not None:
            self.dest_quota_value = m.get('DestQuotaValue')

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        return self

