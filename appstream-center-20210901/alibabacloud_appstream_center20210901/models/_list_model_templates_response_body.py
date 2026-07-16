# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListModelTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListModelTemplatesResponseBodyData] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of returned data objects.
        self.data = data
        # The page number of the current query result.
        self.page_number = page_number
        # The number of entries per page in the query result.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries in the query result.
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
                temp_model = main_models.ListModelTemplatesResponseBodyData()
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

class ListModelTemplatesResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_provider: str = None,
        config: str = None,
        description: str = None,
        has_model: bool = None,
        model_template_id: str = None,
        name: str = None,
    ):
        # The name of the Agent provider.
        self.agent_provider = agent_provider
        # The model group configuration JSON object.
        self.config = config
        # The template group description.
        self.description = description
        # Specifies whether models have been configured in the group.
        self.has_model = has_model
        # The model group ID.
        self.model_template_id = model_template_id
        # The template group name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_provider is not None:
            result['AgentProvider'] = self.agent_provider

        if self.config is not None:
            result['Config'] = self.config

        if self.description is not None:
            result['Description'] = self.description

        if self.has_model is not None:
            result['HasModel'] = self.has_model

        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentProvider') is not None:
            self.agent_provider = m.get('AgentProvider')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HasModel') is not None:
            self.has_model = m.get('HasModel')

        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

