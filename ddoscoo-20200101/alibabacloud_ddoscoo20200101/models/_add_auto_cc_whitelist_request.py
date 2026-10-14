# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAutoCcWhitelistRequest(DaraModel):
    def __init__(
        self,
        expire_time: int = None,
        instance_id: str = None,
        whitelist: str = None,
    ):
        # **[Deprecated]** This parameter is deprecated.
        # 
        # > This parameter specifies the validity period of blacklist IP addresses. Whitelist IP addresses are permanently valid by default. You do not need to set this parameter.
        self.expire_time = expire_time
        # The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance for which you want to add whitelist IP addresses.
        # 
        # > You can invoke [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) to query the IDs of all Anti-DDoS Pro or Anti-DDoS Premium instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The configuration of the whitelist IP addresses to add. This parameter is a string that is converted from a JSON array. Each element in the JSON array is a whitelist IP struct that contains the following field:
        # 
        # - **src**: String | Required | The IP address to add to the whitelist.
        # 
        # This parameter is required.
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

