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
        node_name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        show_own: bool = None,
        sort_by: str = None,
        status: str = None,
        sub_quota_ids: str = None,
        user_ids: str = None,
        with_historical_data: bool = None,
        workload_created_time_range: main_models.TimeRangeFilter = None,
        workload_ids: str = None,
        workload_statuses: str = None,
        workload_type: str = None,
        workspace_ids: str = None,
    ):
        self.before_workload_id = before_workload_id
        self.gmt_dequeued_time_range = gmt_dequeued_time_range
        self.gmt_enqueued_time_range = gmt_enqueued_time_range
        self.gmt_position_modified_time_range = gmt_position_modified_time_range
        self.node_name = node_name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.show_own = show_own
        self.sort_by = sort_by
        self.status = status
        self.sub_quota_ids = sub_quota_ids
        self.user_ids = user_ids
        self.with_historical_data = with_historical_data
        self.workload_created_time_range = workload_created_time_range
        self.workload_ids = workload_ids
        self.workload_statuses = workload_statuses
        self.workload_type = workload_type
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

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.show_own is not None:
            result['ShowOwn'] = self.show_own

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_quota_ids is not None:
            result['SubQuotaIds'] = self.sub_quota_ids

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        if self.with_historical_data is not None:
            result['WithHistoricalData'] = self.with_historical_data

        if self.workload_created_time_range is not None:
            result['WorkloadCreatedTimeRange'] = self.workload_created_time_range.to_map()

        if self.workload_ids is not None:
            result['WorkloadIds'] = self.workload_ids

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

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ShowOwn') is not None:
            self.show_own = m.get('ShowOwn')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubQuotaIds') is not None:
            self.sub_quota_ids = m.get('SubQuotaIds')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        if m.get('WithHistoricalData') is not None:
            self.with_historical_data = m.get('WithHistoricalData')

        if m.get('WorkloadCreatedTimeRange') is not None:
            temp_model = main_models.TimeRangeFilter()
            self.workload_created_time_range = temp_model.from_map(m.get('WorkloadCreatedTimeRange'))

        if m.get('WorkloadIds') is not None:
            self.workload_ids = m.get('WorkloadIds')

        if m.get('WorkloadStatuses') is not None:
            self.workload_statuses = m.get('WorkloadStatuses')

        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')

        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')

        return self

