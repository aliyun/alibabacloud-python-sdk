# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List, Any

from alibabacloud_starops20260428 import models as main_models
from darabonba.model import DaraModel

class UpdateDigitalEmployeeRequest(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        default_rule: str = None,
        description: str = None,
        display_name: str = None,
        knowledges: main_models.UpdateDigitalEmployeeRequestKnowledges = None,
        role_arn: str = None,
        sandbox_network_policy: main_models.UpdateDigitalEmployeeRequestSandboxNetworkPolicy = None,
        tool_policy: main_models.UpdateDigitalEmployeeRequestToolPolicy = None,
    ):
        # The attributes.
        self.attributes = attributes
        # The default rule of the digital employee.
        self.default_rule = default_rule
        # The description of the digital employee.
        self.description = description
        # The display name of the digital employee.
        self.display_name = display_name
        # The list of knowledge bases.
        self.knowledges = knowledges
        # The ARN of the RAM role.
        self.role_arn = role_arn
        # The list of CIDRs or IP addresses that are allowed to be accessed.
        self.sandbox_network_policy = sandbox_network_policy
        # The security policy configuration for tool calling of the digital employee.
        self.tool_policy = tool_policy

    def validate(self):
        if self.knowledges:
            self.knowledges.validate()
        if self.sandbox_network_policy:
            self.sandbox_network_policy.validate()
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

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        if self.sandbox_network_policy is not None:
            result['sandboxNetworkPolicy'] = self.sandbox_network_policy.to_map()

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
            temp_model = main_models.UpdateDigitalEmployeeRequestKnowledges()
            self.knowledges = temp_model.from_map(m.get('knowledges'))

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        if m.get('sandboxNetworkPolicy') is not None:
            temp_model = main_models.UpdateDigitalEmployeeRequestSandboxNetworkPolicy()
            self.sandbox_network_policy = temp_model.from_map(m.get('sandboxNetworkPolicy'))

        if m.get('toolPolicy') is not None:
            temp_model = main_models.UpdateDigitalEmployeeRequestToolPolicy()
            self.tool_policy = temp_model.from_map(m.get('toolPolicy'))

        return self

class UpdateDigitalEmployeeRequestToolPolicy(DaraModel):
    def __init__(
        self,
        aliyun: main_models.UpdateDigitalEmployeeRequestToolPolicyAliyun = None,
    ):
        # The security policy configuration for Aliyun CLI tool calling.
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
            temp_model = main_models.UpdateDigitalEmployeeRequestToolPolicyAliyun()
            self.aliyun = temp_model.from_map(m.get('aliyun'))

        return self

class UpdateDigitalEmployeeRequestToolPolicyAliyun(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        statements: List[main_models.UpdateDigitalEmployeeRequestToolPolicyAliyunStatements] = None,
    ):
        # Specifies whether to enable the policy.
        self.enable = enable
        # The list of Aliyun CLI tool policy statements.
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
                temp_model = main_models.UpdateDigitalEmployeeRequestToolPolicyAliyunStatements()
                self.statements.append(temp_model.from_map(k1))

        return self

class UpdateDigitalEmployeeRequestToolPolicyAliyunStatements(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        api_version: str = None,
        decision: str = None,
        product: str = None,
    ):
        # RAM action
        self.actions = actions
        # The API version. This parameter is deprecated.
        self.api_version = api_version
        # The execution policy.
        self.decision = decision
        # The cloud service code.
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

class UpdateDigitalEmployeeRequestSandboxNetworkPolicy(DaraModel):
    def __init__(
        self,
        allow_cidrs: List[str] = None,
        allow_fqdns: List[str] = None,
        enable_acl: bool = None,
    ):
        # The list of CIDRs or IP addresses that are allowed to be accessed.
        self.allow_cidrs = allow_cidrs
        # The list of FQDNs that are allowed to be accessed.
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

class UpdateDigitalEmployeeRequestKnowledges(DaraModel):
    def __init__(
        self,
        bailian: List[main_models.UpdateDigitalEmployeeRequestKnowledgesBailian] = None,
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
                temp_model = main_models.UpdateDigitalEmployeeRequestKnowledgesBailian()
                self.bailian.append(temp_model.from_map(k1))

        if m.get('sop') is not None:
            self.sop = m.get('sop')

        return self

class UpdateDigitalEmployeeRequestKnowledgesBailian(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        index_id: str = None,
        region: str = None,
        workspace_id: str = None,
    ):
        # The attributes of the knowledge base.
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

