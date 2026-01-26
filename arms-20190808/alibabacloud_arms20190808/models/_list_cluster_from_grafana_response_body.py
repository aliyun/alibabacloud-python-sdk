# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListClusterFromGrafanaResponseBody(DaraModel):
    def __init__(
        self,
        prom_cluster_list: List[main_models.ListClusterFromGrafanaResponseBodyPromClusterList] = None,
        request_id: str = None,
    ):
        # The cluster information.
        self.prom_cluster_list = prom_cluster_list
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.prom_cluster_list:
            for v1 in self.prom_cluster_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PromClusterList'] = []
        if self.prom_cluster_list is not None:
            for k1 in self.prom_cluster_list:
                result['PromClusterList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prom_cluster_list = []
        if m.get('PromClusterList') is not None:
            for k1 in m.get('PromClusterList'):
                temp_model = main_models.ListClusterFromGrafanaResponseBodyPromClusterList()
                self.prom_cluster_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListClusterFromGrafanaResponseBodyPromClusterList(DaraModel):
    def __init__(
        self,
        agent_status: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        controller_id: str = None,
        create_time: int = None,
        extra: str = None,
        id: int = None,
        install_time: int = None,
        is_controller_installed: bool = None,
        last_heart_beat_time: int = None,
        node_num: int = None,
        options: str = None,
        plugins_json_array: str = None,
        region_id: str = None,
        state_json: str = None,
        update_time: int = None,
        user_id: str = None,
    ):
        # The status of the Prometheus agent on the cluster. Valid values:
        # 
        # *   INSTALL_FAILED: The Prometheus agent failed to be installed.
        # *   INSTALL_SUCCEED: The Prometheus agent was installed.
        # *   NOT_REGISTER: You have not registered an Alibaba Cloud account.
        self.agent_status = agent_status
        # The cluster ID.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The type of the cluster.
        self.cluster_type = cluster_type
        # The controller ID.
        self.controller_id = controller_id
        # The time when the dashboard was created.
        self.create_time = create_time
        # The extended fields. This parameter is a JSON string.
        self.extra = extra
        # The ID of a database in the cluster.
        self.id = id
        # The timestamp when the Prometheus agent was installed.
        self.install_time = install_time
        # Indicates whether the Prometheus agent was installed. Valid values:
        # 
        # *   true: The Prometheus agent was installed.
        # *   false: The Prometheus agent was not installed.
        self.is_controller_installed = is_controller_installed
        # The time when the last heartbeat was reported.
        self.last_heart_beat_time = last_heart_beat_time
        # The number of nodes.
        self.node_num = node_num
        # The custom parameter.
        self.options = options
        # The list of nodejsonar logs.
        self.plugins_json_array = plugins_json_array
        # The region ID.
        self.region_id = region_id
        # The information about applications deployed in the cluster.
        self.state_json = state_json
        # The time when the dashboard was updated.
        self.update_time = update_time
        # The ID of the Alibaba Cloud account to which the cluster belongs.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.controller_id is not None:
            result['ControllerId'] = self.controller_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.id is not None:
            result['Id'] = self.id

        if self.install_time is not None:
            result['InstallTime'] = self.install_time

        if self.is_controller_installed is not None:
            result['IsControllerInstalled'] = self.is_controller_installed

        if self.last_heart_beat_time is not None:
            result['LastHeartBeatTime'] = self.last_heart_beat_time

        if self.node_num is not None:
            result['NodeNum'] = self.node_num

        if self.options is not None:
            result['Options'] = self.options

        if self.plugins_json_array is not None:
            result['PluginsJsonArray'] = self.plugins_json_array

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.state_json is not None:
            result['StateJson'] = self.state_json

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('ControllerId') is not None:
            self.controller_id = m.get('ControllerId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')

        if m.get('IsControllerInstalled') is not None:
            self.is_controller_installed = m.get('IsControllerInstalled')

        if m.get('LastHeartBeatTime') is not None:
            self.last_heart_beat_time = m.get('LastHeartBeatTime')

        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('PluginsJsonArray') is not None:
            self.plugins_json_array = m.get('PluginsJsonArray')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StateJson') is not None:
            self.state_json = m.get('StateJson')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

