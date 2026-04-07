# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOpRiskDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risk_data: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the high-risk sensitive data. The information includes totalCount and opRiskDatas. opRiskDatas includes the following parameters:
        # 
        # *   sensType: the type of the sensitive data
        # *   sensLevel: the sensitivity level of the sensitive data
        # *   opType: the type of the operation
        # *   sql: the SQL statement that is executed
        # *   opAccount: the account that is used to perform the operation
        # *   opTime: the time when the operation was performed
        self.risk_data = risk_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_data is not None:
            result['RiskData'] = self.risk_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskData') is not None:
            self.risk_data = m.get('RiskData')

        return self

