# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAvailableZonesRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        commodity_code: str = None,
        dbinstance_name: str = None,
        dispense_mode: str = None,
        engine: str = None,
        engine_version: str = None,
        region_id: str = None,
        resource_owner_id: int = None,
        zone_id: str = None,
    ):
        # The RDS edition of the instance. Valid values:
        # 
        # *   Regular instance
        # 
        #     *   **Basic**: RDS Basic Edition.
        #     *   **HighAvailability**: RDS High-availability Edition.
        #     *   **cluster**: RDS Cluster Edition for ApsaraDB RDS for MySQL.
        #     *   **AlwaysOn**: RDS Cluster Edition for ApsaraDB RDS for SQL Server.
        #     *   **Finance**: RDS Enterprise Edition.
        # 
        # *   Serverless instance
        # 
        #     *   **serverless_basic**: RDS Basic Edition. This edition is available only for instances that run MySQL and PostgreSQL.
        #     *   **serverless_standard**: RDS High-availability Edition for ApsaraDB RDS for MySQL.
        #     *   **serverless_ha**: RDS High-availability Edition for ApsaraDB RDS for SQL Server.
        self.category = category
        # The commodity code of the instance. This operation can return the resources that you can purchase based on the specified commodity code. Valid values:
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
        self.commodity_code = commodity_code
        # The ID of the primary instance. If you want to query the read-only instances that you can purchase for a primary instance, you can specify this parameter.
        # 
        # If you set **CommodityCode** to one of the following values, you must specify this parameter:
        # 
        # *   **rords_intl**
        # *   **rds_rordspre_public_intl**
        # *   **rords**
        # *   **rds_rordspre_public_cn**
        self.dbinstance_name = dbinstance_name
        # Specifies whether to return the zones in which the single-zone deployment method is supported. Valid values:
        # 
        # *   **1** (default): returns the zones.
        # *   **0**: does not return the zones.
        # 
        # >  The single-zone deployment method allows you to deploy an instance that runs RDS Enterprise Edition in a single zone.
        self.dispense_mode = dispense_mode
        # The database engine of the instance. Valid values:
        # 
        # *   **MySQL**
        # *   **SQLServer**
        # *   **PostgreSQL**
        # *   **MariaDB**
        # 
        # This parameter is required.
        self.engine = engine
        # The database engine version. Valid values:
        # 
        # *   Regular instance
        # 
        #     *   Valid values if you set Engine to MySQL: **5.5**, **5.6**, **5.7**, and **8.0**
        #     *   Valid values if you set Engine to SQLServer: **2008r2**, **08r2_ent_ha**, **2012**, **2012_ent_ha**, **2012_std_ha**, **2012_web**, **2014_std_ha**, **2016_ent_ha**, **2016_std_ha**, **2016_web**, **2017_std_ha**, **2017_ent**, **2019_std_ha**, and **2019_ent**
        #     *   Valid values if you set Engine to PostgreSQL: **10.0**, **11.0**, **12.0**, **13.0**, **14.0**, and **15.0**
        #     *   Valid value when you set Engine to MariaDB: **10.3**
        # 
        # *   Serverless instance
        # 
        #     *   Valid values if you set Engine to MySQL: **5.7** and **8.0**
        #     *   Valid values if you set Engine to SQLServer: **2016_std_sl**, **2017_std_sl**, and **2019_std_sl**
        #     *   Valid value if you set Engine to PostgreSQL: **14.0**
        # 
        #     **
        # 
        #     **Note**ApsaraDB RDS for MariaDB does not support serverless instances.
        self.engine_version = engine_version
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # The zone ID. If the instance spans more than one zone, the value of this parameter contains an `MAZ` part, such as `cn-hangzhou-MAZ6(b,f)` and `cn-hangzhou-MAZ5(b,e,f)`. You can call the DescribeRegions operation to query the most recent zone list.
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

        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.dispense_mode is not None:
            result['DispenseMode'] = self.dispense_mode

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

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

        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('DispenseMode') is not None:
            self.dispense_mode = m.get('DispenseMode')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

