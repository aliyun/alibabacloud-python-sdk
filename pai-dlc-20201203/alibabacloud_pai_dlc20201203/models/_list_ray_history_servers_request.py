# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRayHistoryServersRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        end_time: str = None,
        id_prefix: str = None,
        modified_after: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        payment_type: str = None,
        resource_id: str = None,
        show_own: bool = None,
        sort_by: str = None,
        start_time: str = None,
        status: str = None,
        storage_path: str = None,
        user_id_for_filter: str = None,
        username: str = None,
        workspace_id: str = None,
    ):
        # The display name of the job.
        self.display_name = display_name
        # The end time of the query range. The job creation time is used for filtering.
        self.end_time = end_time
        # The ID prefix.
        self.id_prefix = id_prefix
        # Filters results by the time after which they were modified.
        self.modified_after = modified_after
        # The sort order. Valid values:
        # - desc: descending order.
        # - asc: ascending order.
        self.order = order
        # The page number of the page to return in a paged query. Paging starts from page 1.
        self.page_number = page_number
        # The number of RayHistoryServer entries to return on each page in a paged query. Paging is used to return results in batches.
        self.page_size = page_size
        # The billing method. Valid values:
        # - PrePaid
        # - PostPaid.
        self.payment_type = payment_type
        # The resource group ID. For information about how to query the ID of a dedicated resource group, see [Manage resource quotas](https://help.aliyun.com/document_detail/2651299.html).
        self.resource_id = resource_id
        # Specifies whether to return only the RayHistoryServer entries created by the current user.
        self.show_own = show_own
        # The field by which to sort the returned results. Valid values:
        # - DisplayName
        # - GmtCreateTime
        # - UserId
        # - ResourceId
        # - Status
        # - GmtModifyTime.
        self.sort_by = sort_by
        # The start time.
        self.start_time = start_time
        # The RayHistoryServer status. Valid values:
        # - Creating: being created.
        # - Queuing: waiting in queue.
        # - Running: running.
        # - Stopped: stopped.
        # - Failed: failed.
        self.status = status
        # The storage path of Ray logs.
        self.storage_path = storage_path
        # Filters results by user ID.
        self.user_id_for_filter = user_id_for_filter
        # Filters results by username.
        self.username = username
        # The workspace ID. <props="china">For information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html)..
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id_prefix is not None:
            result['IdPrefix'] = self.id_prefix

        if self.modified_after is not None:
            result['ModifiedAfter'] = self.modified_after

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.show_own is not None:
            result['ShowOwn'] = self.show_own

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_path is not None:
            result['StoragePath'] = self.storage_path

        if self.user_id_for_filter is not None:
            result['UserIdForFilter'] = self.user_id_for_filter

        if self.username is not None:
            result['Username'] = self.username

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IdPrefix') is not None:
            self.id_prefix = m.get('IdPrefix')

        if m.get('ModifiedAfter') is not None:
            self.modified_after = m.get('ModifiedAfter')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ShowOwn') is not None:
            self.show_own = m.get('ShowOwn')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StoragePath') is not None:
            self.storage_path = m.get('StoragePath')

        if m.get('UserIdForFilter') is not None:
            self.user_id_for_filter = m.get('UserIdForFilter')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

