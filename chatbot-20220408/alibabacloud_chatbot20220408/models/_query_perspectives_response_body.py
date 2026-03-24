# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class QueryPerspectivesResponseBody(DaraModel):
    def __init__(
        self,
        perspectives: List[main_models.QueryPerspectivesResponseBodyPerspectives] = None,
        request_id: str = None,
    ):
        self.perspectives = perspectives
        self.request_id = request_id

    def validate(self):
        if self.perspectives:
            for v1 in self.perspectives:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Perspectives'] = []
        if self.perspectives is not None:
            for k1 in self.perspectives:
                result['Perspectives'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.perspectives = []
        if m.get('Perspectives') is not None:
            for k1 in m.get('Perspectives'):
                temp_model = main_models.QueryPerspectivesResponseBodyPerspectives()
                self.perspectives.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryPerspectivesResponseBodyPerspectives(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        name: str = None,
        perspective_code: str = None,
        perspective_id: str = None,
        self_define: bool = None,
        status: int = None,
    ):
        self.create_time = create_time
        self.modify_time = modify_time
        self.name = name
        self.perspective_code = perspective_code
        self.perspective_id = perspective_id
        self.self_define = self_define
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.perspective_code is not None:
            result['PerspectiveCode'] = self.perspective_code

        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id

        if self.self_define is not None:
            result['SelfDefine'] = self.self_define

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PerspectiveCode') is not None:
            self.perspective_code = m.get('PerspectiveCode')

        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')

        if m.get('SelfDefine') is not None:
            self.self_define = m.get('SelfDefine')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

