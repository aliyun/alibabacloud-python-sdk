# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRecordPlanDeviceByPlanRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        plan_id: str = None,
    ):
        # The page number to return. Pages start from page 1.
        self.current_page = current_page
        # The number of entries per page. Minimum value: 1. Maximum value: 50. Default value: 10.
        self.page_size = page_size
        # The ID of the recording plan. You can call [QueryRecordPlans](https://help.aliyun.com/document_detail/107896.html) to query the ID.
        # 
        # This parameter is required.
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        return self

