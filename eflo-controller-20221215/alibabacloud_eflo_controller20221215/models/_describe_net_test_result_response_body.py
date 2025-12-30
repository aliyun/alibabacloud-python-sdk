# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class DescribeNetTestResultResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        comm_test: main_models.DescribeNetTestResultResponseBodyCommTest = None,
        creation_time: str = None,
        delay_test: main_models.DescribeNetTestResultResponseBodyDelayTest = None,
        finished_time: str = None,
        net_test_type: str = None,
        port: str = None,
        request_id: str = None,
        result_detial: str = None,
        status: str = None,
        test_id: str = None,
        traffic_test: main_models.DescribeNetTestResultResponseBodyTrafficTest = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # Specify when NetTestType is CommTest.
        self.comm_test = comm_test
        # create time
        self.creation_time = creation_time
        # Fill in when the network test type is a delay test.
        self.delay_test = delay_test
        # finish time
        self.finished_time = finished_time
        # The type of the network test.
        self.net_test_type = net_test_type
        # Test port number.
        self.port = port
        # The request ID.
        self.request_id = request_id
        # result detail
        self.result_detial = result_detial
        # status of session
        self.status = status
        # The ID of the test task. The unique identifier of a network test task.
        self.test_id = test_id
        # Fill in when the network test type is a traffic test.
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

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.delay_test is not None:
            result['DelayTest'] = self.delay_test.to_map()

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.net_test_type is not None:
            result['NetTestType'] = self.net_test_type

        if self.port is not None:
            result['Port'] = self.port

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_detial is not None:
            result['ResultDetial'] = self.result_detial

        if self.status is not None:
            result['Status'] = self.status

        if self.test_id is not None:
            result['TestId'] = self.test_id

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
            temp_model = main_models.DescribeNetTestResultResponseBodyCommTest()
            self.comm_test = temp_model.from_map(m.get('CommTest'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DelayTest') is not None:
            temp_model = main_models.DescribeNetTestResultResponseBodyDelayTest()
            self.delay_test = temp_model.from_map(m.get('DelayTest'))

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('NetTestType') is not None:
            self.net_test_type = m.get('NetTestType')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultDetial') is not None:
            self.result_detial = m.get('ResultDetial')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TestId') is not None:
            self.test_id = m.get('TestId')

        if m.get('TrafficTest') is not None:
            temp_model = main_models.DescribeNetTestResultResponseBodyTrafficTest()
            self.traffic_test = temp_model.from_map(m.get('TrafficTest'))

        return self

class DescribeNetTestResultResponseBodyTrafficTest(DaraModel):
    def __init__(
        self,
        clients: List[main_models.DescribeNetTestResultResponseBodyTrafficTestClients] = None,
        duration: int = None,
        gdr: str = None,
        protocol: str = None,
        qp: int = None,
        servers: List[main_models.DescribeNetTestResultResponseBodyTrafficTestServers] = None,
        traffic_model: str = None,
    ):
        # All clients information
        self.clients = clients
        # Call duration, in seconds.
        self.duration = duration
        # When the protocol is RDMA, fill in True/False,
        # when the protocol is TCP, this field is empty.
        self.gdr = gdr
        # Network protocol, either RDMA or TCP.
        self.protocol = protocol
        # When the protocol is TCP, fill in the number of concurrent connections; when the protocol is RDMA, fill in the configured QP value.
        self.qp = qp
        # Servers infomation.
        self.servers = servers
        # Traffic model, either MTON or Fullmesh.
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
                temp_model = main_models.DescribeNetTestResultResponseBodyTrafficTestClients()
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
                temp_model = main_models.DescribeNetTestResultResponseBodyTrafficTestServers()
                self.servers.append(temp_model.from_map(k1))

        if m.get('TrafficModel') is not None:
            self.traffic_model = m.get('TrafficModel')

        return self

class DescribeNetTestResultResponseBodyTrafficTestServers(DaraModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # Network interface bond port
        self.bond = bond
        # The IP address.
        self.ip = ip
        # The resource ID.
        self.resource_id = resource_id
        # Service name.
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

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')

        return self

class DescribeNetTestResultResponseBodyTrafficTestClients(DaraModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # Network interface bond port
        self.bond = bond
        # IP address.
        self.ip = ip
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

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')

        return self

class DescribeNetTestResultResponseBodyDelayTest(DaraModel):
    def __init__(
        self,
        hosts: List[main_models.DescribeNetTestResultResponseBodyDelayTestHosts] = None,
    ):
        # All hosts infomation
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
                temp_model = main_models.DescribeNetTestResultResponseBodyDelayTestHosts()
                self.hosts.append(temp_model.from_map(k1))

        return self

class DescribeNetTestResultResponseBodyDelayTestHosts(DaraModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # The bonding of network interface card.
        self.bond = bond
        # The IP address.
        self.ip = ip
        # The resource ID.
        self.resource_id = resource_id
        # Service name.
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

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')

        return self

class DescribeNetTestResultResponseBodyCommTest(DaraModel):
    def __init__(
        self,
        gpunum: str = None,
        hosts: List[main_models.DescribeNetTestResultResponseBodyCommTestHosts] = None,
        model: str = None,
        type: str = None,
    ):
        # Number of GPUs
        self.gpunum = gpunum
        # All hosts infomation
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
                temp_model = main_models.DescribeNetTestResultResponseBodyCommTestHosts()
                self.hosts.append(temp_model.from_map(k1))

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeNetTestResultResponseBodyCommTestHosts(DaraModel):
    def __init__(
        self,
        ip: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # The IP address.
        self.ip = ip
        # The resource ID.
        self.resource_id = resource_id
        # Service name.
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

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.server_name is not None:
            result['ServerName'] = self.server_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')

        return self

