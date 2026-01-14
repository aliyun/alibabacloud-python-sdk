# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListModulesRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        keyword: str = None,
        module_name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        tag: List[main_models.ListModulesRequestTag] = None,
    ):
        self.group_id = group_id
        self.keyword = keyword
        self.module_name = module_name
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

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

        result['tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['tag'].append(k1.to_map() if k1 else None)

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

        self.tag = []
        if m.get('tag') is not None:
            for k1 in m.get('tag'):
                temp_model = main_models.ListModulesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListModulesRequestTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

