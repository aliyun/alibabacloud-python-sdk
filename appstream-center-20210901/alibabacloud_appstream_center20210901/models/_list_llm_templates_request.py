# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListLlmTemplatesRequest(DaraModel):
    def __init__(
        self,
        biz_type: int = None,
        language: str = None,
        llm_code: str = None,
        llm_template_ids: List[str] = None,
        model_template_id: str = None,
        page_number: int = None,
        page_size: int = None,
        provider_template_id: str = None,
        smart_model: bool = None,
    ):
        # The business type. This parameter is required when SmartModel is set to true.
        self.biz_type = biz_type
        # The display language of the model. Valid values:
        # - zh-CN: Simplified Chinese.
        # - en-US: English.
        # - ja-JP: Japanese.
        # - zh-TW: Traditional Chinese.
        # Default value: zh-CN. Currently, zh-TW returns Simplified Chinese, and ja-JP returns English. If the model is not included in Alibaba Cloud Model Studio or the English text is missing, the original source text is retained without automatic translation.
        self.language = language
        # The model code for filtering. Fuzzy match is supported.
        self.llm_code = llm_code
        # The model template IDs for filtering.
        self.llm_template_ids = llm_template_ids
        # The associated model group ID.
        self.model_template_id = model_template_id
        # The page number. Pages start from 1. A value of 0 returns the same result as 1.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The model provider template ID.
        self.provider_template_id = provider_template_id
        # Specifies whether to query smart models. Valid values:
        # - true: Only LLMs under system-preset smart models are returned. In this case, BizType is required.
        # - false: Smart models are not specifically filtered.
        # Default value: false.
        self.smart_model = smart_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.language is not None:
            result['Language'] = self.language

        if self.llm_code is not None:
            result['LlmCode'] = self.llm_code

        if self.llm_template_ids is not None:
            result['LlmTemplateIds'] = self.llm_template_ids

        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.provider_template_id is not None:
            result['ProviderTemplateId'] = self.provider_template_id

        if self.smart_model is not None:
            result['SmartModel'] = self.smart_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LlmCode') is not None:
            self.llm_code = m.get('LlmCode')

        if m.get('LlmTemplateIds') is not None:
            self.llm_template_ids = m.get('LlmTemplateIds')

        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProviderTemplateId') is not None:
            self.provider_template_id = m.get('ProviderTemplateId')

        if m.get('SmartModel') is not None:
            self.smart_model = m.get('SmartModel')

        return self

