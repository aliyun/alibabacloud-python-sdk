# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BackFillRequest(DaraModel):
    def __init__(
        self,
        asc: bool = None,
        back_fill_date: str = None,
        back_fill_date_begin: str = None,
        back_fill_date_end: str = None,
        dag_id: int = None,
        filter_node_ids: List[int] = None,
        history_dag_id: int = None,
        interval: int = None,
        is_trigger_sub_tree: bool = None,
        start_node_ids: List[int] = None,
        tid: int = None,
    ):
        # The running sequence of task flows for data backfill. Valid values:
        # 
        # *   **0**: reverse chronological order.
        # *   **1**: chronological order. This is the default value.
        self.asc = asc
        # The date for the data to be backfilled. This parameter is required if you specify a date for data backfill.
        self.back_fill_date = back_fill_date
        # The start date of the date range for the data to be backfilled. This parameter is required if you specify a date range for data backfill.
        self.back_fill_date_begin = back_fill_date_begin
        # The end date of the date range for the data to be backfilled. This parameter is required if you specify a date range for data backfill.
        self.back_fill_date_end = back_fill_date_end
        # The ID of the task flow. You can call the [ListTaskFlow](https://help.aliyun.com/document_detail/424565.html) or [ListLhTaskFlowAndScenario](https://help.aliyun.com/document_detail/426672.html) operation to query the task flow ID.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # Filter condition, which specifies the list of node IDs in the task flow that do not need to supplement data.
        self.filter_node_ids = filter_node_ids
        # The ID of the historical task flow.
        self.history_dag_id = history_dag_id
        # The interval at which data backfill is performed. Unit: hours. Minimum value: 1. Default value: 24.
        self.interval = interval
        # Specifies whether to run descendant nodes. Default value: true.
        self.is_trigger_sub_tree = is_trigger_sub_tree
        # The number of nodes for which you want to backfill data.
        self.start_node_ids = start_node_ids
        # The ID of the tenant.
        # 
        # >  To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asc is not None:
            result['Asc'] = self.asc

        if self.back_fill_date is not None:
            result['BackFillDate'] = self.back_fill_date

        if self.back_fill_date_begin is not None:
            result['BackFillDateBegin'] = self.back_fill_date_begin

        if self.back_fill_date_end is not None:
            result['BackFillDateEnd'] = self.back_fill_date_end

        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.filter_node_ids is not None:
            result['FilterNodeIds'] = self.filter_node_ids

        if self.history_dag_id is not None:
            result['HistoryDagId'] = self.history_dag_id

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.is_trigger_sub_tree is not None:
            result['IsTriggerSubTree'] = self.is_trigger_sub_tree

        if self.start_node_ids is not None:
            result['StartNodeIds'] = self.start_node_ids

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asc') is not None:
            self.asc = m.get('Asc')

        if m.get('BackFillDate') is not None:
            self.back_fill_date = m.get('BackFillDate')

        if m.get('BackFillDateBegin') is not None:
            self.back_fill_date_begin = m.get('BackFillDateBegin')

        if m.get('BackFillDateEnd') is not None:
            self.back_fill_date_end = m.get('BackFillDateEnd')

        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('FilterNodeIds') is not None:
            self.filter_node_ids = m.get('FilterNodeIds')

        if m.get('HistoryDagId') is not None:
            self.history_dag_id = m.get('HistoryDagId')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IsTriggerSubTree') is not None:
            self.is_trigger_sub_tree = m.get('IsTriggerSubTree')

        if m.get('StartNodeIds') is not None:
            self.start_node_ids = m.get('StartNodeIds')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

