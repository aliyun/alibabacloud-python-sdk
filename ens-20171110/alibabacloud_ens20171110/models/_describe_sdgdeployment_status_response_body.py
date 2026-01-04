# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeSDGDeploymentStatusResponseBody(DaraModel):
    def __init__(
        self,
        deployment_status: List[main_models.DescribeSDGDeploymentStatusResponseBodyDeploymentStatus] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of SDG deployment information.
        self.deployment_status = deployment_status
        # The page number. Pages start from page 1. Default value: 1
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of queried deployment records.
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
                temp_model = main_models.DescribeSDGDeploymentStatusResponseBodyDeploymentStatus()
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

class DescribeSDGDeploymentStatusResponseBodyDeploymentStatus(DaraModel):
    def __init__(
        self,
        block_rw_split_size: int = None,
        cache_size: int = None,
        disk_access_protocol: str = None,
        disk_type: str = None,
        instance_id: str = None,
        mount_type: str = None,
        phase: str = None,
        region_id: str = None,
        status: str = None,
        update_time: str = None,
    ):
        self.block_rw_split_size = block_rw_split_size
        self.cache_size = cache_size
        self.disk_access_protocol = disk_access_protocol
        self.disk_type = disk_type
        # The ID of the AIC instance.
        self.instance_id = instance_id
        # The deployment type.
        # 
        # Valid values:
        # 
        # *   overlay: read/write splitting.
        # *   common: common deployment.
        self.mount_type = mount_type
        # The deployment phase of the SDG.
        self.phase = phase
        # The ID of the edge node.
        self.region_id = region_id
        # The deployment status of the SDG.
        # 
        # Valid values:
        # 
        # *   sdg_deploying
        # *   success
        # *   failed
        self.status = status
        # The time when the status was last updated.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mount_type is not None:
            result['MountType'] = self.mount_type

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MountType') is not None:
            self.mount_type = m.get('MountType')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

