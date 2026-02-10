# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListClusterPluginInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListClusterPluginInfoResponseBodyData] = None,
        request_id: str = None,
    ):
        # The information about the plug-in.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListClusterPluginInfoResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListClusterPluginInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_status: str = None,
        node_plugin_info_list: List[main_models.ListClusterPluginInfoResponseBodyDataNodePluginInfoList] = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The status of the cluster. Valid values:
        # 
        # *   1: normal
        # *   2: abnormal
        # *   3: offline
        self.cluster_status = cluster_status
        # The plug-ins.
        self.node_plugin_info_list = node_plugin_info_list

    def validate(self):
        if self.node_plugin_info_list:
            for v1 in self.node_plugin_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status

        result['NodePluginInfoList'] = []
        if self.node_plugin_info_list is not None:
            for k1 in self.node_plugin_info_list:
                result['NodePluginInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')

        self.node_plugin_info_list = []
        if m.get('NodePluginInfoList') is not None:
            for k1 in m.get('NodePluginInfoList'):
                temp_model = main_models.ListClusterPluginInfoResponseBodyDataNodePluginInfoList()
                self.node_plugin_info_list.append(temp_model.from_map(k1))

        return self

class ListClusterPluginInfoResponseBodyDataNodePluginInfoList(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        installed: bool = None,
        machine_internet_ip: str = None,
        machine_intranet_ip: str = None,
        machine_name: str = None,
        machine_type: int = None,
        online: bool = None,
        plugin_name: str = None,
        plugin_version: str = None,
        uuid: str = None,
        instance_id: str = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_msg = error_msg
        # Indicates whether the plug-in is installed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.installed = installed
        # The public IP address of the server.
        self.machine_internet_ip = machine_internet_ip
        # The private IP address of the server.
        self.machine_intranet_ip = machine_intranet_ip
        # The name of the server.
        self.machine_name = machine_name
        # The type of the instance. Valid values include:
        # 
        # *   **ecs**: Elastic Compute Service (ECS) instance
        # *   **slb**: Server Load Balancer (SLB) instance
        self.machine_type = machine_type
        # Indicates whether the Security Center agent is online. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  If the Security Center agent of the server is offline, Security Center does not protect the server.
        self.online = online
        # The name of the plug-in.
        self.plugin_name = plugin_name
        # The version of the plug-in.
        self.plugin_version = plugin_version
        # The UUID of the server.
        self.uuid = uuid
        # The instance ID of the server.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.installed is not None:
            result['Installed'] = self.installed

        if self.machine_internet_ip is not None:
            result['MachineInternetIp'] = self.machine_internet_ip

        if self.machine_intranet_ip is not None:
            result['MachineIntranetIp'] = self.machine_intranet_ip

        if self.machine_name is not None:
            result['MachineName'] = self.machine_name

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        if self.online is not None:
            result['Online'] = self.online

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        if self.plugin_version is not None:
            result['PluginVersion'] = self.plugin_version

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('Installed') is not None:
            self.installed = m.get('Installed')

        if m.get('MachineInternetIp') is not None:
            self.machine_internet_ip = m.get('MachineInternetIp')

        if m.get('MachineIntranetIp') is not None:
            self.machine_intranet_ip = m.get('MachineIntranetIp')

        if m.get('MachineName') is not None:
            self.machine_name = m.get('MachineName')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        if m.get('PluginVersion') is not None:
            self.plugin_version = m.get('PluginVersion')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        return self

