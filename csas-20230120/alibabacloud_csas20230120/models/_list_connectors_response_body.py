# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListConnectorsResponseBody(DaraModel):
    def __init__(
        self,
        connectors: List[main_models.ListConnectorsResponseBodyConnectors] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        # List of Connectors.
        self.connectors = connectors
        # The ID of the current request.
        self.request_id = request_id
        # Total number of Connectors.
        self.total_num = total_num

    def validate(self):
        if self.connectors:
            for v1 in self.connectors:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Connectors'] = []
        if self.connectors is not None:
            for k1 in self.connectors:
                result['Connectors'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connectors = []
        if m.get('Connectors') is not None:
            for k1 in m.get('Connectors'):
                temp_model = main_models.ListConnectorsResponseBodyConnectors()
                self.connectors.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListConnectorsResponseBodyConnectors(DaraModel):
    def __init__(
        self,
        accelerate_status: str = None,
        applications: List[main_models.ListConnectorsResponseBodyConnectorsApplications] = None,
        cluster_ip: str = None,
        cluster_port: str = None,
        connector_clients: List[main_models.ListConnectorsResponseBodyConnectorsConnectorClients] = None,
        connector_id: str = None,
        create_time: str = None,
        name: str = None,
        region_id: str = None,
        status: str = None,
        switch_status: str = None,
        upgrade_time: main_models.ListConnectorsResponseBodyConnectorsUpgradeTime = None,
    ):
        # Whether to enable global acceleration. Values: 
        # - **Enabled**: Turn on. 
        # - **Disabled**: Turn off.
        self.accelerate_status = accelerate_status
        # Collection of associated internal network access applications.
        self.applications = applications
        # Cluster IP.
        self.cluster_ip = cluster_ip
        # Cluster port.
        self.cluster_port = cluster_port
        # Collection of deployed ConnectorClients.
        self.connector_clients = connector_clients
        # ConnectorID.
        self.connector_id = connector_id
        # Connector creation time.
        self.create_time = create_time
        # Connector name.
        self.name = name
        # Region ID.
        self.region_id = region_id
        # Connector connection status. Values:
        # - **Online**: Online.
        # - **Offline**: Offline.
        self.status = status
        # Connector instance status. Values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.switch_status = switch_status
        # Connector升级时间。
        self.upgrade_time = upgrade_time

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()
        if self.connector_clients:
            for v1 in self.connector_clients:
                 if v1:
                    v1.validate()
        if self.upgrade_time:
            self.upgrade_time.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerate_status is not None:
            result['AccelerateStatus'] = self.accelerate_status

        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

        if self.cluster_ip is not None:
            result['ClusterIP'] = self.cluster_ip

        if self.cluster_port is not None:
            result['ClusterPort'] = self.cluster_port

        result['ConnectorClients'] = []
        if self.connector_clients is not None:
            for k1 in self.connector_clients:
                result['ConnectorClients'].append(k1.to_map() if k1 else None)

        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status

        if self.upgrade_time is not None:
            result['UpgradeTime'] = self.upgrade_time.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateStatus') is not None:
            self.accelerate_status = m.get('AccelerateStatus')

        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.ListConnectorsResponseBodyConnectorsApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('ClusterIP') is not None:
            self.cluster_ip = m.get('ClusterIP')

        if m.get('ClusterPort') is not None:
            self.cluster_port = m.get('ClusterPort')

        self.connector_clients = []
        if m.get('ConnectorClients') is not None:
            for k1 in m.get('ConnectorClients'):
                temp_model = main_models.ListConnectorsResponseBodyConnectorsConnectorClients()
                self.connector_clients.append(temp_model.from_map(k1))

        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')

        if m.get('UpgradeTime') is not None:
            temp_model = main_models.ListConnectorsResponseBodyConnectorsUpgradeTime()
            self.upgrade_time = temp_model.from_map(m.get('UpgradeTime'))

        return self

class ListConnectorsResponseBodyConnectorsUpgradeTime(DaraModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        # End time.
        self.end = end
        # Start time.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class ListConnectorsResponseBodyConnectorsConnectorClients(DaraModel):
    def __init__(
        self,
        connection_status: str = None,
        dev_tag: str = None,
        hostname: str = None,
        public_ip: str = None,
    ):
        # Connection status between the ConnectorClient and ConnectorServer.
        self.connection_status = connection_status
        # Unique device identifier for the ConnectorClient.
        self.dev_tag = dev_tag
        # Hostname of the ConnectorClient.
        self.hostname = hostname
        # Public IP of the ConnectorClient.
        self.public_ip = public_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status

        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')

        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        return self

class ListConnectorsResponseBodyConnectorsApplications(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
    ):
        # Internal network access application ID.
        self.application_id = application_id
        # Internal network access application name.
        self.application_name = application_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        return self

