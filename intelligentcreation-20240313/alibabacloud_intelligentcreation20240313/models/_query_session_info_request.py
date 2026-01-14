# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QuerySessionInfoRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        project_id: str = None,
        status_list: List[str] = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.project_id = project_id
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['pageNo'] = self.page_no

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.status_list is not None:
            result['statusList'] = self.status_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('statusList') is not None:
            self.status_list = m.get('statusList')

        return self

