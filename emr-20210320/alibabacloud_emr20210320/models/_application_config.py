# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplicationConfig(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
        config_scope: str = None,
        node_group_id: str = None,
        node_group_name: str = None,
    ):
        # The name of the application. You can view the application names of each EMR version on the cluster creation page in the EMR console.
        # 
        # This parameter is required.
        self.application_name = application_name
        # The name of the configuration file.
        # 
        # This parameter is required.
        self.config_file_name = config_file_name
        # The key of the configuration item.
        # 
        # This parameter is required.
        self.config_item_key = config_item_key
        # The value of the configuration item.
        self.config_item_value = config_item_value
        # The level at which you want to apply the configurations. Valid values:
        # 
        # *   CLUSTER
        # *   NODE_GROUP
        # 
        # Default value: CLUSTER.
        self.config_scope = config_scope
        # The node group ID. This parameter takes effect only when the ConfigScope parameter is set to NODE_GROUP. The NodeGroupId parameter has a higher priority than the NodeGroupName parameter.
        self.node_group_id = node_group_id
        # The name of the node group. This parameter takes effect only when the ConfigScope parameter is set to NODE_GROUP and the NodeGroupId parameter is not configured.
        self.node_group_name = node_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.config_file_name is not None:
            result['ConfigFileName'] = self.config_file_name

        if self.config_item_key is not None:
            result['ConfigItemKey'] = self.config_item_key

        if self.config_item_value is not None:
            result['ConfigItemValue'] = self.config_item_value

        if self.config_scope is not None:
            result['ConfigScope'] = self.config_scope

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ConfigFileName') is not None:
            self.config_file_name = m.get('ConfigFileName')

        if m.get('ConfigItemKey') is not None:
            self.config_item_key = m.get('ConfigItemKey')

        if m.get('ConfigItemValue') is not None:
            self.config_item_value = m.get('ConfigItemValue')

        if m.get('ConfigScope') is not None:
            self.config_scope = m.get('ConfigScope')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        return self

