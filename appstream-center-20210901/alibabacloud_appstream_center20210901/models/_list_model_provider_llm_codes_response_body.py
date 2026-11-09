# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListModelProviderLlmCodesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListModelProviderLlmCodesResponseBodyData = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The paginated data object that contains a list of LLM information.
        self.data = data
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The unique ID of the request.
        self.request_id = request_id
        # The total number of records after filtering.
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

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
        if m.get('Data') is not None:
            temp_model = main_models.ListModelProviderLlmCodesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListModelProviderLlmCodesResponseBodyData(DaraModel):
    def __init__(
        self,
        llm_info_list: List[main_models.ListModelProviderLlmCodesResponseBodyDataLlmInfoList] = None,
    ):
        # The LLM information list.
        self.llm_info_list = llm_info_list

    def validate(self):
        if self.llm_info_list:
            for v1 in self.llm_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LlmInfoList'] = []
        if self.llm_info_list is not None:
            for k1 in self.llm_info_list:
                result['LlmInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.llm_info_list = []
        if m.get('LlmInfoList') is not None:
            for k1 in m.get('LlmInfoList'):
                temp_model = main_models.ListModelProviderLlmCodesResponseBodyDataLlmInfoList()
                self.llm_info_list.append(temp_model.from_map(k1))

        return self

class ListModelProviderLlmCodesResponseBodyDataLlmInfoList(DaraModel):
    def __init__(
        self,
        credit_multiplier: main_models.ListModelProviderLlmCodesResponseBodyDataLlmInfoListCreditMultiplier = None,
        description: str = None,
        features: List[str] = None,
        inference_metadata: main_models.ListModelProviderLlmCodesResponseBodyDataLlmInfoListInferenceMetadata = None,
        llm_code: str = None,
        model_brand: str = None,
        model_info: Dict[str, Any] = None,
        model_series: str = None,
        name: str = None,
        prices: List[main_models.ListModelProviderLlmCodesResponseBodyDataLlmInfoListPrices] = None,
        published_time: str = None,
        recommended: bool = None,
        risk_type: str = None,
    ):
        # The credit consumption multiplier. An empty value indicates that the model does not participate in credit billing.
        self.credit_multiplier = credit_multiplier
        # The model description.
        self.description = description
        # The list of model features, such as function-calling, web-search, and structured-outputs.
        self.features = features
        # The inference metadata, including request and response modalities.
        self.inference_metadata = inference_metadata
        # The LLM code, such as qwen-image-2.0.
        self.llm_code = llm_code
        # The model brand, such as Qwen, Wanx, or DeepSeek. This parameter is returned only for models annotated in the platform-side model pool.
        self.model_brand = model_brand
        # The model information, such as context window size and maximum input/output tokens.
        self.model_info = model_info
        # The model series, such as Qwen-Max or DeepSeek. This parameter is returned only for the wuying-credit provider.
        self.model_series = model_series
        # The model name, such as Qwen-Image-2.0.
        self.name = name
        # The list of price information.
        self.prices = prices
        # The time when the model was published, in ISO 8601 format, such as 2026-03-04T06:25:17.000+00:00.
        self.published_time = published_time
        # Indicates whether the model is recommended. This is a tri-state value: true indicates that the model is recommended for display, false indicates that the model is explicitly not recommended, and null indicates that the status is not applicable, such as for non-Bailian models or unannotated models.
        self.recommended = recommended
        # The model risk type. This parameter is returned only when includeRiskInfo is set to true.
        self.risk_type = risk_type

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
        if self.credit_multiplier is not None:
            result['CreditMultiplier'] = self.credit_multiplier.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.features is not None:
            result['Features'] = self.features

        if self.inference_metadata is not None:
            result['InferenceMetadata'] = self.inference_metadata.to_map()

        if self.llm_code is not None:
            result['LlmCode'] = self.llm_code

        if self.model_brand is not None:
            result['ModelBrand'] = self.model_brand

        if self.model_info is not None:
            result['ModelInfo'] = self.model_info

        if self.model_series is not None:
            result['ModelSeries'] = self.model_series

        if self.name is not None:
            result['Name'] = self.name

        result['Prices'] = []
        if self.prices is not None:
            for k1 in self.prices:
                result['Prices'].append(k1.to_map() if k1 else None)

        if self.published_time is not None:
            result['PublishedTime'] = self.published_time

        if self.recommended is not None:
            result['Recommended'] = self.recommended

        if self.risk_type is not None:
            result['RiskType'] = self.risk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditMultiplier') is not None:
            temp_model = main_models.ListModelProviderLlmCodesResponseBodyDataLlmInfoListCreditMultiplier()
            self.credit_multiplier = temp_model.from_map(m.get('CreditMultiplier'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('InferenceMetadata') is not None:
            temp_model = main_models.ListModelProviderLlmCodesResponseBodyDataLlmInfoListInferenceMetadata()
            self.inference_metadata = temp_model.from_map(m.get('InferenceMetadata'))

        if m.get('LlmCode') is not None:
            self.llm_code = m.get('LlmCode')

        if m.get('ModelBrand') is not None:
            self.model_brand = m.get('ModelBrand')

        if m.get('ModelInfo') is not None:
            self.model_info = m.get('ModelInfo')

        if m.get('ModelSeries') is not None:
            self.model_series = m.get('ModelSeries')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.prices = []
        if m.get('Prices') is not None:
            for k1 in m.get('Prices'):
                temp_model = main_models.ListModelProviderLlmCodesResponseBodyDataLlmInfoListPrices()
                self.prices.append(temp_model.from_map(k1))

        if m.get('PublishedTime') is not None:
            self.published_time = m.get('PublishedTime')

        if m.get('Recommended') is not None:
            self.recommended = m.get('Recommended')

        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')

        return self

class ListModelProviderLlmCodesResponseBodyDataLlmInfoListPrices(DaraModel):
    def __init__(
        self,
        prices: List[main_models.ListModelProviderLlmCodesResponseBodyDataLlmInfoListPricesPrices] = None,
        range_name: str = None,
    ):
        # The list of prices within the range.
        self.prices = prices
        # The name of the range, such as Default or 0-1M tokens.
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
                temp_model = main_models.ListModelProviderLlmCodesResponseBodyDataLlmInfoListPricesPrices()
                self.prices.append(temp_model.from_map(k1))

        if m.get('RangeName') is not None:
            self.range_name = m.get('RangeName')

        return self

class ListModelProviderLlmCodesResponseBodyDataLlmInfoListPricesPrices(DaraModel):
    def __init__(
        self,
        price: str = None,
        price_name: str = None,
        price_unit: str = None,
    ):
        # The price in string format, such as 0.2.
        self.price = price
        # The name of the price item, such as input, output, or image generation.
        self.price_name = price_name
        # The price unit, such as per image or per 1,000 tokens.
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

class ListModelProviderLlmCodesResponseBodyDataLlmInfoListInferenceMetadata(DaraModel):
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

class ListModelProviderLlmCodesResponseBodyDataLlmInfoListCreditMultiplier(DaraModel):
    def __init__(
        self,
        max: float = None,
        min: float = None,
    ):
        # The upper limit of the multiplier. An empty value indicates no upper limit. For example, if the minimum value is 1 and the maximum value is empty, it is displayed as starting from 1x.
        self.max = max
        # The lower limit of the multiplier. If this value is equal to the maximum value, the multiplier is fixed. For example, if both the minimum and maximum values are 2, it is displayed as 2x.
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

