# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInvocationsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        invoke_status: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The instance ID of the simple application server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The execution status of the command. Valid values:
        # - Running: The command is running.
        # - Finished: The command execution is complete.
        # - Failed: The command execution failed.
        self.invoke_status = invoke_status
        # The page number.
        # 
        # Minimum value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page in a paged query. Settings for paging.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID. You can call [ListRegions](https://help.aliyun.com/document_detail/189315.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

