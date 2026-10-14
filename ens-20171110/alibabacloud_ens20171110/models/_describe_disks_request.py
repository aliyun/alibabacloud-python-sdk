# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDisksRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        disk_charge_type: str = None,
        disk_id: str = None,
        disk_ids: str = None,
        disk_name: str = None,
        disk_type: str = None,
        ens_region_id: str = None,
        ens_region_ids: str = None,
        instance_id: str = None,
        order_by_params: str = None,
        page_number: str = None,
        page_size: str = None,
        snapshot_id: str = None,
        status: str = None,
        type: str = None,
    ):
        # The disk category.
        # 
        # - cloud_efficiency: ultra cloud disk
        # - cloud_ssd: all-flash cloud disk
        # - local_hdd: local HDD
        # - local_ssd: local SSD
        self.category = category
        # The billing type.
        # 
        # - prepay: subscription
        # - postpay: pay-as-you-go
        self.disk_charge_type = disk_charge_type
        # The ID of the cloud disk.
        self.disk_id = disk_id
        # The disk IDs.
        self.disk_ids = disk_ids
        # The name of the disk.
        self.disk_name = disk_name
        # The disk purchase method.
        # 
        # - ServiceDisk: disk created by an edge service
        # - ResoureDisk: purchased with an instance
        # - PostPayDisk: purchased separately
        self.disk_type = disk_type
        # The ID of the ENS edge zone.
        self.ens_region_id = ens_region_id
        # The list of edge zones.
        self.ens_region_ids = ens_region_ids
        # The instance to which the cloud disk is mounted.
        self.instance_id = instance_id
        # The sorting parameter. Format example: {"EnsRegionId":"desc"}. By default, results are sorted by edge zone ID in descending order.
        self.order_by_params = order_by_params
        # The page number of the query list. Minimum value: **1**.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries per page for a paged query. Maximum value: **50**.
        # 
        # Default value: **10**.
        self.page_size = page_size
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The disk status.
        # 
        # - In-use: in use
        # - Available: to be mounted
        # - Attaching: being mounted
        # - Detaching: being unmounted
        # - Creating: being created
        # - ReIniting: being reset
        # - Deleting: being released
        # - Deleted: released
        # - Expiring: about to expire
        self.status = status
        # The disk property.
        # 
        # - system: system cloud disk
        # - data: data cloud disk
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.disk_charge_type is not None:
            result['DiskChargeType'] = self.disk_charge_type

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_by_params is not None:
            result['OrderByParams'] = self.order_by_params

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DiskChargeType') is not None:
            self.disk_charge_type = m.get('DiskChargeType')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids = m.get('EnsRegionIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderByParams') is not None:
            self.order_by_params = m.get('OrderByParams')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

