# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEnterpriseAccelerateTargetsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        eap_id: str = None,
        page_size: int = None,
        target: str = None,
    ):
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.eap_id = eap_id
        # This parameter is required.
        self.page_size = page_size
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.eap_id is not None:
            result['EapId'] = self.eap_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EapId') is not None:
            self.eap_id = m.get('EapId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

