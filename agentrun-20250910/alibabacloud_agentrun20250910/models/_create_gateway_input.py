# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateGatewayInput(DaraModel):
    def __init__(
        self,
        identity_id: str = None,
        name: str = None,
        network_configuration: main_models.GatewayNetworkConfiguration = None,
        type: str = None,
    ):
        self.identity_id = identity_id
        self.name = name
        self.network_configuration = network_configuration
        self.type = type

    def validate(self):
        if self.network_configuration:
            self.network_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_id is not None:
            result['identityId'] = self.identity_id

        if self.name is not None:
            result['name'] = self.name

        if self.network_configuration is not None:
            result['networkConfiguration'] = self.network_configuration.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identityId') is not None:
            self.identity_id = m.get('identityId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networkConfiguration') is not None:
            temp_model = main_models.GatewayNetworkConfiguration()
            self.network_configuration = temp_model.from_map(m.get('networkConfiguration'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

