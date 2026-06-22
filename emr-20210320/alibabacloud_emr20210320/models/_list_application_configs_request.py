# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApplicationConfigsRequest(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        cluster_id: str = None,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
        max_results: int = None,
        next_token: str = None,
        node_group_id: str = None,
        node_id: str = None,
        region_id: str = None,
    ):
        # The name of the application.
        self.application_name = application_name
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The name of the configuration file.
        self.config_file_name = config_file_name
        # The key of the configuration item.
        self.config_item_key = config_item_key
        # The value of the configuration item.
        self.config_item_value = config_item_value
        # The number of entries per page.
        self.max_results = max_results
        # The page number of the next page returned.
        self.next_token = next_token
        # The ID of the node group.
        self.node_group_id = node_group_id
        # The node ID.
        self.node_id = node_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.config_file_name is not None:
            result['ConfigFileName'] = self.config_file_name

        if self.config_item_key is not None:
            result['ConfigItemKey'] = self.config_item_key

        if self.config_item_value is not None:
            result['ConfigItemValue'] = self.config_item_value

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConfigFileName') is not None:
            self.config_file_name = m.get('ConfigFileName')

        if m.get('ConfigItemKey') is not None:
            self.config_item_key = m.get('ConfigItemKey')

        if m.get('ConfigItemValue') is not None:
            self.config_item_value = m.get('ConfigItemValue')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

