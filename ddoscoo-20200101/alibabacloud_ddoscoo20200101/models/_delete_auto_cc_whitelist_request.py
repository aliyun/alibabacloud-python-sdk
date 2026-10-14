# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAutoCcWhitelistRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        whitelist: str = None,
    ):
        # The ID of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        # > You can call [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) to query the IDs of all Anti-DDoS Pro or Anti-DDoS Premium instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The details of the whitelist IP, expressed as a JSON string with the following structure.
        # - **src: String** type, required, the whitelist IP.
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

