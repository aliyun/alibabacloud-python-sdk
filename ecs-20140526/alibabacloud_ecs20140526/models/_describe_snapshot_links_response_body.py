# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeSnapshotLinksResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        snapshot_links: main_models.DescribeSnapshotLinksResponseBodySnapshotLinks = None,
        total_count: int = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The information about the snapshot chains.
        self.snapshot_links = snapshot_links
        # The total number of snapshot chains.
        # 
        # > When using the `MaxResults` and `NextToken` parameters for a paginated query, the returned `TotalCount` parameter value is invalid.
        self.total_count = total_count

    def validate(self):
        if self.snapshot_links:
            self.snapshot_links.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshot_links is not None:
            result['SnapshotLinks'] = self.snapshot_links.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnapshotLinks') is not None:
            temp_model = main_models.DescribeSnapshotLinksResponseBodySnapshotLinks()
            self.snapshot_links = temp_model.from_map(m.get('SnapshotLinks'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSnapshotLinksResponseBodySnapshotLinks(DaraModel):
    def __init__(
        self,
        snapshot_link: List[main_models.DescribeSnapshotLinksResponseBodySnapshotLinksSnapshotLink] = None,
    ):
        self.snapshot_link = snapshot_link

    def validate(self):
        if self.snapshot_link:
            for v1 in self.snapshot_link:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SnapshotLink'] = []
        if self.snapshot_link is not None:
            for k1 in self.snapshot_link:
                result['SnapshotLink'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshot_link = []
        if m.get('SnapshotLink') is not None:
            for k1 in m.get('SnapshotLink'):
                temp_model = main_models.DescribeSnapshotLinksResponseBodySnapshotLinksSnapshotLink()
                self.snapshot_link.append(temp_model.from_map(k1))

        return self

class DescribeSnapshotLinksResponseBodySnapshotLinksSnapshotLink(DaraModel):
    def __init__(
        self,
        category: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instant_access: bool = None,
        region_id: str = None,
        snapshot_link_id: str = None,
        source_disk_id: str = None,
        source_disk_name: str = None,
        source_disk_size: int = None,
        source_disk_type: str = None,
        total_count: int = None,
        total_size: int = None,
    ):
        # The type of the snapshot chain. Valid values:
        # 
        # *   standard: standard snapshot chain.
        # *   archive: archive snapshot chain.
        # *   flash: instant access snapshot chain.
        self.category = category
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # Indicates whether the instant access feature is enabled. Valid values:
        # 
        # *   true: The instant access feature is enabled. The feature can be enabled only for Enterprise SSDs (ESSDs).
        # *   false: The instant access feature is disabled. The snapshot is a standard snapshot for which the instant access feature is disabled.
        # 
        # >  This parameter is no longer used. By default, standard snapshots of ESSDs are upgraded to instant access snapshots free of charge without the need for additional configurations. For more information, see [Use the instant access feature](https://help.aliyun.com/document_detail/193667.html).
        self.instant_access = instant_access
        # The region ID of the source disk.
        self.region_id = region_id
        # The ID of the snapshot chain.
        self.snapshot_link_id = snapshot_link_id
        # The ID of the source disk. This parameter is retained even if the source disk is deleted.
        self.source_disk_id = source_disk_id
        # The name of the source disk.
        self.source_disk_name = source_disk_name
        # The capacity of the source disk. Unit: GiB.
        self.source_disk_size = source_disk_size
        # The type of the source disk. Valid values:
        # 
        # *   system: system disk
        # *   data: data disk
        self.source_disk_type = source_disk_type
        # The total number of snapshots.
        self.total_count = total_count
        # The total size of all snapshots in the snapshot chain. Unit: byte.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instant_access is not None:
            result['InstantAccess'] = self.instant_access

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.snapshot_link_id is not None:
            result['SnapshotLinkId'] = self.snapshot_link_id

        if self.source_disk_id is not None:
            result['SourceDiskId'] = self.source_disk_id

        if self.source_disk_name is not None:
            result['SourceDiskName'] = self.source_disk_name

        if self.source_disk_size is not None:
            result['SourceDiskSize'] = self.source_disk_size

        if self.source_disk_type is not None:
            result['SourceDiskType'] = self.source_disk_type

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstantAccess') is not None:
            self.instant_access = m.get('InstantAccess')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SnapshotLinkId') is not None:
            self.snapshot_link_id = m.get('SnapshotLinkId')

        if m.get('SourceDiskId') is not None:
            self.source_disk_id = m.get('SourceDiskId')

        if m.get('SourceDiskName') is not None:
            self.source_disk_name = m.get('SourceDiskName')

        if m.get('SourceDiskSize') is not None:
            self.source_disk_size = m.get('SourceDiskSize')

        if m.get('SourceDiskType') is not None:
            self.source_disk_type = m.get('SourceDiskType')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

