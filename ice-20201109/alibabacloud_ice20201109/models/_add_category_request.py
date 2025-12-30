# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCategoryRequest(DaraModel):
    def __init__(
        self,
        cate_name: str = None,
        parent_id: int = None,
        type: str = None,
    ):
        # The category name.
        # 
        # *   The value can be up to 64 bytes in length.
        # *   The value must be encoded in UTF-8.
        # 
        # This parameter is required.
        self.cate_name = cate_name
        # The ID of the parent category.
        self.parent_id = parent_id
        # The type of the category. Valid values:
        # 
        # *   default: audio, video, and image files. This is the default value.
        # *   material: short video materials.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_name is not None:
            result['CateName'] = self.cate_name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

