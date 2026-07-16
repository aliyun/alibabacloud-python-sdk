# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySupabaseAuthConfigsForAdminRequest(DaraModel):
    def __init__(
        self,
        auth_type: str = None,
        biz_id: str = None,
        env: str = None,
        order_column: str = None,
        order_type: str = None,
        page_num: int = None,
        page_size: int = None,
        user_id: str = None,
    ):
        # The authentication type.
        # 
        # This parameter is required.
        self.auth_type = auth_type
        # The business ID.
        # 
        # This parameter is required.
        self.biz_id = biz_id
        self.env = env
        # The field by which to sort the results.
        self.order_column = order_column
        # The sort order. Valid values:
        # - ASC: ascending order.
        # - DESC: descending order.
        self.order_type = order_type
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.env is not None:
            result['Env'] = self.env

        if self.order_column is not None:
            result['OrderColumn'] = self.order_column

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

