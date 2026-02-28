# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVccRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        enable_page: bool = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        vcc_id: str = None,
    ):
        # By default, popApi is not ignored and idempotent
        self.client_token = client_token
        # Paging Parameters: The current parameters are obsolete.
        self.enable_page = enable_page
        # Paging Parameters: The current parameters are obsolete.
        self.page_number = page_number
        # Paging Parameters: The current parameters are obsolete.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The ID of the Lingjun connection instance.
        # 
        # This parameter is required.
        self.vcc_id = vcc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')

        return self

