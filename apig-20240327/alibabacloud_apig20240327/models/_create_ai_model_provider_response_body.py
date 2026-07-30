# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class CreateAiModelProviderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateAiModelProviderResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response struct.
        self.data = data
        # The response message.
        self.message = message
        # Id of the request
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
            temp_model = main_models.CreateAiModelProviderResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreateAiModelProviderResponseBodyData(DaraModel):
    def __init__(
        self,
        bound_services: List[main_models.ServiceInfo] = None,
        display_name: str = None,
        gateway_id: str = None,
        model_cards: List[main_models.CreateAiModelProviderResponseBodyDataModelCards] = None,
        model_count: int = None,
        model_provider_id: str = None,
        provider: str = None,
        source: str = None,
        update_time: str = None,
    ):
        # The list of services bound to the provider.
        self.bound_services = bound_services
        # The display name of the model provider.
        self.display_name = display_name
        # The gateway instance ID.
        self.gateway_id = gateway_id
        # The list of model cards under the provider.
        self.model_cards = model_cards
        # The number of models under the provider.
        self.model_count = model_count
        # The model provider ID.
        self.model_provider_id = model_provider_id
        # The model provider identifier.
        self.provider = provider
        # The provider source type.
        self.source = source
        # The last update time in the yyyy-MM-ddTHH:mm:ssZ format.
        self.update_time = update_time

    def validate(self):
        if self.bound_services:
            for v1 in self.bound_services:
                 if v1:
                    v1.validate()
        if self.model_cards:
            for v1 in self.model_cards:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['boundServices'] = []
        if self.bound_services is not None:
            for k1 in self.bound_services:
                result['boundServices'].append(k1.to_map() if k1 else None)

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        result['modelCards'] = []
        if self.model_cards is not None:
            for k1 in self.model_cards:
                result['modelCards'].append(k1.to_map() if k1 else None)

        if self.model_count is not None:
            result['modelCount'] = self.model_count

        if self.model_provider_id is not None:
            result['modelProviderId'] = self.model_provider_id

        if self.provider is not None:
            result['provider'] = self.provider

        if self.source is not None:
            result['source'] = self.source

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bound_services = []
        if m.get('boundServices') is not None:
            for k1 in m.get('boundServices'):
                temp_model = main_models.ServiceInfo()
                self.bound_services.append(temp_model.from_map(k1))

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        self.model_cards = []
        if m.get('modelCards') is not None:
            for k1 in m.get('modelCards'):
                temp_model = main_models.CreateAiModelProviderResponseBodyDataModelCards()
                self.model_cards.append(temp_model.from_map(k1))

        if m.get('modelCount') is not None:
            self.model_count = m.get('modelCount')

        if m.get('modelProviderId') is not None:
            self.model_provider_id = m.get('modelProviderId')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class CreateAiModelProviderResponseBodyDataModelCards(DaraModel):
    def __init__(
        self,
        available_paths: List[main_models.CreateAiModelProviderResponseBodyDataModelCardsAvailablePaths] = None,
        credit: main_models.CreateAiModelProviderResponseBodyDataModelCardsCredit = None,
        features: Dict[str, Any] = None,
        gateway_id: str = None,
        meta: main_models.CreateAiModelProviderResponseBodyDataModelCardsMeta = None,
        model_card_id: str = None,
        model_name: str = None,
        model_provider: str = None,
        source: str = None,
        source_url: str = None,
        update_time: str = None,
    ):
        # The list of available paths for the model.
        self.available_paths = available_paths
        # The model credits consumption configuration.
        self.credit = credit
        # The model capability features.
        self.features = features
        # The gateway instance ID to which the model card belongs.
        self.gateway_id = gateway_id
        # The model metadata.
        self.meta = meta
        # The model card ID.
        self.model_card_id = model_card_id
        # The model name.
        self.model_name = model_name
        # The model provider identifier to which the model card belongs.
        self.model_provider = model_provider
        # The model source.
        self.source = source
        # The URL of the model metadata.
        self.source_url = source_url
        # The last update time in the yyyy-MM-ddTHH:mm:ssZ format.
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

        if self.source is not None:
            result['source'] = self.source

        if self.source_url is not None:
            result['sourceURL'] = self.source_url

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_paths = []
        if m.get('availablePaths') is not None:
            for k1 in m.get('availablePaths'):
                temp_model = main_models.CreateAiModelProviderResponseBodyDataModelCardsAvailablePaths()
                self.available_paths.append(temp_model.from_map(k1))

        if m.get('credit') is not None:
            temp_model = main_models.CreateAiModelProviderResponseBodyDataModelCardsCredit()
            self.credit = temp_model.from_map(m.get('credit'))

        if m.get('features') is not None:
            self.features = m.get('features')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('meta') is not None:
            temp_model = main_models.CreateAiModelProviderResponseBodyDataModelCardsMeta()
            self.meta = temp_model.from_map(m.get('meta'))

        if m.get('modelCardId') is not None:
            self.model_card_id = m.get('modelCardId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('modelProvider') is not None:
            self.model_provider = m.get('modelProvider')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourceURL') is not None:
            self.source_url = m.get('sourceURL')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class CreateAiModelProviderResponseBodyDataModelCardsMeta(DaraModel):
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
        # The supported input modalities.
        self.supported_input_modalities = supported_input_modalities
        # The supported output modalities.
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

class CreateAiModelProviderResponseBodyDataModelCardsCredit(DaraModel):
    def __init__(
        self,
        cache_cost: float = None,
        input_cost: float = None,
        output_cost: float = None,
        type: str = None,
    ):
        # The credits consumption coefficient for cached tokens.
        self.cache_cost = cache_cost
        # The credits consumption coefficient for input tokens.
        self.input_cost = input_cost
        # The credits consumption coefficient for output tokens.
        self.output_cost = output_cost
        # The credits billing type.
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

class CreateAiModelProviderResponseBodyDataModelCardsAvailablePaths(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The API path.
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

