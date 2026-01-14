# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendSdkMessageRequest(DaraModel):
    def __init__(
        self,
        data: str = None,
        header: str = None,
        module_name: str = None,
        operation_name: str = None,
        user_id: str = None,
    ):
        self.data = data
        self.header = header
        self.module_name = module_name
        self.operation_name = operation_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.header is not None:
            result['header'] = self.header

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.operation_name is not None:
            result['operationName'] = self.operation_name

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('header') is not None:
            self.header = m.get('header')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('operationName') is not None:
            self.operation_name = m.get('operationName')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

