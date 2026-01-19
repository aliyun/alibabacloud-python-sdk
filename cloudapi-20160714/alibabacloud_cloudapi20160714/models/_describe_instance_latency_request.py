# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceLatencyRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        instance_id: str = None,
        security_token: str = None,
        stage_name: str = None,
        start_time: str = None,
    ):
        # The end time. The time follows the ISO 8601 standard and UTC time is used. Format: YYYY-MM-DDThh:mm:ssZ
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.security_token = security_token
        # The environment in which the API is requested. Valid values:
        # 
        # *   **RELEASE**: the production environment
        # *   **PRE**: the pre-release environment
        # *   **TEST**: the test environment
        # 
        # This parameter is required.
        self.stage_name = stage_name
        # The start time. The time follows the ISO 8601 standard and UTC time is used. Format: YYYY-MM-DDThh:mm:ssZ
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

