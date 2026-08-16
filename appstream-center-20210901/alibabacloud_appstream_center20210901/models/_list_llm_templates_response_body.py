# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListLlmTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListLlmTemplatesResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of returned data objects.
        self.data = data
        # The current page number of the query results.
        self.page_number = page_number
        # The number of query results per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of query results.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListLlmTemplatesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLlmTemplatesResponseBodyData(DaraModel):
    def __init__(
        self,
        config: str = None,
        credit_multiplier: main_models.ListLlmTemplatesResponseBodyDataCreditMultiplier = None,
        description: str = None,
        features: List[str] = None,
        inference_metadata: main_models.ListLlmTemplatesResponseBodyDataInferenceMetadata = None,
        is_default_model: bool = None,
        llm_code: str = None,
        llm_template_id: str = None,
        model_info: Dict[str, Any] = None,
        name: str = None,
        prices: List[main_models.ListLlmTemplatesResponseBodyDataPrices] = None,
        provider_template_id: str = None,
        published_time: str = None,
        ref_scope: str = None,
        route_policy_count: int = None,
    ):
        # The model configuration JSON object.
        self.config = config
        # The credit consumption multiplier (rate). A null value indicates that the model does not participate in credit-based billing.
        self.credit_multiplier = credit_multiplier
        # The template description.
        self.description = description
        # The list of model features, such as function-calling, web-search, and structured-outputs.
        self.features = features
        # The inference metadata, including request and response modalities.
        self.inference_metadata = inference_metadata
        # Indicates whether this is the default model under the associated model group.
        self.is_default_model = is_default_model
        # The model code.
        self.llm_code = llm_code
        # The model template ID.
        self.llm_template_id = llm_template_id
        # The model information, including context window size and maximum input/output tokens.
        self.model_info = model_info
        # The template name.
        self.name = name
        # The list of price information.
        self.prices = prices
        # The ID of the model provider template.
        self.provider_template_id = provider_template_id
        # The publish time in ISO 8601 format, such as 2026-03-04T06:25:17.000+00:00.
        self.published_time = published_time
        # The authorization scope of the associated model group. Valid values: ALL_USER (all users), USER_MIXED (specified users and user groups), RESOURCE_MIXED (specified resources). Returned only when SmartModel is set to true.
        self.ref_scope = ref_scope
        # The number of route policies configured under this model tier. Returned only when SmartModel is set to true. Returns 0 for tiers without configured policies.
        self.route_policy_count = route_policy_count

    def validate(self):
        if self.credit_multiplier:
            self.credit_multiplier.validate()
        if self.inference_metadata:
            self.inference_metadata.validate()
        if self.prices:
            for v1 in self.prices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.credit_multiplier is not None:
            result['CreditMultiplier'] = self.credit_multiplier.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.features is not None:
            result['Features'] = self.features

        if self.inference_metadata is not None:
            result['InferenceMetadata'] = self.inference_metadata.to_map()

        if self.is_default_model is not None:
            result['IsDefaultModel'] = self.is_default_model

        if self.llm_code is not None:
            result['LlmCode'] = self.llm_code

        if self.llm_template_id is not None:
            result['LlmTemplateId'] = self.llm_template_id

        if self.model_info is not None:
            result['ModelInfo'] = self.model_info

        if self.name is not None:
            result['Name'] = self.name

        result['Prices'] = []
        if self.prices is not None:
            for k1 in self.prices:
                result['Prices'].append(k1.to_map() if k1 else None)

        if self.provider_template_id is not None:
            result['ProviderTemplateId'] = self.provider_template_id

        if self.published_time is not None:
            result['PublishedTime'] = self.published_time

        if self.ref_scope is not None:
            result['RefScope'] = self.ref_scope

        if self.route_policy_count is not None:
            result['RoutePolicyCount'] = self.route_policy_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('CreditMultiplier') is not None:
            temp_model = main_models.ListLlmTemplatesResponseBodyDataCreditMultiplier()
            self.credit_multiplier = temp_model.from_map(m.get('CreditMultiplier'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('InferenceMetadata') is not None:
            temp_model = main_models.ListLlmTemplatesResponseBodyDataInferenceMetadata()
            self.inference_metadata = temp_model.from_map(m.get('InferenceMetadata'))

        if m.get('IsDefaultModel') is not None:
            self.is_default_model = m.get('IsDefaultModel')

        if m.get('LlmCode') is not None:
            self.llm_code = m.get('LlmCode')

        if m.get('LlmTemplateId') is not None:
            self.llm_template_id = m.get('LlmTemplateId')

        if m.get('ModelInfo') is not None:
            self.model_info = m.get('ModelInfo')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.prices = []
        if m.get('Prices') is not None:
            for k1 in m.get('Prices'):
                temp_model = main_models.ListLlmTemplatesResponseBodyDataPrices()
                self.prices.append(temp_model.from_map(k1))

        if m.get('ProviderTemplateId') is not None:
            self.provider_template_id = m.get('ProviderTemplateId')

        if m.get('PublishedTime') is not None:
            self.published_time = m.get('PublishedTime')

        if m.get('RefScope') is not None:
            self.ref_scope = m.get('RefScope')

        if m.get('RoutePolicyCount') is not None:
            self.route_policy_count = m.get('RoutePolicyCount')

        return self

class ListLlmTemplatesResponseBodyDataPrices(DaraModel):
    def __init__(
        self,
        prices: List[main_models.ListLlmTemplatesResponseBodyDataPricesPrices] = None,
        range_name: str = None,
    ):
        # The list of prices within the range.
        self.prices = prices
        # The range name, such as Default or 0-1M tokens.
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
        result['Prices'] = []
        if self.prices is not None:
            for k1 in self.prices:
                result['Prices'].append(k1.to_map() if k1 else None)

        if self.range_name is not None:
            result['RangeName'] = self.range_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prices = []
        if m.get('Prices') is not None:
            for k1 in m.get('Prices'):
                temp_model = main_models.ListLlmTemplatesResponseBodyDataPricesPrices()
                self.prices.append(temp_model.from_map(k1))

        if m.get('RangeName') is not None:
            self.range_name = m.get('RangeName')

        return self

class ListLlmTemplatesResponseBodyDataPricesPrices(DaraModel):
    def __init__(
        self,
        price: str = None,
        price_name: str = None,
        price_unit: str = None,
    ):
        # The price in string format, such as 0.2.
        self.price = price
        # The price name, such as Input, Output, or Image Generation.
        self.price_name = price_name
        # The price unit, such as per image or per thousand tokens.
        self.price_unit = price_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price is not None:
            result['Price'] = self.price

        if self.price_name is not None:
            result['PriceName'] = self.price_name

        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('PriceName') is not None:
            self.price_name = m.get('PriceName')

        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')

        return self

class ListLlmTemplatesResponseBodyDataInferenceMetadata(DaraModel):
    def __init__(
        self,
        request_modality: List[str] = None,
        response_modality: List[str] = None,
    ):
        # The list of request modalities, such as Text, Image, and Audio.
        self.request_modality = request_modality
        # The list of response modalities, such as Text, Image, and Audio.
        self.response_modality = response_modality

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_modality is not None:
            result['RequestModality'] = self.request_modality

        if self.response_modality is not None:
            result['ResponseModality'] = self.response_modality

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestModality') is not None:
            self.request_modality = m.get('RequestModality')

        if m.get('ResponseModality') is not None:
            self.response_modality = m.get('ResponseModality')

        return self

class ListLlmTemplatesResponseBodyDataCreditMultiplier(DaraModel):
    def __init__(
        self,
        max: float = None,
        min: float = None,
    ):
        # The maximum multiplier. A null value indicates no upper limit. For example, Min=1 with Max as null is displayed as 1x and above.
        self.max = max
        # The minimum multiplier. When equal to Max, it represents a fixed multiplier. For example, Min=Max=2 is displayed as 2x.
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        return self

