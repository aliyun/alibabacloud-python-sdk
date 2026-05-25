# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class QueryHistoryUsageDurationRankResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        usage_duration_list: List[main_models.QueryHistoryUsageDurationRankResponseBodyUsageDurationList] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.usage_duration_list = usage_duration_list

    def validate(self):
        if self.usage_duration_list:
            for v1 in self.usage_duration_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UsageDurationList'] = []
        if self.usage_duration_list is not None:
            for k1 in self.usage_duration_list:
                result['UsageDurationList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.usage_duration_list = []
        if m.get('UsageDurationList') is not None:
            for k1 in m.get('UsageDurationList'):
                temp_model = main_models.QueryHistoryUsageDurationRankResponseBodyUsageDurationList()
                self.usage_duration_list.append(temp_model.from_map(k1))

        return self

class QueryHistoryUsageDurationRankResponseBodyUsageDurationList(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        desktop_id: str = None,
        desktop_name: str = None,
        end_user_id: str = None,
        region_id: str = None,
        usage_duration: int = None,
    ):
        self.charge_type = charge_type
        self.desktop_id = desktop_id
        self.desktop_name = desktop_name
        self.end_user_id = end_user_id
        self.region_id = region_id
        self.usage_duration = usage_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_name is not None:
            result['DesktopName'] = self.desktop_name

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.usage_duration is not None:
            result['UsageDuration'] = self.usage_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopName') is not None:
            self.desktop_name = m.get('DesktopName')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UsageDuration') is not None:
            self.usage_duration = m.get('UsageDuration')

        return self

