# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyMaskingRulesRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        default_algo: str = None,
        enable: str = None,
        interface_version: str = None,
        masking_algo: str = None,
        rule_config: str = None,
        rule_name: str = None,
        rule_name_list: str = None,
        rule_version: str = None,
    ):
        # The ID of the cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of the clusters that belong to your Alibaba Cloud account, such as cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.default_algo = default_algo
        # Specifies whether to enable the specified masking rule. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # > This parameter is valid only when the `RuleNameList` parameter is specfied.
        self.enable = enable
        self.interface_version = interface_version
        self.masking_algo = masking_algo
        # The parameter that is used to specify the masking rule that you want to modify and the value in the JSON format. All parameter values are of the string type. Example: `{"auto": {"databases": ["db1"], "tables": ["tb1"], "columns": ["c1,c2"] }, "description": "This rule will be applied to the columns c1 and c2 in table t1", "enabled": true, "applies_to": ["user"]}`. Where,
        # 
        # *   `"auto"`: specifies that the dynamic masking algorithm is supported. This parameter is required.
        # *   `"databases"`: Optional. The names of databases to which the masking rule is applied. Separate the names with commas (,). If you leave this parameter empty, the masking rule applies to all databases in the cluster.
        # *   `"tables"`: Optional. The names of tables to which the masking rule is applied. Separate the names with commas (,). If you leave this parameter empty, the rule applies to all tables in the cluster.
        # *   `"columns"`: Required. The names of fields to which the masking rule is applied. Separate the names with commas (,).
        # *   `"description"`: Optional. The description of the masking rule. The description is up to 64 characters in length.
        # *   `"enabled"`: Required. Specifies whether to enable the masking rule. Valid values: **true** (enable) and **false** (disable).
        # *   `"applies_to"`: The names of database accounts to which the masking rule is applied. Separate the names with commas (,).
        # *   `"exempted"`: The names of database accounts to which the masking rule is not applied. Separate the names with commas (,).
        # 
        # > 
        # 
        # *   If you specify `RuleName`, `RuleConfig` parameter is required.
        # 
        # *   You need to select either `"applies_to"` or `"exempted"`.
        self.rule_config = rule_config
        # The name of the data masking rule. You can specify only one rule name at a time.
        # 
        # > 
        # 
        # *   You can call the [DescribeMaskingRules](https://help.aliyun.com/document_detail/212573.html) operation to query the details of all masking rules for a specified cluster, such as the names of the masking rules.
        # 
        # *   If the rule name does not exist in the cluster, the system automatically creates a masking rule based on the name and the value of `RuleConfig`.
        self.rule_name = rule_name
        # The list of masking rule names. You can specify one or more masking rules at a time. Separate the masking rule names with commas (,).
        # 
        # > You must specify either the `RuleName` or `RuleNameList` parameter.
        self.rule_name_list = rule_name_list
        # The version of the masking rule. Default value: v1. Valid values:
        # 
        # *   v1
        # *   v2
        self.rule_version = rule_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.default_algo is not None:
            result['DefaultAlgo'] = self.default_algo

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.interface_version is not None:
            result['InterfaceVersion'] = self.interface_version

        if self.masking_algo is not None:
            result['MaskingAlgo'] = self.masking_algo

        if self.rule_config is not None:
            result['RuleConfig'] = self.rule_config

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_name_list is not None:
            result['RuleNameList'] = self.rule_name_list

        if self.rule_version is not None:
            result['RuleVersion'] = self.rule_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DefaultAlgo') is not None:
            self.default_algo = m.get('DefaultAlgo')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('InterfaceVersion') is not None:
            self.interface_version = m.get('InterfaceVersion')

        if m.get('MaskingAlgo') is not None:
            self.masking_algo = m.get('MaskingAlgo')

        if m.get('RuleConfig') is not None:
            self.rule_config = m.get('RuleConfig')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleNameList') is not None:
            self.rule_name_list = m.get('RuleNameList')

        if m.get('RuleVersion') is not None:
            self.rule_version = m.get('RuleVersion')

        return self

