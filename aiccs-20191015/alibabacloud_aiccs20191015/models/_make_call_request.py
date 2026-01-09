# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MakeCallRequest(DaraModel):
    def __init__(
        self,
        called_number: str = None,
        calling_number: str = None,
        command_code: str = None,
        ext_info: str = None,
        outer_account_id: str = None,
        outer_account_type: str = None,
    ):
        # This parameter is required.
        self.called_number = called_number
        # This parameter is required.
        self.calling_number = calling_number
        # This parameter is required.
        self.command_code = command_code
        self.ext_info = ext_info
        # This parameter is required.
        self.outer_account_id = outer_account_id
        # This parameter is required.
        self.outer_account_type = outer_account_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.command_code is not None:
            result['CommandCode'] = self.command_code

        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info

        if self.outer_account_id is not None:
            result['OuterAccountId'] = self.outer_account_id

        if self.outer_account_type is not None:
            result['OuterAccountType'] = self.outer_account_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('CommandCode') is not None:
            self.command_code = m.get('CommandCode')

        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')

        if m.get('OuterAccountId') is not None:
            self.outer_account_id = m.get('OuterAccountId')

        if m.get('OuterAccountType') is not None:
            self.outer_account_type = m.get('OuterAccountType')

        return self

