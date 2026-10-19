# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeGlobalDistributeCacheResponseBody(DaraModel):
    def __init__(
        self,
        global_distribute_caches: List[main_models.DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCaches] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # The details of the distributed instance.
        self.global_distribute_caches = global_distribute_caches
        # The page number.
        self.page_number = page_number
        # The number of entries that can be displayed per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.global_distribute_caches:
            for v1 in self.global_distribute_caches:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GlobalDistributeCaches'] = []
        if self.global_distribute_caches is not None:
            for k1 in self.global_distribute_caches:
                result['GlobalDistributeCaches'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.global_distribute_caches = []
        if m.get('GlobalDistributeCaches') is not None:
            for k1 in m.get('GlobalDistributeCaches'):
                temp_model = main_models.DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCaches()
                self.global_distribute_caches.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCaches(DaraModel):
    def __init__(
        self,
        global_instance_id: str = None,
        status: str = None,
        sub_instances: List[main_models.DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCachesSubInstances] = None,
    ):
        # The distributed instance ID.
        self.global_instance_id = global_instance_id
        # The instance status of the distributed instance. Valid values:
        # * **Normal**: Running.
        # * **Changing**: Being modified.
        # * **Creating**: Being created.
        self.status = status
        # The details of the child instances.
        self.sub_instances = sub_instances

    def validate(self):
        if self.sub_instances:
            for v1 in self.sub_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id

        if self.status is not None:
            result['Status'] = self.status

        result['SubInstances'] = []
        if self.sub_instances is not None:
            for k1 in self.sub_instances:
                result['SubInstances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.sub_instances = []
        if m.get('SubInstances') is not None:
            for k1 in m.get('SubInstances'):
                temp_model = main_models.DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCachesSubInstances()
                self.sub_instances.append(temp_model.from_map(k1))

        return self

class DescribeGlobalDistributeCacheResponseBodyGlobalDistributeCachesSubInstances(DaraModel):
    def __init__(
        self,
        global_instance_id: str = None,
        instance_class: str = None,
        instance_id: str = None,
        instance_status: str = None,
        region_id: str = None,
    ):
        # The distributed instance ID.
        self.global_instance_id = global_instance_id
        # The instance type of the child instance. For more information, see:
        # * [Memory-optimized Standard Edition instance types](https://help.aliyun.com/document_detail/145228.html).
        # * [Memory-optimized Cluster Edition instance types](https://help.aliyun.com/document_detail/150458.html).
        # * [Memory-optimized read/write splitting instance types](https://help.aliyun.com/document_detail/150459.html).
        self.instance_class = instance_class
        # The child instance ID.
        self.instance_id = instance_id
        # The instance status of the child instance. Valid values:
        # 
        # * **Normal**: Normal.
        # * **Creating**: Being created.
        # * **Changing**: Being modified.
        # * **Inactive**: Disabled.
        # * **Flushing**: Being purged.
        # * **Released**: Released.
        # * **Transforming**: Being transformed.
        # * **Unavailable**: Service stopped.
        # * **Error**: Failed to create.
        # * **Migrating**: Being migrated.
        # * **BackupRecovering**: Being restored from a backup.
        # * **MinorVersionUpgrading**: Minor version being upgraded.
        # * **NetworkModifying**: Network being modified.
        # * **SSLModifying**: SSL being modified.
        # * **MajorVersionUpgrading**: Major engine version upgrade in progress. The instance can be accessed normally.
        # 
        # > For more information about instance status and details, see [Instance states and impacts](https://help.aliyun.com/document_detail/200740.html).
        self.instance_status = instance_status
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.global_instance_id is not None:
            result['GlobalInstanceId'] = self.global_instance_id

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalInstanceId') is not None:
            self.global_instance_id = m.get('GlobalInstanceId')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

