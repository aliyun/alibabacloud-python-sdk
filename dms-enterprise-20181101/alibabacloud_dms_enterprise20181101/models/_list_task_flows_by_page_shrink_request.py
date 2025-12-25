# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTaskFlowsByPageShrinkRequest(DaraModel):
    def __init__(
        self,
        dag_id_list_shrink: str = None,
        page_index: int = None,
        page_size: int = None,
        scenario_id: int = None,
        search_key: str = None,
        tid: int = None,
    ):
        # Filter condition, task flow ID list.
        self.dag_id_list_shrink = dag_id_list_shrink
        # The number of the page to return.
        self.page_index = page_index
        # The number of entries to return on each page.
        self.page_size = page_size
        # Filter condition, application scenario ID.
        self.scenario_id = scenario_id
        # The keyword that is used to search for task flow names.
        self.search_key = search_key
        # The ID of the tenant.
        # 
        # > : To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dag_id_list_shrink is not None:
            result['DagIdList'] = self.dag_id_list_shrink

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DagIdList') is not None:
            self.dag_id_list_shrink = m.get('DagIdList')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

