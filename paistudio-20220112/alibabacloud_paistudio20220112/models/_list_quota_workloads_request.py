# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ListQuotaWorkloadsRequest(DaraModel):
    def __init__(
        self,
        before_workload_id: str = None,
        gmt_dequeued_time_range: main_models.TimeRangeFilter = None,
        gmt_enqueued_time_range: main_models.TimeRangeFilter = None,
        gmt_position_modified_time_range: main_models.TimeRangeFilter = None,
        instance_id: str = None,
        node_name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        position: int = None,
        priority: int = None,
        show_own: bool = None,
        sort_by: str = None,
        status: str = None,
        sub_quota_ids: str = None,
        use_oversold_resource: bool = None,
        user_ids: str = None,
        with_historical_data: bool = None,
        workload_created_time_range: main_models.TimeRangeFilter = None,
        workload_ids: str = None,
        workload_names: str = None,
        workload_statuses: str = None,
        workload_type: str = None,
        workspace_ids: str = None,
    ):
        # The ID of the workload before which to query the queue information of instances in the queue.
        self.before_workload_id = before_workload_id
        # The time range used for a range search on the time when the workloads were dequeued.
        self.gmt_dequeued_time_range = gmt_dequeued_time_range
        # The time range used for a range search on the time when the workloads entered the queue.
        self.gmt_enqueued_time_range = gmt_enqueued_time_range
        # The time range used for a range search on the time when the queue positions of the workloads changed.
        self.gmt_position_modified_time_range = gmt_position_modified_time_range
        # The instance ID.
        self.instance_id = instance_id
        # The name of the node on which to search for workloads.
        self.node_name = node_name
        # The sort order.
        self.order = order
        # The page number.
        self.page_number = page_number
        # The number of entries per page for paging in a paged query.
        self.page_size = page_size
        # The position in the queue.
        self.position = position
        # The priority of the workload.
        self.priority = priority
        # Specifies whether to display only the workloads corresponding to this resource quota.
        self.show_own = show_own
        # The field by which to sort the returned results.
        self.sort_by = sort_by
        # The status of the workload in the queue.
        self.status = status
        # The list of sub-resource quota IDs.
        self.sub_quota_ids = sub_quota_ids
        # Specifies whether the workload uses oversold resources.
        self.use_oversold_resource = use_oversold_resource
        # The IDs of the users.
        self.user_ids = user_ids
        # Specifies whether to include historical data.
        self.with_historical_data = with_historical_data
        # The time range used for a range search on the workload creation time.
        self.workload_created_time_range = workload_created_time_range
        # The IDs of the workloads to query for queue information.
        self.workload_ids = workload_ids
        # The names of the workloads.
        self.workload_names = workload_names
        # The workload statuses used to filter the results.
        self.workload_statuses = workload_statuses
        # The workload type used to query the queue information of instances for the specified sub-product.
        self.workload_type = workload_type
        # The IDs of the workspaces for which to query the workload queue information.
        self.workspace_ids = workspace_ids

    def validate(self):
        if self.gmt_dequeued_time_range:
            self.gmt_dequeued_time_range.validate()
        if self.gmt_enqueued_time_range:
            self.gmt_enqueued_time_range.validate()
        if self.gmt_position_modified_time_range:
            self.gmt_position_modified_time_range.validate()
        if self.workload_created_time_range:
            self.workload_created_time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.before_workload_id is not None:
            result['BeforeWorkloadId'] = self.before_workload_id

        if self.gmt_dequeued_time_range is not None:
            result['GmtDequeuedTimeRange'] = self.gmt_dequeued_time_range.to_map()

        if self.gmt_enqueued_time_range is not None:
            result['GmtEnqueuedTimeRange'] = self.gmt_enqueued_time_range.to_map()

        if self.gmt_position_modified_time_range is not None:
            result['GmtPositionModifiedTimeRange'] = self.gmt_position_modified_time_range.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.position is not None:
            result['Position'] = self.position

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.show_own is not None:
            result['ShowOwn'] = self.show_own

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_quota_ids is not None:
            result['SubQuotaIds'] = self.sub_quota_ids

        if self.use_oversold_resource is not None:
            result['UseOversoldResource'] = self.use_oversold_resource

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        if self.with_historical_data is not None:
            result['WithHistoricalData'] = self.with_historical_data

        if self.workload_created_time_range is not None:
            result['WorkloadCreatedTimeRange'] = self.workload_created_time_range.to_map()

        if self.workload_ids is not None:
            result['WorkloadIds'] = self.workload_ids

        if self.workload_names is not None:
            result['WorkloadNames'] = self.workload_names

        if self.workload_statuses is not None:
            result['WorkloadStatuses'] = self.workload_statuses

        if self.workload_type is not None:
            result['WorkloadType'] = self.workload_type

        if self.workspace_ids is not None:
            result['WorkspaceIds'] = self.workspace_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeforeWorkloadId') is not None:
            self.before_workload_id = m.get('BeforeWorkloadId')

        if m.get('GmtDequeuedTimeRange') is not None:
            temp_model = main_models.TimeRangeFilter()
            self.gmt_dequeued_time_range = temp_model.from_map(m.get('GmtDequeuedTimeRange'))

        if m.get('GmtEnqueuedTimeRange') is not None:
            temp_model = main_models.TimeRangeFilter()
            self.gmt_enqueued_time_range = temp_model.from_map(m.get('GmtEnqueuedTimeRange'))

        if m.get('GmtPositionModifiedTimeRange') is not None:
            temp_model = main_models.TimeRangeFilter()
            self.gmt_position_modified_time_range = temp_model.from_map(m.get('GmtPositionModifiedTimeRange'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ShowOwn') is not None:
            self.show_own = m.get('ShowOwn')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubQuotaIds') is not None:
            self.sub_quota_ids = m.get('SubQuotaIds')

        if m.get('UseOversoldResource') is not None:
            self.use_oversold_resource = m.get('UseOversoldResource')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        if m.get('WithHistoricalData') is not None:
            self.with_historical_data = m.get('WithHistoricalData')

        if m.get('WorkloadCreatedTimeRange') is not None:
            temp_model = main_models.TimeRangeFilter()
            self.workload_created_time_range = temp_model.from_map(m.get('WorkloadCreatedTimeRange'))

        if m.get('WorkloadIds') is not None:
            self.workload_ids = m.get('WorkloadIds')

        if m.get('WorkloadNames') is not None:
            self.workload_names = m.get('WorkloadNames')

        if m.get('WorkloadStatuses') is not None:
            self.workload_statuses = m.get('WorkloadStatuses')

        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')

        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')

        return self

