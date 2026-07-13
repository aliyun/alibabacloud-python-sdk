# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateModelRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        protocols: List[str] = None,
        provider: str = None,
        provider_id: str = None,
        provider_name: str = None,
    ):
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.protocols = protocols
        self.provider = provider
        # This parameter is required.
        self.provider_id = provider_id
        # This parameter is required.
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.protocols is not None:
            result['Protocols'] = self.protocols

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        return self

