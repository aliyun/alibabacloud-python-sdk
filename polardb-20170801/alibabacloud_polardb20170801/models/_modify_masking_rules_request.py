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
        # The cluster ID.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of all clusters in your account, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The default algorithm.
        # 
        # > You must specify either MaskingAlgo or DefaultAIgo.
        self.default_algo = default_algo
        # Enables or disables the specified data masking rules. Valid values:
        # 
        # - **true**: enables the specified rules.
        # 
        # - **false**: disables the specified rules.
        # 
        # > This parameter applies only when the `RuleNameList` parameter is specified.
        self.enable = enable
        # The type of rule to modify. Valid values:
        # 
        # v1: Modifies a data masking rule.
        # v2: Modifies an encryption rule.
        self.interface_version = interface_version
        # The masking algorithm. Specify one or more algorithms and their parameters. Format: `[{ "name": "algorithm_name", "params": {"key": "value"} }]`
        self.masking_algo = masking_algo
        # A JSON string that specifies the rule configuration. Example: `{"auto": {"databases": ["db1"], "tables": ["tb1"], "columns": ["c1,c2"] }, "description": "This rule will be applied to the columns c1 and c2 in table t1", "enabled": true, "applies_to": ["user"]}`. The JSON string includes the following fields:
        # 
        # - `"auto"`: Required. The object that contains the configuration for the dynamic data masking algorithm.
        # 
        # - `"databases"`: Optional. The databases to which the rule applies. Separate multiple database names with a comma (,). If this parameter is omitted, the rule applies to all databases in the cluster.
        # 
        # - `"tables"`: Optional. The tables to which the rule applies. Separate multiple table names with a comma (,). If this parameter is omitted, the rule applies to all tables in the cluster.
        # 
        # - `"columns"`: Required. The columns to which the rule applies. Separate multiple column names with a comma (,).
        # 
        # - `"description"`: Optional. The rule description, up to 64 characters in length.
        # 
        # - `"enabled"`: Required. Specifies whether the data masking rule is enabled. Valid values: **true** (enabled) and **false** (disabled).
        # 
        # - `"applies_to"`: The database accounts to which the rule applies. Separate multiple account names with a comma (,).
        # 
        # - `"exempted"`: The database accounts that are exempt from the rule. Separate multiple account names with a comma (,).
        # 
        # > * If you specify the `RuleName` parameter, you must also specify the `RuleConfig` parameter.
        # >
        # > * You must specify either `"applies_to"` or `"exempted"`.
        self.rule_config = rule_config
        # The name of the data masking rule. You can specify only one rule name at a time.
        # 
        # > - You can call the [DescribeMaskingRules](https://help.aliyun.com/document_detail/212573.html) operation to query the details of all data masking rules in the target cluster, including rule names.
        # >
        # > - If a rule with the specified name does not exist, the system creates a new one based on the provided `RuleConfig`.
        self.rule_name = rule_name
        # A comma-separated list of data masking rule names.
        # 
        # > You must specify either the `RuleName` or `RuleNameList` parameter.
        self.rule_name_list = rule_name_list
        # The version of the data masking rule. Valid values:
        # 
        # - v1 (default)
        # 
        # - v2
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

