# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateExchangeRequest(DaraModel):
    def __init__(
        self,
        alternate_exchange: str = None,
        auto_delete: bool = None,
        console_session_id: str = None,
        exchange_name: str = None,
        exchange_type: int = None,
        instance_id: str = None,
        internal: bool = None,
        vhost_name: str = None,
        xdelayed_type: str = None,
        xhash_header: str = None,
    ):
        self.alternate_exchange = alternate_exchange
        self.auto_delete = auto_delete
        self.console_session_id = console_session_id
        # This parameter is required.
        self.exchange_name = exchange_name
        # This parameter is required.
        self.exchange_type = exchange_type
        self.instance_id = instance_id
        self.internal = internal
        # This parameter is required.
        self.vhost_name = vhost_name
        self.xdelayed_type = xdelayed_type
        self.xhash_header = xhash_header

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alternate_exchange is not None:
            result['AlternateExchange'] = self.alternate_exchange

        if self.auto_delete is not None:
            result['AutoDelete'] = self.auto_delete

        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id

        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name

        if self.exchange_type is not None:
            result['ExchangeType'] = self.exchange_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.internal is not None:
            result['Internal'] = self.internal

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        if self.xdelayed_type is not None:
            result['XDelayedType'] = self.xdelayed_type

        if self.xhash_header is not None:
            result['XHashHeader'] = self.xhash_header

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlternateExchange') is not None:
            self.alternate_exchange = m.get('AlternateExchange')

        if m.get('AutoDelete') is not None:
            self.auto_delete = m.get('AutoDelete')

        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')

        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')

        if m.get('ExchangeType') is not None:
            self.exchange_type = m.get('ExchangeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Internal') is not None:
            self.internal = m.get('Internal')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        if m.get('XDelayedType') is not None:
            self.xdelayed_type = m.get('XDelayedType')

        if m.get('XHashHeader') is not None:
            self.xhash_header = m.get('XHashHeader')

        return self

