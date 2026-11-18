# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetDirectSupplyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDirectSupplyResponseBodyData = None,
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
            temp_model = main_models.GetDirectSupplyResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetDirectSupplyResponseBodyData(DaraModel):
    def __init__(
        self,
        candidate_models: List[main_models.GetDirectSupplyResponseBodyDataCandidateModels] = None,
        catalog_error: main_models.GetDirectSupplyResponseBodyDataCatalogError = None,
        enabled: bool = None,
        gateway_id: str = None,
        models: List[main_models.GetDirectSupplyResponseBodyDataModels] = None,
    ):
        # The list of candidate models that can be added to direct supply.
        self.candidate_models = candidate_models
        # The error message returned when the model catalog query fails. This parameter is not returned when the query succeeds.
        self.catalog_error = catalog_error
        # Indicates whether direct supply is enabled.
        self.enabled = enabled
        # The ID of the gateway instance.
        self.gateway_id = gateway_id
        # The list of models for which direct supply is enabled.
        self.models = models

    def validate(self):
        if self.candidate_models:
            for v1 in self.candidate_models:
                 if v1:
                    v1.validate()
        if self.catalog_error:
            self.catalog_error.validate()
        if self.models:
            for v1 in self.models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['candidateModels'] = []
        if self.candidate_models is not None:
            for k1 in self.candidate_models:
                result['candidateModels'].append(k1.to_map() if k1 else None)

        if self.catalog_error is not None:
            result['catalogError'] = self.catalog_error.to_map()

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        result['models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['models'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.candidate_models = []
        if m.get('candidateModels') is not None:
            for k1 in m.get('candidateModels'):
                temp_model = main_models.GetDirectSupplyResponseBodyDataCandidateModels()
                self.candidate_models.append(temp_model.from_map(k1))

        if m.get('catalogError') is not None:
            temp_model = main_models.GetDirectSupplyResponseBodyDataCatalogError()
            self.catalog_error = temp_model.from_map(m.get('catalogError'))

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        self.models = []
        if m.get('models') is not None:
            for k1 in m.get('models'):
                temp_model = main_models.GetDirectSupplyResponseBodyDataModels()
                self.models.append(temp_model.from_map(k1))

        return self

class GetDirectSupplyResponseBodyDataModels(DaraModel):
    def __init__(
        self,
        available_paths: List[main_models.GetDirectSupplyResponseBodyDataModelsAvailablePaths] = None,
        credit: main_models.GetDirectSupplyResponseBodyDataModelsCredit = None,
        features: Dict[str, Any] = None,
        gateway_id: str = None,
        meta: main_models.GetDirectSupplyResponseBodyDataModelsMeta = None,
        model_card_id: str = None,
        model_name: str = None,
        model_provider: str = None,
        model_source_id: str = None,
        source: str = None,
        update_time: str = None,
    ):
        # The list of available invocation paths.
        self.available_paths = available_paths
        # The billing information of the model.
        self.credit = credit
        # The capabilities and features supported by the model.
        self.features = features
        # The ID of the gateway instance.
        self.gateway_id = gateway_id
        # The capability information of the model.
        self.meta = meta
        # The ID of the model card, which starts with msc-.
        self.model_card_id = model_card_id
        # The name of the model.
        self.model_name = model_name
        # The model provider.
        self.model_provider = model_provider
        # The ID of the model source.
        self.model_source_id = model_source_id
        # The source of the model.
        self.source = source
        # The last update time in ISO 8601 (RFC 3339) format in the UTC time zone, such as 2026-05-15T10:00:00Z.
        self.update_time = update_time

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

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.meta is not None:
            result['meta'] = self.meta.to_map()

        if self.model_card_id is not None:
            result['modelCardId'] = self.model_card_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_provider is not None:
            result['modelProvider'] = self.model_provider

        if self.model_source_id is not None:
            result['modelSourceId'] = self.model_source_id

        if self.source is not None:
            result['source'] = self.source

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_paths = []
        if m.get('availablePaths') is not None:
            for k1 in m.get('availablePaths'):
                temp_model = main_models.GetDirectSupplyResponseBodyDataModelsAvailablePaths()
                self.available_paths.append(temp_model.from_map(k1))

        if m.get('credit') is not None:
            temp_model = main_models.GetDirectSupplyResponseBodyDataModelsCredit()
            self.credit = temp_model.from_map(m.get('credit'))

        if m.get('features') is not None:
            self.features = m.get('features')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('meta') is not None:
            temp_model = main_models.GetDirectSupplyResponseBodyDataModelsMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        if m.get('modelCardId') is not None:
            self.model_card_id = m.get('modelCardId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelProvider') is not None:
            self.model_provider = m.get('modelProvider')

        if m.get('modelSourceId') is not None:
            self.model_source_id = m.get('modelSourceId')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class GetDirectSupplyResponseBodyDataModelsMeta(DaraModel):
    def __init__(
        self,
        max_input_tokens: int = None,
        max_output_tokens: int = None,
        max_tokens: int = None,
        supported_input_modalities: List[str] = None,
        supported_output_modalities: List[str] = None,
    ):
        # The maximum number of input tokens.
        self.max_input_tokens = max_input_tokens
        # The maximum number of output tokens.
        self.max_output_tokens = max_output_tokens
        # The maximum total number of tokens.
        self.max_tokens = max_tokens
        # The list of supported input modalities.
        self.supported_input_modalities = supported_input_modalities
        # The list of supported output modalities.
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

class GetDirectSupplyResponseBodyDataModelsCredit(DaraModel):
    def __init__(
        self,
        cache_cost: float = None,
        input_cost: float = None,
        output_cost: float = None,
        type: str = None,
    ):
        # The unit price of cache-hit tokens.
        self.cache_cost = cache_cost
        # The unit price of input tokens.
        self.input_cost = input_cost
        # The unit price of output tokens.
        self.output_cost = output_cost
        # The billing type.
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

class GetDirectSupplyResponseBodyDataModelsAvailablePaths(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The invocation path.
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

class GetDirectSupplyResponseBodyDataCatalogError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetDirectSupplyResponseBodyDataCandidateModels(DaraModel):
    def __init__(
        self,
        available_paths: List[main_models.GetDirectSupplyResponseBodyDataCandidateModelsAvailablePaths] = None,
        credit: main_models.GetDirectSupplyResponseBodyDataCandidateModelsCredit = None,
        features: Dict[str, Any] = None,
        gateway_id: str = None,
        meta: main_models.GetDirectSupplyResponseBodyDataCandidateModelsMeta = None,
        model_card_id: str = None,
        model_name: str = None,
        model_provider: str = None,
        model_source_id: str = None,
        source: str = None,
        update_time: str = None,
    ):
        # The list of available invocation paths.
        self.available_paths = available_paths
        # The billing information of the model.
        self.credit = credit
        # The capabilities and features supported by the model.
        self.features = features
        # The ID of the gateway instance.
        self.gateway_id = gateway_id
        # The capability information of the model.
        self.meta = meta
        # The ID of the model card, which starts with msc-.
        self.model_card_id = model_card_id
        # The name of the model.
        self.model_name = model_name
        # The model provider.
        self.model_provider = model_provider
        # The ID of the model source.
        self.model_source_id = model_source_id
        # The source of the model.
        self.source = source
        # The last update time in ISO 8601 (RFC 3339) format in the UTC time zone, such as 2026-05-15T10:00:00Z.
        self.update_time = update_time

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

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.meta is not None:
            result['meta'] = self.meta.to_map()

        if self.model_card_id is not None:
            result['modelCardId'] = self.model_card_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.model_provider is not None:
            result['modelProvider'] = self.model_provider

        if self.model_source_id is not None:
            result['modelSourceId'] = self.model_source_id

        if self.source is not None:
            result['source'] = self.source

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_paths = []
        if m.get('availablePaths') is not None:
            for k1 in m.get('availablePaths'):
                temp_model = main_models.GetDirectSupplyResponseBodyDataCandidateModelsAvailablePaths()
                self.available_paths.append(temp_model.from_map(k1))

        if m.get('credit') is not None:
            temp_model = main_models.GetDirectSupplyResponseBodyDataCandidateModelsCredit()
            self.credit = temp_model.from_map(m.get('credit'))

        if m.get('features') is not None:
            self.features = m.get('features')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('meta') is not None:
            temp_model = main_models.GetDirectSupplyResponseBodyDataCandidateModelsMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        if m.get('modelCardId') is not None:
            self.model_card_id = m.get('modelCardId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelProvider') is not None:
            self.model_provider = m.get('modelProvider')

        if m.get('modelSourceId') is not None:
            self.model_source_id = m.get('modelSourceId')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class GetDirectSupplyResponseBodyDataCandidateModelsMeta(DaraModel):
    def __init__(
        self,
        max_input_tokens: int = None,
        max_output_tokens: int = None,
        max_tokens: int = None,
        supported_input_modalities: List[str] = None,
        supported_output_modalities: List[str] = None,
    ):
        # The maximum number of input tokens.
        self.max_input_tokens = max_input_tokens
        # The maximum number of output tokens.
        self.max_output_tokens = max_output_tokens
        # The maximum total number of tokens.
        self.max_tokens = max_tokens
        # The list of supported input modalities.
        self.supported_input_modalities = supported_input_modalities
        # The list of supported output modalities.
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

class GetDirectSupplyResponseBodyDataCandidateModelsCredit(DaraModel):
    def __init__(
        self,
        cache_cost: float = None,
        input_cost: float = None,
        output_cost: float = None,
        type: str = None,
    ):
        # The unit price of cache-hit tokens.
        self.cache_cost = cache_cost
        # The unit price of input tokens.
        self.input_cost = input_cost
        # The unit price of output tokens.
        self.output_cost = output_cost
        # The billing type.
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

class GetDirectSupplyResponseBodyDataCandidateModelsAvailablePaths(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The invocation path.
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

