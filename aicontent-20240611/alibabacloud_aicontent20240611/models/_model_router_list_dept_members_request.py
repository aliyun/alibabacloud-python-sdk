# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelRouterListDeptMembersRequest(DaraModel):
    def __init__(
        self,
        auth_config: str = None,
        include_authorization: bool = None,
        include_balance: bool = None,
        keyword: str = None,
        model: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # The authorization configuration filter. Valid values:
        # - inherit: only members that inherit department settings.
        # - custom: only members with custom settings.
        # - Empty: all members.
        self.auth_config = auth_config
        # Specifies whether to include the authorized models and the number of associated keys for the member.
        self.include_authorization = include_authorization
        # Specifies whether to include the monthly and permanent balance of the member\\"s sub-wallet.
        self.include_balance = include_balance
        # The search keyword.
        self.keyword = keyword
        # Filters members by the authorized model ID.
        self.model = model
        # The page number.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config

        if self.include_authorization is not None:
            result['includeAuthorization'] = self.include_authorization

        if self.include_balance is not None:
            result['includeBalance'] = self.include_balance

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.model is not None:
            result['model'] = self.model

        if self.page_index is not None:
            result['pageIndex'] = self.page_index

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            self.auth_config = m.get('authConfig')

        if m.get('includeAuthorization') is not None:
            self.include_authorization = m.get('includeAuthorization')

        if m.get('includeBalance') is not None:
            self.include_balance = m.get('includeBalance')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        return self

