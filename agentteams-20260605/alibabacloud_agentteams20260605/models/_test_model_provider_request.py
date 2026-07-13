# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TestModelProviderRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        model_name: str = None,
        prompt: str = None,
        provider_id: str = None,
        provider_name: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.model_name = model_name
        # This parameter is required.
        self.prompt = prompt
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        return self

