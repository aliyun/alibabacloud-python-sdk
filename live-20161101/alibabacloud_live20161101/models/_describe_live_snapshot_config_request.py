# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveSnapshotConfigRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        order: str = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The sort order. Valid values:
        # 
        # *   **asc** (default): ascending order
        # *   **desc**: descending order
        self.order = order
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        self.page_num = page_num
        # The number of entries per page. Valid values: **5 to 30**. Default value: **10**.
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.order is not None:
            result['Order'] = self.order

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

