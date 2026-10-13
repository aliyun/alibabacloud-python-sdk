# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLLMTokenUsageRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        instance_name: str = None,
        model: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The end time of the inspection in UTC. Specify the time in the ISO 8601 standard. Format: YYYY-MM-DDTHH:mm:ssZ. The end time must be at least 2 hours later than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The instance ID of the AI application.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The model to query.
        self.model = model
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The start time of the inspection in UTC. Specify the time in the ISO 8601 standard. Format: YYYY-MM-DDTHH:mm:ssZ.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.model is not None:
            result['Model'] = self.model

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

