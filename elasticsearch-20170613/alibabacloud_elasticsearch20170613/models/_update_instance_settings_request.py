# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class UpdateInstanceSettingsRequest(DaraModel):
    def __init__(
        self,
        es_config: Dict[str, str] = None,
        client_token: str = None,
        force: bool = None,
        update_strategy: str = None,
    ):
        # The YML file configuration of the instance.
        self.es_config = es_config
        # A unique token used to ensure the idempotence of the request. The client generates this value. The value must be unique among different requests and cannot exceed 64 ASCII characters in length.
        self.client_token = client_token
        # Specifies whether to forcibly apply the change.
        self.force = force
        # The change strategy for Elasticsearch (for example, the change method used during index updates, cluster upgrades, or service deployments). Valid values:
        # - blue_green: blue-green change. Achieves seamless switchover by running two identical environments (blue and green) in parallel.
        # - normal: in-place change. Performs changes directly in the current environment (for example, upgrades or scaling) without requiring additional resources.
        # - intelligent: intelligent change. The system automatically analyzes the change type and environment state, and dynamically selects the optimal change method (blue-green change or in-place change).
        self.update_strategy = update_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.es_config is not None:
            result['esConfig'] = self.es_config

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.force is not None:
            result['force'] = self.force

        if self.update_strategy is not None:
            result['updateStrategy'] = self.update_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('esConfig') is not None:
            self.es_config = m.get('esConfig')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('force') is not None:
            self.force = m.get('force')

        if m.get('updateStrategy') is not None:
            self.update_strategy = m.get('updateStrategy')

        return self

