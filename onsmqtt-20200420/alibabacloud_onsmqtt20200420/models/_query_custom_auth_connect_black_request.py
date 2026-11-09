# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCustomAuthConnectBlackRequest(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        instance_id: str = None,
        next_token: str = None,
        size: int = None,
    ):
        # The ID of the client to be queried.
        self.client_id = client_id
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token
        # The number of clients to be queried. Maximum value: 100.
        # 
        # This parameter is required.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

