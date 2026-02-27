# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs_workbench20220220 import models as main_models
from darabonba.model import DaraModel

class ListTerminalCommandsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        terminal_command_list: List[main_models.ListTerminalCommandsResponseBodyTerminalCommandList] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.terminal_command_list = terminal_command_list
        self.total_count = total_count

    def validate(self):
        if self.terminal_command_list:
            for v1 in self.terminal_command_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TerminalCommandList'] = []
        if self.terminal_command_list is not None:
            for k1 in self.terminal_command_list:
                result['TerminalCommandList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.terminal_command_list = []
        if m.get('TerminalCommandList') is not None:
            for k1 in m.get('TerminalCommandList'):
                temp_model = main_models.ListTerminalCommandsResponseBodyTerminalCommandList()
                self.terminal_command_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTerminalCommandsResponseBodyTerminalCommandList(DaraModel):
    def __init__(
        self,
        command_line: str = None,
        create_time: str = None,
        execute_path: str = None,
        login_user: str = None,
    ):
        self.command_line = command_line
        self.create_time = create_time
        self.execute_path = execute_path
        self.login_user = login_user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_line is not None:
            result['CommandLine'] = self.command_line

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.execute_path is not None:
            result['ExecutePath'] = self.execute_path

        if self.login_user is not None:
            result['LoginUser'] = self.login_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExecutePath') is not None:
            self.execute_path = m.get('ExecutePath')

        if m.get('LoginUser') is not None:
            self.login_user = m.get('LoginUser')

        return self

