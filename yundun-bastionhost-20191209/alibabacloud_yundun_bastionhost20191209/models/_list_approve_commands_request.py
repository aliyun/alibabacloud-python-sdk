# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApproveCommandsRequest(DaraModel):
    def __init__(
        self,
        approval_status: int = None,
        approve_command_id: str = None,
        instance_id: str = None,
        page_number: str = None,
        page_size: str = None,
        project_id: int = None,
        region_id: str = None,
    ):
        # The approval status. Valid values:
        # - 1: Pending.
        # - 2: Processed.
        self.approval_status = approval_status
        # The ID of the command approval.
        self.approve_command_id = approve_command_id
        # The instance ID of the Bastionhost.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain the parameter value.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number of the current page for a paged query. Default value: **1**.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The maximum number of entries to return on each page for a paged query.  
        # The maximum value of the PageSize parameter is 1000. The default number of entries per page is 20. If the PageSize parameter is left empty, 20 entries are returned by default.
        # > Specify a value for the PageSize parameter.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The project ID.
        self.project_id = project_id
        # The region ID of the Bastionhost instance.
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_status is not None:
            result['ApprovalStatus'] = self.approval_status

        if self.approve_command_id is not None:
            result['ApproveCommandId'] = self.approve_command_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalStatus') is not None:
            self.approval_status = m.get('ApprovalStatus')

        if m.get('ApproveCommandId') is not None:
            self.approve_command_id = m.get('ApproveCommandId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

