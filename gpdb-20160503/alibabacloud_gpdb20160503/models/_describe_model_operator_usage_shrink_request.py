# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeModelOperatorUsageShrinkRequest(DaraModel):
    def __init__(
        self,
        api_key_ids_shrink: str = None,
        end_time: str = None,
        group_by: str = None,
        keys_shrink: str = None,
        model_names_shrink: str = None,
        period: int = None,
        start_time: str = None,
    ):
        self.api_key_ids_shrink = api_key_ids_shrink
        self.end_time = end_time
        self.group_by = group_by
        self.keys_shrink = keys_shrink
        self.model_names_shrink = model_names_shrink
        self.period = period
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_ids_shrink is not None:
            result['ApiKeyIds'] = self.api_key_ids_shrink

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.group_by is not None:
            result['GroupBy'] = self.group_by

        if self.keys_shrink is not None:
            result['Keys'] = self.keys_shrink

        if self.model_names_shrink is not None:
            result['ModelNames'] = self.model_names_shrink

        if self.period is not None:
            result['Period'] = self.period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeyIds') is not None:
            self.api_key_ids_shrink = m.get('ApiKeyIds')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')

        if m.get('Keys') is not None:
            self.keys_shrink = m.get('Keys')

        if m.get('ModelNames') is not None:
            self.model_names_shrink = m.get('ModelNames')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

