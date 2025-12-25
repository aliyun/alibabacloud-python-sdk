# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDataTrackResultDownloadStatusRequest(DaraModel):
    def __init__(
        self,
        download_key_id: str = None,
        order_id: int = None,
        tid: int = None,
    ):
        # The ID of the download key, which is used to identify the parsing progress of data tracking logs. You can call the DownloadDataTrackResult operation to query the ID of the key.
        # 
        # This parameter is required.
        self.download_key_id = download_key_id
        # The ID of the ticket. You can call the [ListOrders](https://help.aliyun.com/document_detail/144643.html) operation to query the ID of the ticket.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the ID of the tenant.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.download_key_id is not None:
            result['DownloadKeyId'] = self.download_key_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadKeyId') is not None:
            self.download_key_id = m.get('DownloadKeyId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

