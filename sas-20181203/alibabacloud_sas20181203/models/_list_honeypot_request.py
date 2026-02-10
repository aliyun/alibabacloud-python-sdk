# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListHoneypotRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        honeypot_ids: List[str] = None,
        honeypot_name: str = None,
        node_id: str = None,
        node_name: str = None,
        page_size: int = None,
    ):
        # The number of the page to return.
        self.current_page = current_page
        # The IDs of the honeypots.
        self.honeypot_ids = honeypot_ids
        # The name of the honeypot.
        self.honeypot_name = honeypot_name
        # The ID of the management node.
        self.node_id = node_id
        # The name of the management node.
        self.node_name = node_name
        # The number of entries to return on each page.
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

        if self.honeypot_ids is not None:
            result['HoneypotIds'] = self.honeypot_ids

        if self.honeypot_name is not None:
            result['HoneypotName'] = self.honeypot_name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HoneypotIds') is not None:
            self.honeypot_ids = m.get('HoneypotIds')

        if m.get('HoneypotName') is not None:
            self.honeypot_name = m.get('HoneypotName')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

