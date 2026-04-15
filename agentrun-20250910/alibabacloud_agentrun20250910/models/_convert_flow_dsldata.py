# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class ConvertFlowDSLData(DaraModel):
    def __init__(
        self,
        conversion_plan: main_models.ConvertFlowDSLDataConversionPlan = None,
        flow: main_models.ConvertFlowDSLDataFlow = None,
        plugin_errors: List[main_models.ConvertFlowDSLDataPluginErrors] = None,
        toolset_installations: List[main_models.ConvertFlowDSLDataToolsetInstallations] = None,
    ):
        # DSL兼容性分析和转换计划
        self.conversion_plan = conversion_plan
        # 转换后的AgentRun Flow配置信息
        # 
        # This parameter is required.
        self.flow = flow
        # 插件识别或转换过程中的错误信息
        self.plugin_errors = plugin_errors
        # 需要安装的Toolset配置列表
        self.toolset_installations = toolset_installations

    def validate(self):
        if self.conversion_plan:
            self.conversion_plan.validate()
        if self.flow:
            self.flow.validate()
        if self.plugin_errors:
            for v1 in self.plugin_errors:
                 if v1:
                    v1.validate()
        if self.toolset_installations:
            for v1 in self.toolset_installations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversion_plan is not None:
            result['conversionPlan'] = self.conversion_plan.to_map()

        if self.flow is not None:
            result['flow'] = self.flow.to_map()

        result['pluginErrors'] = []
        if self.plugin_errors is not None:
            for k1 in self.plugin_errors:
                result['pluginErrors'].append(k1.to_map() if k1 else None)

        result['toolsetInstallations'] = []
        if self.toolset_installations is not None:
            for k1 in self.toolset_installations:
                result['toolsetInstallations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conversionPlan') is not None:
            temp_model = main_models.ConvertFlowDSLDataConversionPlan()
            self.conversion_plan = temp_model.from_map(m.get('conversionPlan'))

        if m.get('flow') is not None:
            temp_model = main_models.ConvertFlowDSLDataFlow()
            self.flow = temp_model.from_map(m.get('flow'))

        self.plugin_errors = []
        if m.get('pluginErrors') is not None:
            for k1 in m.get('pluginErrors'):
                temp_model = main_models.ConvertFlowDSLDataPluginErrors()
                self.plugin_errors.append(temp_model.from_map(k1))

        self.toolset_installations = []
        if m.get('toolsetInstallations') is not None:
            for k1 in m.get('toolsetInstallations'):
                temp_model = main_models.ConvertFlowDSLDataToolsetInstallations()
                self.toolset_installations.append(temp_model.from_map(k1))

        return self

class ConvertFlowDSLDataToolsetInstallations(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        spec: Dict[str, Any] = None,
    ):
        # Toolset描述
        self.description = description
        # Toolset名称
        # 
        # This parameter is required.
        self.name = name
        # Toolset规格配置（JSON对象）
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.spec is not None:
            result['spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('spec') is not None:
            self.spec = m.get('spec')

        return self

class ConvertFlowDSLDataPluginErrors(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        provider_name: str = None,
        reason: str = None,
        tool_name: str = None,
    ):
        # 相关节点的标识符
        self.node_id = node_id
        # 插件提供商名称
        # 
        # This parameter is required.
        self.provider_name = provider_name
        # 错误原因描述
        # 
        # This parameter is required.
        self.reason = reason
        # 工具名称
        self.tool_name = tool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.provider_name is not None:
            result['providerName'] = self.provider_name

        if self.reason is not None:
            result['reason'] = self.reason

        if self.tool_name is not None:
            result['toolName'] = self.tool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('providerName') is not None:
            self.provider_name = m.get('providerName')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('toolName') is not None:
            self.tool_name = m.get('toolName')

        return self

class ConvertFlowDSLDataFlow(DaraModel):
    def __init__(
        self,
        definition: str = None,
        description: str = None,
        environment_configuration: main_models.EnvironmentConfiguration = None,
        flow_name: str = None,
    ):
        # 工作流的FnF State Machine定义（YAML格式）
        # 
        # This parameter is required.
        self.definition = definition
        # 工作流的描述信息
        self.description = description
        # 工作流的环境变量配置
        self.environment_configuration = environment_configuration
        # 转换后的工作流名称
        # 
        # This parameter is required.
        self.flow_name = flow_name

    def validate(self):
        if self.environment_configuration:
            self.environment_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.definition is not None:
            result['definition'] = self.definition

        if self.description is not None:
            result['description'] = self.description

        if self.environment_configuration is not None:
            result['environmentConfiguration'] = self.environment_configuration.to_map()

        if self.flow_name is not None:
            result['flowName'] = self.flow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('definition') is not None:
            self.definition = m.get('definition')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environmentConfiguration') is not None:
            temp_model = main_models.EnvironmentConfiguration()
            self.environment_configuration = temp_model.from_map(m.get('environmentConfiguration'))

        if m.get('flowName') is not None:
            self.flow_name = m.get('flowName')

        return self

class ConvertFlowDSLDataConversionPlan(DaraModel):
    def __init__(
        self,
        issues: List[main_models.ConvertFlowDSLDataConversionPlanIssues] = None,
        summary: main_models.ConvertFlowDSLDataConversionPlanSummary = None,
    ):
        # 节点兼容性问题详情
        self.issues = issues
        # 节点兼容性统计摘要
        # 
        # This parameter is required.
        self.summary = summary

    def validate(self):
        if self.issues:
            for v1 in self.issues:
                 if v1:
                    v1.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['issues'] = []
        if self.issues is not None:
            for k1 in self.issues:
                result['issues'].append(k1.to_map() if k1 else None)

        if self.summary is not None:
            result['summary'] = self.summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.issues = []
        if m.get('issues') is not None:
            for k1 in m.get('issues'):
                temp_model = main_models.ConvertFlowDSLDataConversionPlanIssues()
                self.issues.append(temp_model.from_map(k1))

        if m.get('summary') is not None:
            temp_model = main_models.ConvertFlowDSLDataConversionPlanSummary()
            self.summary = temp_model.from_map(m.get('summary'))

        return self

class ConvertFlowDSLDataConversionPlanSummary(DaraModel):
    def __init__(
        self,
        compatible_nodes: int = None,
        nodes_need_config: int = None,
        nodes_need_conversion: int = None,
        total_nodes: int = None,
        unsupported_nodes: int = None,
    ):
        # 完全兼容的节点数
        # 
        # This parameter is required.
        self.compatible_nodes = compatible_nodes
        # 需要手动配置的节点数
        # 
        # This parameter is required.
        self.nodes_need_config = nodes_need_config
        # 需要特殊转换处理的节点数
        # 
        # This parameter is required.
        self.nodes_need_conversion = nodes_need_conversion
        # Dify DSL中的总节点数
        # 
        # This parameter is required.
        self.total_nodes = total_nodes
        # 不支持的节点数
        # 
        # This parameter is required.
        self.unsupported_nodes = unsupported_nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compatible_nodes is not None:
            result['compatibleNodes'] = self.compatible_nodes

        if self.nodes_need_config is not None:
            result['nodesNeedConfig'] = self.nodes_need_config

        if self.nodes_need_conversion is not None:
            result['nodesNeedConversion'] = self.nodes_need_conversion

        if self.total_nodes is not None:
            result['totalNodes'] = self.total_nodes

        if self.unsupported_nodes is not None:
            result['unsupportedNodes'] = self.unsupported_nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('compatibleNodes') is not None:
            self.compatible_nodes = m.get('compatibleNodes')

        if m.get('nodesNeedConfig') is not None:
            self.nodes_need_config = m.get('nodesNeedConfig')

        if m.get('nodesNeedConversion') is not None:
            self.nodes_need_conversion = m.get('nodesNeedConversion')

        if m.get('totalNodes') is not None:
            self.total_nodes = m.get('totalNodes')

        if m.get('unsupportedNodes') is not None:
            self.unsupported_nodes = m.get('unsupportedNodes')

        return self



class ConvertFlowDSLDataConversionPlanIssues(DaraModel):
    def __init__(
        self,
        description: str = None,
        details: Dict[str, str] = None,
        issue_type: str = None,
        level: str = None,
        node_id: str = None,
        node_title: str = None,
        node_type: str = None,
        suggestion: str = None,
    ):
        # 问题描述
        # 
        # This parameter is required.
        self.description = description
        # 问题的详细信息（JSON对象）
        self.details = details
        # 问题类型：needs_config, needs_conversion, unsupported
        # 
        # This parameter is required.
        self.issue_type = issue_type
        # 问题严重程度：info, warning, error
        # 
        # This parameter is required.
        self.level = level
        # Dify DSL中的节点标识符
        # 
        # This parameter is required.
        self.node_id = node_id
        # 节点显示名称
        self.node_title = node_title
        # 节点类型
        # 
        # This parameter is required.
        self.node_type = node_type
        # 解决建议
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.details is not None:
            result['details'] = self.details

        if self.issue_type is not None:
            result['issueType'] = self.issue_type

        if self.level is not None:
            result['level'] = self.level

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.node_title is not None:
            result['nodeTitle'] = self.node_title

        if self.node_type is not None:
            result['nodeType'] = self.node_type

        if self.suggestion is not None:
            result['suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('details') is not None:
            self.details = m.get('details')

        if m.get('issueType') is not None:
            self.issue_type = m.get('issueType')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('nodeTitle') is not None:
            self.node_title = m.get('nodeTitle')

        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')

        if m.get('suggestion') is not None:
            self.suggestion = m.get('suggestion')

        return self

