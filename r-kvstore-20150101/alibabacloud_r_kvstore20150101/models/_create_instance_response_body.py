# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceResponseBody(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        capacity: int = None,
        charge_type: str = None,
        config: str = None,
        connection_domain: str = None,
        connections: int = None,
        end_time: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        network_type: str = None,
        node_type: str = None,
        order_id: int = None,
        port: int = None,
        private_ip_addr: str = None,
        qps: int = None,
        region_id: str = None,
        request_id: str = None,
        user_name: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The maximum bandwidth of the instance. Unit: MB/s.
        self.bandwidth = bandwidth
        # The storage capacity of the instance. Unit: MB.
        self.capacity = capacity
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type
        # The configurations of the instance.
        self.config = config
        # The internal endpoint of the instance.
        self.connection_domain = connection_domain
        # The maximum number of connections supported by the instance.
        self.connections = connections
        # The time when the subscription expires. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The GUID of the instance.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The state of the instance. The return value is Creating.
        self.instance_status = instance_status
        # The network type of the instance. Valid values:
        # 
        # *   **CLASSIC**: classic network
        # *   **VPC**: VPC
        self.network_type = network_type
        # The node type. Valid values:
        # 
        # *   **STAND_ALONE**: standalone
        # *   **MASTER_SLAVE**: master-replica
        self.node_type = node_type
        # The ID of the order.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The port number that is used to connect to the instance.
        self.port = port
        # The private IP address of the instance.
        self.private_ip_addr = private_ip_addr
        # The expected maximum queries per second (QPS).
        self.qps = qps
        # The region ID of the instance.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The username that is used to connect to the instance. By default, Tair (Redis OSS-compatible) provides a username that is named after the instance ID.
        self.user_name = user_name
        # The ID of the vSwitch to which the instance is connected.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.config is not None:
            result['Config'] = self.config

        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain

        if self.connections is not None:
            result['Connections'] = self.connections

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.port is not None:
            result['Port'] = self.port

        if self.private_ip_addr is not None:
            result['PrivateIpAddr'] = self.private_ip_addr

        if self.qps is not None:
            result['QPS'] = self.qps

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')

        if m.get('Connections') is not None:
            self.connections = m.get('Connections')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('PrivateIpAddr') is not None:
            self.private_ip_addr = m.get('PrivateIpAddr')

        if m.get('QPS') is not None:
            self.qps = m.get('QPS')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

