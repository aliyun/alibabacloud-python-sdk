# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_companyreg20200306 import models as main_models
from darabonba.model import DaraModel

class QueryCallRecordListResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryCallRecordListResponseBodyData] = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryCallRecordListResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryCallRecordListResponseBodyData(DaraModel):
    def __init__(
        self,
        contact_disposition: str = None,
        duration: int = None,
        signature_url: str = None,
        start_time: int = None,
        task_id: str = None,
    ):
        self.contact_disposition = contact_disposition
        self.duration = duration
        self.signature_url = signature_url
        self.start_time = start_time
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_disposition is not None:
            result['ContactDisposition'] = self.contact_disposition

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.signature_url is not None:
            result['SignatureUrl'] = self.signature_url

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactDisposition') is not None:
            self.contact_disposition = m.get('ContactDisposition')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('SignatureUrl') is not None:
            self.signature_url = m.get('SignatureUrl')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

