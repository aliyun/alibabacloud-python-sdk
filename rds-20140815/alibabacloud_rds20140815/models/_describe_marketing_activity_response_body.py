# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeMarketingActivityResponseBody(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        bid: str = None,
        items: List[main_models.DescribeMarketingActivityResponseBodyItems] = None,
        region_id: str = None,
        request_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # *   China site: 26842
        # *   International site: 26888
        self.bid = bid
        # The activity parameters
        self.items = items
        # The region ID.
        self.region_id = region_id
        # The request ID.
        # 
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.bid is not None:
            result['Bid'] = self.bid

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeMarketingActivityResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMarketingActivityResponseBodyItems(DaraModel):
    def __init__(
        self,
        category: str = None,
        charge_type: str = None,
        class_code: str = None,
        class_group: str = None,
        cpu: str = None,
        disk_size: int = None,
        engine: str = None,
        engine_version: str = None,
        instance_id: str = None,
        instance_name: str = None,
        max_connections: int = None,
        max_iombps: int = None,
        max_iops: int = None,
        memory: int = None,
        storage_type: str = None,
        upgrade_category: str = None,
        upgrade_class_code: str = None,
        upgrade_class_group: str = None,
        upgrade_cpu: str = None,
        upgrade_desc_content: str = None,
        upgrade_disk_size: int = None,
        upgrade_max_connections: int = None,
        upgrade_max_iombps: int = None,
        upgrade_max_iops: int = None,
        upgrade_memory: int = None,
        upgrade_reference_price: str = None,
        upgrade_storage_type: str = None,
    ):
        # The RDS edition of the instance. Valid values:
        # 
        # *   **Basic**: RDS Basic Edition
        # *   **HighAvailability**: RDS High-availability Edition
        # *   **AlwaysOn**: RDS Cluster Edition
        # *   **Finance**: RDS Enterprise Edition
        self.category = category
        # The payment type. Valid values:
        # 
        # *   POSTPAY: pay-as-you-go
        # *   PREPAY: subscription
        self.charge_type = charge_type
        # The instance type. For more information, see [Primary ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/26312.html) and [Read-only ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/145759.html).
        self.class_code = class_code
        # The instance family. For more information, see [Overview of instance families](https://help.aliyun.com/document_detail/57184.html).
        self.class_group = class_group
        # The number of CPU cores that are supported by the instance type. Unit: cores.
        self.cpu = cpu
        # The disk capacity per node. Unit: GB.
        self.disk_size = disk_size
        # The database engine of the instance. Valid values:
        # 
        # *   MySQL
        # *   SQLServer
        # *   PostgreSQL
        # *   PPAS
        # *   MariaDB
        self.engine = engine
        # The version of the database engine.
        self.engine_version = engine_version
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The maximum number of concurrent connections.
        self.max_connections = max_connections
        # The maximum I/O throughput. Unit: Mbit/s.
        self.max_iombps = max_iombps
        # The maximum IOPS.
        self.max_iops = max_iops
        # The memory size.
        self.memory = memory
        # The storage type of the instance. Valid values:
        # 
        # *   **local_ssd**: local SSD
        # *   **cloud_ssd**: standard SSD
        # *   **cloud_essd**: performance level 1 (PL1) enhanced SSD (ESSD)
        # *   **cloud_essd2**: PL2 ESSD
        # *   **cloud_essd3**: PL3 ESSD
        self.storage_type = storage_type
        # The RDS edition after the upgrade.
        self.upgrade_category = upgrade_category
        # The instance type after the upgrade.
        self.upgrade_class_code = upgrade_class_code
        # The instance family after the upgrade.
        self.upgrade_class_group = upgrade_class_group
        # The number of CPU cores after the upgrade.
        self.upgrade_cpu = upgrade_cpu
        # The description of the upgrade.
        self.upgrade_desc_content = upgrade_desc_content
        # The disk capacity after the upgrade.
        self.upgrade_disk_size = upgrade_disk_size
        # The maximum number of concurrent connections after the upgrade.
        self.upgrade_max_connections = upgrade_max_connections
        # The maximum I/O throughput after the upgrade. Unit: Mbit/s.
        self.upgrade_max_iombps = upgrade_max_iombps
        # The maximum IOPS after the upgrade.
        self.upgrade_max_iops = upgrade_max_iops
        # The memory size after the upgrade.
        self.upgrade_memory = upgrade_memory
        # The reference price of the upgrade.
        self.upgrade_reference_price = upgrade_reference_price
        # The storage type after the upgrade.
        self.upgrade_storage_type = upgrade_storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.class_code is not None:
            result['ClassCode'] = self.class_code

        if self.class_group is not None:
            result['ClassGroup'] = self.class_group

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.max_connections is not None:
            result['MaxConnections'] = self.max_connections

        if self.max_iombps is not None:
            result['MaxIombps'] = self.max_iombps

        if self.max_iops is not None:
            result['MaxIops'] = self.max_iops

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.upgrade_category is not None:
            result['UpgradeCategory'] = self.upgrade_category

        if self.upgrade_class_code is not None:
            result['UpgradeClassCode'] = self.upgrade_class_code

        if self.upgrade_class_group is not None:
            result['UpgradeClassGroup'] = self.upgrade_class_group

        if self.upgrade_cpu is not None:
            result['UpgradeCpu'] = self.upgrade_cpu

        if self.upgrade_desc_content is not None:
            result['UpgradeDescContent'] = self.upgrade_desc_content

        if self.upgrade_disk_size is not None:
            result['UpgradeDiskSize'] = self.upgrade_disk_size

        if self.upgrade_max_connections is not None:
            result['UpgradeMaxConnections'] = self.upgrade_max_connections

        if self.upgrade_max_iombps is not None:
            result['UpgradeMaxIombps'] = self.upgrade_max_iombps

        if self.upgrade_max_iops is not None:
            result['UpgradeMaxIops'] = self.upgrade_max_iops

        if self.upgrade_memory is not None:
            result['UpgradeMemory'] = self.upgrade_memory

        if self.upgrade_reference_price is not None:
            result['UpgradeReferencePrice'] = self.upgrade_reference_price

        if self.upgrade_storage_type is not None:
            result['UpgradeStorageType'] = self.upgrade_storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClassCode') is not None:
            self.class_code = m.get('ClassCode')

        if m.get('ClassGroup') is not None:
            self.class_group = m.get('ClassGroup')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MaxConnections') is not None:
            self.max_connections = m.get('MaxConnections')

        if m.get('MaxIombps') is not None:
            self.max_iombps = m.get('MaxIombps')

        if m.get('MaxIops') is not None:
            self.max_iops = m.get('MaxIops')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('UpgradeCategory') is not None:
            self.upgrade_category = m.get('UpgradeCategory')

        if m.get('UpgradeClassCode') is not None:
            self.upgrade_class_code = m.get('UpgradeClassCode')

        if m.get('UpgradeClassGroup') is not None:
            self.upgrade_class_group = m.get('UpgradeClassGroup')

        if m.get('UpgradeCpu') is not None:
            self.upgrade_cpu = m.get('UpgradeCpu')

        if m.get('UpgradeDescContent') is not None:
            self.upgrade_desc_content = m.get('UpgradeDescContent')

        if m.get('UpgradeDiskSize') is not None:
            self.upgrade_disk_size = m.get('UpgradeDiskSize')

        if m.get('UpgradeMaxConnections') is not None:
            self.upgrade_max_connections = m.get('UpgradeMaxConnections')

        if m.get('UpgradeMaxIombps') is not None:
            self.upgrade_max_iombps = m.get('UpgradeMaxIombps')

        if m.get('UpgradeMaxIops') is not None:
            self.upgrade_max_iops = m.get('UpgradeMaxIops')

        if m.get('UpgradeMemory') is not None:
            self.upgrade_memory = m.get('UpgradeMemory')

        if m.get('UpgradeReferencePrice') is not None:
            self.upgrade_reference_price = m.get('UpgradeReferencePrice')

        if m.get('UpgradeStorageType') is not None:
            self.upgrade_storage_type = m.get('UpgradeStorageType')

        return self

