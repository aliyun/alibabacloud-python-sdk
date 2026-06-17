# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDownloadTaskRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        lang: str = None,
        page_size: str = None,
        task_type: str = None,
    ):
        # The page number for a paged query.
        self.current_page = current_page
        # The language of the response message. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The maximum number of entries to return on each page for a paged query. The default value is 10. The maximum value is 50.
        self.page_size = page_size
        # The type of the task. This is an enumeration. For a list of valid values, see the API for querying file download task types. If you do not set this parameter, tasks for all file types are queried.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

