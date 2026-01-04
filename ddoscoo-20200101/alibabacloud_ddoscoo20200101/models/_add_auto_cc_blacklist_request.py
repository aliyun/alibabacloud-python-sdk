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
        # The IP addresses that you want to manage. This parameter is a JSON string. The string contains the following field:
        # 
        # *   **src**: the IP address. This field is required and must be of the STRING type.
        # 
        # >  You can manually add up to 2,000 IP addresses to the IP address blacklist. Separate multiple IP addresses with spaces or line breaks.
        # 
        # This parameter is required.
        self.blacklist = blacklist
        # This parameter is required.
        self.expire_time = expire_time
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

