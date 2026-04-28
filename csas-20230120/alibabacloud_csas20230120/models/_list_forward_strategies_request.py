# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListForwardStrategiesRequest(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        destination_ids: List[str] = None,
        destination_type: str = None,
        forward_ids: List[str] = None,
        name: str = None,
        page_size: str = None,
    ):
        self.current_page = current_page
        self.destination_ids = destination_ids
        self.destination_type = destination_type
        self.forward_ids = forward_ids
        self.name = name
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.destination_ids is not None:
            result['DestinationIds'] = self.destination_ids

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.forward_ids is not None:
            result['ForwardIds'] = self.forward_ids

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DestinationIds') is not None:
            self.destination_ids = m.get('DestinationIds')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('ForwardIds') is not None:
            self.forward_ids = m.get('ForwardIds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

