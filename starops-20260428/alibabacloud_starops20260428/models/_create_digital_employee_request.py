# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List, Any

from alibabacloud_starops20260428 import models as main_models
from darabonba.model import DaraModel

class CreateDigitalEmployeeRequest(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        default_rule: str = None,
        description: str = None,
        display_name: str = None,
        knowledges: main_models.CreateDigitalEmployeeRequestKnowledges = None,
        name: str = None,
        resource_group_id: str = None,
        role_arn: str = None,
        tags: List[main_models.Tag] = None,
        tool_policy: main_models.CreateDigitalEmployeeRequestToolPolicy = None,
    ):
        self.attributes = attributes
        self.default_rule = default_rule
        self.description = description
        self.display_name = display_name
        self.knowledges = knowledges
        # This parameter is required.
        self.name = name
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.role_arn = role_arn
        self.tags = tags
        # 数字员工工具调用安全策略配置。
        self.tool_policy = tool_policy

    def validate(self):
        if self.knowledges:
            self.knowledges.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.tool_policy:
            self.tool_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['attributes'] = self.attributes

        if self.default_rule is not None:
            result['defaultRule'] = self.default_rule

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.knowledges is not None:
            result['knowledges'] = self.knowledges.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.tool_policy is not None:
            result['toolPolicy'] = self.tool_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('defaultRule') is not None:
            self.default_rule = m.get('defaultRule')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('knowledges') is not None:
            temp_model = main_models.CreateDigitalEmployeeRequestKnowledges()
            self.knowledges = temp_model.from_map(m.get('knowledges'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('toolPolicy') is not None:
            temp_model = main_models.CreateDigitalEmployeeRequestToolPolicy()
            self.tool_policy = temp_model.from_map(m.get('toolPolicy'))

        return self

class CreateDigitalEmployeeRequestToolPolicy(DaraModel):
    def __init__(
        self,
        aliyun: main_models.CreateDigitalEmployeeRequestToolPolicyAliyun = None,
    ):
        # Aliyun MCP 工具调用安全策略配置。
        self.aliyun = aliyun

    def validate(self):
        if self.aliyun:
            self.aliyun.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun is not None:
            result['aliyun'] = self.aliyun.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyun') is not None:
            temp_model = main_models.CreateDigitalEmployeeRequestToolPolicyAliyun()
            self.aliyun = temp_model.from_map(m.get('aliyun'))

        return self

class CreateDigitalEmployeeRequestToolPolicyAliyun(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        statements: List[main_models.CreateDigitalEmployeeRequestToolPolicyAliyunStatements] = None,
    ):
        # 是否启用 Aliyun MCP 工具策略。
        self.enable = enable
        # Aliyun OpenAPI 工具策略语句列表。
        self.statements = statements

    def validate(self):
        if self.statements:
            for v1 in self.statements:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        result['statements'] = []
        if self.statements is not None:
            for k1 in self.statements:
                result['statements'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        self.statements = []
        if m.get('statements') is not None:
            for k1 in m.get('statements'):
                temp_model = main_models.CreateDigitalEmployeeRequestToolPolicyAliyunStatements()
                self.statements.append(temp_model.from_map(k1))

        return self

class CreateDigitalEmployeeRequestToolPolicyAliyunStatements(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        api_version: str = None,
        decision: str = None,
        product: str = None,
    ):
        # Aliyun OpenAPI Action 列表，格式为 product:ApiName、product:Prefix* 或 product:*。
        self.actions = actions
        # 本条语句对应的 Aliyun OpenAPI API 版本。
        self.api_version = api_version
        # 命中该 API 后的执行策略。
        self.decision = decision
        # 本条语句对应的 Aliyun OpenAPI 产品名。
        self.product = product

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.api_version is not None:
            result['apiVersion'] = self.api_version

        if self.decision is not None:
            result['decision'] = self.decision

        if self.product is not None:
            result['product'] = self.product

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        if m.get('decision') is not None:
            self.decision = m.get('decision')

        if m.get('product') is not None:
            self.product = m.get('product')

        return self

class CreateDigitalEmployeeRequestKnowledges(DaraModel):
    def __init__(
        self,
        bailian: List[main_models.CreateDigitalEmployeeRequestKnowledgesBailian] = None,
        sop: List[Dict[str, Any]] = None,
    ):
        self.bailian = bailian
        self.sop = sop

    def validate(self):
        if self.bailian:
            for v1 in self.bailian:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['bailian'] = []
        if self.bailian is not None:
            for k1 in self.bailian:
                result['bailian'].append(k1.to_map() if k1 else None)

        if self.sop is not None:
            result['sop'] = self.sop

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bailian = []
        if m.get('bailian') is not None:
            for k1 in m.get('bailian'):
                temp_model = main_models.CreateDigitalEmployeeRequestKnowledgesBailian()
                self.bailian.append(temp_model.from_map(k1))

        if m.get('sop') is not None:
            self.sop = m.get('sop')

        return self

class CreateDigitalEmployeeRequestKnowledgesBailian(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        index_id: str = None,
        region: str = None,
        workspace_id: str = None,
    ):
        self.attributes = attributes
        self.index_id = index_id
        self.region = region
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['attributes'] = self.attributes

        if self.index_id is not None:
            result['indexId'] = self.index_id

        if self.region is not None:
            result['region'] = self.region

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('indexId') is not None:
            self.index_id = m.get('indexId')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

