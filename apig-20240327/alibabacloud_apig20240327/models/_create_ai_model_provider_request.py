# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateAiModelProviderRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        gateway_id: str = None,
        provider: str = None,
        service_ids: List[str] = None,
    ):
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.gateway_id = gateway_id
        # This parameter is required.
        self.provider = provider
        self.service_ids = service_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.provider is not None:
            result['provider'] = self.provider

        if self.service_ids is not None:
            result['serviceIds'] = self.service_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('serviceIds') is not None:
            self.service_ids = m.get('serviceIds')

        return self

