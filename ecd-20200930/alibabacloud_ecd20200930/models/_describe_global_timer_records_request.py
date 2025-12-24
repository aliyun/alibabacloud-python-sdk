# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeGlobalTimerRecordsRequest(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        desktop_ids: List[str] = None,
        display_result_name: str = None,
        group_id: str = None,
        max_results: str = None,
        next_token: str = None,
        region_id: str = None,
        result_category: str = None,
        retryable: bool = None,
        search_region_id: str = None,
        timer_result: str = None,
        timer_types: List[str] = None,
    ):
        # The ID of the batch in which the scheduled task is executed.
        self.batch_id = batch_id
        # The cloud computer IDs.
        self.desktop_ids = desktop_ids
        self.display_result_name = display_result_name
        # The ID of the scheduled task group.
        self.group_id = group_id
        # The number of entries per page.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        self.region_id = region_id
        # The type of the execution result. You can specify this parameter to filter the execution results.
        # 
        # Valid values:
        # 
        # *   FAILED: The execution is successful.
        # *   FAILED: The execution failed.
        # *   RUNNING: The execution is in progress.
        # *   SKIPPED: The execution is skipped.
        self.result_category = result_category
        self.retryable = retryable
        # The ID of the searched region. You can specify this parameter to filter cloud computers in specific regions.
        self.search_region_id = search_region_id
        # The execution result of the scheduled task.
        # 
        # Valid values:
        # 
        # *   CONNECTED_NOT_RUN: The cloud computer is connected, but the scheduled task is not executed.
        # *   PAUSED: The scheduled task is suspended.
        # *   COMPLETED: The scheduled task is executed.
        # *   FAILED: The scheduled task failed to be executed.
        # *   RUNNING: The scheduled task is being executed.
        # *   TERMINATED: The scheduled task is stopped.
        self.timer_result = timer_result
        # The scheduled tasks.
        self.timer_types = timer_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.desktop_ids is not None:
            result['DesktopIds'] = self.desktop_ids

        if self.display_result_name is not None:
            result['DisplayResultName'] = self.display_result_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.result_category is not None:
            result['ResultCategory'] = self.result_category

        if self.retryable is not None:
            result['Retryable'] = self.retryable

        if self.search_region_id is not None:
            result['SearchRegionId'] = self.search_region_id

        if self.timer_result is not None:
            result['TimerResult'] = self.timer_result

        if self.timer_types is not None:
            result['TimerTypes'] = self.timer_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('DesktopIds') is not None:
            self.desktop_ids = m.get('DesktopIds')

        if m.get('DisplayResultName') is not None:
            self.display_result_name = m.get('DisplayResultName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResultCategory') is not None:
            self.result_category = m.get('ResultCategory')

        if m.get('Retryable') is not None:
            self.retryable = m.get('Retryable')

        if m.get('SearchRegionId') is not None:
            self.search_region_id = m.get('SearchRegionId')

        if m.get('TimerResult') is not None:
            self.timer_result = m.get('TimerResult')

        if m.get('TimerTypes') is not None:
            self.timer_types = m.get('TimerTypes')

        return self

