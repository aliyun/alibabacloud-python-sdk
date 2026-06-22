# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class UpdateApplicationConfigsRequest(DaraModel):
    def __init__(
        self,
        application_configs: List[main_models.UpdateApplicationConfig] = None,
        application_name: str = None,
        cluster_id: str = None,
        config_action: str = None,
        config_scope: str = None,
        description: str = None,
        node_group_id: str = None,
        node_id: str = None,
        refresh_config: bool = None,
        region_id: str = None,
    ):
        # The list of application configurations.
        # 
        # This parameter is required.
        self.application_configs = application_configs
        # The application name.
        # 
        # This parameter is required.
        self.application_name = application_name
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The operation on the configuration items. Valid values:
        # 
        # - ADD: Adds configuration items.
        # 
        # - UPDATE: Updates configuration items.
        # 
        # - DELETE: Deletes configuration items.
        self.config_action = config_action
        # The scope of the configuration operation. Valid values:
        # 
        # - CLUSTER: The cluster level.
        # 
        # - NODE_GROUP: The node group level.
        self.config_scope = config_scope
        # The description.
        self.description = description
        # The node group ID.
        self.node_group_id = node_group_id
        # The node ID.
        self.node_id = node_id
        # Specifies whether to refresh the configurations.
        # The default value is true.
        self.refresh_config = refresh_config
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.application_configs:
            for v1 in self.application_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationConfigs'] = []
        if self.application_configs is not None:
            for k1 in self.application_configs:
                result['ApplicationConfigs'].append(k1.to_map() if k1 else None)

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.config_action is not None:
            result['ConfigAction'] = self.config_action

        if self.config_scope is not None:
            result['ConfigScope'] = self.config_scope

        if self.description is not None:
            result['Description'] = self.description

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.refresh_config is not None:
            result['RefreshConfig'] = self.refresh_config

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_configs = []
        if m.get('ApplicationConfigs') is not None:
            for k1 in m.get('ApplicationConfigs'):
                temp_model = main_models.UpdateApplicationConfig()
                self.application_configs.append(temp_model.from_map(k1))

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConfigAction') is not None:
            self.config_action = m.get('ConfigAction')

        if m.get('ConfigScope') is not None:
            self.config_scope = m.get('ConfigScope')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('RefreshConfig') is not None:
            self.refresh_config = m.get('RefreshConfig')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

