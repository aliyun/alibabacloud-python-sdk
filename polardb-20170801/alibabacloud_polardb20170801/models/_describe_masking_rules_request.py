# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMaskingRulesRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        interface_version: str = None,
        rule_name_list: str = None,
    ):
        # The ID of the cluster.
        # 
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the details of the clusters that belong to your Alibaba Cloud account, such as cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Queries data masking rules or encryption rules. Valid values:
        # 
        # v1: queries data masking rules. v2: queries data encryption rules.
        self.interface_version = interface_version
        # The name of the masking rule.
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

