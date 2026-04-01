# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAvailableClassesRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        commodity_code: str = None,
        dbinstance_id: str = None,
        dbinstance_storage_type: str = None,
        engine: str = None,
        engine_version: str = None,
        instance_charge_type: str = None,
        order_type: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        zone_id: str = None,
    ):
        # The RDS edition of the instance. Valid values:
        # 
        # *   Regular instance
        # 
        #     *   **Basic**: RDS Basic Edition
        #     *   **HighAvailability**: RDS High-availability Edition
        #     *   **cluster**: RDS Cluster Edition for ApsaraDB RDS for MySQL
        #     *   **AlwaysOn**: RDS Cluster Edition for ApsaraDB RDS for SQL Server
        #     *   **Finance**: RDS Enterprise Edition
        # 
        # *   Serverless instance
        # 
        #     *   **serverless_basic**: RDS Basic Edition. This edition is available only for serverless instances that run MySQL and PostgreSQL.
        #     *   **serverless_standard**: RDS High-availability Edition for ApsaraDB RDS for MySQL.
        #     *   **serverless_ha**: RDS High-availability Edition for ApsaraDB RDS for SQL Server.
        # 
        #     > If you create a serverless instance, you must specify this parameter.
        # 
        # This parameter is required.
        self.category = category
        # The commodity code of the instance. Valid values:
        # 
        # *   **bards**: The instance is a pay-as-you-go primary instance. This value is available at the China site (aliyun.com).
        # *   **rds**: The instance is a subscription primary instance. This value is available at the China site (aliyun.com).
        # *   **rords**: The instance is a pay-as-you-go read-only instance. This value is available at the China site (aliyun.com).
        # *   **rds_rordspre_public_cn**: The instance is a subscription read-only instance. This value is available at the China site (aliyun.com).
        # *   **bards_intl**: The instance is a pay-as-you-go primary instance. This value is available at the International site (alibabacloud.com).
        # *   **rds_intl**: The instance is a subscription primary instance. This value is available at the International site (alibabacloud.com).
        # *   **rords_intl**: The instance is a pay-as-you-go read-only instance. This value is available at the International site (alibabacloud.com).
        # *   **rds_rordspre_public_intl**: The instance is a subscription read-only instance. This value is available at the International site (alibabacloud.com).
        # *   **rds_serverless_public_cn**: The instance is a serverless instance. This value is available at the China site (aliyun.com).
        # *   **rds_serverless_public_intl**: The instance is a serverless instance. This value is available at the International site (alibabacloud.com).
        # 
        # > If you want to query the price of a read-only instance, you must specify this parameter.
        self.commodity_code = commodity_code
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        self.dbinstance_id = dbinstance_id
        # The storage type of the instance. Valid values:
        # 
        # *   **local_ssd**: local SSD. This is the recommended storage type.
        # *   **cloud_ssd**: standard SSD.
        # *   **cloud_essd**: performance level 1 (PL1) Enterprise SSD (ESSD)
        # *   **cloud_essd2**: PL2 ESSD
        # *   **cloud_essd3**: PL3 ESSD
        # 
        # >  Serverless instances use only PL1 ESSDs. If you want to create a serverless instance, you must set this parameter to **cloud_essd**.
        # 
        # This parameter is required.
        self.dbinstance_storage_type = dbinstance_storage_type
        # The database engine that is run by the instance. Valid values:
        # 
        # * **MySQL**
        # * **SQLServer**
        # * **PostgreSQL**
        # * **MariaDB**
        # 
        # This parameter is required.
        self.engine = engine
        # The database engine version of the instance. Valid values:
        # 
        # *   Regular instance
        # 
        #     *   Valid values if you set Engine to MySQL: **5.5, 5.6, 5.7, and 8.0**
        #     *   Valid values if you set Engine to SQLServer: **2008r2, 08r2_ent_ha, 2012, 2012_ent_ha, 2012_std_ha, 2012_web, 2014_std_ha, 2016_ent_ha, 2016_std_ha, 2016_web, 2017_std_ha, 2017_ent, 2019_std_ha, and 2019_ent**
        #     *   Valid values if you set Engine to PostgreSQL: **10.0, 11.0, 12.0, 13.0, 14.0, and 15.0**
        #     *   Valid value when you set Engine to MariaDB: **10.3**
        # 
        # *   Serverless instance
        # 
        #     *   Valid values if you set Engine to MySQL: **5.7** and **8.0**
        #     *   Valid values if you set Engine to SQLServer: **2016_std_sl**, **2017_std_sl**, and **2019_std_sl**
        #     *   Valid value if you set Engine to PostgreSQL: **14.0**
        # 
        #     > ApsaraDB RDS for MariaDB does not support serverless instances.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The billing method of the instance. Valid values:
        # 
        # *   **Prepaid**: subscription
        # *   **Postpaid**: pay-as-you-go
        # *   **Serverless**: serverless
        # 
        # > ApsaraDB RDS for MariaDB does not support serverless instances.
        self.instance_charge_type = instance_charge_type
        # The type of order. Set the value to **BUY**
        self.order_type = order_type
        # The region ID of the instance. You can call the DescribeDBInstanceAttribute operation to query the region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # The zone ID of the instance. You can call the DescribeDBInstanceAttribute operation to query the zone ID of the instance.
        # 
        # >  If the DescribeDBInstanceAttribute operation returns multiple zones, you must specify only one of the returned zones. For example, if the DescribeDBInstanceAttribute operation returns `cn-hangzhou-MAZ9(g,h)`, you can set this parameter to `cn-hangzhou-g` or `cn-hangzhou-h`.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_storage_type is not None:
            result['DBInstanceStorageType'] = self.dbinstance_storage_type

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStorageType') is not None:
            self.dbinstance_storage_type = m.get('DBInstanceStorageType')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

