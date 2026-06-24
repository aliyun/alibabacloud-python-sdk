# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListLlmTemplatesRequest(DaraModel):
    def __init__(
        self,
        llm_code: str = None,
        llm_template_ids: List[str] = None,
        model_template_id: str = None,
        page_number: int = None,
        page_size: int = None,
        provider_template_id: str = None,
    ):
        # The model code used for filtering. Fuzzy match is supported.
        self.llm_code = llm_code
        # The model template IDs used for filtering.
        self.llm_template_ids = llm_template_ids
        # The ID of the associated model group.
        self.model_template_id = model_template_id
        # The page number. Pages start from page 1. Values 0 and 1 return the same result.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the model provider template.
        self.provider_template_id = provider_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        return self

