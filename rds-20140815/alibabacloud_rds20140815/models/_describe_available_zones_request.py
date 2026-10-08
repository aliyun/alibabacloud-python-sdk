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
        # The instance edition. Valid values:
        # * Regular instances
        #     * **Basic**: Basic Edition
        #     * **HighAvailability**: High-availability Edition
        #     * **cluster**: MySQL Cluster Edition
        #     * **AlwaysOn**: SQL Server Cluster Edition
        #     * **Finance**: RDS Enterprise Edition
        # * Serverless instances
        #     * **serverless_basic**: Serverless Basic Edition (applicable only to MySQL and PostgreSQL)
        #     * **serverless_standard**: MySQL Serverless High-availability Edition
        #     * **serverless_ha**: SQL Server Serverless High-availability Edition
        self.category = category
        # The commodity code of the instance. The operation queries available resources for sale based on the specified commodity code. Valid values:
        # 
        # * **bards**: pay-as-you-go primary instance (China site)
        # * **rds**: subscription primary instance (China site)
        # * **rords**: pay-as-you-go read-only instance (China site)
        # * **rds_rordspre_public_cn**: subscription read-only instance (China site)
        # * **bards_intl**: pay-as-you-go primary instance (international site)
        # * **rds_intl**: subscription primary instance (international site)
        # * **rords_intl**: pay-as-you-go read-only instance (international site)
        # * **rds_rordspre_public_intl**: subscription read-only instance (international site)
        # * **rds_serverless_public_cn**: serverless (China site)
        # * **rds_serverless_public_intl**: serverless (international site)
        self.commodity_code = commodity_code
        # The instance ID of the primary instance. This parameter is used to query available read-only instance resources for the specified primary instance.
        # 
        # This parameter is required when **CommodityCode** is set to one of the following values:
        # * **rords_intl**
        # * **rds_rordspre_public_intl**
        # * **rords**
        # * **rds_rordspre_public_cn**
        self.dbinstance_name = dbinstance_name
        # Specifies whether to return the list of zones that support single-zone deployment. Valid values:
        # * **1** (default): Returns the list.
        # * **0**: Does not return the list.
        # 
        # > The single-zone deployment feature allows you to deploy RDS Enterprise Edition instances in a single zone.
        self.dispense_mode = dispense_mode
        # The database engine. Valid values:
        # * **MySQL**
        # * **SQLServer**
        # * **PostgreSQL**
        # * **MariaDB**
        # 
        # This parameter is required.
        self.engine = engine
        # The database engine version. Valid values:
        # - Regular instances
        #     - MySQL: **5.5**, **5.6**, **5.7**, **8.0**
        #     - SQL Server: **2008r2**, **08r2_ent_ha**, **2012**, **2012_ent_ha**, **2012_std_ha**, **2012_web**, **2014_std_ha**, **2016_ent_ha**, **2016_std_ha**, **2016_web**, **2017_std_ha**, **2017_ent**, **2019_std_ha**, **2019_ent**
        #     - PostgreSQL: **10.0**, **11.0**, **12.0**, **13.0**, **14.0**, **15.0**
        #     - MariaDB: **10.3**
        # - Serverless instances
        #     - MySQL: **5.7**, **8.0**
        #     - SQL Server: **2016_std_sl**, **2017_std_sl**, **2019_std_sl**
        #     - PostgreSQL: **14.0**
        # 
        #     > MariaDB does not support serverless instances.
        self.engine_version = engine_version
        # The region ID. You can call DescribeRegions to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_id = resource_owner_id
        # The zone ID. The format of multi-zone IDs differs from that of single-zone IDs and contains `MAZ`, such as `cn-hangzhou-MAZ6(b,f)` and `cn-hangzhou-MAZ5(b,e,f)`. You can call DescribeRegions to query zone IDs.
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

