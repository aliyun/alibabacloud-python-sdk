# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetLlmModelProvidersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetLlmModelProvidersResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetLlmModelProvidersResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetLlmModelProvidersResponseBodyData(DaraModel):
    def __init__(
        self,
        base_url: str = None,
        enabled: bool = None,
        id: int = None,
        llm_models: List[main_models.GetLlmModelProvidersResponseBodyDataLlmModels] = None,
        provider_source: str = None,
        provider_type: str = None,
        service_provider: str = None,
    ):
        self.base_url = base_url
        self.enabled = enabled
        self.id = id
        self.llm_models = llm_models
        self.provider_source = provider_source
        self.provider_type = provider_type
        self.service_provider = service_provider

    def validate(self):
        if self.llm_models:
            for v1 in self.llm_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.id is not None:
            result['Id'] = self.id

        result['LlmModels'] = []
        if self.llm_models is not None:
            for k1 in self.llm_models:
                result['LlmModels'].append(k1.to_map() if k1 else None)

        if self.provider_source is not None:
            result['ProviderSource'] = self.provider_source

        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type

        if self.service_provider is not None:
            result['ServiceProvider'] = self.service_provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.llm_models = []
        if m.get('LlmModels') is not None:
            for k1 in m.get('LlmModels'):
                temp_model = main_models.GetLlmModelProvidersResponseBodyDataLlmModels()
                self.llm_models.append(temp_model.from_map(k1))

        if m.get('ProviderSource') is not None:
            self.provider_source = m.get('ProviderSource')

        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')

        if m.get('ServiceProvider') is not None:
            self.service_provider = m.get('ServiceProvider')

        return self

class GetLlmModelProvidersResponseBodyDataLlmModels(DaraModel):
    def __init__(
        self,
        cn_name: str = None,
        description: str = None,
        embedding_dimensions: List[int] = None,
        enabled: bool = None,
        invoke_type: str = None,
        model_id: int = None,
        model_types: List[str] = None,
        name: str = None,
        service_provider: str = None,
        tasks: List[str] = None,
    ):
        self.cn_name = cn_name
        self.description = description
        self.embedding_dimensions = embedding_dimensions
        self.enabled = enabled
        self.invoke_type = invoke_type
        self.model_id = model_id
        self.model_types = model_types
        self.name = name
        self.service_provider = service_provider
        self.tasks = tasks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cn_name is not None:
            result['CnName'] = self.cn_name

        if self.description is not None:
            result['Description'] = self.description

        if self.embedding_dimensions is not None:
            result['EmbeddingDimensions'] = self.embedding_dimensions

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_types is not None:
            result['ModelTypes'] = self.model_types

        if self.name is not None:
            result['Name'] = self.name

        if self.service_provider is not None:
            result['ServiceProvider'] = self.service_provider

        if self.tasks is not None:
            result['Tasks'] = self.tasks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CnName') is not None:
            self.cn_name = m.get('CnName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EmbeddingDimensions') is not None:
            self.embedding_dimensions = m.get('EmbeddingDimensions')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelTypes') is not None:
            self.model_types = m.get('ModelTypes')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ServiceProvider') is not None:
            self.service_provider = m.get('ServiceProvider')

        if m.get('Tasks') is not None:
            self.tasks = m.get('Tasks')

        return self

