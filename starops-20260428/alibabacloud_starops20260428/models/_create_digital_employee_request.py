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
        channel: str = None,
        default_rule: str = None,
        description: str = None,
        display_name: str = None,
        knowledges: main_models.CreateDigitalEmployeeRequestKnowledges = None,
        name: str = None,
        resource_group_id: str = None,
        role_arn: str = None,
        sandbox_network_policy: main_models.CreateDigitalEmployeeRequestSandboxNetworkPolicy = None,
        tags: List[main_models.Tag] = None,
        tool_policy: main_models.CreateDigitalEmployeeRequestToolPolicy = None,
    ):
        # The attributes of the digital employee.
        self.attributes = attributes
        # The channel type.
        self.channel = channel
        # The default rule of the digital employee.
        self.default_rule = default_rule
        # The description of the digital employee.
        self.description = description
        # The display name of the digital employee.
        self.display_name = display_name
        # The list of knowledge bases.
        self.knowledges = knowledges
        # The name of the digital employee.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ARN of the RAM role.
        # 
        # This parameter is required.
        self.role_arn = role_arn
        # The sandbox network ACL policy configuration for the digital employee.
        self.sandbox_network_policy = sandbox_network_policy
        # The tags.
        self.tags = tags
        # The tool policy.
        self.tool_policy = tool_policy

    def validate(self):
        if self.knowledges:
            self.knowledges.validate()
        if self.sandbox_network_policy:
            self.sandbox_network_policy.validate()
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

        if self.channel is not None:
            result['channel'] = self.channel

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

        if self.sandbox_network_policy is not None:
            result['sandboxNetworkPolicy'] = self.sandbox_network_policy.to_map()

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

        if m.get('channel') is not None:
            self.channel = m.get('channel')

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

        if m.get('sandboxNetworkPolicy') is not None:
            temp_model = main_models.CreateDigitalEmployeeRequestSandboxNetworkPolicy()
            self.sandbox_network_policy = temp_model.from_map(m.get('sandboxNetworkPolicy'))

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
        global_: main_models.CreateDigitalEmployeeRequestToolPolicyGlobal = None,
        hooks: List[main_models.Hook] = None,
    ):
        # The security policy configuration for Aliyun CLI tool invocation.
        self.aliyun = aliyun
        # The global auto-pass rules for tool invocation.
        self.global_ = global_
        # The hook configuration.
        self.hooks = hooks

    def validate(self):
        if self.aliyun:
            self.aliyun.validate()
        if self.global_:
            self.global_.validate()
        if self.hooks:
            for v1 in self.hooks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun is not None:
            result['aliyun'] = self.aliyun.to_map()

        if self.global_ is not None:
            result['global'] = self.global_.to_map()

        result['hooks'] = []
        if self.hooks is not None:
            for k1 in self.hooks:
                result['hooks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyun') is not None:
            temp_model = main_models.CreateDigitalEmployeeRequestToolPolicyAliyun()
            self.aliyun = temp_model.from_map(m.get('aliyun'))

        if m.get('global') is not None:
            temp_model = main_models.CreateDigitalEmployeeRequestToolPolicyGlobal()
            self.global_ = temp_model.from_map(m.get('global'))

        self.hooks = []
        if m.get('hooks') is not None:
            for k1 in m.get('hooks'):
                temp_model = main_models.Hook()
                self.hooks.append(temp_model.from_map(k1))

        return self

class CreateDigitalEmployeeRequestToolPolicyGlobal(DaraModel):
    def __init__(
        self,
        auto_pass_policy: List[main_models.AutoPassPolicy] = None,
    ):
        # The array of auto-pass policies.
        self.auto_pass_policy = auto_pass_policy

    def validate(self):
        if self.auto_pass_policy:
            for v1 in self.auto_pass_policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['autoPassPolicy'] = []
        if self.auto_pass_policy is not None:
            for k1 in self.auto_pass_policy:
                result['autoPassPolicy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_pass_policy = []
        if m.get('autoPassPolicy') is not None:
            for k1 in m.get('autoPassPolicy'):
                temp_model = main_models.AutoPassPolicy()
                self.auto_pass_policy.append(temp_model.from_map(k1))

        return self

class CreateDigitalEmployeeRequestToolPolicyAliyun(DaraModel):
    def __init__(
        self,
        auto_pass_policy: List[str] = None,
        deny_policy: List[str] = None,
        enable: bool = None,
        statements: List[main_models.CreateDigitalEmployeeRequestToolPolicyAliyunStatements] = None,
    ):
        # The auto-passed RAM actions. The format is *, product:ApiName, or product:Prefix*.
        self.auto_pass_policy = auto_pass_policy
        # The denied RAM actions. The format is *, product:ApiName, or product:Prefix*.
        self.deny_policy = deny_policy
        # Specifies whether to enable the policy.
        self.enable = enable
        # **[Deprecated]** Use denyPolicy and autoPassPolicy instead. This field is still read during the transition period. Original description: The list of Aliyun OpenAPI tool policy statements.
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
        if self.auto_pass_policy is not None:
            result['autoPassPolicy'] = self.auto_pass_policy

        if self.deny_policy is not None:
            result['denyPolicy'] = self.deny_policy

        if self.enable is not None:
            result['enable'] = self.enable

        result['statements'] = []
        if self.statements is not None:
            for k1 in self.statements:
                result['statements'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoPassPolicy') is not None:
            self.auto_pass_policy = m.get('autoPassPolicy')

        if m.get('denyPolicy') is not None:
            self.deny_policy = m.get('denyPolicy')

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
        # The list of Aliyun OpenAPI actions. The format is product:ApiName, product:Prefix*, or product:*.
        self.actions = actions
        # The Aliyun OpenAPI version corresponding to this statement.
        self.api_version = api_version
        # The execution policy after the API is matched.
        self.decision = decision
        # The Aliyun OpenAPI product name corresponding to this statement.
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

class CreateDigitalEmployeeRequestSandboxNetworkPolicy(DaraModel):
    def __init__(
        self,
        allow_cidrs: List[str] = None,
        allow_fqdns: List[str] = None,
        enable_acl: bool = None,
    ):
        # The list of allowed CIDR blocks or IP addresses.
        self.allow_cidrs = allow_cidrs
        # The list of allowed FQDNs.
        self.allow_fqdns = allow_fqdns
        # Specifies whether to enable the sandbox network ACL.
        self.enable_acl = enable_acl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_cidrs is not None:
            result['allowCidrs'] = self.allow_cidrs

        if self.allow_fqdns is not None:
            result['allowFqdns'] = self.allow_fqdns

        if self.enable_acl is not None:
            result['enableAcl'] = self.enable_acl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowCidrs') is not None:
            self.allow_cidrs = m.get('allowCidrs')

        if m.get('allowFqdns') is not None:
            self.allow_fqdns = m.get('allowFqdns')

        if m.get('enableAcl') is not None:
            self.enable_acl = m.get('enableAcl')

        return self

class CreateDigitalEmployeeRequestKnowledges(DaraModel):
    def __init__(
        self,
        bailian: List[main_models.CreateDigitalEmployeeRequestKnowledgesBailian] = None,
        sop: List[Dict[str, Any]] = None,
    ):
        # The list of Bailian knowledge bases.
        self.bailian = bailian
        # The list of SOP knowledge bases.
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
        # The attributes of the knowledge base.
        self.attributes = attributes
        # The ID of the Bailian index.
        self.index_id = index_id
        # The region of the knowledge base.
        self.region = region
        # The ID of the Bailian workspace.
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

