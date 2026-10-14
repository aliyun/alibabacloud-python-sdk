# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceSDGStatusResponseBody(DaraModel):
    def __init__(
        self,
        deployment_status: List[main_models.DescribeInstanceSDGStatusResponseBodyDeploymentStatus] = None,
        page_number: int = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The list of SDG deployment information.
        self.deployment_status = deployment_status
        # The page number. Starting value: 1. Default value: 1.
        self.page_number = page_number
        # The Settings for the number of entries per page for paging in a paged query. Default value: **10**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of deployment records returned.
        self.total_count = total_count

    def validate(self):
        if self.deployment_status:
            for v1 in self.deployment_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeploymentStatus'] = []
        if self.deployment_status is not None:
            for k1 in self.deployment_status:
                result['DeploymentStatus'].append(k1.to_map() if k1 else None)

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
        self.deployment_status = []
        if m.get('DeploymentStatus') is not None:
            for k1 in m.get('DeploymentStatus'):
                temp_model = main_models.DescribeInstanceSDGStatusResponseBodyDeploymentStatus()
                self.deployment_status.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstanceSDGStatusResponseBodyDeploymentStatus(DaraModel):
    def __init__(
        self,
        block_rw_split_size: int = None,
        cache_size: int = None,
        disk_access_protocol: str = None,
        disk_type: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        mount_type: str = None,
        phase: str = None,
        sdgid: str = None,
        status: str = None,
        update_time: str = None,
    ):
        # The size of the writable layer of the block device. Unit: GiB. A value of 0 indicates that this feature is disabled.
        self.block_rw_split_size = block_rw_split_size
        # The cache size. Unit: GiB. A value of 0 indicates that this feature is disabled.
        self.cache_size = cache_size
        # The disk access protocol type of the mounted shared cloud disk.
        self.disk_access_protocol = disk_access_protocol
        # The disk type of the mounted shared cloud disk.
        self.disk_type = disk_type
        # The edge zone ID.
        self.ens_region_id = ens_region_id
        # The AIC instance ID.
        self.instance_id = instance_id
        # The deployment type of the SDG.
        self.mount_type = mount_type
        # The deployment phase of the SDG.
        self.phase = phase
        # The ID of the SDG.
        self.sdgid = sdgid
        # The deployment status of the SDG.
        self.status = status
        # The latest status update time. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_rw_split_size is not None:
            result['BlockRwSplitSize'] = self.block_rw_split_size

        if self.cache_size is not None:
            result['CacheSize'] = self.cache_size

        if self.disk_access_protocol is not None:
            result['DiskAccessProtocol'] = self.disk_access_protocol

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mount_type is not None:
            result['MountType'] = self.mount_type

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.sdgid is not None:
            result['SDGId'] = self.sdgid

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockRwSplitSize') is not None:
            self.block_rw_split_size = m.get('BlockRwSplitSize')

        if m.get('CacheSize') is not None:
            self.cache_size = m.get('CacheSize')

        if m.get('DiskAccessProtocol') is not None:
            self.disk_access_protocol = m.get('DiskAccessProtocol')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MountType') is not None:
            self.mount_type = m.get('MountType')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('SDGId') is not None:
            self.sdgid = m.get('SDGId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

