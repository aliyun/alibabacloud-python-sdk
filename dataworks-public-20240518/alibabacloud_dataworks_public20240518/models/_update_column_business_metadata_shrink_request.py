# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateColumnBusinessMetadataShrinkRequest(DaraModel):
    def __init__(
        self,
        custom_attributes_shrink: str = None,
        description: str = None,
        id: str = None,
    ):
        # The custom attributes of the column, specified as key-value pairs. The key is the attribute identifier, and the value is an array that can contain at most one element. An empty array deletes the attribute\\"s value. To avoid overwriting the column\\"s business description, omit the `Description` parameter from the request. An empty object (`{}`) indicates that no custom attributes are updated.
        self.custom_attributes_shrink = custom_attributes_shrink
        # The business description of the column.
        self.description = description
        # The ID of the column. You can obtain this ID from the response of the `ListColumns` operation. For more information, see [Metadata Entity Concepts](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_attributes_shrink is not None:
            result['CustomAttributes'] = self.custom_attributes_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAttributes') is not None:
            self.custom_attributes_shrink = m.get('CustomAttributes')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

