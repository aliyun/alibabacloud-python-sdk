# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeRestoreDBInstanceListResponseBody(DaraModel):
    def __init__(
        self,
        dbinstances: main_models.DescribeRestoreDBInstanceListResponseBodyDBInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # DB instances list.
        self.dbinstances = dbinstances
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The number of instances in the query results.
        self.total_count = total_count

    def validate(self):
        if self.dbinstances:
            self.dbinstances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstances is not None:
            result['DBInstances'] = self.dbinstances.to_map()

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
        if m.get('DBInstances') is not None:
            temp_model = main_models.DescribeRestoreDBInstanceListResponseBodyDBInstances()
            self.dbinstances = temp_model.from_map(m.get('DBInstances'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRestoreDBInstanceListResponseBodyDBInstances(DaraModel):
    def __init__(
        self,
        dbinstance: List[main_models.DescribeRestoreDBInstanceListResponseBodyDBInstancesDBInstance] = None,
    ):
        self.dbinstance = dbinstance

    def validate(self):
        if self.dbinstance:
            for v1 in self.dbinstance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstance'] = []
        if self.dbinstance is not None:
            for k1 in self.dbinstance:
                result['DBInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance = []
        if m.get('DBInstance') is not None:
            for k1 in m.get('DBInstance'):
                temp_model = main_models.DescribeRestoreDBInstanceListResponseBodyDBInstancesDBInstance()
                self.dbinstance.append(temp_model.from_map(k1))

        return self

class DescribeRestoreDBInstanceListResponseBodyDBInstancesDBInstance(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_status: str = None,
        dbinstance_type: str = None,
        engine_version: str = None,
        hidden_zone_id: str = None,
        is_deleted: int = None,
        lock_mode: str = None,
        region_id: str = None,
        secondary_zone_id: str = None,
        zone_id: str = None,
    ):
        # The time of instance creation, formatted as <i>yyyy-MM-dd</i>T<i>HH:00:00</i>Z (UTC time).
        self.creation_time = creation_time
        # The description of the instance.
        self.dbinstance_description = dbinstance_description
        # The instance ID.
        self.dbinstance_id = dbinstance_id
        # The status of the instance. For more information, see [Instance states](https://help.aliyun.com/document_detail/63870.html).
        self.dbinstance_status = dbinstance_status
        # The architecture of the instance. Valid values:
        # 
        # *   **sharding**: sharded cluster instance
        # *   **replicate**: replica set or standalone instance
        self.dbinstance_type = dbinstance_type
        # The database engine version of the instance. Valid values:
        # 
        # *   **7.0**
        # *   **6.0**
        # *   **5.0**
        # *   **4.4**
        # *   **4.2**
        # *   **4.0**
        # *   **3.4**
        self.engine_version = engine_version
        # The secondary availability zone 2 for the instance when implementing multi-AZ deployment.
        self.hidden_zone_id = hidden_zone_id
        # Specifies whether the instance is deleted. Valid values:
        # 
        # *   **0**: not deleted
        # *   **1**: deleted
        self.is_deleted = is_deleted
        # The locked state of the instance, value description:
        # - Unlock: Normal.
        # - ManualLock: Manually triggered lock.
        # - LockByExpiration: Automatically locked due to expiration.
        # - LockByRestoration: Automatically locked before restoration.
        # - LockByDiskQuota: Automatically locked due to disk quota exceeded.
        self.lock_mode = lock_mode
        # The region ID of the instance.
        self.region_id = region_id
        # The secondary availability zone 1 for the instance when implementing multi-AZ deployment.
        self.secondary_zone_id = secondary_zone_id
        # The zone ID of the instance.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.hidden_zone_id is not None:
            result['HiddenZoneId'] = self.hidden_zone_id

        if self.is_deleted is not None:
            result['IsDeleted'] = self.is_deleted

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.secondary_zone_id is not None:
            result['SecondaryZoneId'] = self.secondary_zone_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('HiddenZoneId') is not None:
            self.hidden_zone_id = m.get('HiddenZoneId')

        if m.get('IsDeleted') is not None:
            self.is_deleted = m.get('IsDeleted')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecondaryZoneId') is not None:
            self.secondary_zone_id = m.get('SecondaryZoneId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

