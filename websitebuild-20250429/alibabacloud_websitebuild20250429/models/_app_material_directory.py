# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class AppMaterialDirectory(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        children: List[main_models.AppMaterialDirectory] = None,
        directory_id: str = None,
        name: str = None,
        sort_num: str = None,
        type: str = None,
    ):
        self.biz_id = biz_id
        self.children = children
        self.directory_id = directory_id
        self.name = name
        self.sort_num = sort_num
        self.type = type

    def validate(self):
        if self.children:
            for v1 in self.children:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        result['Children'] = []
        if self.children is not None:
            for k1 in self.children:
                result['Children'].append(k1.to_map() if k1 else None)

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.name is not None:
            result['Name'] = self.name

        if self.sort_num is not None:
            result['SortNum'] = self.sort_num

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        self.children = []
        if m.get('Children') is not None:
            for k1 in m.get('Children'):
                temp_model = main_models.AppMaterialDirectory()
                self.children.append(temp_model.from_map(k1))

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SortNum') is not None:
            self.sort_num = m.get('SortNum')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

