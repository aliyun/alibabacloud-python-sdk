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
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because it will be deprecated.
        self.account_id = account_id
        # The client token that is used to ensure the idempotence of the request. Generate a value from your client to ensure uniqueness across different requests. **ClientToken** supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The number of private custom ApsaraDB RDS instances attached to the source PolarDB-X instance. This parameter is required when **SourceEndpoint.InstanceType** is set to **DRDS**. Default value: **1**.
        self.dbinstance_count = dbinstance_count
        # The region ID of the destination database for data synchronization. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # > If the region specified by the **SourceRegion** parameter is Hong Kong (China) or a region outside China, set this parameter to the same region ID.
        # 
        # This parameter is required.
        self.dest_region = dest_region
        self.owner_id = owner_id
        # The billing method. Valid values:
        # 
        # - **PrePaid**: subscription.
        # - **PostPaid**: pay-as-you-go. This is the default value.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The billing method of the subscription instance. Valid values:
        # 
        # - **Year**: annual subscription.
        # - **Month**: monthly subscription.
        # 
        # > This parameter is valid and required only when **PayType** is set to **PrePaid** (subscription).
        self.period = period
        # The region ID of the data synchronization instance. Set this parameter to the same value as the **DestRegion** parameter.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The region ID of the source database for data synchronization. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # 
        # This parameter is required.
        self.source_region = source_region
        # The specification of the data synchronization link. Valid values: **micro**, **small**, **medium**, **large**.
        # > For more information about the description and performance test results of each specification, see [Specifications of data synchronization links](https://help.aliyun.com/document_detail/26605.html).
        # 
        # This parameter is required.
        self.synchronization_job_class = synchronization_job_class
        # The synchronization topology. Valid values:
        # 
        # - **oneway**: one-way synchronization.
        # - **bidirectional**: two-way synchronization.
        # 
        # > - Default value: **oneway**.
        # - You can set this parameter to **bidirectional** only when both **SourceEndpoint.InstanceType** and **DestinationEndpoint.InstanceType** are set to **MySQL**, **PolarDB**, or **Redis**.
        self.topology = topology
        # The subscription duration of the subscription instance.
        # 
        # - If the billing method is set to **Year**, valid values are **1 to 5**.
        # - If the billing method is set to **Month**, valid values are **1 to 60**.
        # 
        # > This parameter is valid and required only when **PayType** is set to **PrePaid** (subscription).
        self.used_time = used_time
        # The network type for Data Transmission Service. Set the value to **Intranet** (Express Connect).
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
        # 源库的实例类型，取值：
        # 
        # - **MySQL**：MySQL数据库（包括RDS MySQL和自建MySQL）。
        # - **PolarDB**：PolarDB集群（仅支持MySQL或兼容Oracle语法的引擎）。
        # - **Redis**：Redis数据库。
        # - **DRDS**：云原生分布式数据库PolarDB-X 1.0。
        # 
        # > - 默认取值为**MySQL**。
        # - 关于支持的源库和目标库对应情况，请参见支持的[数据库、同步初始化类型和同步拓扑](https://help.aliyun.com/document_detail/130744.html)。
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
        # 目标库的实例类型，取值：
        # - **MySQL**：MySQL数据库（包括RDS MySQL和自建MySQL）。
        # - **PolarDB**：PolarDB集群（仅支持MySQL或兼容Oracle语法的引擎）。
        # - **Redis**：Redis数据库。
        # - **MaxCompute**：MaxCompute实例。
        # 
        # >- 默认取值为**MySQL**。
        # - 关于支持的源库和目标库对应情况，请参见支持的[数据库、同步初始化类型和同步拓扑](https://help.aliyun.com/document_detail/130744.html)。
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

