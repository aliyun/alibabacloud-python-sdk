# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelsRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        instance_id: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        provider_name: str = None,
    ):
        self.id = id
        # This parameter is required.
        self.instance_id = instance_id
        self.max_results = max_results
        self.name = name
        self.next_token = next_token
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        return self

