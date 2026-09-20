# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAvailableResourceRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        core_instance_type: str = None,
        disk_type: str = None,
        engine: str = None,
        engine_version: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        # The billing method. Valid values:
        # - **Prepaid**: subscription.
        # - **PostPaid**: pay-as-you-go.
        # 
        # This parameter is required.
        self.charge_type = charge_type
        # The specifications of the core node. For more information about valid values, see [Instance node specifications](https://help.aliyun.com/document_detail/194870.html).
        self.core_instance_type = core_instance_type
        # The disk type of the core node. Valid values:
        # - **cloud_efficiency**: ultra cloud disk
        # - **cloud_ssd**: standard SSD
        # - **cloud_essd_pl1**: ESSD
        # - **local_hdd_pro**: local HDD
        # - **local_ssd_pro**: local SSD.
        self.disk_type = disk_type
        # The service type of the instance. Valid values:
        # - **hbase**: ApsaraDB for HBase Standard Edition standard instance.
        # - **hbaseue**: ApsaraDB for HBase Performance-enhanced Edition standard instance.
        # - **singlehbase**: ApsaraDB for HBase single-node standard instance.
        # - **bds**: Data Synchronization (BDS) service.
        self.engine = engine
        # The version number of the service type. Valid values:
        # - **1.0**: The Data Synchronization (BDS) service supports version 1.0.
        # - **1.1**: ApsaraDB for HBase Standard Edition standard instances and ApsaraDB for HBase single-node standard instances support version 1.1.
        # - **2.0**: ApsaraDB for HBase Standard Edition standard instances, ApsaraDB for HBase Performance-enhanced Edition standard instances, and ApsaraDB for HBase single-node standard instances support version 2.0.
        # 
        # > Specify the version number based on the service type of the ApsaraDB for HBase instance.
        self.engine_version = engine_version
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/144489.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The zone. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/144489.html) operation to query available zones.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

