# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class ListModelsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        max_results: int = None,
        models: List[main_models.ListModelsResponseBodyModels] = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.error_message = error_message
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.models = models
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.models:
            for v1 in self.models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        result['models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['models'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        self.models = []
        if m.get('models') is not None:
            for k1 in m.get('models'):
                temp_model = main_models.ListModelsResponseBodyModels()
                self.models.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListModelsResponseBodyModels(DaraModel):
    def __init__(
        self,
        capabilities: List[str] = None,
        description: str = None,
        features: List[str] = None,
        inference_metadata: main_models.ListModelsResponseBodyModelsInferenceMetadata = None,
        model: str = None,
        model_info: main_models.ListModelsResponseBodyModelsModelInfo = None,
        name: str = None,
        prices: List[main_models.ListModelsResponseBodyModelsPrices] = None,
        provider: str = None,
        published_time: int = None,
    ):
        self.capabilities = capabilities
        self.description = description
        self.features = features
        self.inference_metadata = inference_metadata
        self.model = model
        self.model_info = model_info
        self.name = name
        self.prices = prices
        self.provider = provider
        self.published_time = published_time

    def validate(self):
        if self.inference_metadata:
            self.inference_metadata.validate()
        if self.model_info:
            self.model_info.validate()
        if self.prices:
            for v1 in self.prices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capabilities is not None:
            result['capabilities'] = self.capabilities

        if self.description is not None:
            result['description'] = self.description

        if self.features is not None:
            result['features'] = self.features

        if self.inference_metadata is not None:
            result['inferenceMetadata'] = self.inference_metadata.to_map()

        if self.model is not None:
            result['model'] = self.model

        if self.model_info is not None:
            result['modelInfo'] = self.model_info.to_map()

        if self.name is not None:
            result['name'] = self.name

        result['prices'] = []
        if self.prices is not None:
            for k1 in self.prices:
                result['prices'].append(k1.to_map() if k1 else None)

        if self.provider is not None:
            result['provider'] = self.provider

        if self.published_time is not None:
            result['publishedTime'] = self.published_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capabilities') is not None:
            self.capabilities = m.get('capabilities')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('features') is not None:
            self.features = m.get('features')

        if m.get('inferenceMetadata') is not None:
            temp_model = main_models.ListModelsResponseBodyModelsInferenceMetadata()
            self.inference_metadata = temp_model.from_map(m.get('inferenceMetadata'))

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('modelInfo') is not None:
            temp_model = main_models.ListModelsResponseBodyModelsModelInfo()
            self.model_info = temp_model.from_map(m.get('modelInfo'))

        if m.get('name') is not None:
            self.name = m.get('name')

        self.prices = []
        if m.get('prices') is not None:
            for k1 in m.get('prices'):
                temp_model = main_models.ListModelsResponseBodyModelsPrices()
                self.prices.append(temp_model.from_map(k1))

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('publishedTime') is not None:
            self.published_time = m.get('publishedTime')

        return self

class ListModelsResponseBodyModelsPrices(DaraModel):
    def __init__(
        self,
        prices: List[main_models.ListModelsResponseBodyModelsPricesPrices] = None,
        range_name: str = None,
    ):
        self.prices = prices
        self.range_name = range_name

    def validate(self):
        if self.prices:
            for v1 in self.prices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['prices'] = []
        if self.prices is not None:
            for k1 in self.prices:
                result['prices'].append(k1.to_map() if k1 else None)

        if self.range_name is not None:
            result['rangeName'] = self.range_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prices = []
        if m.get('prices') is not None:
            for k1 in m.get('prices'):
                temp_model = main_models.ListModelsResponseBodyModelsPricesPrices()
                self.prices.append(temp_model.from_map(k1))

        if m.get('rangeName') is not None:
            self.range_name = m.get('rangeName')

        return self

class ListModelsResponseBodyModelsPricesPrices(DaraModel):
    def __init__(
        self,
        price: str = None,
        price_name: str = None,
        price_unit: str = None,
    ):
        self.price = price
        self.price_name = price_name
        self.price_unit = price_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price is not None:
            result['price'] = self.price

        if self.price_name is not None:
            result['priceName'] = self.price_name

        if self.price_unit is not None:
            result['priceUnit'] = self.price_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('priceName') is not None:
            self.price_name = m.get('priceName')

        if m.get('priceUnit') is not None:
            self.price_unit = m.get('priceUnit')

        return self

class ListModelsResponseBodyModelsModelInfo(DaraModel):
    def __init__(
        self,
        context_window: int = None,
        max_input_tokens: int = None,
        max_output_tokens: int = None,
        max_reasoning_tokens: int = None,
        reasoning_max_input_tokens: int = None,
        reasoning_max_output_tokens: int = None,
    ):
        self.context_window = context_window
        self.max_input_tokens = max_input_tokens
        self.max_output_tokens = max_output_tokens
        self.max_reasoning_tokens = max_reasoning_tokens
        self.reasoning_max_input_tokens = reasoning_max_input_tokens
        self.reasoning_max_output_tokens = reasoning_max_output_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_window is not None:
            result['contextWindow'] = self.context_window

        if self.max_input_tokens is not None:
            result['maxInputTokens'] = self.max_input_tokens

        if self.max_output_tokens is not None:
            result['maxOutputTokens'] = self.max_output_tokens

        if self.max_reasoning_tokens is not None:
            result['maxReasoningTokens'] = self.max_reasoning_tokens

        if self.reasoning_max_input_tokens is not None:
            result['reasoningMaxInputTokens'] = self.reasoning_max_input_tokens

        if self.reasoning_max_output_tokens is not None:
            result['reasoningMaxOutputTokens'] = self.reasoning_max_output_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contextWindow') is not None:
            self.context_window = m.get('contextWindow')

        if m.get('maxInputTokens') is not None:
            self.max_input_tokens = m.get('maxInputTokens')

        if m.get('maxOutputTokens') is not None:
            self.max_output_tokens = m.get('maxOutputTokens')

        if m.get('maxReasoningTokens') is not None:
            self.max_reasoning_tokens = m.get('maxReasoningTokens')

        if m.get('reasoningMaxInputTokens') is not None:
            self.reasoning_max_input_tokens = m.get('reasoningMaxInputTokens')

        if m.get('reasoningMaxOutputTokens') is not None:
            self.reasoning_max_output_tokens = m.get('reasoningMaxOutputTokens')

        return self

class ListModelsResponseBodyModelsInferenceMetadata(DaraModel):
    def __init__(
        self,
        request_modality: List[str] = None,
        response_modality: List[str] = None,
    ):
        self.request_modality = request_modality
        self.response_modality = response_modality

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_modality is not None:
            result['requestModality'] = self.request_modality

        if self.response_modality is not None:
            result['responseModality'] = self.response_modality

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestModality') is not None:
            self.request_modality = m.get('requestModality')

        if m.get('responseModality') is not None:
            self.response_modality = m.get('responseModality')

        return self

