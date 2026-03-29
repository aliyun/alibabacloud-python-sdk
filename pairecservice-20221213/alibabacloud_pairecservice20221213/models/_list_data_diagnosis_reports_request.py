# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataDiagnosisReportsRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        feature_name: str = None,
        instance_id: str = None,
        remain_rate_type: str = None,
        start_date: str = None,
        top_n: int = None,
    ):
        # This parameter is required.
        self.end_date = end_date
        self.feature_name = feature_name
        # This parameter is required.
        self.instance_id = instance_id
        self.remain_rate_type = remain_rate_type
        # This parameter is required.
        self.start_date = start_date
        self.top_n = top_n

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.remain_rate_type is not None:
            result['RemainRateType'] = self.remain_rate_type

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.top_n is not None:
            result['TopN'] = self.top_n

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RemainRateType') is not None:
            self.remain_rate_type = m.get('RemainRateType')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TopN') is not None:
            self.top_n = m.get('TopN')

        return self

