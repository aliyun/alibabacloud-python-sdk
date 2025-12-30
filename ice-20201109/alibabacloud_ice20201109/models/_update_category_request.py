# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCategoryRequest(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        cate_name: str = None,
    ):
        # The category ID. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [Intelligent Media Services (IMS) console](https://ims.console.aliyun.com) and choose **Media Asset Management** > **Category Management** to view the category ID.
        # *   View the value of CateId returned by the AddCategory operation that you called to create a category.
        # *   View the value of CateId returned by the GetCategories operation that you called to query a category.
        # 
        # This parameter is required.
        self.cate_id = cate_id
        # The category name.
        # 
        # This parameter is required.
        self.cate_name = cate_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cate_name is not None:
            result['CateName'] = self.cate_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        return self

