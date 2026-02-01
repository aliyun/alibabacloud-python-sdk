# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetListRecordResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetListRecordResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.total = total

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
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetListRecordResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class GetListRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        analysis_id: str = None,
        analysis_time: str = None,
        arguments: str = None,
        failed_log: str = None,
        status: str = None,
    ):
        self.analysis_id = analysis_id
        self.analysis_time = analysis_time
        self.arguments = arguments
        self.failed_log = failed_log
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id

        if self.analysis_time is not None:
            result['analysisTime'] = self.analysis_time

        if self.arguments is not None:
            result['arguments'] = self.arguments

        if self.failed_log is not None:
            result['failedLog'] = self.failed_log

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')

        if m.get('analysisTime') is not None:
            self.analysis_time = m.get('analysisTime')

        if m.get('arguments') is not None:
            self.arguments = m.get('arguments')

        if m.get('failedLog') is not None:
            self.failed_log = m.get('failedLog')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

