# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class CreateSynchronizationJobRequest(DaraModel):
    def __init__(
        self,
        destination_endpoint: main_models.CreateSynchronizationJobRequestDestinationEndpoint = None,
        source_endpoint: main_models.CreateSynchronizationJobRequestSourceEndpoint = None,
        account_id: str = None,
        client_token: str = None,
        dbinstance_count: int = None,
        dest_region: str = None,
        owner_id: str = None,
        pay_type: str = None,
        period: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_region: str = None,
        synchronization_job_class: str = None,
        topology: str = None,
        used_time: int = None,
        network_type: str = None,
    ):
        self.destination_endpoint = destination_endpoint
        self.source_endpoint = source_endpoint
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future.
        self.account_id = account_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The **ClientToken** parameter can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # If you set the **SourceEndpoint.InstanceType** parameter to **DRDS**, you must specify the DBInstanceCount parameter. This parameter specifies the number of private RDS instances attached to the source PolarDB-X instance. Default value: **1**.
        self.dbinstance_count = dbinstance_count
        # The ID of the region where the destination database resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # >  If the **SourceRegion** parameter is set to the China (Hong Kong) region or a region outside the Chinese mainland, you must set the DestRegion parameter to the same region ID.
        # 
        # This parameter is required.
        self.dest_region = dest_region
        self.owner_id = owner_id
        # The billing method of the data synchronization instance.
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid** (default value): pay-as-you-go
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The billing cycle of the subscription instance. Valid values:
        # 
        # *   **Year**
        # *   **Month**
        # 
        # >  You must specify this parameter only if you set the PayType parameter to **PrePaid**.
        self.period = period
        # The ID of the region where the data synchronization instance resides. The region ID is the same as the value of the **DestRegion** parameter.
        self.region_id = region_id
        # Resource GroupId
        self.resource_group_id = resource_group_id
        # The ID of the region where the source database resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # This parameter is required.
        self.source_region = source_region
        # The specification of the data synchronization instance. Valid values: **micro**, **small**, **medium**, and **large**.
        # 
        # >  For more information about the test performance of each specification, see [Specifications of data synchronization instances](https://help.aliyun.com/document_detail/26605.html).
        # 
        # This parameter is required.
        self.synchronization_job_class = synchronization_job_class
        # The synchronization topology. Valid values:
        # 
        # *   **oneway**: one-way synchronization
        # *   **bidirectional**: two-way synchronization
        # 
        # > 
        # *   The default value is **oneway**.
        # *   This parameter can be set to **bidirectional** only when the **SourceEndpoint.InstanceType** and **DestinationEndpoint.InstanceType** parameters are set to **MySQL**, **PolarDB**, or **Redis**.
        self.topology = topology
        # The subscription length.
        # 
        # *   If the billing cycle is **Year**, the value range is **1 to 5**.
        # *   If the billing cycle is **Month**, the value range is **1 to 60**.
        # 
        # >  You must specify this parameter only if you set the PayType parameter to **PrePaid**.
        self.used_time = used_time
        # The network type. Valid value: **Intranet**, which indicates virtual private cloud (VPC).
        self.network_type = network_type

    def validate(self):
        if self.destination_endpoint:
            self.destination_endpoint.validate()
        if self.source_endpoint:
            self.source_endpoint.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_endpoint is not None:
            result['DestinationEndpoint'] = self.destination_endpoint.to_map()

        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_count is not None:
            result['DBInstanceCount'] = self.dbinstance_count

        if self.dest_region is not None:
            result['DestRegion'] = self.dest_region

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_region is not None:
            result['SourceRegion'] = self.source_region

        if self.synchronization_job_class is not None:
            result['SynchronizationJobClass'] = self.synchronization_job_class

        if self.topology is not None:
            result['Topology'] = self.topology

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.network_type is not None:
            result['networkType'] = self.network_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationEndpoint') is not None:
            temp_model = main_models.CreateSynchronizationJobRequestDestinationEndpoint()
            self.destination_endpoint = temp_model.from_map(m.get('DestinationEndpoint'))

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.CreateSynchronizationJobRequestSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceCount') is not None:
            self.dbinstance_count = m.get('DBInstanceCount')

        if m.get('DestRegion') is not None:
            self.dest_region = m.get('DestRegion')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')

        if m.get('SynchronizationJobClass') is not None:
            self.synchronization_job_class = m.get('SynchronizationJobClass')

        if m.get('Topology') is not None:
            self.topology = m.get('Topology')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('networkType') is not None:
            self.network_type = m.get('networkType')

        return self

class CreateSynchronizationJobRequestSourceEndpoint(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        # The instance type of the source database. Valid values:
        # 
        # *   **MySQL**: ApsaraDB RDS for MySQL instance or self-managed MySQL database
        # *   **PolarDB**: PolarDB for MySQL cluster or PolarDB O Edition cluster
        # *   **Redis**: Redis database
        # *   **DRDS**: PolarDB-X instance V1.0
        # 
        # > 
        # *   Default value: **MySQL**.
        # *   For more information about the supported source and destination databases, see [Database types, initial synchronization types, and synchronization topologies](https://help.aliyun.com/document_detail/130744.html).
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

class CreateSynchronizationJobRequestDestinationEndpoint(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        # The instance type of the destination database. Valid values:
        # 
        # *   **MySQL**: ApsaraDB RDS for MySQL instance or self-managed MySQL database
        # *   **PolarDB**: PolarDB for MySQL cluster or PolarDB O Edition cluster
        # *   **Redis**: Redis database
        # *   **MaxCompute**: MaxCompute project
        # 
        # > 
        # *   Default value: **MySQL**.
        # *   For more information about the supported source and destination databases, see [Database types, initial synchronization types, and synchronization topologies](https://help.aliyun.com/document_detail/130744.html).
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

