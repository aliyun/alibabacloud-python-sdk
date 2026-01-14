# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModulesShrinkRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        keyword: str = None,
        module_name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        tag_shrink: str = None,
    ):
        self.group_id = group_id
        self.keyword = keyword
        self.module_name = module_name
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.project_id is not None:
            result['projectId'] = self.project_id

        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')

        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')

        return self

