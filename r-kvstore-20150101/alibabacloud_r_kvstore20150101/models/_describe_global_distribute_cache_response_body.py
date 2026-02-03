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
        # Details of the distributed instance.
        self.global_distribute_caches = global_distribute_caches
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
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
        # The ID of the distributed instance.
        self.global_instance_id = global_instance_id
        # The state of the distributed instance. Valid values:
        # 
        # *   **Normal**: The instance is normal.
        # *   **Changing**: The configurations of the instance are being changed.
        # *   **Creating**: The instance is being created.
        self.status = status
        # Details of the child instances.
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
        # The ID of the distributed instance.
        self.global_instance_id = global_instance_id
        # The instance type of the child instance. For more information, see the following topics:
        # 
        # *   [Standard DRAM-based instances](https://help.aliyun.com/document_detail/145228.html)
        # *   [Cluster DRAM-based instances](https://help.aliyun.com/document_detail/150458.html)
        # *   [Read/write splitting DRAM-based instances](https://help.aliyun.com/document_detail/150459.html)
        self.instance_class = instance_class
        # The ID of the child instance.
        self.instance_id = instance_id
        # The state of the child instance. Valid values:
        # 
        # *   **Normal**: The instance is normal.
        # *   **Creating**: The instance is being created.
        # *   **Changing**: The configurations of the instance are being changed.
        # *   **Inactive**: The instance is disabled.
        # *   **Flushing**: The instance is being released.
        # *   **Released**: The instance is released.
        # *   **Transforming**: The billing method of the instance is changing.
        # *   **Unavailable**: The instance is suspended.
        # *   **Error**: The instance failed to be created.
        # *   **Migrating**: The instance is being migrated.
        # *   **BackupRecovering**: The instance is being restored from a backup.
        # *   **MinorVersionUpgrading**: The minor version of the instance is being updated.
        # *   **NetworkModifying**: The network type of the instance is being changed.
        # *   **SSLModifying**: The SSL certificate of the instance is being changed.
        # *   **MajorVersionUpgrading**: The major version of the instance is being upgraded. The instance remains available during the upgrade.
        # 
        # >  For more information about instance states, see [Instance states and impacts](https://help.aliyun.com/document_detail/200740.html).
        self.instance_status = instance_status
        # The ID of the region.
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

