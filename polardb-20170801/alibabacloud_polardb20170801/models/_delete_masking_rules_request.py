# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMaskingRulesRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        interface_version: str = None,
        rule_name_list: str = None,
    ):
        # The cluster ID.
        # 
        # > For more information, see [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html).
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The type of rule to delete. Valid values:
        # 
        # v1: deletes data masking rules.
        # v2: deletes data encryption rules.
        self.interface_version = interface_version
        # The names of the data masking rules to delete. To delete multiple rules in a batch, separate the names with commas (,).
        # 
        # > For more information, see [DescribeMaskingRules](https://help.aliyun.com/document_detail/212573.html).
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

        if self.interface_version is not None:
            result['InterfaceVersion'] = self.interface_version

        if self.rule_name_list is not None:
            result['RuleNameList'] = self.rule_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('InterfaceVersion') is not None:
            self.interface_version = m.get('InterfaceVersion')

        if m.get('RuleNameList') is not None:
            self.rule_name_list = m.get('RuleNameList')

        return self

