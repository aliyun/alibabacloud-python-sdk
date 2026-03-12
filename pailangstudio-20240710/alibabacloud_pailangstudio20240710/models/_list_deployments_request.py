# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDeploymentsRequest(DaraModel):
    def __init__(
        self,
        creator: str = None,
        deployment_id: str = None,
        deployment_status: str = None,
        max_results: int = None,
        next_token: str = None,
        operation_type: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_id: str = None,
        resource_snapshot_id: str = None,
        resource_type: str = None,
        service_name: str = None,
        sort_by: str = None,
        workspace_id: str = None,
    ):
        self.creator = creator
        self.deployment_id = deployment_id
        self.deployment_status = deployment_status
        self.max_results = max_results
        self.next_token = next_token
        self.operation_type = operation_type
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.resource_id = resource_id
        self.resource_snapshot_id = resource_snapshot_id
        self.resource_type = resource_type
        self.service_name = service_name
        self.sort_by = sort_by
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id

        if self.deployment_status is not None:
            result['DeploymentStatus'] = self.deployment_status

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_snapshot_id is not None:
            result['ResourceSnapshotId'] = self.resource_snapshot_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')

        if m.get('DeploymentStatus') is not None:
            self.deployment_status = m.get('DeploymentStatus')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceSnapshotId') is not None:
            self.resource_snapshot_id = m.get('ResourceSnapshotId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

