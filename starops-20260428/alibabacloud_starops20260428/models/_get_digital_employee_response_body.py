# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List, Any

from alibabacloud_starops20260428 import models as main_models
from darabonba.model import DaraModel

class GetDigitalEmployeeResponseBody(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        channel: str = None,
        create_time: str = None,
        default_rule: str = None,
        description: str = None,
        display_name: str = None,
        employee_type: str = None,
        knowledges: main_models.GetDigitalEmployeeResponseBodyKnowledges = None,
        name: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        role_arn: str = None,
        sandbox_network_policy: main_models.GetDigitalEmployeeResponseBodySandboxNetworkPolicy = None,
        tags: List[main_models.Tag] = None,
        tool_policy: main_models.GetDigitalEmployeeResponseBodyToolPolicy = None,
        update_time: str = None,
    ):
        # The attributes.
        self.attributes = attributes
        # The channel type.
        self.channel = channel
        # The creation time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        # The default rule of the digital employee.
        self.default_rule = default_rule
        # The description of the digital employee.
        self.description = description
        # The display name of the digital employee.
        self.display_name = display_name
        # The type of the digital employee.
        self.employee_type = employee_type
        # The knowledge base list.
        self.knowledges = knowledges
        # The name of the digital employee.
        self.name = name
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The Alibaba Cloud Resource Name (ARN) of the RAM role.
        self.role_arn = role_arn
        # The sandbox network ACL policy configuration of the digital employee.
        self.sandbox_network_policy = sandbox_network_policy
        # The tags.
        self.tags = tags
        # The tool policy.
        self.tool_policy = tool_policy
        # The modification time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time

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

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.default_rule is not None:
            result['defaultRule'] = self.default_rule

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.employee_type is not None:
            result['employeeType'] = self.employee_type

        if self.knowledges is not None:
            result['knowledges'] = self.knowledges.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

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

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('defaultRule') is not None:
            self.default_rule = m.get('defaultRule')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('employeeType') is not None:
            self.employee_type = m.get('employeeType')

        if m.get('knowledges') is not None:
            temp_model = main_models.GetDigitalEmployeeResponseBodyKnowledges()
            self.knowledges = temp_model.from_map(m.get('knowledges'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        if m.get('sandboxNetworkPolicy') is not None:
            temp_model = main_models.GetDigitalEmployeeResponseBodySandboxNetworkPolicy()
            self.sandbox_network_policy = temp_model.from_map(m.get('sandboxNetworkPolicy'))

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('toolPolicy') is not None:
            temp_model = main_models.GetDigitalEmployeeResponseBodyToolPolicy()
            self.tool_policy = temp_model.from_map(m.get('toolPolicy'))

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class GetDigitalEmployeeResponseBodyToolPolicy(DaraModel):
    def __init__(
        self,
        aliyun: main_models.GetDigitalEmployeeResponseBodyToolPolicyAliyun = None,
    ):
        # The security policy configuration for Alibaba Cloud CLI tool calling invokes.
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
            temp_model = main_models.GetDigitalEmployeeResponseBodyToolPolicyAliyun()
            self.aliyun = temp_model.from_map(m.get('aliyun'))

        return self

class GetDigitalEmployeeResponseBodyToolPolicyAliyun(DaraModel):
    def __init__(
        self,
        auto_pass_policy: List[str] = None,
        deny_policy: List[str] = None,
        enable: bool = None,
        statements: List[main_models.GetDigitalEmployeeResponseBodyToolPolicyAliyunStatements] = None,
    ):
        # The auto-pass policy. Each entry is a RAM Action string in the format of product:ApiName, product:Prefix*, or product:*. Matched actions are automatically approved without human confirmation. If this parameter is empty or not configured, built-in read-only actions (Get*, List*, Describe*) are automatically approved. Unmatched actions require human-in-the-loop (HIL) confirmation.
        self.auto_pass_policy = auto_pass_policy
        # The explicit deny policy with the highest priority. Each entry is a RAM Action string in the format of product:ApiName, product:Prefix*, or product:*. If this parameter is empty or not configured, no actions are actively denied. STAROps directly denies matched actions. The Pop side performs secondary fallback enforcement.
        self.deny_policy = deny_policy
        # Indicates whether the policy is enabled.
        self.enable = enable
        # The list of Alibaba Cloud CLI tool policy statements.
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
                temp_model = main_models.GetDigitalEmployeeResponseBodyToolPolicyAliyunStatements()
                self.statements.append(temp_model.from_map(k1))

        return self

class GetDigitalEmployeeResponseBodyToolPolicyAliyunStatements(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        api_version: str = None,
        decision: str = None,
        product: str = None,
    ):
        # The list of RAM actions.
        self.actions = actions
        # The API version.
        self.api_version = api_version
        # The execution policy.
        self.decision = decision
        # The cloud product code.
        # 
        # This parameter is required.
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

class GetDigitalEmployeeResponseBodySandboxNetworkPolicy(DaraModel):
    def __init__(
        self,
        allow_cidrs: List[str] = None,
        allow_fqdns: List[str] = None,
        enable_acl: bool = None,
    ):
        # The list of allowed CIDRs or IP addresses.
        self.allow_cidrs = allow_cidrs
        # The list of allowed FQDNs.
        self.allow_fqdns = allow_fqdns
        # Indicates whether the sandbox network ACL is enabled.
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

class GetDigitalEmployeeResponseBodyKnowledges(DaraModel):
    def __init__(
        self,
        bailian: List[main_models.GetDigitalEmployeeResponseBodyKnowledgesBailian] = None,
        sop: List[Dict[str, Any]] = None,
    ):
        # The Bailian knowledge base list.
        self.bailian = bailian
        # The SOP knowledge base list.
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
                temp_model = main_models.GetDigitalEmployeeResponseBodyKnowledgesBailian()
                self.bailian.append(temp_model.from_map(k1))

        if m.get('sop') is not None:
            self.sop = m.get('sop')

        return self

class GetDigitalEmployeeResponseBodyKnowledgesBailian(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        index_id: str = None,
        region: str = None,
        workspace_id: str = None,
    ):
        # The knowledge base attributes.
        self.attributes = attributes
        # The Bailian index ID.
        self.index_id = index_id
        # The region of the knowledge base.
        self.region = region
        # The Bailian workspace ID.
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

