# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class BatchCreateLlmTemplatesRequest(DaraModel):
    def __init__(
        self,
        llm_template_items: List[main_models.BatchCreateLlmTemplatesRequestLlmTemplateItems] = None,
        model_template_id: str = None,
        provider_template_id: str = None,
    ):
        # The list of model configurations to create.
        self.llm_template_items = llm_template_items
        # The ID of the associated model group.
        self.model_template_id = model_template_id
        # The ID of the model provider template to which the models belong.
        # 
        # This parameter is required.
        self.provider_template_id = provider_template_id

    def validate(self):
        if self.llm_template_items:
            for v1 in self.llm_template_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LlmTemplateItems'] = []
        if self.llm_template_items is not None:
            for k1 in self.llm_template_items:
                result['LlmTemplateItems'].append(k1.to_map() if k1 else None)

        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        if self.provider_template_id is not None:
            result['ProviderTemplateId'] = self.provider_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.llm_template_items = []
        if m.get('LlmTemplateItems') is not None:
            for k1 in m.get('LlmTemplateItems'):
                temp_model = main_models.BatchCreateLlmTemplatesRequestLlmTemplateItems()
                self.llm_template_items.append(temp_model.from_map(k1))

        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        if m.get('ProviderTemplateId') is not None:
            self.provider_template_id = m.get('ProviderTemplateId')

        return self

class BatchCreateLlmTemplatesRequestLlmTemplateItems(DaraModel):
    def __init__(
        self,
        config: str = None,
        description: str = None,
        is_default_model: bool = None,
        llm_code: str = None,
        name: str = None,
    ):
        # The model configuration JSON object.
        self.config = config
        # The model description.
        self.description = description
        # Specifies whether to set this model as the default model. Each model group can have at most one default model.
        self.is_default_model = is_default_model
        # The model code, which must be unique within the same provider.
        self.llm_code = llm_code
        # The model name.
        self.name = name

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

        if self.name is not None:
            result['Name'] = self.name

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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

