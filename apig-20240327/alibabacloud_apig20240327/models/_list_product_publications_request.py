# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProductPublicationsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        portal_name: str = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The name of the portal to which the API product is published.
        self.portal_name = portal_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.portal_name is not None:
            result['portalName'] = self.portal_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('portalName') is not None:
            self.portal_name = m.get('portalName')

        return self

