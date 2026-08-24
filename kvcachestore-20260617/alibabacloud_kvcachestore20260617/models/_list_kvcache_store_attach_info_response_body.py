# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kvcachestore20260617 import models as main_models
from darabonba.model import DaraModel

class ListKVCacheStoreAttachInfoResponseBody(DaraModel):
    def __init__(
        self,
        attach_infos: List[main_models.ListKVCacheStoreAttachInfoResponseBodyAttachInfos] = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of mount information.
        self.attach_infos = attach_infos
        # The pagination token used to query the next batch of data.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID. A request ID is returned regardless of whether the call is successful.
        self.request_id = request_id
        # The total number of entries returned for the paged query.
        self.total_count = total_count

    def validate(self):
        if self.attach_infos:
            for v1 in self.attach_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttachInfos'] = []
        if self.attach_infos is not None:
            for k1 in self.attach_infos:
                result['AttachInfos'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

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
        self.attach_infos = []
        if m.get('AttachInfos') is not None:
            for k1 in m.get('AttachInfos'):
                temp_model = main_models.ListKVCacheStoreAttachInfoResponseBodyAttachInfos()
                self.attach_infos.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListKVCacheStoreAttachInfoResponseBodyAttachInfos(DaraModel):
    def __init__(
        self,
        attached_at: str = None,
        capacity: int = None,
        kvcs_id: str = None,
        mount_point_id: str = None,
        region_id: str = None,
        status: str = None,
        type: str = None,
        vsc_id: str = None,
        zone_id: str = None,
    ):
        # The time of the most recent attach operation, in ISO 8601 format. The value is null if the instance has not been attached.
        self.attached_at = attached_at
        # The file system capacity, in GiB.
        self.capacity = capacity
        # KVCacheStore KvcsId
        self.kvcs_id = kvcs_id
        # The mount point ID at the file system level.
        self.mount_point_id = mount_point_id
        # The region where the instance is deployed.
        self.region_id = region_id
        # The attach status. Valid values:
        # 
        # - Attaching: The instance is being mounted.
        # - Attached: The instance is mounted.
        # - Detaching: The instance is being unmounted.
        # 
        # After unmounting is complete, the record is deleted and not returned.
        self.status = status
        # The instance type. Valid values:
        # 
        # - kvcs: KVCacheStore (CPFS).
        self.type = type
        # The VSC ID on the compute side.
        self.vsc_id = vsc_id
        # The zone where the instance is deployed.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attached_at is not None:
            result['AttachedAt'] = self.attached_at

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.kvcs_id is not None:
            result['KvcsId'] = self.kvcs_id

        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedAt') is not None:
            self.attached_at = m.get('AttachedAt')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('KvcsId') is not None:
            self.kvcs_id = m.get('KvcsId')

        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

