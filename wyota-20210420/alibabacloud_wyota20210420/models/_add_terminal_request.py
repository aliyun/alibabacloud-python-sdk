# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddTerminalRequest(DaraModel):
    def __init__(
        self,
        alias: str = None,
        client_type: str = None,
        main_biz_type: str = None,
        serial_number: str = None,
        terminal_group_id: str = None,
        uuid: str = None,
    ):
        self.alias = alias
        self.client_type = client_type
        self.main_biz_type = main_biz_type
        self.serial_number = serial_number
        self.terminal_group_id = terminal_group_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.main_biz_type is not None:
            result['MainBizType'] = self.main_biz_type

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.terminal_group_id is not None:
            result['TerminalGroupId'] = self.terminal_group_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('MainBizType') is not None:
            self.main_biz_type = m.get('MainBizType')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('TerminalGroupId') is not None:
            self.terminal_group_id = m.get('TerminalGroupId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

