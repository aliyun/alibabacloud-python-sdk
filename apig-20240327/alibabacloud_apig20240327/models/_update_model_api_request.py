# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateModelApiRequest(DaraModel):
    def __init__(
        self,
        base_path: str = None,
        description: str = None,
        direct_supply_fallback_enabled: bool = None,
        domain_ids: List[str] = None,
        enable_auth: bool = None,
        first_byte_timeout: int = None,
        model_selection: main_models.ModelSelection = None,
        model_selection_delta: main_models.ModelSelectionDelta = None,
        name: str = None,
        policy_configs: List[main_models.ModelApiPolicyConfig] = None,
    ):
        # The API access prefix. The default value is / during creation. If omitted during an update, the original value is retained.
        self.base_path = base_path
        # The description of the model API. If omitted during an update, the original value is retained.
        self.description = description
        # Specifies whether to enable direct supply fallback. If omitted during an update, the original value is retained. Explicitly set to false to disable it.
        self.direct_supply_fallback_enabled = direct_supply_fallback_enabled
        # The IDs of the selected custom or default domain names of the instance. This parameter must be explicitly non-empty during creation. If omitted during an update, the original value is retained. When submitted, the entire list is replaced and cannot be empty.
        self.domain_ids = domain_ids
        # Specifies whether to enable consumer API key authentication. If omitted during an update, the original value is retained. The type is fixed to Apikey or Custom.
        self.enable_auth = enable_auth
        # The time to first byte.
        self.first_byte_timeout = first_byte_timeout
        # The model selection. This parameter is required during creation. If omitted during an update, the original value is retained. When submitted, the entire selection is replaced.
        self.model_selection = model_selection
        # Supported only by the new version of ModelAPI in minimalist mode: merges the actual source model IDs added to or removed from the model source in this request into the latest selection within the lock. This parameter is mutually exclusive with modelSelection and cannot be null or an empty delta. The standard update and publish process applies.
        self.model_selection_delta = model_selection_delta
        # The name of the model API. If omitted or set to null, the original value is retained. When submitted, the value is trimmed of leading and trailing whitespace, must be non-empty, contain a maximum of 128 UTF-8 bytes, and cannot contain @ or /. Renaming the API does not change the API ID or access prefix.
        self.name = name
        # The configurations for AI request logs and AI security protection. If omitted during an update, the original values are retained. When submitted, the inline policies of both types are entirely replaced. An empty array clears both types. Independent token quotas are not affected.
        self.policy_configs = policy_configs

    def validate(self):
        if self.model_selection:
            self.model_selection.validate()
        if self.model_selection_delta:
            self.model_selection_delta.validate()
        if self.policy_configs:
            for v1 in self.policy_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_path is not None:
            result['basePath'] = self.base_path

        if self.description is not None:
            result['description'] = self.description

        if self.direct_supply_fallback_enabled is not None:
            result['directSupplyFallbackEnabled'] = self.direct_supply_fallback_enabled

        if self.domain_ids is not None:
            result['domainIds'] = self.domain_ids

        if self.enable_auth is not None:
            result['enableAuth'] = self.enable_auth

        if self.first_byte_timeout is not None:
            result['firstByteTimeout'] = self.first_byte_timeout

        if self.model_selection is not None:
            result['modelSelection'] = self.model_selection.to_map()

        if self.model_selection_delta is not None:
            result['modelSelectionDelta'] = self.model_selection_delta.to_map()

        if self.name is not None:
            result['name'] = self.name

        result['policyConfigs'] = []
        if self.policy_configs is not None:
            for k1 in self.policy_configs:
                result['policyConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basePath') is not None:
            self.base_path = m.get('basePath')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directSupplyFallbackEnabled') is not None:
            self.direct_supply_fallback_enabled = m.get('directSupplyFallbackEnabled')

        if m.get('domainIds') is not None:
            self.domain_ids = m.get('domainIds')

        if m.get('enableAuth') is not None:
            self.enable_auth = m.get('enableAuth')

        if m.get('firstByteTimeout') is not None:
            self.first_byte_timeout = m.get('firstByteTimeout')

        if m.get('modelSelection') is not None:
            temp_model = main_models.ModelSelection()
            self.model_selection = temp_model.from_map(m.get('modelSelection'))

        if m.get('modelSelectionDelta') is not None:
            temp_model = main_models.ModelSelectionDelta()
            self.model_selection_delta = temp_model.from_map(m.get('modelSelectionDelta'))

        if m.get('name') is not None:
            self.name = m.get('name')

        self.policy_configs = []
        if m.get('policyConfigs') is not None:
            for k1 in m.get('policyConfigs'):
                temp_model = main_models.ModelApiPolicyConfig()
                self.policy_configs.append(temp_model.from_map(k1))

        return self

