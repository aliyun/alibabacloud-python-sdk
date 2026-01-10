# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Model(DaraModel):
    def __init__(
        self,
        address: str = None,
        api_key: str = None,
        created_time: str = None,
        desc: str = None,
        gateway_id: str = None,
        model_id: str = None,
        models: str = None,
        models_weight: str = None,
        name: str = None,
        provider: str = None,
        target_id: str = None,
        tenant_id: str = None,
        type: str = None,
        update_time: str = None,
    ):
        self.address = address
        self.api_key = api_key
        self.created_time = created_time
        self.desc = desc
        self.gateway_id = gateway_id
        self.model_id = model_id
        self.models = models
        self.models_weight = models_weight
        self.name = name
        self.provider = provider
        self.target_id = target_id
        self.tenant_id = tenant_id
        self.type = type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.desc is not None:
            result['desc'] = self.desc

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.models is not None:
            result['models'] = self.models

        if self.models_weight is not None:
            result['modelsWeight'] = self.models_weight

        if self.name is not None:
            result['name'] = self.name

        if self.provider is not None:
            result['provider'] = self.provider

        if self.target_id is not None:
            result['targetId'] = self.target_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.type is not None:
            result['type'] = self.type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('models') is not None:
            self.models = m.get('models')

        if m.get('modelsWeight') is not None:
            self.models_weight = m.get('modelsWeight')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

