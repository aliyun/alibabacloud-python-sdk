# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class SetEntityTagsRequest(DaraModel):
    def __init__(
        self,
        qualified_name: str = None,
        tags: List[main_models.UserEntityTag] = None,
    ):
        # The unique identifier of the entity. Example: maxcompute-table.projectA.tableA.
        # 
        # This parameter is required.
        self.qualified_name = qualified_name
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.UserEntityTag()
                self.tags.append(temp_model.from_map(k1))

        return self

