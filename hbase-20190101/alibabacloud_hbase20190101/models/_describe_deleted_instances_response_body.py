# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeDeletedInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: main_models.DescribeDeletedInstancesResponseBodyInstances = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instances = instances
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()

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
        if m.get('Instances') is not None:
            temp_model = main_models.DescribeDeletedInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m.get('Instances'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDeletedInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        instance: List[main_models.DescribeDeletedInstancesResponseBodyInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.DescribeDeletedInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class DescribeDeletedInstancesResponseBodyInstancesInstance(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        created_time: str = None,
        delete_time: str = None,
        engine: str = None,
        instance_id: str = None,
        instance_name: str = None,
        major_version: str = None,
        module_stack_version: str = None,
        parent_id: str = None,
        region_id: str = None,
        status: str = None,
        zone_id: str = None,
    ):
        self.cluster_type = cluster_type
        self.created_time = created_time
        self.delete_time = delete_time
        self.engine = engine
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.major_version = major_version
        self.module_stack_version = module_stack_version
        self.parent_id = parent_id
        self.region_id = region_id
        self.status = status
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.delete_time is not None:
            result['DeleteTime'] = self.delete_time

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.major_version is not None:
            result['MajorVersion'] = self.major_version

        if self.module_stack_version is not None:
            result['ModuleStackVersion'] = self.module_stack_version

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DeleteTime') is not None:
            self.delete_time = m.get('DeleteTime')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')

        if m.get('ModuleStackVersion') is not None:
            self.module_stack_version = m.get('ModuleStackVersion')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

