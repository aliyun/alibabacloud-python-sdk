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
        # * **bards**: pay-as-you-go primary instance (China site)
        # * **rds** (default): subscription primary instance (China site)
        # * **rords**: pay-as-you-go read-only instance (China site)
        # * **rds_rordspre_public_cn**: subscription read-only instance (China site)
        # * **bards_intl**: pay-as-you-go primary instance (international site)
        # * **rds_intl**: subscription primary instance (international site)
        # * **rords_intl**: pay-as-you-go read-only instance (international site)
        # * **rds_rordspre_public_intl**: subscription read-only instance (international site)
        # 
        # > This parameter is required when you query the price of a read-only instance.
        self.commodity_code = commodity_code
        # The instance type. For more information, see [Primary instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # This parameter is required.
        self.dbinstance_class = dbinstance_class
        # Instance ID of the instance for which you want to change the specifications or renew.
        # > - This parameter is required when you query the price for a specification change or renewal.
        # > - If the instance is a read-only instance, specify instance ID of its primary instance.
        self.dbinstance_id = dbinstance_id
        # The instance storage space. Unit: GB. The value increases in increments of 5 GB. For more information about the value range, see [Instance types](https://help.aliyun.com/document_detail/26312.html).
        # 
        # This parameter is required.
        self.dbinstance_storage = dbinstance_storage
        # The instance storage type. Valid values:
        # * **general_essd**: Premium ESSD
        # * **local_ssd**: Premium Local SSDs
        # * **cloud_ssd**: standard SSD
        # * **cloud_essd**: PL1 ESSD cloud disk
        # * **cloud_essd2**: PL2 ESSD cloud disk
        # * **cloud_essd3**: PL3 ESSD cloud disk
        self.dbinstance_storage_type = dbinstance_storage_type
        # The node information.
        # > This parameter is used for ApsaraDB RDS for MySQL instances in the cluster edition.
        self.dbnode_shrink = dbnode_shrink
        # The database engine. Valid values:
        # * **MySQL**
        # * **SQLServer**
        # * **PostgreSQL**
        # * **MariaDB**
        # 
        # This parameter is required.
        self.engine = engine
        # <props="china">The database engine version. Valid values:
        # - **MySQL**: **5.5**, **5.6**, **5.7**, **8.0**
        # - **SQL Server**: **08r2_ent_ha** (cloud disk, discontinued), **2008r2** (Premium Local SSDs, discontinued), **2012** (Enterprise Edition Basic), **2012_ent_ha**, **2012_std_ha**, **2012_web**, **2014_ent_ha**, **2014_std_ha**, **2016_ent_ha**, **2016_std_ha**, **2016_web**, **2017_ent**, **2017_std_ha**, **2017_web**, **2019_ent**, **2019_std_ha**, **2019_web**, **2022_ent**, **2022_std_ha**, **2022_web**
        # - **PostgreSQL**: **10.0**, **11.0**, **12.0**, **13.0**, **14.0**, **15.0**
        # - **MariaDB**: **10.3**
        # 
        # 
        # 
        # <props="intl">The database engine version. Valid values:
        # - **MySQL**: **5.5**, **5.6**, **5.7**, **8.0**
        # - **SQL Server**: **08r2_ent_ha** (cloud disk, discontinued), **2008r2** (Premium Local SSDs, discontinued), **2012** (Enterprise Edition Basic), **2012_ent_ha**, **2012_std_ha**, **2012_web**, **2014_ent_ha**, **2014_std_ha**, **2016_ent_ha**, **2016_std_ha**, **2016_web**, **2017_ent**, **2017_std_ha**, **2017_web**, **2019_ent**, **2019_std_ha**, **2019_web**, **2022_ent**, **2022_std_ha**, **2022_web**
        # - **PostgreSQL**: **10.0**, **11.0**, **12.0**, **13.0**, **14.0**, **15.0**
        # - **MariaDB**: **10.3**
        # 
        # > For SQL Server instances, `_ent` indicates Enterprise Edition (Cluster), `_ent_ha` indicates Enterprise Edition, `_std_ha` indicates Standard Edition, and `_web` indicates Web Edition.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The instance type. Valid values:
        # * **0**: primary instance
        # * **3**: read-only instance
        self.instance_used_type = instance_used_type
        # The order type. Valid values:
        # * **BUY**: purchase
        # * **RENEW**: renewal
        # * **UPGRADE**: upgrade
        # * **DOWNGRADE**: downgrade
        self.order_type = order_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The billing method of the instance. Valid values:
        # * **Prepaid**: subscription
        # * **Postpaid**: pay-as-you-go
        self.pay_type = pay_type
        # The number of instances to purchase. Valid values: **0 to 30**.
        # 
        # This parameter is required.
        self.quantity = quantity
        # The region ID. You can call DescribeRegions to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The settings of the serverless ApsaraDB RDS instance.
        # > MariaDB does not support serverless instances.
        self.serverless_config_shrink = serverless_config_shrink
        # The subscription type. This parameter is required when **CommodityCode** is set to **rds**, **rds_rordspre_public_cn**, **rds_intl**, or **rds_rordspre_public_intl**. Valid values:
        # * **Year**: yearly subscription
        # * **Month**: monthly subscription
        self.time_type = time_type
        # The subscription duration. Valid values:
        # * If **TimeType** is set to **Year**, the value of UsedTime ranges from **1 to 100**.
        # * If **TimeType** is set to **Month**, the value of UsedTime ranges from **1 to 999**.
        # 
        # Default value: **1**.
        self.used_time = used_time
        # The zone ID of the primary node. You can call DescribeRegions to query the most recent zone list.
        # 
        # > If you specify a VPC and a vSwitch, this parameter is required to match the zone of the specified vSwitch.
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

