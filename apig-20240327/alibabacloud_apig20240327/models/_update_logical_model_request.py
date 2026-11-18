# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateLogicalModelRequest(DaraModel):
    def __init__(
        self,
        call_strategy: str = None,
        fallback_targets: List[main_models.UpdateLogicalModelRequestFallbackTargets] = None,
        name: str = None,
        response_model: str = None,
        routing_policy: str = None,
        slots: main_models.UpdateLogicalModelRequestSlots = None,
        targets: List[main_models.UpdateLogicalModelRequestTargets] = None,
        confirmation_token: str = None,
        expected_revision: int = None,
    ):
        # The call strategy. This parameter is required for new Auto write requests. Valid values: balanced, cheap, fast, and quality. The new version uses only the basic invocation name. Do not submit this parameter for Mapping and Weighted. The server performs conditional validation.
        self.call_strategy = call_strategy
        # The ordered fallback targets. A maximum of 5 targets are supported. The targets are deduplicated by the actual card ID. This can be an empty array.
        # 
        # This parameter is required.
        self.fallback_targets = fallback_targets
        # The client logical invocation name. It must be encoded in UTF-8 and can be up to 256 bytes in length. It cannot contain spaces or slashes, and cannot start with auto.
        # 
        # This parameter is required.
        self.name = name
        # The response model. If set to Actual, the public name of the actual model is returned. If set to Logical, the entry name is returned, including Server-Sent Events (SSE).
        # 
        # This parameter is required.
        self.response_model = response_model
        # The routing policy. Valid values: Mapping, Weighted, and Auto. If you set this parameter to Auto, targets must be an empty array and slots is required.
        # 
        # This parameter is required.
        self.routing_policy = routing_policy
        # The slots. This parameter is submitted only for Auto. Each of the simple, standard, and complex slots requires 1 to 3 source cards. The three slots are globally deduplicated by modelCardId. Omit this parameter for Mapping and Weighted.
        self.slots = slots
        # The primary targets. For Mapping, exactly one item is allowed. For Weighted, the sum of original relative weights must be greater than 0. For Auto, this must be an empty array.
        # 
        # This parameter is required.
        self.targets = targets
        # The confirmation token returned by the configuration update dry run. Pass this token as is when you submit the update.
        self.confirmation_token = confirmation_token
        # The expected configuration revision number. Use the revision returned by the most recent query or dry run.
        # 
        # This parameter is required.
        self.expected_revision = expected_revision

    def validate(self):
        if self.fallback_targets:
            for v1 in self.fallback_targets:
                 if v1:
                    v1.validate()
        if self.slots:
            self.slots.validate()
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_strategy is not None:
            result['callStrategy'] = self.call_strategy

        result['fallbackTargets'] = []
        if self.fallback_targets is not None:
            for k1 in self.fallback_targets:
                result['fallbackTargets'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.response_model is not None:
            result['responseModel'] = self.response_model

        if self.routing_policy is not None:
            result['routingPolicy'] = self.routing_policy

        if self.slots is not None:
            result['slots'] = self.slots.to_map()

        result['targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['targets'].append(k1.to_map() if k1 else None)

        if self.confirmation_token is not None:
            result['confirmationToken'] = self.confirmation_token

        if self.expected_revision is not None:
            result['expectedRevision'] = self.expected_revision

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callStrategy') is not None:
            self.call_strategy = m.get('callStrategy')

        self.fallback_targets = []
        if m.get('fallbackTargets') is not None:
            for k1 in m.get('fallbackTargets'):
                temp_model = main_models.UpdateLogicalModelRequestFallbackTargets()
                self.fallback_targets.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('responseModel') is not None:
            self.response_model = m.get('responseModel')

        if m.get('routingPolicy') is not None:
            self.routing_policy = m.get('routingPolicy')

        if m.get('slots') is not None:
            temp_model = main_models.UpdateLogicalModelRequestSlots()
            self.slots = temp_model.from_map(m.get('slots'))

        self.targets = []
        if m.get('targets') is not None:
            for k1 in m.get('targets'):
                temp_model = main_models.UpdateLogicalModelRequestTargets()
                self.targets.append(temp_model.from_map(k1))

        if m.get('confirmationToken') is not None:
            self.confirmation_token = m.get('confirmationToken')

        if m.get('expectedRevision') is not None:
            self.expected_revision = m.get('expectedRevision')

        return self

class UpdateLogicalModelRequestTargets(DaraModel):
    def __init__(
        self,
        model_card_id: str = None,
        weight: int = None,
    ):
        # The ID of the actual source model card in the same instance. The ID starts with msc-. VMs or service overrides are not supported.
        # 
        # This parameter is required.
        self.model_card_id = model_card_id
        # The weight. Valid values: integers from 0 to 10000. The original value is preserved. For Mapping, 0 is allowed.
        # 
        # This parameter is required.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_card_id is not None:
            result['modelCardId'] = self.model_card_id

        if self.weight is not None:
            result['weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelCardId') is not None:
            self.model_card_id = m.get('modelCardId')

        if m.get('weight') is not None:
            self.weight = m.get('weight')

        return self

class UpdateLogicalModelRequestSlots(DaraModel):
    def __init__(
        self,
        complex: List[main_models.UpdateLogicalModelRequestSlotsComplex] = None,
        simple: List[main_models.UpdateLogicalModelRequestSlotsSimple] = None,
        standard: List[main_models.UpdateLogicalModelRequestSlotsStandard] = None,
    ):
        # The complex slot. It requires 1 to 3 source cards. The three slots are globally deduplicated by modelCardId.
        # 
        # This parameter is required.
        self.complex = complex
        # The simple slot. It requires 1 to 3 source cards. The three slots are globally deduplicated by modelCardId.
        # 
        # This parameter is required.
        self.simple = simple
        # The standard slot. It requires 1 to 3 source cards. The three slots are globally deduplicated by modelCardId.
        # 
        # This parameter is required.
        self.standard = standard

    def validate(self):
        if self.complex:
            for v1 in self.complex:
                 if v1:
                    v1.validate()
        if self.simple:
            for v1 in self.simple:
                 if v1:
                    v1.validate()
        if self.standard:
            for v1 in self.standard:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['complex'] = []
        if self.complex is not None:
            for k1 in self.complex:
                result['complex'].append(k1.to_map() if k1 else None)

        result['simple'] = []
        if self.simple is not None:
            for k1 in self.simple:
                result['simple'].append(k1.to_map() if k1 else None)

        result['standard'] = []
        if self.standard is not None:
            for k1 in self.standard:
                result['standard'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.complex = []
        if m.get('complex') is not None:
            for k1 in m.get('complex'):
                temp_model = main_models.UpdateLogicalModelRequestSlotsComplex()
                self.complex.append(temp_model.from_map(k1))

        self.simple = []
        if m.get('simple') is not None:
            for k1 in m.get('simple'):
                temp_model = main_models.UpdateLogicalModelRequestSlotsSimple()
                self.simple.append(temp_model.from_map(k1))

        self.standard = []
        if m.get('standard') is not None:
            for k1 in m.get('standard'):
                temp_model = main_models.UpdateLogicalModelRequestSlotsStandard()
                self.standard.append(temp_model.from_map(k1))

        return self

class UpdateLogicalModelRequestSlotsStandard(DaraModel):
    def __init__(
        self,
        model_card_id: str = None,
    ):
        # The ID of the actual source card in the same instance. The ID starts with msc-. VMs or service overrides are not supported.
        # 
        # This parameter is required.
        self.model_card_id = model_card_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_card_id is not None:
            result['modelCardId'] = self.model_card_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelCardId') is not None:
            self.model_card_id = m.get('modelCardId')

        return self

class UpdateLogicalModelRequestSlotsSimple(DaraModel):
    def __init__(
        self,
        model_card_id: str = None,
    ):
        # The ID of the actual source card in the same instance. The ID starts with msc-. VMs or service overrides are not supported.
        # 
        # This parameter is required.
        self.model_card_id = model_card_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_card_id is not None:
            result['modelCardId'] = self.model_card_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelCardId') is not None:
            self.model_card_id = m.get('modelCardId')

        return self

class UpdateLogicalModelRequestSlotsComplex(DaraModel):
    def __init__(
        self,
        model_card_id: str = None,
    ):
        # The ID of the actual source card in the same instance. The ID starts with msc-. VMs or service overrides are not supported.
        # 
        # This parameter is required.
        self.model_card_id = model_card_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_card_id is not None:
            result['modelCardId'] = self.model_card_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelCardId') is not None:
            self.model_card_id = m.get('modelCardId')

        return self

class UpdateLogicalModelRequestFallbackTargets(DaraModel):
    def __init__(
        self,
        model_card_id: str = None,
    ):
        # The ID of the actual source card in the same instance.
        # 
        # This parameter is required.
        self.model_card_id = model_card_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_card_id is not None:
            result['modelCardId'] = self.model_card_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('modelCardId') is not None:
            self.model_card_id = m.get('modelCardId')

        return self

