# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSoarTaskAndActionsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        query_type: str = None,
        query_value: str = None,
        request_uuid: str = None,
    ):
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. The maximum value is 20. If you do not specify this parameter, 10 entries are returned.
        # 
        # > Specify a value for this parameter.
        self.page_size = page_size
        # The trigger type of the task. Valid values:
        # 
        # - **stream**: The task is triggered by a data stream.
        # 
        # - **debug**: The task is triggered by a debugging process.
        # 
        # - **manual**: The task is triggered manually.
        # 
        # - **timer**: The task is triggered by a timer.
        # 
        # - **SubInvoke**: The task is triggered by a child flow.
        self.query_type = query_type
        # The input parameter of the playbook.
        self.query_value = query_value
        # The UUID of the playbook task.
        self.request_uuid = request_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.query_value is not None:
            result['QueryValue'] = self.query_value

        if self.request_uuid is not None:
            result['RequestUuid'] = self.request_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('QueryValue') is not None:
            self.query_value = m.get('QueryValue')

        if m.get('RequestUuid') is not None:
            self.request_uuid = m.get('RequestUuid')

        return self

