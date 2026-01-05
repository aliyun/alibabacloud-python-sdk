# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableFirewallRulesRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        enable: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        rule_name_list: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to enable or disable the specified firewall rules. Valid values:
        # 
        # *   **true**: enables the specified firewall rules.
        # *   **false**: disables the specified firewall rules.
        # 
        # > This parameter is valid only when you specify the **RuleNameList** parameter.
        self.enable = enable
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the firewall rule that you want to enable for the cluster. You can specify multiple firewall rules at a time. Separate multiple rules with commas (,).
        # 
        # > You can call the **DescribeFirewallRules** operation to query the details of all firewall rules that are applicable to a cluster, such as rule names.
        # 
        # This parameter is required.
        self.rule_name_list = rule_name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.rule_name_list is not None:
            result['RuleNameList'] = self.rule_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RuleNameList') is not None:
            self.rule_name_list = m.get('RuleNameList')

        return self

