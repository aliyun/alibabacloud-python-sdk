# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCustomAuthPermissionRequest(DaraModel):
    def __init__(
        self,
        identity: str = None,
        identity_type: str = None,
        instance_id: str = None,
        next_token: str = None,
        size: int = None,
        topic: str = None,
    ):
        # The username or client ID.
        self.identity = identity
        # The identity type.
        self.identity_type = identity_type
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The token that marks the end position of the previous returned page. To obtain the next batch of data, call the operation again by using the value of NextToken returned by the previous request. If you call this operation for the first time or want to query all results, set NextToken to an empty string.
        self.next_token = next_token
        # The number of queries to be returned. Maximum value: 100.
        # 
        # This parameter is required.
        self.size = size
        # The topic whose authorization information you want to query. Multi-level topics and wildcard characters are supported.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity is not None:
            result['Identity'] = self.identity

        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.size is not None:
            result['Size'] = self.size

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identity') is not None:
            self.identity = m.get('Identity')

        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

