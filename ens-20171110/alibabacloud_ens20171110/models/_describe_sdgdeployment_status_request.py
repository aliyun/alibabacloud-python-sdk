# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSDGDeploymentStatusRequest(DaraModel):
    def __init__(
        self,
        deployment_type: str = None,
        disk_ids: List[str] = None,
        instance_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        region_ids: List[str] = None,
        sdgid: str = None,
        status: str = None,
    ):
        # The deployment type.
        self.deployment_type = deployment_type
        self.disk_ids = disk_ids
        # IDs of Android in Container (AIC) instances.
        self.instance_ids = instance_ids
        # The number of the page to return. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The IDs of the nodes.
        self.region_ids = region_ids
        # The ID of the SDG.
        # 
        # This parameter is required.
        self.sdgid = sdgid
        # The deployment status of the SDG.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_type is not None:
            result['DeploymentType'] = self.deployment_type

        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids

        if self.sdgid is not None:
            result['SDGId'] = self.sdgid

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentType') is not None:
            self.deployment_type = m.get('DeploymentType')

        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')

        if m.get('SDGId') is not None:
            self.sdgid = m.get('SDGId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

