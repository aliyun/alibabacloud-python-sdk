# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTairInstanceResponseBody(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        charge_type: str = None,
        config: str = None,
        connection_domain: str = None,
        connections: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: str = None,
        order_id: int = None,
        port: int = None,
        qps: int = None,
        region_id: str = None,
        request_id: str = None,
        task_id: str = None,
        zone_id: str = None,
    ):
        # The maximum bandwidth of the instance. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The billing method of the instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.charge_type = charge_type
        # The detailed configurations of the instance. The value is a JSON string. For more information about the parameters, see [Configure parameters](https://help.aliyun.com/document_detail/43885.html).
        self.config = config
        # The internal endpoint of the instance.
        self.connection_domain = connection_domain
        # The maximum number of connections to the instance.
        self.connections = connections
        # The ID of the instance.
        self.instance_id = instance_id
        # The instance name.
        # 
        # >  This parameter is returned only if the **InstanceName** parameter is specified in the request.
        self.instance_name = instance_name
        # The current status of the instance. The value is **Creating**.
        self.instance_status = instance_status
        # The order ID.
        self.order_id = order_id
        # The service port number of the instance.
        self.port = port
        # The maximum number of read and write operations that can be processed by the instance per second. The value is a theoretical value.
        self.qps = qps
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id
        # The zone ID.
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

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.config is not None:
            result['Config'] = self.config

        if self.connection_domain is not None:
            result['ConnectionDomain'] = self.connection_domain

        if self.connections is not None:
            result['Connections'] = self.connections

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.port is not None:
            result['Port'] = self.port

        if self.qps is not None:
            result['QPS'] = self.qps

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ConnectionDomain') is not None:
            self.connection_domain = m.get('ConnectionDomain')

        if m.get('Connections') is not None:
            self.connections = m.get('Connections')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('QPS') is not None:
            self.qps = m.get('QPS')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

