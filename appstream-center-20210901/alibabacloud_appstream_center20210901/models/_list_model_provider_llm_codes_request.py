# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListModelProviderLlmCodesRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        llm_code: str = None,
        model_brands: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        provider_name: str = None,
        provider_template_id: str = None,
        recommended: bool = None,
        recommended_levels: List[str] = None,
    ):
        # The display language for models. Valid values: zh-CN (Simplified Chinese), en-US (English), ja-JP (Japanese), and zh-TW (Traditional Chinese). Default value: zh-CN. Currently, zh-TW returns Simplified Chinese, and ja-JP returns English. If the text is not included in Model Studio or the English text is missing, the original source text is retained without automatic translation.
        self.language = language
        # The LLM code used for fuzzy match filtering.
        self.llm_code = llm_code
        # The list of model brands as a JSON array string. Supports multi-select filtering and returns results that match any of the specified brands.
        self.model_brands = model_brands
        # The page number, starting from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 1000. Maximum value: 1000.
        self.page_size = page_size
        # The name of the model provider.
        # 
        # This parameter is required.
        self.provider_name = provider_name
        # The ID of the provider template.
        # 
        # This parameter is required.
        self.provider_template_id = provider_template_id
        # Specifies whether to filter by recommended models. If this parameter is not specified, no filtering is applied.
        self.recommended = recommended
        # The list of recommended levels. This parameter takes effect only for wuying-plan. Results must match any of the selected levels and intersect with other filtering conditions such as region and brand. If this parameter is not specified or an empty array is passed, filtering by level is not applied.
        self.recommended_levels = recommended_levels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.llm_code is not None:
            result['LlmCode'] = self.llm_code

        if self.model_brands is not None:
            result['ModelBrands'] = self.model_brands

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        if self.provider_template_id is not None:
            result['ProviderTemplateId'] = self.provider_template_id

        if self.recommended is not None:
            result['Recommended'] = self.recommended

        if self.recommended_levels is not None:
            result['RecommendedLevels'] = self.recommended_levels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LlmCode') is not None:
            self.llm_code = m.get('LlmCode')

        if m.get('ModelBrands') is not None:
            self.model_brands = m.get('ModelBrands')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        if m.get('ProviderTemplateId') is not None:
            self.provider_template_id = m.get('ProviderTemplateId')

        if m.get('Recommended') is not None:
            self.recommended = m.get('Recommended')

        if m.get('RecommendedLevels') is not None:
            self.recommended_levels = m.get('RecommendedLevels')

        return self

