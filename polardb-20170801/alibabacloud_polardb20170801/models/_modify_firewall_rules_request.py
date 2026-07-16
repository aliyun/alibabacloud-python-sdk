# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyFirewallRulesRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        rule_config: str = None,
        rule_name: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # A JSON string that contains the configuration parameters of the firewall rule to modify and their values. The parameter values are strings. Example: `{ "id": "test", "enabled": "true", "mode": "Defending", "users": { "applies_to": [] }, "endpoint": "[{"EndpointName":"pe-***************","EndpointType":"Cluster","DBEndpointDescription":"Cluster Endpoint"},{"EndpointName":"pe-***************","EndpointType":"Custom","DBEndpointDescription":"pc-***************"},{"EndpointName":"pe-***************","EndpointType":"Custom","DBEndpointDescription":"pc-***************"}]", "type": "BlackList", "sub_rules": [] }, "RuleName": "test" }`. The parameters are described as follows:
        # 
        # - `"id"`: Required. The name of the firewall rule.
        # 
        # - `"databases"`: Optional. The names of the databases to which the rule applies. You can specify multiple database names. Separate the names with commas (,). If you leave this parameter empty, the rule applies to all databases in the cluster.
        # 
        # - `"tables"`: Optional. The names of the tables to which the rule applies. You can specify multiple table names. Separate the names with commas (,). If you leave this parameter empty, the rule applies to all tables in the cluster.
        # 
        # - `"columns"`: Required. The names of the fields to which the rule applies. You can specify multiple field names. Separate the names with commas (,).
        # 
        # - `"description"`: Optional. The description of the data masking rule. The description can be up to 64 characters in length.
        # 
        # - `"enabled"`: Required. Specifies whether to enable or disable the data masking rule. Valid values: **true** (enable) and **false** (disable).
        # 
        # - `"applies_to"`: The names of the database accounts to which the rule applies. You can specify multiple database account names. Separate the names with commas (,).
        # 
        # - `"exempted"`: The names of the database accounts to which the rule does not apply. You can specify multiple database account names. Separate the names with commas (,).
        # 
        # > * If you specify the `RuleName` parameter, the `RuleConfig` parameter is required.
        # >
        # > * You must specify either `"applies_to"` or `"exempted"`.
        # 
        # This parameter is required.
        self.rule_config = rule_config
        # The name of the firewall rule. You can specify only one rule name at a time.
        # 
        # > - Call the [DescribeFirewallRules](https://help.aliyun.com/document_detail/212573.html) operation to query the details of all firewall rules for the target cluster, including the rule names.
        # >
        # > - If the specified rule name does not exist in the current cluster, the system automatically creates a new firewall rule based on the rule name and the value of `RuleConfig`.
        # 
        # This parameter is required.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.rule_config is not None:
            result['RuleConfig'] = self.rule_config

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RuleConfig') is not None:
            self.rule_config = m.get('RuleConfig')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

