# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRuntimesRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        creator: str = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        runtime_id: str = None,
        runtime_name: str = None,
        runtime_status: str = None,
        sort_by: str = None,
        version: str = None,
        work_dir: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        # The creator ID.
        self.creator = creator
        # The maximum number of records allowed to be returned by this request.
        self.max_results = max_results
        # The pagination token. The pagination token used in the next request to retrieve a new page of results.
        # 
        # *   This value is left empty during the first request.
        # *   The `NextToken` value returned by the previous response passed in subsequent requests.
        self.next_token = next_token
        # The sorting method.
        # 
        # *   ASC: ascending order.
        # *   DESC: Descending order.
        self.order = order
        # The page number in a paged query.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # Runtime ID. Supports exact search by runtime ID.
        self.runtime_id = runtime_id
        # The name of the runtime. Supports fuzzy search by name.
        self.runtime_name = runtime_name
        # Runtime status. Valid values:
        # 
        # *   Creating: The data cache is being created.
        # *   SaveFailed: Failed to save the runtime image.
        # *   Stopped: The file system is stopped.
        # *   Failed: Failed
        # *   ResourceAllocating: Resource allocation in progress
        # *   Stopping: Stopping in progress
        # *   Updating: Updating in progress
        # *   Saving: Saving the runtime image in progress
        # *   Queuing: Queuing in progress
        # *   Recovering: The instance is recovering.
        # *   Starting: The instance is being created.
        # *   Running: The gateway is running.
        # *   Saved: The runtime image is saved.
        # *   Deleting: The mount target is being deleted.
        # *   EnvPreparing: Preparing environment.
        self.runtime_status = runtime_status
        # The field used to sort the results in paged queries. Default value: GmtCreateTime. Valid values are as follows:
        # 
        # *   GmtCreateTime (default value): Sort by the time when created.
        # *   GmtModifiedTime: Sorted by modification time.
        # *   Creator: The ID of the creator.
        # *   WorkDir: the working path.
        # *   RuntimeName: the runtime parameter.
        # *   Status: the status of the runtime.
        self.sort_by = sort_by
        # Version
        self.version = version
        # The OSS path of the working directory.
        self.work_dir = work_dir
        # The ID of the DataWorks workspace. You can call [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html) to obtain the workspace ID.
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

        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        if self.runtime_name is not None:
            result['RuntimeName'] = self.runtime_name

        if self.runtime_status is not None:
            result['RuntimeStatus'] = self.runtime_status

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.version is not None:
            result['Version'] = self.version

        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

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

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        if m.get('RuntimeName') is not None:
            self.runtime_name = m.get('RuntimeName')

        if m.get('RuntimeStatus') is not None:
            self.runtime_status = m.get('RuntimeStatus')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

