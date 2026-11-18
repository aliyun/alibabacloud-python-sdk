# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListLogicalModelsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListLogicalModelsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListLogicalModelsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListLogicalModelsResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListLogicalModelsResponseBodyDataItems] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The list of logical models.
        self.items = items
        # The maximum number of entries returned for the current request.
        self.max_results = max_results
        # The cursor token for querying the next page. This parameter is not returned if no more data is available.
        self.next_token = next_token
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListLogicalModelsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListLogicalModelsResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        available_paths: List[main_models.ListLogicalModelsResponseBodyDataItemsAvailablePaths] = None,
        call_strategy: str = None,
        deployment: main_models.ListLogicalModelsResponseBodyDataItemsDeployment = None,
        fallback_targets: List[main_models.ListLogicalModelsResponseBodyDataItemsFallbackTargets] = None,
        features: Dict[str, Any] = None,
        gateway_id: str = None,
        logical_model_id: str = None,
        meta: main_models.ListLogicalModelsResponseBodyDataItemsMeta = None,
        name: str = None,
        requires_activation: bool = None,
        response_model: str = None,
        revision: int = None,
        routing_policy: str = None,
        slots: main_models.ListLogicalModelsResponseBodyDataItemsSlots = None,
        targets: List[main_models.ListLogicalModelsResponseBodyDataItemsTargets] = None,
        update_time: str = None,
    ):
        # The list of call paths commonly supported by all primary targets.
        self.available_paths = available_paths
        # The call strategy. This parameter is returned only for the Auto policy. Valid values: balanced, cheap, fast, and quality. This parameter can be omitted. If omitted, the default strategy is balanced. This parameter is not returned for the Mapping and Weighted policies.
        self.call_strategy = call_strategy
        # The configuration delivery record. A successful API response only indicates that the request is accepted, not that the configuration has taken effect.
        self.deployment = deployment
        # The ordered fallback targets. A maximum of 5 fallback targets are supported. The targets are deduplicated by the actual card ID. This parameter can be an empty array.
        self.fallback_targets = fallback_targets
        # The intersection of the Boolean capabilities of all primary targets.
        self.features = features
        # The ID of the gateway instance to which the logical model belongs.
        self.gateway_id = gateway_id
        # The logical model ID. The ID starts with "vm-".
        self.logical_model_id = logical_model_id
        # The aggregated information about the capabilities of the primary targets.
        self.meta = meta
        # The client logical call name. It supports a maximum of 256 bytes in UTF-8, must not contain spaces or slashes, and must not start with "auto".
        self.name = name
        # Specifies whether activation is required. This parameter is returned only for the Auto policy. The value is true if the AI Credits Router commodity is not activated, and false if it is activated. This parameter is omitted if the read operation fails or the status is unknown. This parameter is omitted for the Mapping and Weighted policies.
        self.requires_activation = requires_activation
        # The response model type. If the value is Actual, the public name of the actual model is returned. If the value is Logical, the entry name of the logical model is returned.
        self.response_model = response_model
        # The object version number. The initial value is 1 upon creation and increments after each successful update.
        self.revision = revision
        # The routing policy. Valid values: Mapping, Weighted, and Auto. If the value is Auto, the targets parameter must be an empty array and the slots parameter is required.
        self.routing_policy = routing_policy
        # The slots. This parameter is returned only for the Auto policy. Each of the simple, standard, and complex slots contains 1 to 3 source cards. The three slots are globally deduplicated by modelCardId. This parameter is omitted for the Mapping and Weighted policies.
        self.slots = slots
        # The primary targets. For the Mapping policy, exactly one target is allowed. For the Weighted policy, the sum of original relative weights must be greater than 0. For the Auto policy, this must be an empty array.
        self.targets = targets
        # The last modification time. The time is in the ISO 8601 (RFC 3339) format and UTC time zone, such as 2026-05-15T10:00:00Z.
        self.update_time = update_time

    def validate(self):
        if self.available_paths:
            for v1 in self.available_paths:
                 if v1:
                    v1.validate()
        if self.deployment:
            self.deployment.validate()
        if self.fallback_targets:
            for v1 in self.fallback_targets:
                 if v1:
                    v1.validate()
        if self.meta:
            self.meta.validate()
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
        result['availablePaths'] = []
        if self.available_paths is not None:
            for k1 in self.available_paths:
                result['availablePaths'].append(k1.to_map() if k1 else None)

        if self.call_strategy is not None:
            result['callStrategy'] = self.call_strategy

        if self.deployment is not None:
            result['deployment'] = self.deployment.to_map()

        result['fallbackTargets'] = []
        if self.fallback_targets is not None:
            for k1 in self.fallback_targets:
                result['fallbackTargets'].append(k1.to_map() if k1 else None)

        if self.features is not None:
            result['features'] = self.features

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.logical_model_id is not None:
            result['logicalModelId'] = self.logical_model_id

        if self.meta is not None:
            result['meta'] = self.meta.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.requires_activation is not None:
            result['requiresActivation'] = self.requires_activation

        if self.response_model is not None:
            result['responseModel'] = self.response_model

        if self.revision is not None:
            result['revision'] = self.revision

        if self.routing_policy is not None:
            result['routingPolicy'] = self.routing_policy

        if self.slots is not None:
            result['slots'] = self.slots.to_map()

        result['targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['targets'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_paths = []
        if m.get('availablePaths') is not None:
            for k1 in m.get('availablePaths'):
                temp_model = main_models.ListLogicalModelsResponseBodyDataItemsAvailablePaths()
                self.available_paths.append(temp_model.from_map(k1))

        if m.get('callStrategy') is not None:
            self.call_strategy = m.get('callStrategy')

        if m.get('deployment') is not None:
            temp_model = main_models.ListLogicalModelsResponseBodyDataItemsDeployment()
            self.deployment = temp_model.from_map(m.get('deployment'))

        self.fallback_targets = []
        if m.get('fallbackTargets') is not None:
            for k1 in m.get('fallbackTargets'):
                temp_model = main_models.ListLogicalModelsResponseBodyDataItemsFallbackTargets()
                self.fallback_targets.append(temp_model.from_map(k1))

        if m.get('features') is not None:
            self.features = m.get('features')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('logicalModelId') is not None:
            self.logical_model_id = m.get('logicalModelId')

        if m.get('meta') is not None:
            temp_model = main_models.ListLogicalModelsResponseBodyDataItemsMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('requiresActivation') is not None:
            self.requires_activation = m.get('requiresActivation')

        if m.get('responseModel') is not None:
            self.response_model = m.get('responseModel')

        if m.get('revision') is not None:
            self.revision = m.get('revision')

        if m.get('routingPolicy') is not None:
            self.routing_policy = m.get('routingPolicy')

        if m.get('slots') is not None:
            temp_model = main_models.ListLogicalModelsResponseBodyDataItemsSlots()
            self.slots = temp_model.from_map(m.get('slots'))

        self.targets = []
        if m.get('targets') is not None:
            for k1 in m.get('targets'):
                temp_model = main_models.ListLogicalModelsResponseBodyDataItemsTargets()
                self.targets.append(temp_model.from_map(k1))

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class ListLogicalModelsResponseBodyDataItemsTargets(DaraModel):
    def __init__(
        self,
        model_card_id: str = None,
        weight: int = None,
    ):
        # The ID of the actual source model card within the same instance. The ID starts with "msc-". Virtual machines (VMs) or service overrides are not supported.
        # 
        # This parameter is required.
        self.model_card_id = model_card_id
        # The weight. The value is an integer from 0 to 10000 and is saved as the original value. A value of 0 is allowed for the Mapping policy.
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

class ListLogicalModelsResponseBodyDataItemsSlots(DaraModel):
    def __init__(
        self,
        complex: List[main_models.ListLogicalModelsResponseBodyDataItemsSlotsComplex] = None,
        simple: List[main_models.ListLogicalModelsResponseBodyDataItemsSlotsSimple] = None,
        standard: List[main_models.ListLogicalModelsResponseBodyDataItemsSlotsStandard] = None,
    ):
        # The complex slot, which contains 1 to 3 source cards. The three slots are globally deduplicated by modelCardId.
        # 
        # This parameter is required.
        self.complex = complex
        # The simple slot, which contains 1 to 3 source cards. The three slots are globally deduplicated by modelCardId.
        # 
        # This parameter is required.
        self.simple = simple
        # The standard slot, which contains 1 to 3 source cards. The three slots are globally deduplicated by modelCardId.
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
                temp_model = main_models.ListLogicalModelsResponseBodyDataItemsSlotsComplex()
                self.complex.append(temp_model.from_map(k1))

        self.simple = []
        if m.get('simple') is not None:
            for k1 in m.get('simple'):
                temp_model = main_models.ListLogicalModelsResponseBodyDataItemsSlotsSimple()
                self.simple.append(temp_model.from_map(k1))

        self.standard = []
        if m.get('standard') is not None:
            for k1 in m.get('standard'):
                temp_model = main_models.ListLogicalModelsResponseBodyDataItemsSlotsStandard()
                self.standard.append(temp_model.from_map(k1))

        return self

class ListLogicalModelsResponseBodyDataItemsSlotsStandard(DaraModel):
    def __init__(
        self,
        model_card_id: str = None,
    ):
        # The ID of the actual source card within the same instance. The ID starts with "msc-". VMs or service overrides are not supported.
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

class ListLogicalModelsResponseBodyDataItemsSlotsSimple(DaraModel):
    def __init__(
        self,
        model_card_id: str = None,
    ):
        # The ID of the actual source card within the same instance. The ID starts with "msc-". VMs or service overrides are not supported.
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

class ListLogicalModelsResponseBodyDataItemsSlotsComplex(DaraModel):
    def __init__(
        self,
        model_card_id: str = None,
    ):
        # The ID of the actual source card within the same instance. The ID starts with "msc-". VMs or service overrides are not supported.
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

class ListLogicalModelsResponseBodyDataItemsMeta(DaraModel):
    def __init__(
        self,
        max_input_tokens: int = None,
        max_output_tokens: int = None,
        max_tokens: int = None,
        supported_input_modalities: List[str] = None,
        supported_output_modalities: List[str] = None,
    ):
        # The minimum input token limit when all primary targets declare the limit. This parameter is not returned if the limit of any target is unknown.
        self.max_input_tokens = max_input_tokens
        # The minimum output token limit when all primary targets declare the limit. This parameter is not returned if the limit of any target is unknown.
        self.max_output_tokens = max_output_tokens
        # The minimum total token limit when all primary targets declare the limit. This parameter is not returned if the limit of any target is unknown.
        self.max_tokens = max_tokens
        # The input modalities commonly supported by all primary targets.
        self.supported_input_modalities = supported_input_modalities
        # The output modalities commonly supported by all primary targets.
        self.supported_output_modalities = supported_output_modalities

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_input_tokens is not None:
            result['maxInputTokens'] = self.max_input_tokens

        if self.max_output_tokens is not None:
            result['maxOutputTokens'] = self.max_output_tokens

        if self.max_tokens is not None:
            result['maxTokens'] = self.max_tokens

        if self.supported_input_modalities is not None:
            result['supportedInputModalities'] = self.supported_input_modalities

        if self.supported_output_modalities is not None:
            result['supportedOutputModalities'] = self.supported_output_modalities

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxInputTokens') is not None:
            self.max_input_tokens = m.get('maxInputTokens')

        if m.get('maxOutputTokens') is not None:
            self.max_output_tokens = m.get('maxOutputTokens')

        if m.get('maxTokens') is not None:
            self.max_tokens = m.get('maxTokens')

        if m.get('supportedInputModalities') is not None:
            self.supported_input_modalities = m.get('supportedInputModalities')

        if m.get('supportedOutputModalities') is not None:
            self.supported_output_modalities = m.get('supportedOutputModalities')

        return self

class ListLogicalModelsResponseBodyDataItemsFallbackTargets(DaraModel):
    def __init__(
        self,
        model_card_id: str = None,
    ):
        # The ID of the actual source card within the same instance.
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

class ListLogicalModelsResponseBodyDataItemsDeployment(DaraModel):
    def __init__(
        self,
        operation_id: str = None,
        revision: int = None,
        status: str = None,
    ):
        # The ID of the current configuration delivery operation.
        self.operation_id = operation_id
        # The object configuration version.
        self.revision = revision
        # The configuration delivery status. Valid values: Pending, Running, Succeeded, PartiallyFailed, and Failed. This status is independent of the API release status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_id is not None:
            result['operationId'] = self.operation_id

        if self.revision is not None:
            result['revision'] = self.revision

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')

        if m.get('revision') is not None:
            self.revision = m.get('revision')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class ListLogicalModelsResponseBodyDataItemsAvailablePaths(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The call path.
        self.path = path
        # The path type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['path'] = self.path

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

