# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

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
        # The page number of the current page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
        description: str = None,
        is_default_model: bool = None,
        llm_code: str = None,
        llm_template_id: str = None,
        name: str = None,
        provider_template_id: str = None,
    ):
        # The model configuration JSON object.
        self.config = config
        # The template description.
        self.description = description
        # Indicates whether this is the default model in the associated model group.
        self.is_default_model = is_default_model
        # The model code.
        self.llm_code = llm_code
        # The model template ID.
        self.llm_template_id = llm_template_id
        # The template name.
        self.name = name
        # The ID of the model provider template.
        self.provider_template_id = provider_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.description is not None:
            result['Description'] = self.description

        if self.is_default_model is not None:
            result['IsDefaultModel'] = self.is_default_model

        if self.llm_code is not None:
            result['LlmCode'] = self.llm_code

        if self.llm_template_id is not None:
            result['LlmTemplateId'] = self.llm_template_id

        if self.name is not None:
            result['Name'] = self.name

        if self.provider_template_id is not None:
            result['ProviderTemplateId'] = self.provider_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsDefaultModel') is not None:
            self.is_default_model = m.get('IsDefaultModel')

        if m.get('LlmCode') is not None:
            self.llm_code = m.get('LlmCode')

        if m.get('LlmTemplateId') is not None:
            self.llm_template_id = m.get('LlmTemplateId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProviderTemplateId') is not None:
            self.provider_template_id = m.get('ProviderTemplateId')

        return self

