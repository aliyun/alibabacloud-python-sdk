# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstancesResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeDBInstancesResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeDBInstancesResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeDBInstancesResponseBodyItems(DaraModel):
    def __init__(
        self,
        dbinstance: List[main_models.DescribeDBInstancesResponseBodyItemsDBInstance] = None,
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
                temp_model = main_models.DescribeDBInstancesResponseBodyItemsDBInstance()
                self.dbinstance.append(temp_model.from_map(k1))

        return self

class DescribeDBInstancesResponseBodyItemsDBInstance(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        dbcluster_id: str = None,
        dbinstance_class: str = None,
        dbinstance_description: str = None,
        dbinstance_id: str = None,
        dbinstance_status: str = None,
        dbinstance_type: str = None,
        dbtype: str = None,
        dbversion: str = None,
        engine: str = None,
        expire_time: str = None,
        instance_network_type: str = None,
        lock_mode: str = None,
        lock_reason: str = None,
        pay_type: str = None,
        region_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.create_time = create_time
        self.dbcluster_id = dbcluster_id
        self.dbinstance_class = dbinstance_class
        self.dbinstance_description = dbinstance_description
        self.dbinstance_id = dbinstance_id
        self.dbinstance_status = dbinstance_status
        self.dbinstance_type = dbinstance_type
        self.dbtype = dbtype
        self.dbversion = dbversion
        self.engine = engine
        self.expire_time = expire_time
        self.instance_network_type = instance_network_type
        self.lock_mode = lock_mode
        self.lock_reason = lock_reason
        self.pay_type = pay_type
        self.region_id = region_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class

        if self.dbinstance_description is not None:
            result['DBInstanceDescription'] = self.dbinstance_description

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_status is not None:
            result['DBInstanceStatus'] = self.dbinstance_status

        if self.dbinstance_type is not None:
            result['DBInstanceType'] = self.dbinstance_type

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_network_type is not None:
            result['InstanceNetworkType'] = self.instance_network_type

        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')

        if m.get('DBInstanceDescription') is not None:
            self.dbinstance_description = m.get('DBInstanceDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceStatus') is not None:
            self.dbinstance_status = m.get('DBInstanceStatus')

        if m.get('DBInstanceType') is not None:
            self.dbinstance_type = m.get('DBInstanceType')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceNetworkType') is not None:
            self.instance_network_type = m.get('InstanceNetworkType')

        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

