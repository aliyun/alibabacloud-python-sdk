# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class CreateNetTestTaskRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        comm_test: main_models.CreateNetTestTaskRequestCommTest = None,
        delay_test: main_models.CreateNetTestTaskRequestDelayTest = None,
        net_test_type: str = None,
        network_mode: str = None,
        port: str = None,
        traffic_test: main_models.CreateNetTestTaskRequestTrafficTest = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # Specify when NetTestType is CommTest.
        self.comm_test = comm_test
        # Specify when NetTestType is DelayTest.
        self.delay_test = delay_test
        # The type of the network test. Valid values: DelayTest, TrafficTest, and CommTest.
        self.net_test_type = net_test_type
        # The network mode.
        self.network_mode = network_mode
        # The port number.
        self.port = port
        # If the TrafficModel is Fullmesh, leave this parameter empty.
        self.traffic_test = traffic_test

    def validate(self):
        if self.comm_test:
            self.comm_test.validate()
        if self.delay_test:
            self.delay_test.validate()
        if self.traffic_test:
            self.traffic_test.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.comm_test is not None:
            result['CommTest'] = self.comm_test.to_map()

        if self.delay_test is not None:
            result['DelayTest'] = self.delay_test.to_map()

        if self.net_test_type is not None:
            result['NetTestType'] = self.net_test_type

        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode

        if self.port is not None:
            result['Port'] = self.port

        if self.traffic_test is not None:
            result['TrafficTest'] = self.traffic_test.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CommTest') is not None:
            temp_model = main_models.CreateNetTestTaskRequestCommTest()
            self.comm_test = temp_model.from_map(m.get('CommTest'))

        if m.get('DelayTest') is not None:
            temp_model = main_models.CreateNetTestTaskRequestDelayTest()
            self.delay_test = temp_model.from_map(m.get('DelayTest'))

        if m.get('NetTestType') is not None:
            self.net_test_type = m.get('NetTestType')

        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('TrafficTest') is not None:
            temp_model = main_models.CreateNetTestTaskRequestTrafficTest()
            self.traffic_test = temp_model.from_map(m.get('TrafficTest'))

        return self

class CreateNetTestTaskRequestTrafficTest(DaraModel):
    def __init__(
        self,
        clients: List[main_models.CreateNetTestTaskRequestTrafficTestClients] = None,
        duration: int = None,
        gdr: bool = None,
        protocol: str = None,
        qp: int = None,
        servers: List[main_models.CreateNetTestTaskRequestTrafficTestServers] = None,
        traffic_model: str = None,
    ):
        # The client IDs.
        self.clients = clients
        # The running duration of the pipeline job. Unit: seconds.
        self.duration = duration
        # If the protocol is RDMA, enter True or False. If the protocol is TCP, leave this field empty.
        self.gdr = gdr
        # The network protocol, which can be RDMA or TCP.
        self.protocol = protocol
        # If the protocol is TCP, enter the number of concurrent connections. If the protocol is RDMA, enter the configured QP value.
        self.qp = qp
        # The services.
        self.servers = servers
        # The traffic model, which can be MTON or Fullmesh.
        self.traffic_model = traffic_model

    def validate(self):
        if self.clients:
            for v1 in self.clients:
                 if v1:
                    v1.validate()
        if self.servers:
            for v1 in self.servers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Clients'] = []
        if self.clients is not None:
            for k1 in self.clients:
                result['Clients'].append(k1.to_map() if k1 else None)

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.gdr is not None:
            result['GDR'] = self.gdr

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.qp is not None:
            result['QP'] = self.qp

        result['Servers'] = []
        if self.servers is not None:
            for k1 in self.servers:
                result['Servers'].append(k1.to_map() if k1 else None)

        if self.traffic_model is not None:
            result['TrafficModel'] = self.traffic_model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clients = []
        if m.get('Clients') is not None:
            for k1 in m.get('Clients'):
                temp_model = main_models.CreateNetTestTaskRequestTrafficTestClients()
                self.clients.append(temp_model.from_map(k1))

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('GDR') is not None:
            self.gdr = m.get('GDR')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('QP') is not None:
            self.qp = m.get('QP')

        self.servers = []
        if m.get('Servers') is not None:
            for k1 in m.get('Servers'):
                temp_model = main_models.CreateNetTestTaskRequestTrafficTestServers()
                self.servers.append(temp_model.from_map(k1))

        if m.get('TrafficModel') is not None:
            self.traffic_model = m.get('TrafficModel')

        return self

class CreateNetTestTaskRequestTrafficTestServers(DaraModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        node_id: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # The bonding of network interface card.
        self.bond = bond
        # The IP address of the node.
        self.ip = ip
        # The node ID.
        self.node_id = node_id
        # The resource ID.
        self.resource_id = resource_id
        # The name of the service.
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bond is not None:
            result['Bond'] = self.bond

        if self.ip is not None:
            result['IP'] = self.ip

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.server_name is not None:
            result['ServerName'] = self.server_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bond') is not None:
            self.bond = m.get('Bond')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')

        return self

class CreateNetTestTaskRequestTrafficTestClients(DaraModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        node_id: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # The bonding of network interface card.
        self.bond = bond
        # The IP address of the node.
        self.ip = ip
        # The node ID.
        self.node_id = node_id
        # The resource ID.
        self.resource_id = resource_id
        # The name of the service.
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bond is not None:
            result['Bond'] = self.bond

        if self.ip is not None:
            result['IP'] = self.ip

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.server_name is not None:
            result['ServerName'] = self.server_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bond') is not None:
            self.bond = m.get('Bond')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')

        return self

class CreateNetTestTaskRequestDelayTest(DaraModel):
    def __init__(
        self,
        hosts: List[main_models.CreateNetTestTaskRequestDelayTestHosts] = None,
    ):
        # The hosts of the test node.
        self.hosts = hosts

    def validate(self):
        if self.hosts:
            for v1 in self.hosts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Hosts'] = []
        if self.hosts is not None:
            for k1 in self.hosts:
                result['Hosts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k1 in m.get('Hosts'):
                temp_model = main_models.CreateNetTestTaskRequestDelayTestHosts()
                self.hosts.append(temp_model.from_map(k1))

        return self

class CreateNetTestTaskRequestDelayTestHosts(DaraModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        node_id: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # The bonding of network interface card.
        self.bond = bond
        # The IP address of the node.
        self.ip = ip
        # The node ID.
        self.node_id = node_id
        # The resource ID.
        self.resource_id = resource_id
        # The name of the service.
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bond is not None:
            result['Bond'] = self.bond

        if self.ip is not None:
            result['IP'] = self.ip

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.server_name is not None:
            result['ServerName'] = self.server_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bond') is not None:
            self.bond = m.get('Bond')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')

        return self

class CreateNetTestTaskRequestCommTest(DaraModel):
    def __init__(
        self,
        gpunum: int = None,
        hosts: List[main_models.CreateNetTestTaskRequestCommTestHosts] = None,
        model: str = None,
        type: str = None,
    ):
        # The number of GPUs.
        self.gpunum = gpunum
        # The host IDs.
        self.hosts = hosts
        # The communication library model.
        self.model = model
        # The CommTest type, which can be ACCL or NCCL.
        self.type = type

    def validate(self):
        if self.hosts:
            for v1 in self.hosts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gpunum is not None:
            result['GPUNum'] = self.gpunum

        result['Hosts'] = []
        if self.hosts is not None:
            for k1 in self.hosts:
                result['Hosts'].append(k1.to_map() if k1 else None)

        if self.model is not None:
            result['Model'] = self.model

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GPUNum') is not None:
            self.gpunum = m.get('GPUNum')

        self.hosts = []
        if m.get('Hosts') is not None:
            for k1 in m.get('Hosts'):
                temp_model = main_models.CreateNetTestTaskRequestCommTestHosts()
                self.hosts.append(temp_model.from_map(k1))

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateNetTestTaskRequestCommTestHosts(DaraModel):
    def __init__(
        self,
        ip: str = None,
        node_id: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # The IP address.
        self.ip = ip
        # The node ID.
        self.node_id = node_id
        # The resource ID.
        self.resource_id = resource_id
        # The name of the service.
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['IP'] = self.ip

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.server_name is not None:
            result['ServerName'] = self.server_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')

        return self

