# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAccountInfoRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        uid: int = None,
        user_type: str = None,
    ):
        # The current page number for pagination.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The number of entries per page for pagination. Maximum value: 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The UID of the distribution customer account. Either this parameter or the UserType parameter must be specified. If this parameter is empty, all distribution customer accounts of the specified UserType are queried.
        self.uid = uid
        # The type of the distribution customer account. Valid values:
        # - 1: End user.
        # - 2: Enterprise customer. 
        # - 3: T2 partner.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.uid is not None:
            result['Uid'] = self.uid

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

