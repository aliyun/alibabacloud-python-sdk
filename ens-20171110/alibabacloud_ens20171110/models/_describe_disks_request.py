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
        # The category of the disk.
        # 
        # *   cloud_efficiency: ultra disk.
        # *   cloud_ssd: all-flash disk.
        # *   local_hdd: local HDD.
        # *   local_ssd: local SSD.
        self.category = category
        # The billing method.
        # 
        # *   prePay: subscription.
        # *   postpay: pay-as-you-go.
        self.disk_charge_type = disk_charge_type
        # The ID of the disk.
        self.disk_id = disk_id
        # The ID of the disk.
        self.disk_ids = disk_ids
        # The name of the disk.
        self.disk_name = disk_name
        # The purchase method of the disk. Valid values:
        # 
        # *   ServiceDisk: The disk is purchased when ENS is activated.
        # *   ResoureDisk: The disk is purchased when the instance is created.
        # *   PostPayDisk: The disk is separately purchased.
        self.disk_type = disk_type
        # The ID of the edge node.
        self.ens_region_id = ens_region_id
        # The node information.
        self.ens_region_ids = ens_region_ids
        # The ID of the instance to which the disk is attached.
        self.instance_id = instance_id
        # The order in which you want to sort the returned data. Example: {"EnsRegionId":"desc"}. By default, the nodes are sorted by IDs in descending order.
        self.order_by_params = order_by_params
        # The number of the page to return. Pages start from page **1**.
        # 
        # Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **50**.
        # 
        # Default value: **10**.
        self.page_size = page_size
        # The ID of the snapshot.
        self.snapshot_id = snapshot_id
        # The status of the disk. Valid values:
        # 
        # *   In-use: The disk is in use.
        # *   Available: The disk can be attached.
        # *   Attaching: The disk is being attached.
        # *   Detaching: The disk is being detached.
        # *   Creating: The disk is being created.
        # *   ReIniting: The disk is being reset.
        # *   Deleting: The disk is being released.
        # *   Deleted: The disk is released.
        # *   Expiring: The disk is about to expire.
        self.status = status
        # The type of the disk. Valid values:
        # 
        # *   system: system disk.
        # *   data: data disk.
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

