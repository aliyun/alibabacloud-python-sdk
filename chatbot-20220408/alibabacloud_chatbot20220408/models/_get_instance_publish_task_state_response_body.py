# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from darabonba.model import DaraModel

class GetInstancePublishTaskStateResponseBody(DaraModel):
    def __init__(
        self,
        biz_type_list: List[str] = None,
        create_time: str = None,
        error: str = None,
        errors: Dict[str, Any] = None,
        id: int = None,
        modify_time: str = None,
        request_id: str = None,
        response: str = None,
        status: str = None,
        warnings: Dict[str, Any] = None,
    ):
        self.biz_type_list = biz_type_list
        self.create_time = create_time
        self.error = error
        self.errors = errors
        self.id = id
        self.modify_time = modify_time
        self.request_id = request_id
        self.response = response
        self.status = status
        self.warnings = warnings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error is not None:
            result['Error'] = self.error

        if self.errors is not None:
            result['Errors'] = self.errors

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.response is not None:
            result['Response'] = self.response

        if self.status is not None:
            result['Status'] = self.status

        if self.warnings is not None:
            result['Warnings'] = self.warnings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Errors') is not None:
            self.errors = m.get('Errors')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Response') is not None:
            self.response = m.get('Response')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Warnings') is not None:
            self.warnings = m.get('Warnings')

        return self

