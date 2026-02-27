# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wyota20210420 import models as main_models
from darabonba.model import DaraModel

class AddTerminalsRequest(DaraModel):
    def __init__(
        self,
        add_terminal_params: List[main_models.AddTerminalsRequestAddTerminalParams] = None,
        main_biz_type: str = None,
    ):
        self.add_terminal_params = add_terminal_params
        self.main_biz_type = main_biz_type

    def validate(self):
        if self.add_terminal_params:
            for v1 in self.add_terminal_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddTerminalParams'] = []
        if self.add_terminal_params is not None:
            for k1 in self.add_terminal_params:
                result['AddTerminalParams'].append(k1.to_map() if k1 else None)

        if self.main_biz_type is not None:
            result['MainBizType'] = self.main_biz_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_terminal_params = []
        if m.get('AddTerminalParams') is not None:
            for k1 in m.get('AddTerminalParams'):
                temp_model = main_models.AddTerminalsRequestAddTerminalParams()
                self.add_terminal_params.append(temp_model.from_map(k1))

        if m.get('MainBizType') is not None:
            self.main_biz_type = m.get('MainBizType')

        return self



class AddTerminalsRequestAddTerminalParams(DaraModel):
    def __init__(
        self,
        alias: str = None,
        client_type: int = None,
        serial_number: str = None,
        terminal_group_id: str = None,
        uuid: str = None,
    ):
        self.alias = alias
        self.client_type = client_type
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

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('TerminalGroupId') is not None:
            self.terminal_group_id = m.get('TerminalGroupId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

