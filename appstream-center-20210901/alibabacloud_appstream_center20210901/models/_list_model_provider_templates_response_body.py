# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListModelProviderTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListModelProviderTemplatesResponseBodyData] = None,
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
                temp_model = main_models.ListModelProviderTemplatesResponseBodyData()
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

class ListModelProviderTemplatesResponseBodyData(DaraModel):
    def __init__(
        self,
        config: str = None,
        description: str = None,
        enable_wuying_proxy: bool = None,
        name: str = None,
        provider_name: str = None,
        provider_template_id: str = None,
        provider_type: str = None,
    ):
        # The model provider configuration as a JSON object.
        self.config = config
        # The description of the model provider template.
        self.description = description
        # Indicates whether the WUYING secure gateway proxy is enabled.
        self.enable_wuying_proxy = enable_wuying_proxy
        # The name of the model provider template.
        self.name = name
        # The name of the model provider.
        self.provider_name = provider_name
        # The model provider template ID.
        self.provider_template_id = provider_template_id
        # The model provider type.
        self.provider_type = provider_type

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

        if self.enable_wuying_proxy is not None:
            result['EnableWuyingProxy'] = self.enable_wuying_proxy

        if self.name is not None:
            result['Name'] = self.name

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        if self.provider_template_id is not None:
            result['ProviderTemplateId'] = self.provider_template_id

        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableWuyingProxy') is not None:
            self.enable_wuying_proxy = m.get('EnableWuyingProxy')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        if m.get('ProviderTemplateId') is not None:
            self.provider_template_id = m.get('ProviderTemplateId')

        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')

        return self

