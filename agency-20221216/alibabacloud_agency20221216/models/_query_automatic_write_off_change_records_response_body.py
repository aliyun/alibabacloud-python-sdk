# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class QueryAutomaticWriteOffChangeRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.QueryAutomaticWriteOffChangeRecordsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryAutomaticWriteOffChangeRecordsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryAutomaticWriteOffChangeRecordsResponseBodyData(DaraModel):
    def __init__(
        self,
        change_content: str = None,
        operate_id: str = None,
        operate_source: str = None,
        operation_time: str = None,
    ):
        self.change_content = change_content
        self.operate_id = operate_id
        self.operate_source = operate_source
        self.operation_time = operation_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_content is not None:
            result['ChangeContent'] = self.change_content

        if self.operate_id is not None:
            result['OperateId'] = self.operate_id

        if self.operate_source is not None:
            result['OperateSource'] = self.operate_source

        if self.operation_time is not None:
            result['OperationTime'] = self.operation_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeContent') is not None:
            self.change_content = m.get('ChangeContent')

        if m.get('OperateId') is not None:
            self.operate_id = m.get('OperateId')

        if m.get('OperateSource') is not None:
            self.operate_source = m.get('OperateSource')

        if m.get('OperationTime') is not None:
            self.operation_time = m.get('OperationTime')

        return self

