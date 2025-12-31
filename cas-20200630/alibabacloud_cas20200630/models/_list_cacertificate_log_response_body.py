# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class ListCACertificateLogResponseBody(DaraModel):
    def __init__(
        self,
        log_list: List[main_models.ListCACertificateLogResponseBodyLogList] = None,
        request_id: str = None,
    ):
        self.log_list = log_list
        self.request_id = request_id

    def validate(self):
        if self.log_list:
            for v1 in self.log_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogList'] = []
        if self.log_list is not None:
            for k1 in self.log_list:
                result['LogList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_list = []
        if m.get('LogList') is not None:
            for k1 in m.get('LogList'):
                temp_model = main_models.ListCACertificateLogResponseBodyLogList()
                self.log_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCACertificateLogResponseBodyLogList(DaraModel):
    def __init__(
        self,
        content: str = None,
        create_time: int = None,
        identifier: str = None,
        op_type: str = None,
    ):
        self.content = content
        self.create_time = create_time
        self.identifier = identifier
        self.op_type = op_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.op_type is not None:
            result['OpType'] = self.op_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')

        return self

