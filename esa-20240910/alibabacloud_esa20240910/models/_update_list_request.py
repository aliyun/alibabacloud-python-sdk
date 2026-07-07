# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateListRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        items: List[str] = None,
        name: str = None,
    ):
        # The new description of the list.
        # 
        # This parameter is required.
        self.description = description
        # The ID of the custom list. You can obtain the ID by calling the [ListLists](https://help.aliyun.com/document_detail/2850217.html) operation.
        # 
        # This parameter is required.
        self.id = id
        # The new list content. The value is a JSON array string, for example, `["1.1.1.1","2.2.2.2"]`.
        # 
        # **Full overwrite semantics**: The specified `Items` value completely overwrites the existing list content instead of appending to it.
        # 
        # > ⚠️ **If this parameter is not specified or is set to an empty value, the existing list content is cleared**. To retain existing items and append new ones, call `GetList` to retrieve the current `Items`, merge them, and then submit the combined list.
        # 
        # **Element format**: The format depends on the `Kind` value specified when the list was created. UpdateList does not support modifying Kind.
        # - Kind = `ip`: Each element must be a valid IP address or CIDR block. If an element is invalid, `WrongValueMatched` is returned.
        # - Other Kind values: The element format is subject to the relevant specifications. The number of elements is limited by the tenant quota `NumberItemsPerList`. This limit does not apply to the `ip` Kind.
        # 
        # This parameter is required.
        self.items = items
        # The new name of the custom list. If this parameter is not specified, the original name is retained.
        # 
        # **Naming rules**: Only letters, digits, and underscores are supported (`^\\w{1,64}$`). The name must be 1 to 64 characters in length.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.items is not None:
            result['Items'] = self.items

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Items') is not None:
            self.items = m.get('Items')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

