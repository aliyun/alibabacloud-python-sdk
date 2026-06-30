# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeModelOperatorUsageRequest(DaraModel):
    def __init__(
        self,
        api_key_ids: List[int] = None,
        end_time: str = None,
        group_by: str = None,
        keys: List[str] = None,
        model_names: List[str] = None,
        period: int = None,
        start_time: str = None,
    ):
        self.api_key_ids = api_key_ids
        self.end_time = end_time
        self.group_by = group_by
        self.keys = keys
        self.model_names = model_names
        self.period = period
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_ids is not None:
            result['ApiKeyIds'] = self.api_key_ids

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_by is not None:
            result['GroupBy'] = self.group_by

        if self.keys is not None:
            result['Keys'] = self.keys

        if self.model_names is not None:
            result['ModelNames'] = self.model_names

        if self.period is not None:
            result['Period'] = self.period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeyIds') is not None:
            self.api_key_ids = m.get('ApiKeyIds')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')

        if m.get('Keys') is not None:
            self.keys = m.get('Keys')

        if m.get('ModelNames') is not None:
            self.model_names = m.get('ModelNames')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

