# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckAssumeSlrRoleResponseBody(DaraModel):
    def __init__(
        self,
        error_msg: str = None,
        is_exist: str = None,
        request_id: str = None,
    ):
        self.error_msg = error_msg
        self.is_exist = is_exist
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.is_exist is not None:
            result['IsExist'] = self.is_exist

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('IsExist') is not None:
            self.is_exist = m.get('IsExist')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

