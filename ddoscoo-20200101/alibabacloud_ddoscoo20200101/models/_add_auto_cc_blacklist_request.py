# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAutoCcBlacklistRequest(DaraModel):
    def __init__(
        self,
        blacklist: str = None,
        expire_time: int = None,
        instance_id: str = None,
    ):
        # The IP addresses to add to the blacklist. This is a JSON array. Each object in the array contains the following field:
        # 
        # - **src**: String. Required. The IP address to add.
        # 
        # > You can add up to 2,000 IP addresses per request.
        # 
        # This parameter is required.
        self.blacklist = blacklist
        # The expiration time for the blacklist entries, in seconds. Valid values: **300** to **604800**.
        # 
        # This parameter is required.
        self.expire_time = expire_time
        # The ID of the Anti-DDoS Pro instance.
        # 
        # > Call the **DescribeInstanceIds** operation to query the IDs of all Anti-DDoS Pro instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blacklist is not None:
            result['Blacklist'] = self.blacklist

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Blacklist') is not None:
            self.blacklist = m.get('Blacklist')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

