# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ManageSchedulerxNotificationPolicyRequest(DaraModel):
    def __init__(
        self,
        channel_time_range: str = None,
        description: str = None,
        policy_name: str = None,
        region_id: str = None,
    ):
        # The time range configuration for notification channels.
        # 
        # >  See the supplementary description of ChannelTimeRange in the request parameters.
        self.channel_time_range = channel_time_range
        # The notification policy description.
        self.description = description
        # The name of the notification policy.
        # 
        # This parameter is required.
        self.policy_name = policy_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_time_range is not None:
            result['ChannelTimeRange'] = self.channel_time_range

        if self.description is not None:
            result['Description'] = self.description

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelTimeRange') is not None:
            self.channel_time_range = m.get('ChannelTimeRange')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

