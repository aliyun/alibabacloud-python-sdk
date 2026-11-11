# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateListShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        items_shrink: str = None,
        name: str = None,
    ):
        # The updated description of the list.
        # 
        # This parameter is required.
        self.description = description
        # The ID of the custom list. You can obtain the ID by calling the [ListLists](https://help.aliyun.com/document_detail/2850217.html) operation.
        # 
        # This parameter is required.
        self.id = id
        # The updated items in the list. The value is a JSON array string, such as `["1.1.1.1","2.2.2.2"]`.
        # 
        # **Full overwrite semantics**: The specified `Items` completely overwrites the original list content instead of appending to it.
        # 
        # > ⚠️ **If this parameter is not specified or is left empty, the original list content is cleared**. To retain the original items and append new ones, call `GetList` to retrieve the existing `Items`, concatenate them, and submit them at once.
        # 
        # **Element format**: The format depends on the `Kind` specified when the list was created. UpdateList does not support modifying the kind.
        # - Kind = `ip`: Each element must be a valid IP address or CIDR block. If an element is invalid, `WrongValueMatched` is returned.
        # - Other kinds: The element format is subject to conventions, and the number of elements is limited by the tenant quota `NumberItemsPerList`. Only the `ip` kind is not subject to this limit.
        # 
        # This parameter is required.
        self.items_shrink = items_shrink
        # The updated name of the custom list. If this parameter is not specified, the original name is retained.
        # 
        # **Naming rules**: Only letters, digits, and underscores are supported. The regular expression is `^\\w{1,64}$`, and the length is 1 to 64 characters.
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

        if self.items_shrink is not None:
            result['Items'] = self.items_shrink

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
            self.items_shrink = m.get('Items')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

