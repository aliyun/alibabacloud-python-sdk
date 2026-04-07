# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPermissionApplyOrdersRequest(DaraModel):
    def __init__(
        self,
        apply_type: str = None,
        catalog_name: str = None,
        end_time: int = None,
        engine_type: str = None,
        flow_status: int = None,
        max_compute_project_name: str = None,
        order_type: int = None,
        page_num: int = None,
        page_size: int = None,
        query_type: int = None,
        start_time: int = None,
        table_name: str = None,
        workspace_id: int = None,
    ):
        # The type of permission request. Valid values:
        # 
        # *   MaxComputeTable: Permission request for MaxCompute tables
        # *   MaxComputeFunction: Permission request for MaxCompute functions
        # *   MaxComputeResource: Permission request for MaxCompute resources
        # *   DLFSchema: Permission request for DLF 1.0 schemas
        # *   DLFTable: Permission request for DLF 1.0 tables
        # *   DLFColumn: Permission request for DLF 1.0 columns
        # *   DsApiDeploy: Permission request for publishing data services
        self.apply_type = apply_type
        # The name of the data catalog to query.
        self.catalog_name = catalog_name
        # The end of the time range to query. You can query all the permissions request orders that have been submitted before the time. The parameter value is a UNIX timestamp. If you do not specify the parameter, all permission request orders that are submitted before the current time are queried.
        self.end_time = end_time
        # This parameter is deprecated and does not take effect.
        # 
        # Valid values:
        # 
        # *   odps
        self.engine_type = engine_type
        # The status of the permission request. Valid values:
        # 
        # *   1: Pending approval
        # *   2: Approved and authorization succeeded
        # *   3: Approved but authorization failed
        # *   4: Rejected
        # *   5: Withdrawn
        # 
        # Valid values:
        # 
        # *   0
        # *   1
        # *   2
        # *   3
        # *   4
        # *   5
        self.flow_status = flow_status
        # The name of the MaxCompute project with which the permission request order is associated. If you do not specify the parameter, the permission request orders of all MaxCompute projects are returned.
        self.max_compute_project_name = max_compute_project_name
        # This parameter is deprecated and does not take effect.
        # 
        # Valid values:
        # 
        # *   1
        # *   0
        self.order_type = order_type
        # The page number for pagination. The value must be a positive integer greater than or equal to 1. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The query type for permission requests. Valid values:
        # 
        # *   0: Permission requests submitted by me
        # *   1: Permission requests pending my approval
        # *   2: All permission requests
        # 
        # This parameter is required.
        self.query_type = query_type
        # The beginning of the time range to query. You can query all the permissions request orders that have been submitted after the time. The parameter value is a UNIX timestamp. If you do not specify the parameter, all permission request orders are queried.
        self.start_time = start_time
        # The name of the table with which the permission request order is associated. If you do not specify the parameter, the permission request orders of all tables are returned.
        self.table_name = table_name
        # The ID of the workspace to which the permission request belongs. If you do not specify this parameter, permission requests from all workspaces are returned. To obtain the workspace ID, log on to the DataWorks console and navigate to the workspace configuration page.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type

        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status

        if self.max_compute_project_name is not None:
            result['MaxComputeProjectName'] = self.max_compute_project_name

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')

        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')

        if m.get('MaxComputeProjectName') is not None:
            self.max_compute_project_name = m.get('MaxComputeProjectName')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

