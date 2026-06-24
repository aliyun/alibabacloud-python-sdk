# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class GetRuntimeModelConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetRuntimeModelConfigResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned result object.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetRuntimeModelConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetRuntimeModelConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        default_model: str = None,
        model_provider_list: List[main_models.GetRuntimeModelConfigResponseBodyDataModelProviderList] = None,
        model_template_id: str = None,
        model_template_name: str = None,
        model_template_ref_type: str = None,
        resource_group_id: str = None,
    ):
        # The default model (format: providerName/llmCode).
        self.default_model = default_model
        # The list of model providers.
        self.model_provider_list = model_provider_list
        # The configured model group ID.
        self.model_template_id = model_template_id
        # The model group name.
        self.model_template_name = model_template_name
        # The model template association type (returned only when an association exists).
        self.model_template_ref_type = model_template_ref_type
        # The resource group ID to which the runtime belongs. The value is null if the runtime is not associated with a resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        if self.model_provider_list:
            for v1 in self.model_provider_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_model is not None:
            result['DefaultModel'] = self.default_model

        result['ModelProviderList'] = []
        if self.model_provider_list is not None:
            for k1 in self.model_provider_list:
                result['ModelProviderList'].append(k1.to_map() if k1 else None)

        if self.model_template_id is not None:
            result['ModelTemplateId'] = self.model_template_id

        if self.model_template_name is not None:
            result['ModelTemplateName'] = self.model_template_name

        if self.model_template_ref_type is not None:
            result['ModelTemplateRefType'] = self.model_template_ref_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultModel') is not None:
            self.default_model = m.get('DefaultModel')

        self.model_provider_list = []
        if m.get('ModelProviderList') is not None:
            for k1 in m.get('ModelProviderList'):
                temp_model = main_models.GetRuntimeModelConfigResponseBodyDataModelProviderList()
                self.model_provider_list.append(temp_model.from_map(k1))

        if m.get('ModelTemplateId') is not None:
            self.model_template_id = m.get('ModelTemplateId')

        if m.get('ModelTemplateName') is not None:
            self.model_template_name = m.get('ModelTemplateName')

        if m.get('ModelTemplateRefType') is not None:
            self.model_template_ref_type = m.get('ModelTemplateRefType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

class GetRuntimeModelConfigResponseBodyDataModelProviderList(DaraModel):
    def __init__(
        self,
        llm_info_list: List[main_models.GetRuntimeModelConfigResponseBodyDataModelProviderListLlmInfoList] = None,
        model_provider_template_id: str = None,
        name: str = None,
        provider_name: str = None,
    ):
        # The list of model information.
        self.llm_info_list = llm_info_list
        # The model provider template ID.
        self.model_provider_template_id = model_provider_template_id
        # The model provider template name.
        self.name = name
        # The model provider name.
        self.provider_name = provider_name

    def validate(self):
        if self.llm_info_list:
            for v1 in self.llm_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LlmInfoList'] = []
        if self.llm_info_list is not None:
            for k1 in self.llm_info_list:
                result['LlmInfoList'].append(k1.to_map() if k1 else None)

        if self.model_provider_template_id is not None:
            result['ModelProviderTemplateId'] = self.model_provider_template_id

        if self.name is not None:
            result['Name'] = self.name

        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.llm_info_list = []
        if m.get('LlmInfoList') is not None:
            for k1 in m.get('LlmInfoList'):
                temp_model = main_models.GetRuntimeModelConfigResponseBodyDataModelProviderListLlmInfoList()
                self.llm_info_list.append(temp_model.from_map(k1))

        if m.get('ModelProviderTemplateId') is not None:
            self.model_provider_template_id = m.get('ModelProviderTemplateId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')

        return self

class GetRuntimeModelConfigResponseBodyDataModelProviderListLlmInfoList(DaraModel):
    def __init__(
        self,
        description: str = None,
        features: List[str] = None,
        inference_metadata: main_models.GetRuntimeModelConfigResponseBodyDataModelProviderListLlmInfoListInferenceMetadata = None,
        llm_code: str = None,
        name: str = None,
        published_time: str = None,
        risk_type: str = None,
    ):
        # The model description.
        self.description = description
        # The list of model features, such as function-calling, web-search, and structured-outputs.
        self.features = features
        # The inference metadata, including request and response modalities.
        self.inference_metadata = inference_metadata
        # The model code.
        self.llm_code = llm_code
        # The model name.
        self.name = name
        # The publish time in ISO 8601 format.
        self.published_time = published_time
        # The model risk type. This parameter is returned only when the request parameter IncludeRiskInfo is set to true.
        self.risk_type = risk_type

    def validate(self):
        if self.inference_metadata:
            self.inference_metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.features is not None:
            result['Features'] = self.features

        if self.inference_metadata is not None:
            result['InferenceMetadata'] = self.inference_metadata.to_map()

        if self.llm_code is not None:
            result['LlmCode'] = self.llm_code

        if self.name is not None:
            result['Name'] = self.name

        if self.published_time is not None:
            result['PublishedTime'] = self.published_time

        if self.risk_type is not None:
            result['RiskType'] = self.risk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('InferenceMetadata') is not None:
            temp_model = main_models.GetRuntimeModelConfigResponseBodyDataModelProviderListLlmInfoListInferenceMetadata()
            self.inference_metadata = temp_model.from_map(m.get('InferenceMetadata'))

        if m.get('LlmCode') is not None:
            self.llm_code = m.get('LlmCode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PublishedTime') is not None:
            self.published_time = m.get('PublishedTime')

        if m.get('RiskType') is not None:
            self.risk_type = m.get('RiskType')

        return self

class GetRuntimeModelConfigResponseBodyDataModelProviderListLlmInfoListInferenceMetadata(DaraModel):
    def __init__(
        self,
        request_modality: List[str] = None,
        response_modality: List[str] = None,
    ):
        # The list of request modalities, such as Text, Image, and Audio.
        self.request_modality = request_modality
        # The list of response modalities, such as Text, Image, and Audio.
        self.response_modality = response_modality

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_modality is not None:
            result['RequestModality'] = self.request_modality

        if self.response_modality is not None:
            result['ResponseModality'] = self.response_modality

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestModality') is not None:
            self.request_modality = m.get('RequestModality')

        if m.get('ResponseModality') is not None:
            self.response_modality = m.get('ResponseModality')

        return self

