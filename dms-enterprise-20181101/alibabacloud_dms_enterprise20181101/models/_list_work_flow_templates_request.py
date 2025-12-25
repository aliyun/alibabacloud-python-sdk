# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkFlowTemplatesRequest(DaraModel):
    def __init__(
        self,
        search_name: str = None,
        tid: int = None,
    ):
        # The name that is used to query approval templates.
        self.search_name = search_name
        # The ID of the tenant.
        # 
        # > : To view the ID of the tenant, log on to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.search_name is not None:
            result['SearchName'] = self.search_name

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

