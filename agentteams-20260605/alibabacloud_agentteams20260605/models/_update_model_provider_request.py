# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateModelProviderRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        api_keys: List[str] = None,
        client_token: str = None,
        description: str = None,
        id: str = None,
        instance_id: str = None,
        protocols: List[str] = None,
    ):
        # This parameter is required.
        self.address = address
        # This parameter is required.
        self.api_keys = api_keys
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.protocols = protocols

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.api_keys is not None:
            result['ApiKeys'] = self.api_keys

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.protocols is not None:
            result['Protocols'] = self.protocols

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('ApiKeys') is not None:
            self.api_keys = m.get('ApiKeys')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')

        return self

