# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePriceShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        commodity_code: str = None,
        dbinstance_class: str = None,
        dbinstance_id: str = None,
        dbinstance_storage: int = None,
        dbinstance_storage_type: str = None,
        dbnode_shrink: str = None,
        engine: str = None,
        engine_version: str = None,
        instance_used_type: int = None,
        order_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        quantity: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        serverless_config_shrink: str = None,
        time_type: str = None,
        used_time: int = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The commodity code of the instance. Valid values:
        # 
        # *   **bards**: The instance is a pay-as-you-go primary instance. This value is available at the China site (aliyun.com).
        # *   **rds** (default): The instance is a subscription primary instance. This value is available at the China site (aliyun.com).
        # *   **rords**: The instance is a pay-as-you-go read-only instance. This value is available at the China site (aliyun.com).
        # *   **rds_rordspre_public_cn**: The instance is a subscription read-only instance. This value is available at the China site (aliyun.com).
        # *   **bards_intl**: The instance is a pay-as-you-go primary instance. This value is available at the international site (alibabacloud.com).
        # *   **rds_intl**: The instance is a subscription primary instance. This value is available at the international site (alibabacloud.com).
        # *   **rords_intl**: The instance is a pay-as-you-go read-only instance. This value is available at the international site (alibabacloud.com).
        # *   **rds_rordspre_public_intl**: The instance is a subscription read-only instance. This value is available at the international site (alibabacloud.com).
        # 
        # >  If you want to query the price of a read-only instance, you must specify this parameter.
        self.commodity_code = commodity_code
        # The instance type of the instance. For more information, see [Primary ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # This parameter is required.
        self.dbinstance_class = dbinstance_class
        # The ID of the instance for which you want to change the specifications or the instance that you want to renew.
        # 
        # > *   If you want to query the price of a specification change order or a renewal order, you must specify this parameter.
        # > *   If the instance is a read-only instance, you must set this parameter to the ID of its primary instance.
        self.dbinstance_id = dbinstance_id
        # The storage capacity of the instance. Unit: GB. You can increase the storage capacity at a step size of 5 GB. For more information, see [Primary ApsaraDB RDS instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # This parameter is required.
        self.dbinstance_storage = dbinstance_storage
        # The storage type of the new instance. Valid values:
        # 
        # *   **general_essd**: premium Enterprise SSD (ESSD)
        # *   **local_ssd**: premium local SSD
        # *   **cloud_ssd**: standard SSD
        # *   **cloud_essd**: performance level 1 (PL1) ESSD
        # *   **cloud_essd2**: PL2 ESSD
        # *   **cloud_essd3**: PL3 ESSD
        self.dbinstance_storage_type = dbinstance_storage_type
        # The information about the node.
        # 
        # >  This parameter is supported for ApsaraDB RDS for MySQL instances that run RDS Cluster Edition.
        self.dbnode_shrink = dbnode_shrink
        # The database engine of the instance. Valid values:
        # 
        # *   **MySQL**
        # *   **SQLServer**
        # *   **PostgreSQL**
        # *   **MariaDB**
        # 
        # This parameter is required.
        self.engine = engine
        # The database engine version of the instance. Valid values:
        # 
        # *   Valid values if you set Engine to **MySQL**: **5.5**, **5.6**, **5.7**, and **8.0**
        # *   Valid values if you set Engine to **SQL Server**: **08r2_ent_ha**(cloud disks, discontinued), **2008r2**(high-performance local disks, discontinued), **2012** (SQL Server EE Basic)**2012_ent_ha**, **2012_std_ha**, **2012_web**, **2016_ent_ha**, **2016_std_ha**, **2016_web**, **2017_ent**, **2017_std_ha**, **2017_web**, **2019_ent**, **2019_std_ha**, **2019_web**, **2022_ent**, **2022_std_ha**, and **2022_web**
        # *   Valid values if you set Engine to **PostgreSQL**: **10.0**, **11.0**, **12.0**, **13.0**, **14.0**, and **15.0**
        # *   Valid value if you set Engine to **MariaDB**: **10.3**
        # 
        # >  The following information describes the valid values when you set Engine to SQLServer: `_ent` specifies SQL Server EE on RDS Cluster Edition, `_ent_ha` specifies SQL Server EE, `_std_ha` specifies SQL Server SE, and `_web` specifies SQL Server Web.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The role of the instance. Valid values:
        # 
        # *   **0**: primary instance
        # *   **3**: read-only instance
        self.instance_used_type = instance_used_type
        # The order type. Valid values:
        # 
        # *   **BUY**
        # *   **RENEW**
        # *   **UPGRADE**
        # *   **DOWNGRADE**
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the instance. Valid values:
        # 
        # *   **Prepaid**: subscription
        # *   **Postpaid**: pay-as-you-go
        self.pay_type = pay_type
        # The number of instances that you want to purchase. Valid values: **0 to 30**.
        # 
        # This parameter is required.
        self.quantity = quantity
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The settings of the serverless instance.
        # 
        # > ApsaraDB RDS for MariaDB does not support serverless instances.
        self.serverless_config_shrink = serverless_config_shrink
        # The billing cycle of the subscription instance. This parameter is required when **CommodityCode** is set to **rds**, **rds_rordspre_public_cn**, **rds_intl**, or **rds_rordspre_public_intl**. Valid values:
        # 
        # *   **Year**
        # *   **Month**
        self.time_type = time_type
        # The subscription duration of the instance.
        # 
        # *   If you set the **TimeType** parameter to **Year**, the value of the UsedTime parameter ranges from **1 to 100**.
        # *   If you set the **TimeType** parameter to **Month**, the value of the UsedTime parameter ranges from **1 to 999**.
        # 
        # Default value: **1**.
        self.used_time = used_time
        # The zone ID of the primary instance. You can call the DescribeRegions operation to query the most recent zone list.
        # 
        # >  If you specify a virtual private cloud (VPC) and a vSwitch, this parameter is required to identify the zone for the vSwitch.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

        if self.dbnode_shrink is not None:
            result['DBNode'] = self.dbnode_shrink

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_used_type is not None:
            result['InstanceUsedType'] = self.instance_used_type

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.serverless_config_shrink is not None:
            result['ServerlessConfig'] = self.serverless_config_shrink

        if self.time_type is not None:
            result['TimeType'] = self.time_type

        if self.used_time is not None:
            result['UsedTime'] = self.used_time

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

        if m.get('DBNode') is not None:
            self.dbnode_shrink = m.get('DBNode')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceUsedType') is not None:
            self.instance_used_type = m.get('InstanceUsedType')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ServerlessConfig') is not None:
            self.serverless_config_shrink = m.get('ServerlessConfig')

        if m.get('TimeType') is not None:
            self.time_type = m.get('TimeType')

        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

