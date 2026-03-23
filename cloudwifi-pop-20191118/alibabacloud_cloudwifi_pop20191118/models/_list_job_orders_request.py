# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobOrdersRequest(DaraModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        changing_type: str = None,
        client_system: str = None,
        client_unique_id: str = None,
        cursor: int = None,
        end_time: str = None,
        handler: str = None,
        id: str = None,
        order_status: str = None,
        page_size: int = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        title: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.changing_type = changing_type
        self.client_system = client_system
        self.client_unique_id = client_unique_id
        # This parameter is required.
        self.cursor = cursor
        self.end_time = end_time
        self.handler = handler
        self.id = id
        self.order_status = order_status
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.request_id = request_id
        self.start_time = start_time
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.changing_type is not None:
            result['ChangingType'] = self.changing_type

        if self.client_system is not None:
            result['ClientSystem'] = self.client_system

        if self.client_unique_id is not None:
            result['ClientUniqueId'] = self.client_unique_id

        if self.cursor is not None:
            result['Cursor'] = self.cursor

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.handler is not None:
            result['Handler'] = self.handler

        if self.id is not None:
            result['Id'] = self.id

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ChangingType') is not None:
            self.changing_type = m.get('ChangingType')

        if m.get('ClientSystem') is not None:
            self.client_system = m.get('ClientSystem')

        if m.get('ClientUniqueId') is not None:
            self.client_unique_id = m.get('ClientUniqueId')

        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Handler') is not None:
            self.handler = m.get('Handler')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

