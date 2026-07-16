# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class GetChainResponseBody(DaraModel):
    def __init__(
        self,
        chain_config: main_models.GetChainResponseBodyChainConfig = None,
        chain_id: str = None,
        code: str = None,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        is_success: bool = None,
        modified_time: int = None,
        name: str = None,
        request_id: str = None,
        scope_exclude: List[str] = None,
        scope_id: str = None,
        scope_type: str = None,
    ):
        # Delivery chain configuration description
        self.chain_config = chain_config
        # Delivery chain ID
        self.chain_id = chain_id
        # Return code
        self.code = code
        # Delivery chain creation time
        self.create_time = create_time
        # Delivery chain description
        self.description = description
        # Instance ID
        self.instance_id = instance_id
        # Indicates whether the operation succeeded
        self.is_success = is_success
        # Updated At of the delivery chain description
        self.modified_time = modified_time
        # Delivery chain name
        self.name = name
        # Request ID
        self.request_id = request_id
        # Collection of repositories excluded from delivery chain execution
        self.scope_exclude = scope_exclude
        # Delivery chain scope ID
        self.scope_id = scope_id
        # Delivery chain scope type
        self.scope_type = scope_type

    def validate(self):
        if self.chain_config:
            self.chain_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chain_config is not None:
            result['ChainConfig'] = self.chain_config.to_map()

        if self.chain_id is not None:
            result['ChainId'] = self.chain_id

        if self.code is not None:
            result['Code'] = self.code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scope_exclude is not None:
            result['ScopeExclude'] = self.scope_exclude

        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainConfig') is not None:
            temp_model = main_models.GetChainResponseBodyChainConfig()
            self.chain_config = temp_model.from_map(m.get('ChainConfig'))

        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScopeExclude') is not None:
            self.scope_exclude = m.get('ScopeExclude')

        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        return self

class GetChainResponseBodyChainConfig(DaraModel):
    def __init__(
        self,
        chain_config_id: str = None,
        is_active: bool = None,
        nodes: List[main_models.GetChainResponseBodyChainConfigNodes] = None,
        routers: List[main_models.GetChainResponseBodyChainConfigRouters] = None,
        version: str = None,
    ):
        # Delivery chain configuration ID
        self.chain_config_id = chain_config_id
        # Indicates whether the delivery chain configuration is active. Valid values:
        # 
        # - `true`: The configuration is active.
        # 
        # - `false`: The configuration is not active.
        self.is_active = is_active
        # Each edge zone in the delivery chain
        self.nodes = nodes
        # Execution order relationships between edge zones in the delivery chain
        self.routers = routers
        # Delivery chain version
        self.version = version

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()
        if self.routers:
            for v1 in self.routers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chain_config_id is not None:
            result['ChainConfigId'] = self.chain_config_id

        if self.is_active is not None:
            result['IsActive'] = self.is_active

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        result['Routers'] = []
        if self.routers is not None:
            for k1 in self.routers:
                result['Routers'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainConfigId') is not None:
            self.chain_config_id = m.get('ChainConfigId')

        if m.get('IsActive') is not None:
            self.is_active = m.get('IsActive')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.GetChainResponseBodyChainConfigNodes()
                self.nodes.append(temp_model.from_map(k1))

        self.routers = []
        if m.get('Routers') is not None:
            for k1 in m.get('Routers'):
                temp_model = main_models.GetChainResponseBodyChainConfigRouters()
                self.routers.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetChainResponseBodyChainConfigRouters(DaraModel):
    def __init__(
        self,
        from_: main_models.GetChainResponseBodyChainConfigRoutersFrom_ = None,
        to: main_models.GetChainResponseBodyChainConfigRoutersTo = None,
    ):
        # source edge zone
        self.from_ = from_
        # destination edge zone
        self.to = to

    def validate(self):
        if self.from_:
            self.from_.validate()
        if self.to:
            self.to.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_.to_map()

        if self.to is not None:
            result['To'] = self.to.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            temp_model = main_models.GetChainResponseBodyChainConfigRoutersFrom_()
            self.from_ = temp_model.from_map(m.get('From'))

        if m.get('To') is not None:
            temp_model = main_models.GetChainResponseBodyChainConfigRoutersTo()
            self.to = temp_model.from_map(m.get('To'))

        return self

class GetChainResponseBodyChainConfigRoutersTo(DaraModel):
    def __init__(
        self,
        node_name: str = None,
    ):
        # destination edge zone name
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_name is not None:
            result['NodeName'] = self.node_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        return self

class GetChainResponseBodyChainConfigRoutersFrom(DaraModel):
    def __init__(
        self,
        node_name: str = None,
    ):
        # source edge zone name
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_name is not None:
            result['NodeName'] = self.node_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        return self

class GetChainResponseBodyChainConfigNodes(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        node_config: main_models.GetChainResponseBodyChainConfigNodesNodeConfig = None,
        node_name: str = None,
    ):
        # Indicates whether to enable the delivery chain edge zone. Valid values:
        # 
        # - `true`: Enable the delivery chain edge zone.
        # 
        # - `false`: Do not enable the delivery chain edge zone.
        self.enable = enable
        # Delivery chain edge zone configuration
        self.node_config = node_config
        # Delivery chain edge zone name
        self.node_name = node_name

    def validate(self):
        if self.node_config:
            self.node_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.node_config is not None:
            result['NodeConfig'] = self.node_config.to_map()

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('NodeConfig') is not None:
            temp_model = main_models.GetChainResponseBodyChainConfigNodesNodeConfig()
            self.node_config = temp_model.from_map(m.get('NodeConfig'))

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        return self

class GetChainResponseBodyChainConfigNodesNodeConfig(DaraModel):
    def __init__(
        self,
        deny_policy: main_models.GetChainResponseBodyChainConfigNodesNodeConfigDenyPolicy = None,
        retry: int = None,
        scan_engine: str = None,
        timeout: int = None,
    ):
        # Deny rules for scan nodes in the delivery chain
        self.deny_policy = deny_policy
        # Retry Count
        self.retry = retry
        # Scan engine for the delivery chain node  
        # 
        # - `SAS_SCAN_SERVICE`, Security Center scan engine (requires paid activation)  
        # - `ACR_SCAN_SERVICE`, ACR scan engine
        self.scan_engine = scan_engine
        # Timeout (in seconds)
        self.timeout = timeout

    def validate(self):
        if self.deny_policy:
            self.deny_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deny_policy is not None:
            result['DenyPolicy'] = self.deny_policy.to_map()

        if self.retry is not None:
            result['Retry'] = self.retry

        if self.scan_engine is not None:
            result['ScanEngine'] = self.scan_engine

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DenyPolicy') is not None:
            temp_model = main_models.GetChainResponseBodyChainConfigNodesNodeConfigDenyPolicy()
            self.deny_policy = temp_model.from_map(m.get('DenyPolicy'))

        if m.get('Retry') is not None:
            self.retry = m.get('Retry')

        if m.get('ScanEngine') is not None:
            self.scan_engine = m.get('ScanEngine')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class GetChainResponseBodyChainConfigNodesNodeConfigDenyPolicy(DaraModel):
    def __init__(
        self,
        action: str = None,
        baseline_list: str = None,
        issue_count: str = None,
        issue_level: str = None,
        issue_list: str = None,
        logic: str = None,
        malicious_list: str = None,
    ):
        # Deny action. Valid values:
        # 
        # - `BLOCK`: Block further execution of the delivery chain
        # 
        # - `BLOCK_RETAG`: Block overwriting and pushing image tags
        # 
        # - `BLOCK_DELETE_TAG`: Block deleting image tags
        self.action = action
        # Collection of baseline samples to block. Separate multiple baseline sample names with commas.
        self.baseline_list = baseline_list
        # Number of scanned vulnerabilities that triggers a block
        self.issue_count = issue_count
        # The vulnerability Level at which blocking is triggered during a scan
        self.issue_level = issue_level
        # Collection of CVE vulnerabilities to block. Separate multiple CVE vulnerability names with commas.
        self.issue_list = issue_list
        # The logic that triggers blocking upon scan detection
        self.logic = logic
        # The collection of malicious samples to block, with multiple sample names separated by commas
        self.malicious_list = malicious_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.baseline_list is not None:
            result['BaselineList'] = self.baseline_list

        if self.issue_count is not None:
            result['IssueCount'] = self.issue_count

        if self.issue_level is not None:
            result['IssueLevel'] = self.issue_level

        if self.issue_list is not None:
            result['IssueList'] = self.issue_list

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.malicious_list is not None:
            result['MaliciousList'] = self.malicious_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('BaselineList') is not None:
            self.baseline_list = m.get('BaselineList')

        if m.get('IssueCount') is not None:
            self.issue_count = m.get('IssueCount')

        if m.get('IssueLevel') is not None:
            self.issue_level = m.get('IssueLevel')

        if m.get('IssueList') is not None:
            self.issue_list = m.get('IssueList')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('MaliciousList') is not None:
            self.malicious_list = m.get('MaliciousList')

        return self

