# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetContextStoreAPIKeyResponseBody(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        api_key: str = None,
        context_store_name: str = None,
        create_time: str = None,
        name: str = None,
        region_id: str = None,
        request_id: str = None,
    ):
        self.agent_space = agent_space
        self.api_key = api_key
        self.context_store_name = context_store_name
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.name = name
        self.region_id = region_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.context_store_name is not None:
            result['contextStoreName'] = self.context_store_name

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.name is not None:
            result['name'] = self.name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('contextStoreName') is not None:
            self.context_store_name = m.get('contextStoreName')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

