# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCategoryRequest(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
    ):
        # The ID of the category. You can specify only one ID. You can use one of the following methods to obtain the ID:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). Choose **Configuration Management** > **Media Management** > **Categories**. On the Audio and Video / Image Category or Short Video Material Category tab, view the category ID.
        # *   Obtain the category ID from the response to the [AddCategory](~~AddCategory~~) operation.
        # 
        # >  If you specify the ID of a parent category, all subcategories under the parent category are deleted at the same time.
        # 
        # This parameter is required.
        self.cate_id = cate_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        return self

