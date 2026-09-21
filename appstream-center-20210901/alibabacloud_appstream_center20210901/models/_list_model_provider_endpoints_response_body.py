# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListModelProviderEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListModelProviderEndpointsResponseBodyData] = None,
        request_id: str = None,
    ):
        # The returned data object.
        self.data = data
        # The request ID, which uniquely identifies the request.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListModelProviderEndpointsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListModelProviderEndpointsResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        endpoints: List[main_models.ListModelProviderEndpointsResponseBodyDataEndpoints] = None,
        provider_name: str = None,
        provider_url: str = None,
    ):
        # The provider description, such as Alibaba Cloud Bailian.
        self.description = description
        # The list of all endpoints under the provider.
        self.endpoints = endpoints
        # The provider name, such as bailian or moonshot.
        self.provider_name = provider_name
        # The provider website URL, which is used to direct users to obtain an API key.
        self.provider_url = provider_url

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        if self.provider_url is not None:
            result['ProviderUrl'] = self.provider_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.ListModelProviderEndpointsResponseBodyDataEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        if m.get('ProviderUrl') is not None:
            self.provider_url = m.get('ProviderUrl')

        return self

class ListModelProviderEndpointsResponseBodyDataEndpoints(DaraModel):
    def __init__(
        self,
        api_type: str = None,
        base_url: str = None,
        description: str = None,
        name: str = None,
        provider_url: str = None,
        tags: List[str] = None,
    ):
        # The API compatibility type, such as openai-compatible or anthropic-compatible.
        self.api_type = api_type
        # The API base URL, such as https://coding.dashscope.aliyuncs.com/v1.
        self.base_url = base_url
        # The endpoint description, such as Coding Plan - OpenAI compatible protocol.
        self.description = description
        # The endpoint identifier name, such as coding-openai or cn-beijing.
        self.name = name
        # The provider URL.
        self.provider_url = provider_url
        # The list of tags used for categorization and filtering, such as coding-plan, on-demand, or cn-beijing.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_type is not None:
            result['ApiType'] = self.api_type

        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.provider_url is not None:
            result['ProviderUrl'] = self.provider_url

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')

        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProviderUrl') is not None:
            self.provider_url = m.get('ProviderUrl')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

