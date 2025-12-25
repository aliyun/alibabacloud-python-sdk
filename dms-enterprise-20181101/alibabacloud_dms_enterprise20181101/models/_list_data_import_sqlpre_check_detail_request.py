# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataImportSQLPreCheckDetailRequest(DaraModel):
    def __init__(
        self,
        order_id: int = None,
        page_numer: int = None,
        page_size: int = None,
        sql_type: str = None,
        status_code: str = None,
        tid: int = None,
    ):
        # The ticket ID. You can call the [ListOrders](https://help.aliyun.com/document_detail/144643.html) operation to query the ticket ID.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The page number. Pages start from page 1.
        self.page_numer = page_numer
        # The number of entries per page.
        self.page_size = page_size
        # The type of the SQL statement. Valid values:
        # 
        # *   **SELECT**
        # *   **INSERT**
        # *   **DELETE**
        # *   **CREATE_TABLE**
        # 
        # > You can log on to the Data Management (DMS) console and choose **Security and Specifications** > **Operation Audit** in the top navigation bar to view more types of SQL statements.
        self.sql_type = sql_type
        # The state of the ticket. If you leave this parameter empty, all the states are queried by default. Valid values:
        # 
        # *   **INIT**: The ticket is being initialized.
        # *   **RUNNING**: The ticket is in progress.
        # *   **SUCCESS**: The ticket is complete.
        # *   **TIMEOUT**: The ticket is skipped due to timeout.
        # *   **FAIL**: The ticket fails.
        self.status_code = status_code
        # The tenant ID. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.page_numer is not None:
            result['PageNumer'] = self.page_numer

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('PageNumer') is not None:
            self.page_numer = m.get('PageNumer')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

