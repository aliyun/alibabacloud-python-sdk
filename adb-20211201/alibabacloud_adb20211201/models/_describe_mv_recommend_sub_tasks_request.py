# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMvRecommendSubTasksRequest(DaraModel):
    def __init__(
        self,
        action_inner: str = None,
        dbcluster_id: str = None,
        from_: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        subtask_id: int = None,
        task_name: str = None,
    ):
        # Fixed system value (non-modifiable).
        self.action_inner = action_inner
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # Fixed system value (non-modifiable).
        self.from_ = from_
        # The sorting field. Valid values for Type:
        # 
        # *   Asc.
        # *   Desc.
        # 
        # Valid values for Field:
        # 
        # *   StartTime;
        # *   EndTime;
        self.order_by = order_by
        # The page number.
        self.page_number = page_number
        # The number of entries to return per page.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The subtask ID.
        self.subtask_id = subtask_id
        # The name of the recommendation task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_inner is not None:
            result['ActionInner'] = self.action_inner

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.from_ is not None:
            result['From'] = self.from_

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.subtask_id is not None:
            result['SubtaskId'] = self.subtask_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionInner') is not None:
            self.action_inner = m.get('ActionInner')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SubtaskId') is not None:
            self.subtask_id = m.get('SubtaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

