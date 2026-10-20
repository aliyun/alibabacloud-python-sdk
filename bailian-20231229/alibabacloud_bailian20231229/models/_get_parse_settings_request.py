# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetParseSettingsRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
    ):
        # The category ID, which is the `CategoryId` returned by the **AddCategory** operation. You can also obtain it from the <props="china">[Application Data](https://bailian.console.aliyun.com/?tab=app#/data-center) - File tab<props="intl">[Application Data](https://bailian.console.alibabacloud.com/?tab=app#/data-center) - Unstructured Data tab by clicking the ID icon next to the category name.
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        return self

