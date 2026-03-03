# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateSupabaseForAdminRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        execute_sql: str = None,
        operate_type: str = None,
        order_by_clause: str = None,
        order_column: str = None,
        order_type: str = None,
        page_num: int = None,
        page_size: int = None,
        table_name: str = None,
        user_id: str = None,
        where_clause: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        self.execute_sql = execute_sql
        self.operate_type = operate_type
        self.order_by_clause = order_by_clause
        self.order_column = order_column
        self.order_type = order_type
        self.page_num = page_num
        self.page_size = page_size
        self.table_name = table_name
        self.user_id = user_id
        self.where_clause = where_clause

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.execute_sql is not None:
            result['ExecuteSql'] = self.execute_sql

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        if self.order_by_clause is not None:
            result['OrderByClause'] = self.order_by_clause

        if self.order_column is not None:
            result['OrderColumn'] = self.order_column

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.where_clause is not None:
            result['WhereClause'] = self.where_clause

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('ExecuteSql') is not None:
            self.execute_sql = m.get('ExecuteSql')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        if m.get('OrderByClause') is not None:
            self.order_by_clause = m.get('OrderByClause')

        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WhereClause') is not None:
            self.where_clause = m.get('WhereClause')

        return self

