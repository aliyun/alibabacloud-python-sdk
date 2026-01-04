# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeGlobalAccelerationInstancesResponseBody(DaraModel):
    def __init__(
        self,
        global_acceleration_instances: main_models.DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the GA instances.
        self.global_acceleration_instances = global_acceleration_instances
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.global_acceleration_instances:
            self.global_acceleration_instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.global_acceleration_instances is not None:
            result['GlobalAccelerationInstances'] = self.global_acceleration_instances.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalAccelerationInstances') is not None:
            temp_model = main_models.DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstances()
            self.global_acceleration_instances = temp_model.from_map(m.get('GlobalAccelerationInstances'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstances(DaraModel):
    def __init__(
        self,
        global_acceleration_instance: List[main_models.DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstance] = None,
    ):
        self.global_acceleration_instance = global_acceleration_instance

    def validate(self):
        if self.global_acceleration_instance:
            for v1 in self.global_acceleration_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GlobalAccelerationInstance'] = []
        if self.global_acceleration_instance is not None:
            for k1 in self.global_acceleration_instance:
                result['GlobalAccelerationInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.global_acceleration_instance = []
        if m.get('GlobalAccelerationInstance') is not None:
            for k1 in m.get('GlobalAccelerationInstance'):
                temp_model = main_models.DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstance()
                self.global_acceleration_instance.append(temp_model.from_map(k1))

        return self

class DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstance(DaraModel):
    def __init__(
        self,
        acceleration_location: str = None,
        backend_servers: main_models.DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstanceBackendServers = None,
        bandwidth: str = None,
        bandwidth_type: str = None,
        charge_type: str = None,
        creation_time: str = None,
        description: str = None,
        expired_time: str = None,
        global_acceleration_instance_id: str = None,
        internet_charge_type: str = None,
        ip_address: str = None,
        name: str = None,
        public_ip_addresses: main_models.DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstancePublicIpAddresses = None,
        region_id: str = None,
        service_location: str = None,
        status: str = None,
    ):
        # The acceleration area of the GA instance.
        self.acceleration_location = acceleration_location
        # The details about the backend servers of the GA instance.
        self.backend_servers = backend_servers
        # The maximum bandwidth of the GA instance.
        self.bandwidth = bandwidth
        # The bandwidth type of the GA instance.
        # 
        # *   **Sharing**
        # *   **Exclusive** (default)
        self.bandwidth_type = bandwidth_type
        # The billing method of the GA instance.
        self.charge_type = charge_type
        # The time when the GA instance was created. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the GA instance.
        self.description = description
        # The time when the instance expires.
        self.expired_time = expired_time
        # The ID of the GA instance.
        self.global_acceleration_instance_id = global_acceleration_instance_id
        # The billing method of the GA instance.
        self.internet_charge_type = internet_charge_type
        # The public IP address of the dedicated GA instance.
        self.ip_address = ip_address
        # The name of the GA instance.
        self.name = name
        # The public IP address.
        self.public_ip_addresses = public_ip_addresses
        # The region ID of the GA instance.
        self.region_id = region_id
        # The service area of the GA instance.
        self.service_location = service_location
        # The status of the GA instance.
        # 
        # *   **Available**
        # *   **Inuse**
        # *   **Associating**
        # *   **Unassociating**
        self.status = status

    def validate(self):
        if self.backend_servers:
            self.backend_servers.validate()
        if self.public_ip_addresses:
            self.public_ip_addresses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acceleration_location is not None:
            result['AccelerationLocation'] = self.acceleration_location

        if self.backend_servers is not None:
            result['BackendServers'] = self.backend_servers.to_map()

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.global_acceleration_instance_id is not None:
            result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.name is not None:
            result['Name'] = self.name

        if self.public_ip_addresses is not None:
            result['PublicIpAddresses'] = self.public_ip_addresses.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerationLocation') is not None:
            self.acceleration_location = m.get('AccelerationLocation')

        if m.get('BackendServers') is not None:
            temp_model = main_models.DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstanceBackendServers()
            self.backend_servers = temp_model.from_map(m.get('BackendServers'))

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('GlobalAccelerationInstanceId') is not None:
            self.global_acceleration_instance_id = m.get('GlobalAccelerationInstanceId')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PublicIpAddresses') is not None:
            temp_model = main_models.DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstancePublicIpAddresses()
            self.public_ip_addresses = temp_model.from_map(m.get('PublicIpAddresses'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstancePublicIpAddresses(DaraModel):
    def __init__(
        self,
        public_ip_address: List[main_models.DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstancePublicIpAddressesPublicIpAddress] = None,
    ):
        self.public_ip_address = public_ip_address

    def validate(self):
        if self.public_ip_address:
            for v1 in self.public_ip_address:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PublicIpAddress'] = []
        if self.public_ip_address is not None:
            for k1 in self.public_ip_address:
                result['PublicIpAddress'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.public_ip_address = []
        if m.get('PublicIpAddress') is not None:
            for k1 in m.get('PublicIpAddress'):
                temp_model = main_models.DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstancePublicIpAddressesPublicIpAddress()
                self.public_ip_address.append(temp_model.from_map(k1))

        return self

class DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstancePublicIpAddressesPublicIpAddress(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        ip_address: str = None,
    ):
        # The ID of the public IP address of the GA instance.
        self.allocation_id = allocation_id
        # The public IP address of the GA instance.
        self.ip_address = ip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        return self

class DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstanceBackendServers(DaraModel):
    def __init__(
        self,
        backend_server: List[main_models.DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstanceBackendServersBackendServer] = None,
    ):
        self.backend_server = backend_server

    def validate(self):
        if self.backend_server:
            for v1 in self.backend_server:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackendServer'] = []
        if self.backend_server is not None:
            for k1 in self.backend_server:
                result['BackendServer'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backend_server = []
        if m.get('BackendServer') is not None:
            for k1 in m.get('BackendServer'):
                temp_model = main_models.DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstanceBackendServersBackendServer()
                self.backend_server.append(temp_model.from_map(k1))

        return self

class DescribeGlobalAccelerationInstancesResponseBodyGlobalAccelerationInstancesGlobalAccelerationInstanceBackendServersBackendServer(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        server_id: str = None,
        server_ip_address: str = None,
        server_type: str = None,
    ):
        # The region where the backend servers are deployed.
        self.region_id = region_id
        # The ID of the backend server.
        self.server_id = server_id
        # The IP address of the backend server.
        self.server_ip_address = server_ip_address
        # The type of the backend server.
        # 
        # *   **EcsInstance**: Elastic Compute Service (ECS) instance
        # *   **SlbInstance**: Server Load Balancer (SLB) instance
        self.server_type = server_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.server_ip_address is not None:
            result['ServerIpAddress'] = self.server_ip_address

        if self.server_type is not None:
            result['ServerType'] = self.server_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('ServerIpAddress') is not None:
            self.server_ip_address = m.get('ServerIpAddress')

        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')

        return self

