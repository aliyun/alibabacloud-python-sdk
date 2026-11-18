# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ModelSelection(DaraModel):
    def __init__(
        self,
        convenience_alias_enabled: bool = None,
        endpoints: List[str] = None,
        fallback_chains: List[main_models.ModelSelectionFallbackChains] = None,
        model_group_ids: List[str] = None,
        models: List[main_models.ModelSelectionModels] = None,
    ):
        # Specifies whether to enable convenience aliases. When enabled, all selected model names must be unique.
        self.convenience_alias_enabled = convenience_alias_enabled
        # The collection of explicitly selected built-in endpoint (route) names. This parameter is required and cannot be empty.
        self.endpoints = endpoints
        # The ordered fallback chains configured by endpoint and initial model.
        self.fallback_chains = fallback_chains
        # The selected model group IDs within the instance. Group identity is retained, the union of current members and single-selected models is calculated, and empty groups can be saved as drafts.
        self.model_group_ids = model_group_ids
        # The selected model collection.
        self.models = models

    def validate(self):
        if self.fallback_chains:
            for v1 in self.fallback_chains:
                 if v1:
                    v1.validate()
        if self.models:
            for v1 in self.models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.convenience_alias_enabled is not None:
            result['convenienceAliasEnabled'] = self.convenience_alias_enabled

        if self.endpoints is not None:
            result['endpoints'] = self.endpoints

        result['fallbackChains'] = []
        if self.fallback_chains is not None:
            for k1 in self.fallback_chains:
                result['fallbackChains'].append(k1.to_map() if k1 else None)

        if self.model_group_ids is not None:
            result['modelGroupIds'] = self.model_group_ids

        result['models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['models'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('convenienceAliasEnabled') is not None:
            self.convenience_alias_enabled = m.get('convenienceAliasEnabled')

        if m.get('endpoints') is not None:
            self.endpoints = m.get('endpoints')

        self.fallback_chains = []
        if m.get('fallbackChains') is not None:
            for k1 in m.get('fallbackChains'):
                temp_model = main_models.ModelSelectionFallbackChains()
                self.fallback_chains.append(temp_model.from_map(k1))

        if m.get('modelGroupIds') is not None:
            self.model_group_ids = m.get('modelGroupIds')

        self.models = []
        if m.get('models') is not None:
            for k1 in m.get('models'):
                temp_model = main_models.ModelSelectionModels()
                self.models.append(temp_model.from_map(k1))

        return self

class ModelSelectionModels(DaraModel):
    def __init__(
        self,
        model_card_id: str = None,
        service_id: str = None,
    ):
        # The model card ID.
        self.model_card_id = model_card_id
        # The explicit execution target AI service ID for the model. This parameter is optional and takes precedence over the provider default.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_card_id is not None:
            result['modelCardId'] = self.model_card_id

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelCardId') is not None:
            self.model_card_id = m.get('modelCardId')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        return self

class ModelSelectionFallbackChains(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        fallback_model_card_ids: List[str] = None,
        source_model_card_id: str = None,
    ):
        # The endpoint name to which the chain belongs. It must be one of the currently selected endpoints.
        self.endpoint = endpoint
        # The ordered collection of fallback model card IDs.
        self.fallback_model_card_ids = fallback_model_card_ids
        # The source model card ID.
        self.source_model_card_id = source_model_card_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.fallback_model_card_ids is not None:
            result['fallbackModelCardIds'] = self.fallback_model_card_ids

        if self.source_model_card_id is not None:
            result['sourceModelCardId'] = self.source_model_card_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('fallbackModelCardIds') is not None:
            self.fallback_model_card_ids = m.get('fallbackModelCardIds')

        if m.get('sourceModelCardId') is not None:
            self.source_model_card_id = m.get('sourceModelCardId')

        return self

