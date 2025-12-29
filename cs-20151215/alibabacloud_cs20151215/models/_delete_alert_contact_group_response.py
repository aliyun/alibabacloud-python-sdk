# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DeleteAlertContactGroupResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.DeleteAlertContactGroupResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.DeleteAlertContactGroupResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class DeleteAlertContactGroupResponseBody(DaraModel):
    def __init__(
        self,
        status: bool = None,
        msg: str = None,
        contact_group_id: str = None,
    ):
        # The deletion status.
        # 
        # *   true: The alert contact group was deleted.
        # *   false: The alert contact group failed to be deleted.
        self.status = status
        # The error message returned if the call fails.
        self.msg = msg
        # The alert contact group ID.
        self.contact_group_id = contact_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        if self.msg is not None:
            result['msg'] = self.msg

        if self.contact_group_id is not None:
            result['contact_group_id'] = self.contact_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('msg') is not None:
            self.msg = m.get('msg')

        if m.get('contact_group_id') is not None:
            self.contact_group_id = m.get('contact_group_id')

        return self

