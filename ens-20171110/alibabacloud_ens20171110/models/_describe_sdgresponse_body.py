# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeSDGResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        sdgs: List[main_models.DescribeSDGResponseBodySDGs] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The information about the SDGs.
        self.sdgs = sdgs
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.sdgs:
            for v1 in self.sdgs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SDGs'] = []
        if self.sdgs is not None:
            for k1 in self.sdgs:
                result['SDGs'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sdgs = []
        if m.get('SDGs') is not None:
            for k1 in m.get('SDGs'):
                temp_model = main_models.DescribeSDGResponseBodySDGs()
                self.sdgs.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSDGResponseBodySDGs(DaraModel):
    def __init__(
        self,
        avaliable_region_ids: List[main_models.DescribeSDGResponseBodySDGsAvaliableRegionIds] = None,
        billing_cycle: str = None,
        billing_type: str = None,
        creation_disk_type: str = None,
        creation_instance_id: str = None,
        creation_region_id: str = None,
        creation_time: str = None,
        description: str = None,
        parent_sdgid: str = None,
        performance_level: str = None,
        preload_infos: List[main_models.DescribeSDGResponseBodySDGsPreloadInfos] = None,
        sdgid: str = None,
        size: int = None,
        status: str = None,
        update_time: str = None,
    ):
        # SDGs that have snapshots.
        self.avaliable_region_ids = avaliable_region_ids
        self.billing_cycle = billing_cycle
        self.billing_type = billing_type
        self.creation_disk_type = creation_disk_type
        # The ID of the instance on which the SDG is created.
        self.creation_instance_id = creation_instance_id
        # The ID of the node on which the SDG is created.
        self.creation_region_id = creation_region_id
        # The time when the first SDG in the node was created.
        self.creation_time = creation_time
        # The description of the SDG.
        self.description = description
        # The ID of the source SDG from which you want to create an SDG. The value of this parameter is the value of the **FromSDGId** parameter that you need to specify when you call the [CreateSDG](https://help.aliyun.com/document_detail/608128.html) operation.
        self.parent_sdgid = parent_sdgid
        self.performance_level = performance_level
        # The preload information.
        self.preload_infos = preload_infos
        # The ID of the SDG.
        self.sdgid = sdgid
        # The size of the SDG. Unit: GB.
        self.size = size
        # The status of the SDG creation. Valid values:
        # 
        # *   **sdg_making**
        # *   **sdg_saving**
        # *   **failed**
        # *   **success**
        self.status = status
        # The time when the SDG was last updated.
        self.update_time = update_time

    def validate(self):
        if self.avaliable_region_ids:
            for v1 in self.avaliable_region_ids:
                 if v1:
                    v1.validate()
        if self.preload_infos:
            for v1 in self.preload_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvaliableRegionIds'] = []
        if self.avaliable_region_ids is not None:
            for k1 in self.avaliable_region_ids:
                result['AvaliableRegionIds'].append(k1.to_map() if k1 else None)

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.billing_type is not None:
            result['BillingType'] = self.billing_type

        if self.creation_disk_type is not None:
            result['CreationDiskType'] = self.creation_disk_type

        if self.creation_instance_id is not None:
            result['CreationInstanceId'] = self.creation_instance_id

        if self.creation_region_id is not None:
            result['CreationRegionId'] = self.creation_region_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.parent_sdgid is not None:
            result['ParentSDGId'] = self.parent_sdgid

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        result['PreloadInfos'] = []
        if self.preload_infos is not None:
            for k1 in self.preload_infos:
                result['PreloadInfos'].append(k1.to_map() if k1 else None)

        if self.sdgid is not None:
            result['SDGId'] = self.sdgid

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.avaliable_region_ids = []
        if m.get('AvaliableRegionIds') is not None:
            for k1 in m.get('AvaliableRegionIds'):
                temp_model = main_models.DescribeSDGResponseBodySDGsAvaliableRegionIds()
                self.avaliable_region_ids.append(temp_model.from_map(k1))

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')

        if m.get('CreationDiskType') is not None:
            self.creation_disk_type = m.get('CreationDiskType')

        if m.get('CreationInstanceId') is not None:
            self.creation_instance_id = m.get('CreationInstanceId')

        if m.get('CreationRegionId') is not None:
            self.creation_region_id = m.get('CreationRegionId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ParentSDGId') is not None:
            self.parent_sdgid = m.get('ParentSDGId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        self.preload_infos = []
        if m.get('PreloadInfos') is not None:
            for k1 in m.get('PreloadInfos'):
                temp_model = main_models.DescribeSDGResponseBodySDGsPreloadInfos()
                self.preload_infos.append(temp_model.from_map(k1))

        if m.get('SDGId') is not None:
            self.sdgid = m.get('SDGId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeSDGResponseBodySDGsPreloadInfos(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        disk_type: str = None,
        namespace: str = None,
        redundant_num: int = None,
        region_id: str = None,
        update_time: str = None,
    ):
        # The time when the SDG was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        self.disk_type = disk_type
        # The namespace.
        self.namespace = namespace
        # The number of redundant replicas to quickly respond to shared mounts.
        self.redundant_num = redundant_num
        # The ID of the node.
        self.region_id = region_id
        # The time when the status was last updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.redundant_num is not None:
            result['RedundantNum'] = self.redundant_num

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RedundantNum') is not None:
            self.redundant_num = m.get('RedundantNum')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeSDGResponseBodySDGsAvaliableRegionIds(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        region_id: str = None,
        snapshot_id: str = None,
        status: str = None,
    ):
        # The time when the SDG was created on the node.
        self.creation_time = creation_time
        # The ID of the node.
        self.region_id = region_id
        # The ID of the snapshot.
        self.snapshot_id = snapshot_id
        # The status of the SDG on the node. Valid values:
        # 
        # *   **sdg_making**
        # *   **sdg_saving**
        # *   **sdg_copying**
        # *   **failed**
        # *   **success**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

