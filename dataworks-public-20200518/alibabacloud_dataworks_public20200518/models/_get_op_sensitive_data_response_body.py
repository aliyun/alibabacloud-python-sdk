# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOpSensitiveDataResponseBody(DaraModel):
    def __init__(
        self,
        op_sensitive_data: str = None,
        request_id: str = None,
    ):
        # The information about the access records of the sensitive data. The information includes totalCount and opRiskDatas. opRiskDatas includes the following parameters:
        # 
        # *   sensType: the type of the sensitive data.
        # *   sensLevel: the sensitivity level of the sensitive data. A larger value indicates a higher sensitivity level.
        # *   opType: the type of the operation.
        # *   sql: the SQL statement that is executed.
        # *   opAccount: the account that is used to perform the operation.
        # *   opTime: the time when the operation was performed.
        self.op_sensitive_data = op_sensitive_data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_sensitive_data is not None:
            result['OpSensitiveData'] = self.op_sensitive_data

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpSensitiveData') is not None:
            self.op_sensitive_data = m.get('OpSensitiveData')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

