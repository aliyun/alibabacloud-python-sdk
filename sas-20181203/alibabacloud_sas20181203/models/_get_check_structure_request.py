# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetCheckStructureRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        region_id: str = None,
        task_sources: List[str] = None,
    ):
        # The page number of the current page in a paging query.
        self.current_page = current_page
        # The language type for requests and responses. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries per page in a paging query.
        self.page_size = page_size
        # The region where the asset resides. Valid values:
        # 
        # - cn-hangzhou: China
        # - ap-southeast-1: outside China.
        self.region_id = region_id
        # The list of task sources.
        self.task_sources = task_sources

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.task_sources is not None:
            result['TaskSources'] = self.task_sources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TaskSources') is not None:
            self.task_sources = m.get('TaskSources')

        return self

