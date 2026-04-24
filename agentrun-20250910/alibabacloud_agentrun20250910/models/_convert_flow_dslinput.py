# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class ConvertFlowDSLInput(DaraModel):
    def __init__(
        self,
        dsl_source: main_models.ConvertFlowDSLInputDslSource = None,
        options: main_models.ConvertFlowDSLInputOptions = None,
    ):
        # 工作流DSL的来源配置，支持inline和base64两种格式
        # 
        # This parameter is required.
        self.dsl_source = dsl_source
        # DSL转换的可选配置参数
        self.options = options

    def validate(self):
        if self.dsl_source:
            self.dsl_source.validate()
        if self.options:
            self.options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dsl_source is not None:
            result['dslSource'] = self.dsl_source.to_map()

        if self.options is not None:
            result['options'] = self.options.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dslSource') is not None:
            temp_model = main_models.ConvertFlowDSLInputDslSource()
            self.dsl_source = temp_model.from_map(m.get('dslSource'))

        if m.get('options') is not None:
            temp_model = main_models.ConvertFlowDSLInputOptions()
            self.options = temp_model.from_map(m.get('options'))

        return self

class ConvertFlowDSLInputOptions(DaraModel):
    def __init__(
        self,
        compatibility_check: bool = None,
        credential_name: str = None,
        flow_name: str = None,
        vpc_endpoint_name: str = None,
        vpc_endpoints: Dict[str, str] = None,
    ):
        # 是否执行兼容性检查，默认为true
        self.compatibility_check = compatibility_check
        self.credential_name = credential_name
        self.flow_name = flow_name
        # 全局VPC端点名称，对所有节点统一生效。如果指定了vpcEndpoints映射，则映射中的节点优先使用映射值
        self.vpc_endpoint_name = vpc_endpoint_name
        # 按节点名称指定VPC端点，key为节点名称(stateName)，value为该节点使用的VPC端点名称。优先级高于vpcEndpointName
        self.vpc_endpoints = vpc_endpoints

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compatibility_check is not None:
            result['compatibilityCheck'] = self.compatibility_check

        if self.credential_name is not None:
            result['credentialName'] = self.credential_name

        if self.flow_name is not None:
            result['flowName'] = self.flow_name

        if self.vpc_endpoint_name is not None:
            result['vpcEndpointName'] = self.vpc_endpoint_name

        if self.vpc_endpoints is not None:
            result['vpcEndpoints'] = self.vpc_endpoints

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('compatibilityCheck') is not None:
            self.compatibility_check = m.get('compatibilityCheck')

        if m.get('credentialName') is not None:
            self.credential_name = m.get('credentialName')

        if m.get('flowName') is not None:
            self.flow_name = m.get('flowName')

        if m.get('vpcEndpointName') is not None:
            self.vpc_endpoint_name = m.get('vpcEndpointName')

        if m.get('vpcEndpoints') is not None:
            self.vpc_endpoints = m.get('vpcEndpoints')

        return self

class ConvertFlowDSLInputDslSource(DaraModel):
    def __init__(
        self,
        content: str = None,
        encoding: str = None,
        provider: str = None,
    ):
        # DSL内容，可以是原始JSON字符串，或根据encoding字段指定的编码格式
        # 
        # This parameter is required.
        self.content = content
        # DSL内容的编码方式。不填表示内容为原始字符串；base64表示内容经过Base64编码；base64+gzip表示内容经过gzip压缩后再Base64编码
        self.encoding = encoding
        # 源DSL的提供商类型，如：dify、n8n、zapier等
        # 
        # This parameter is required.
        self.provider = provider

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.encoding is not None:
            result['encoding'] = self.encoding

        if self.provider is not None:
            result['provider'] = self.provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('encoding') is not None:
            self.encoding = m.get('encoding')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        return self

