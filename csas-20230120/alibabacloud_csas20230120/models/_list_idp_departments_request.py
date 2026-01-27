# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIdpDepartmentsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        idp_config_id: str = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        # This parameter is required.
        self.idp_config_id = idp_config_id
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

        if self.idp_config_id is not None:
            result['IdpConfigId'] = self.idp_config_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('IdpConfigId') is not None:
            self.idp_config_id = m.get('IdpConfigId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

