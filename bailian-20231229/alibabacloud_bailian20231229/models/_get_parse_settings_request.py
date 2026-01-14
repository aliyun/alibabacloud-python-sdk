# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetParseSettingsRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
    ):
        # The category ID, which is the `CategoryId` returned by **AddCategory**. To view the category ID, click the ID icon next to the category name on the Unstructured Data tab of the [Application Data](https://bailian.console.alibabacloud.com/?tab=app#/data-center) page.
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

