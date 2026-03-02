# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExchangeUpstreamBindingsRequest(DaraModel):
    def __init__(
        self,
        console_session_id: str = None,
        current_page: int = None,
        exchange_name: str = None,
        instance_id: str = None,
        page_size: int = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.exchange_name = exchange_name
        self.instance_id = instance_id
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        return self

