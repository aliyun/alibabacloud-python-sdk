# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetListResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        items: List[str] = None,
        kind: str = None,
        name: str = None,
        request_id: str = None,
        update_time: str = None,
    ):
        # The description of the custom list.
        self.description = description
        # The ID of the custom list.[](~~2850217~~)
        self.id = id
        # The items in the custom list, which are displayed as an array.
        self.items = items
        # The type of the custom list.
        self.kind = kind
        # The name of the custom list.
        # 
        # This parameter is required.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The time when the custom list was last modified.
        self.update_time = update_time

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

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Items') is not None:
            self.items = m.get('Items')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

