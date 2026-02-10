# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListClusterCnnfStatusDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListClusterCnnfStatusDetailResponseBodyData] = None,
        request_id: str = None,
    ):
        # An array that consists of the protection status of the container firewall.
        self.data = data
        # The ID of the request, which is used to locate and troubleshoot issues.
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
                temp_model = main_models.ListClusterCnnfStatusDetailResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListClusterCnnfStatusDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        installed: bool = None,
        instance_id: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        invalid_type: str = None,
        machine_name: str = None,
        machine_type: int = None,
        plugin_name: str = None,
        plugin_version: str = None,
        status: str = None,
        uuid: str = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # Indicates whether the container firewall plug-in is installed.
        self.installed = installed
        # The ID of the server.
        self.instance_id = instance_id
        # The public IP address of the associated instance.
        self.internet_ip = internet_ip
        # The private IP address of the associated instance.
        self.intranet_ip = intranet_ip
        # The cause why the plug-in is invalid. Valid values:
        # 
        # *   **PLUGIN_OFFLINE**: The plug-in is offline.
        # *   **PLUGIN_NOT_INSTALLED**: The plug-in is not installed.
        # *   **PLUGIN_INVALID_VERSION**: The version of the plug-in is invalid.
        self.invalid_type = invalid_type
        # The name of the server.
        self.machine_name = machine_name
        # The machine type of the instance. The value is fixed as **ecs**.
        self.machine_type = machine_type
        # The name of the plug-in. The value is fixed as **alinet**.
        self.plugin_name = plugin_name
        # The version of the plug-in.
        self.plugin_version = plugin_version
        # The online status of the plug-in. Valid values:
        # 
        # *   **false**: The plug-in is offline.
        # *   **true**: The plug-in is online.
        self.status = status
        # The UUID of the asset.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.installed is not None:
            result['Installed'] = self.installed

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.invalid_type is not None:
            result['InvalidType'] = self.invalid_type

        if self.machine_name is not None:
            result['MachineName'] = self.machine_name

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        if self.plugin_name is not None:
            result['PluginName'] = self.plugin_name

        if self.plugin_version is not None:
            result['PluginVersion'] = self.plugin_version

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Installed') is not None:
            self.installed = m.get('Installed')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('InvalidType') is not None:
            self.invalid_type = m.get('InvalidType')

        if m.get('MachineName') is not None:
            self.machine_name = m.get('MachineName')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        if m.get('PluginName') is not None:
            self.plugin_name = m.get('PluginName')

        if m.get('PluginVersion') is not None:
            self.plugin_version = m.get('PluginVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

