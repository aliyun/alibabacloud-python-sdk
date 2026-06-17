# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMonitorGroupNotifyPolicyRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        group_id: str = None,
        policy_type: str = None,
        region_id: str = None,
        start_time: int = None,
    ):
        # The end timestamp for pausing notifications.
        # 
        # The value is a UNIX timestamp, which represents the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The application group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The type of the pause notification. Currently, only PauseNotify is supported.
        # 
        # This parameter is required.
        self.policy_type = policy_type
        self.region_id = region_id
        # The start timestamp for pausing notifications.
        # 
        # The value is a UNIX timestamp, which represents the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
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

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

