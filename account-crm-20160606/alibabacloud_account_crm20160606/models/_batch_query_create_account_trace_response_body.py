# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class BatchQueryCreateAccountTraceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        traces: List[main_models.BatchQueryCreateAccountTraceResponseBodyTraces] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.traces = traces

    def validate(self):
        if self.traces:
            for v1 in self.traces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['Traces'] = []
        if self.traces is not None:
            for k1 in self.traces:
                result['Traces'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.traces = []
        if m.get('Traces') is not None:
            for k1 in m.get('Traces'):
                temp_model = main_models.BatchQueryCreateAccountTraceResponseBodyTraces()
                self.traces.append(temp_model.from_map(k1))

        return self

class BatchQueryCreateAccountTraceResponseBodyTraces(DaraModel):
    def __init__(
        self,
        now_login_email: str = None,
        pk: str = None,
        status: str = None,
        trace_no: str = None,
    ):
        self.now_login_email = now_login_email
        self.pk = pk
        self.status = status
        self.trace_no = trace_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.now_login_email is not None:
            result['NowLoginEmail'] = self.now_login_email

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.status is not None:
            result['Status'] = self.status

        if self.trace_no is not None:
            result['TraceNo'] = self.trace_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NowLoginEmail') is not None:
            self.now_login_email = m.get('NowLoginEmail')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TraceNo') is not None:
            self.trace_no = m.get('TraceNo')

        return self

