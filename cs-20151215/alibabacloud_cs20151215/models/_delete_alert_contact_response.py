# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DeleteAlertContactResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: main_models.DeleteAlertContactResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        if m.get('body') is not None:
            temp_model = main_models.DeleteAlertContactResponseBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class DeleteAlertContactResponseBody(DaraModel):
    def __init__(
        self,
        result: List[main_models.DeleteAlertContactResponseBodyResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('result') is not None:
            for k1 in m.get('result'):
                temp_model = main_models.DeleteAlertContactResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class DeleteAlertContactResponseBodyResult(DaraModel):
    def __init__(
        self,
        status: bool = None,
        msg: str = None,
        contact_id: str = None,
    ):
        # The deletion status.
        # 
        # *   true: The alert contact was deleted.
        # *   false: The alert contact failed to be deleted.
        self.status = status
        # The error message returned if the call fails.
        self.msg = msg
        # An alert contact ID.
        self.contact_id = contact_id

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

        if self.contact_id is not None:
            result['contact_id'] = self.contact_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('msg') is not None:
            self.msg = m.get('msg')

        if m.get('contact_id') is not None:
            self.contact_id = m.get('contact_id')

        return self

