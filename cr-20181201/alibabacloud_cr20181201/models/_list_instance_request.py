# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceRequest(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        instance_status: str = None,
        page_no: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        # The instance name.
        self.instance_name = instance_name
        # The status of the instance. Valid values:
        # 
        # *   `PENDING`: The instance is being initialized.
        # *   `INIT_ERROR`: The initialization of the instance fails.
        # *   `STARTING`: The instance is being started.
        # *   `RUNNING`: The instance is running.
        # *   `STOPPING`: The instance is being stopped.
        # *   `STOPPED`: The instance is stopped.
        # *   `DELETING`: The instance is being deleted.
        # *   `DELETED`: The instance is deleted.
        self.instance_status = instance_status
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

