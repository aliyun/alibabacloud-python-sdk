# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAutoCcBlacklistRequest(DaraModel):
    def __init__(
        self,
        blacklist: str = None,
        instance_id: str = None,
        query_type: str = None,
    ):
        # A JSON string that contains the IP addresses to remove from the blacklist. The string has the following structure:
        # 
        # - **src**: The IP address to remove. This is a required string.
        # 
        # This parameter is required.
        self.blacklist = blacklist
        # The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # 
        # > Call [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) to query the IDs of all Anti-DDoS Pro and Anti-DDoS Premium instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.query_type = query_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.blacklist is not None:
            result['Blacklist'] = self.blacklist

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Blacklist') is not None:
            self.blacklist = m.get('Blacklist')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        return self

