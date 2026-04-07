# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBaselineStatusesRequest(DaraModel):
    def __init__(
        self,
        baseline_types: str = None,
        bizdate: str = None,
        finish_status: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        priority: str = None,
        search_text: str = None,
        status: str = None,
        topic_id: int = None,
    ):
        # The type of the baseline. Valid values: DAILY and HOURLY. The value DAILY indicates that the baseline is scheduled by day. The value HOURLY indicates that the baseline is scheduled by hour. Multiple types are separated by commas (,).
        self.baseline_types = baseline_types
        # The data timestamp of the baseline instance. Specify the time in the ISO 8601 standard in the yyyy-MM-dd\\"T\\"HH:mm:ssZ format. The time must be in UTC.
        # 
        # This parameter is required.
        self.bizdate = bizdate
        # The status of the baseline instance. Valid values: UNFINISH and FINISH. The value UNFINISH indicates that the baseline instance is still running. The value FINISH indicates that the baseline instance finishes running. Multiple states are separated by commas (,).
        self.finish_status = finish_status
        # The ID of the Alibaba Cloud account used by the baseline owner.
        self.owner = owner
        # The number of the page to return. Valid values: 1 to 30. Default value: 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The priority of the baseline. Valid values: 1, 3, 5, 7, and 8. Multiple priorities are separated by commas (,).
        self.priority = priority
        # The keyword of the baseline name used to search for the baseline.
        self.search_text = search_text
        # The status of the baseline. Valid values: ERROR, SAFE, DANGEROUS, and OVER. The value ERROR indicates that no nodes are associated with the baseline, or all nodes associated with the baseline are suspended. The value SAFE indicates that nodes finish running before the alerting time. The value DANGEROUS indicates that nodes are still running after the alerting time but before the committed completion time. The value OVER indicates that nodes are still running after the committed completion time. Multiple states are separated by commas (,).
        self.status = status
        # The ID of the event.
        self.topic_id = topic_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_types is not None:
            result['BaselineTypes'] = self.baseline_types

        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.finish_status is not None:
            result['FinishStatus'] = self.finish_status

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.search_text is not None:
            result['SearchText'] = self.search_text

        if self.status is not None:
            result['Status'] = self.status

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineTypes') is not None:
            self.baseline_types = m.get('BaselineTypes')

        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('FinishStatus') is not None:
            self.finish_status = m.get('FinishStatus')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SearchText') is not None:
            self.search_text = m.get('SearchText')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        return self

