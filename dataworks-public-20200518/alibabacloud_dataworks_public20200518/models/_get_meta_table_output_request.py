# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetaTableOutputRequest(DaraModel):
    def __init__(
        self,
        end_date: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: str = None,
        table_guid: str = None,
        task_id: str = None,
    ):
        # The end date.
        # 
        # This parameter is required.
        self.end_date = end_date
        # The page number. Valid values: 1 to 30. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The start date.
        # 
        # This parameter is required.
        self.start_date = start_date
        # The GUID of the metatable.
        # 
        # This parameter is required.
        self.table_guid = table_guid
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

