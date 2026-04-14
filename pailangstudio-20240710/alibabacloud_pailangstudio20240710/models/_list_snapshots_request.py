# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSnapshotsRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        creation_type: str = None,
        creator: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        snapshot_id: str = None,
        snapshot_resource_id: str = None,
        snapshot_resource_type: str = None,
        snapshot_status: str = None,
        sort_by: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        # The creation type of the snapshot. To query multiple types at the same time, separate them with commas.
        self.creation_type = creation_type
        # The creator ID.
        self.creator = creator
        # The maximum number of records allowed to be returned in this request.
        self.max_results = max_results
        # Pagination cursor used to retrieve results for the next page.
        # 
        # * Leave empty for the first request.
        # * For subsequent requests, pass the NextToken value returned in the previous response.
        self.next_token = next_token
        # Sorting order.
        # 
        # - ASC: ascending order.
        # - DESC: descending order.
        self.order = order
        # Page number of the current page in paged query.
        self.page_number = page_number
        # Number of items displayed per page. Default value is 10.
        self.page_size = page_size
        # Snapshot ID.
        self.snapshot_id = snapshot_id
        # Snapshot resource ID.
        self.snapshot_resource_id = snapshot_resource_id
        # The snapshot resource type. Valid values:
        # * Flow: pipeline
        self.snapshot_resource_type = snapshot_resource_type
        self.snapshot_status = snapshot_status
        # Sorting field used in paged query. The default value is GmtCreateTime. Valid values:
        # 
        # - GmtCreateTime (default): sort by Creation Time.
        # - GmtModifiedTime: sort by Updated At.
        self.sort_by = sort_by
        # The workspace ID. For information about how to obtain a workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.creation_type is not None:
            result['CreationType'] = self.creation_type

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.snapshot_resource_id is not None:
            result['SnapshotResourceId'] = self.snapshot_resource_id

        if self.snapshot_resource_type is not None:
            result['SnapshotResourceType'] = self.snapshot_resource_type

        if self.snapshot_status is not None:
            result['SnapshotStatus'] = self.snapshot_status

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('CreationType') is not None:
            self.creation_type = m.get('CreationType')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('SnapshotResourceId') is not None:
            self.snapshot_resource_id = m.get('SnapshotResourceId')

        if m.get('SnapshotResourceType') is not None:
            self.snapshot_resource_type = m.get('SnapshotResourceType')

        if m.get('SnapshotStatus') is not None:
            self.snapshot_status = m.get('SnapshotStatus')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

