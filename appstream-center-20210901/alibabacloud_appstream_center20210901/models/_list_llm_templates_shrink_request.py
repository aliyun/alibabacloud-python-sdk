# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLlmTemplatesShrinkRequest(DaraModel):
    def __init__(
        self,
        biz_type: int = None,
        llm_code: str = None,
        llm_template_ids_shrink: str = None,
        model_template_id: str = None,
        page_number: int = None,
        page_size: int = None,
        provider_template_id: str = None,
        smart_model: bool = None,
    ):
        # The business type. This parameter is required when SmartModel is set to true.
        self.biz_type = biz_type
        # The model code filter. Fuzzy match is supported.
        self.llm_code = llm_code
        # The model template IDs used for filtering.
        self.llm_template_ids_shrink = llm_template_ids_shrink
        # The ID of the associated model group.
        self.model_template_id = model_template_id
        # The page number, starting from 1. Values 0 and 1 return the same result.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the model provider template.
        self.provider_template_id = provider_template_id
        # Specifies whether to query smart models. If set to true, only LLMs under system preset smart models are returned, and BizType is required. Default value: false.
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

        if self.llm_code is not None:
            result['LlmCode'] = self.llm_code

        if self.llm_template_ids_shrink is not None:
            result['LlmTemplateIds'] = self.llm_template_ids_shrink

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

        if m.get('LlmCode') is not None:
            self.llm_code = m.get('LlmCode')

        if m.get('LlmTemplateIds') is not None:
            self.llm_template_ids_shrink = m.get('LlmTemplateIds')

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

