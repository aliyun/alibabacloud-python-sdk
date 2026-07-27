# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRbacUserRolesRequest(DaraModel):
    def __init__(
        self,
        application_user_id: str = None,
        biz_id: str = None,
        order_column: str = None,
        order_type: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # The site end-user ID.
        self.application_user_id = application_user_id
        # The business instance ID.
        self.biz_id = biz_id
        # The field used for sorting.
        self.order_column = order_column
        # The sort type. Valid values: ASC and DESC.
        self.order_type = order_type
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of entries per page. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_user_id is not None:
            result['ApplicationUserId'] = self.application_user_id

        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.order_column is not None:
            result['OrderColumn'] = self.order_column

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationUserId') is not None:
            self.application_user_id = m.get('ApplicationUserId')

        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

