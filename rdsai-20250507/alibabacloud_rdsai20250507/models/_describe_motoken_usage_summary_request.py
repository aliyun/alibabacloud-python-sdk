# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMOTokenUsageSummaryRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        end_time: str = None,
        instance_id: str = None,
        model: str = None,
        start_time: str = None,
        usage_type: str = None,
    ):
        self.api_key = api_key
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        self.model = model
        self.start_time = start_time
        self.usage_type = usage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.model is not None:
            result['Model'] = self.model

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.usage_type is not None:
            result['UsageType'] = self.usage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UsageType') is not None:
            self.usage_type = m.get('UsageType')

        return self

