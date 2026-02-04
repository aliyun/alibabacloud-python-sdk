# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeGadInstancesResponseBody(DaraModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        instances: main_models.DescribeGadInstancesResponseBodyInstances = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        success: str = None,
        total_record_count: int = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.instances = instances
        self.page_number = page_number
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.success = success
        self.total_record_count = total_record_count

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Instances') is not None:
            temp_model = main_models.DescribeGadInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeGadInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeGadInstancesResponseBodyInstancesInstances] = None,
    ):
        self.instances = instances

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeGadInstancesResponseBodyInstancesInstances()
                self.instances.append(temp_model.from_map(k1))

        return self

class DescribeGadInstancesResponseBodyInstancesInstances(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        db_engine_type: str = None,
        db_instance_count: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_region: str = None,
        instance_type: str = None,
        master_db_instance_id: str = None,
        master_db_instance_name: str = None,
        master_db_instance_region: str = None,
        master_db_instance_zone_id: str = None,
        master_engine_arch_type: int = None,
        resource_group_id: str = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.db_engine_type = db_engine_type
        self.db_instance_count = db_instance_count
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_region = instance_region
        self.instance_type = instance_type
        self.master_db_instance_id = master_db_instance_id
        self.master_db_instance_name = master_db_instance_name
        self.master_db_instance_region = master_db_instance_region
        self.master_db_instance_zone_id = master_db_instance_zone_id
        self.master_engine_arch_type = master_engine_arch_type
        self.resource_group_id = resource_group_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.db_engine_type is not None:
            result['DbEngineType'] = self.db_engine_type

        if self.db_instance_count is not None:
            result['DbInstanceCount'] = self.db_instance_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_region is not None:
            result['InstanceRegion'] = self.instance_region

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.master_db_instance_id is not None:
            result['MasterDbInstanceId'] = self.master_db_instance_id

        if self.master_db_instance_name is not None:
            result['MasterDbInstanceName'] = self.master_db_instance_name

        if self.master_db_instance_region is not None:
            result['MasterDbInstanceRegion'] = self.master_db_instance_region

        if self.master_db_instance_zone_id is not None:
            result['MasterDbInstanceZoneId'] = self.master_db_instance_zone_id

        if self.master_engine_arch_type is not None:
            result['MasterEngineArchType'] = self.master_engine_arch_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DbEngineType') is not None:
            self.db_engine_type = m.get('DbEngineType')

        if m.get('DbInstanceCount') is not None:
            self.db_instance_count = m.get('DbInstanceCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceRegion') is not None:
            self.instance_region = m.get('InstanceRegion')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MasterDbInstanceId') is not None:
            self.master_db_instance_id = m.get('MasterDbInstanceId')

        if m.get('MasterDbInstanceName') is not None:
            self.master_db_instance_name = m.get('MasterDbInstanceName')

        if m.get('MasterDbInstanceRegion') is not None:
            self.master_db_instance_region = m.get('MasterDbInstanceRegion')

        if m.get('MasterDbInstanceZoneId') is not None:
            self.master_db_instance_zone_id = m.get('MasterDbInstanceZoneId')

        if m.get('MasterEngineArchType') is not None:
            self.master_engine_arch_type = m.get('MasterEngineArchType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

