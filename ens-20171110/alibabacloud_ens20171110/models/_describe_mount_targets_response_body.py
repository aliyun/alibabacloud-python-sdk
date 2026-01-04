# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeMountTargetsResponseBody(DaraModel):
    def __init__(
        self,
        mount_targets: List[main_models.DescribeMountTargetsResponseBodyMountTargets] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about mount targets.
        self.mount_targets = mount_targets
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of mount targets.
        self.total_count = total_count

    def validate(self):
        if self.mount_targets:
            for v1 in self.mount_targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MountTargets'] = []
        if self.mount_targets is not None:
            for k1 in self.mount_targets:
                result['MountTargets'].append(k1.to_map() if k1 else None)

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
        self.mount_targets = []
        if m.get('MountTargets') is not None:
            for k1 in m.get('MountTargets'):
                temp_model = main_models.DescribeMountTargetsResponseBodyMountTargets()
                self.mount_targets.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeMountTargetsResponseBodyMountTargets(DaraModel):
    def __init__(
        self,
        ens_region_id: str = None,
        file_system_id: str = None,
        mount_target_domain: str = None,
        mount_target_name: str = None,
        net_work_id: str = None,
        status: str = None,
    ):
        # The ID of the region.
        self.ens_region_id = ens_region_id
        # The ID of the file system.
        self.file_system_id = file_system_id
        # The path of the mount target.
        self.mount_target_domain = mount_target_domain
        # The name of the mount target.
        self.mount_target_name = mount_target_name
        # The ID of the network.
        self.net_work_id = net_work_id
        # The state of the mount target. Valid values:
        # 
        # *   active: The mount target is available.
        # *   inactive: The mount target is unavailable.
        # *   pending: A task is being queued for the mount target.
        # *   deleting: The mount target is being deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.mount_target_domain is not None:
            result['MountTargetDomain'] = self.mount_target_domain

        if self.mount_target_name is not None:
            result['MountTargetName'] = self.mount_target_name

        if self.net_work_id is not None:
            result['NetWorkId'] = self.net_work_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('MountTargetDomain') is not None:
            self.mount_target_domain = m.get('MountTargetDomain')

        if m.get('MountTargetName') is not None:
            self.mount_target_name = m.get('MountTargetName')

        if m.get('NetWorkId') is not None:
            self.net_work_id = m.get('NetWorkId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

