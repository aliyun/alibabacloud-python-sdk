# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateAiModelCardRequest(DaraModel):
    def __init__(
        self,
        available_paths: List[main_models.UpdateAiModelCardRequestAvailablePaths] = None,
        credit: main_models.UpdateAiModelCardRequestCredit = None,
        features: Dict[str, Any] = None,
        meta: main_models.UpdateAiModelCardRequestMeta = None,
        model_name: str = None,
        model_provider: str = None,
    ):
        # The list of invocation paths supported by the model. Each item must include both path and type. The list is overwritten as a whole during updates.
        self.available_paths = available_paths
        # The credit billing information of the model. Only the fixed type is supported. The unit is Credits per million tokens. If not specified, all cost values default to 0.
        self.credit = credit
        # The model capability switches. Keys must be model capability names supported by the API gateway. Values are Boolean.
        self.features = features
        # The token limits and input/output modality information of the model.
        self.meta = meta
        # The model name. The name must be unique within the same AI gateway instance and model provider. Maximum length: 256 characters.
        # 
        # This parameter is required.
        self.model_name = model_name
        # The model provider identifier. The value must reference an existing model provider in the target AI gateway instance. Maximum length: 128 characters.
        # 
        # This parameter is required.
        self.model_provider = model_provider

    def validate(self):
        if self.available_paths:
            for v1 in self.available_paths:
                 if v1:
                    v1.validate()
        if self.credit:
            self.credit.validate()
        if self.meta:
            self.meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['availablePaths'] = []
        if self.available_paths is not None:
            for k1 in self.available_paths:
                result['availablePaths'].append(k1.to_map() if k1 else None)

        if self.credit is not None:
            result['credit'] = self.credit.to_map()

        if self.features is not None:
            result['features'] = self.features

        if self.meta is not None:
            result['meta'] = self.meta.to_map()

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_provider is not None:
            result['modelProvider'] = self.model_provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_paths = []
        if m.get('availablePaths') is not None:
            for k1 in m.get('availablePaths'):
                temp_model = main_models.UpdateAiModelCardRequestAvailablePaths()
                self.available_paths.append(temp_model.from_map(k1))

        if m.get('credit') is not None:
            temp_model = main_models.UpdateAiModelCardRequestCredit()
            self.credit = temp_model.from_map(m.get('credit'))

        if m.get('features') is not None:
            self.features = m.get('features')

        if m.get('meta') is not None:
            temp_model = main_models.UpdateAiModelCardRequestMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelProvider') is not None:
            self.model_provider = m.get('modelProvider')

        return self

class UpdateAiModelCardRequestMeta(DaraModel):
    def __init__(
        self,
        max_input_tokens: int = None,
        max_output_tokens: int = None,
        max_tokens: int = None,
        supported_input_modalities: List[str] = None,
        supported_output_modalities: List[str] = None,
    ):
        # The maximum number of input tokens supported by the model. The value must be greater than or equal to 0.
        self.max_input_tokens = max_input_tokens
        # The maximum number of output tokens supported by the model. The value must be greater than or equal to 0.
        self.max_output_tokens = max_output_tokens
        # The maximum total number of context tokens supported by the model. The value must be greater than or equal to 0.
        self.max_tokens = max_tokens
        # The list of input modalities supported by the model. The list contains up to 16 items, and each item must not be empty.
        self.supported_input_modalities = supported_input_modalities
        # The list of output modalities supported by the model. The list contains up to 16 items, and each item must not be empty.
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

class UpdateAiModelCardRequestCredit(DaraModel):
    def __init__(
        self,
        cache_cost: float = None,
        input_cost: float = None,
        output_cost: float = None,
        type: str = None,
    ):
        # The cache hit token cost in Credits per million tokens. The value must be greater than or equal to 0. Default value: 0.
        self.cache_cost = cache_cost
        # The input token cost in Credits per million tokens. The value must be greater than or equal to 0. Default value: 0.
        self.input_cost = input_cost
        # The output token cost in Credits per million tokens. The value must be greater than or equal to 0. Default value: 0.
        self.output_cost = output_cost
        # The billing type. Only fixed is supported. Default value: fixed.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cache_cost is not None:
            result['cacheCost'] = self.cache_cost

        if self.input_cost is not None:
            result['inputCost'] = self.input_cost

        if self.output_cost is not None:
            result['outputCost'] = self.output_cost

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cacheCost') is not None:
            self.cache_cost = m.get('cacheCost')

        if m.get('inputCost') is not None:
            self.input_cost = m.get('inputCost')

        if m.get('outputCost') is not None:
            self.output_cost = m.get('outputCost')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdateAiModelCardRequestAvailablePaths(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The model invocation path. Maximum length: 2048 characters.
        self.path = path
        # The protocol type of the path. Maximum length: 64 characters.
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

