# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DiagnoseVpnGatewayResponseBody(DaraModel):
    def __init__(
        self,
        diagnose_id: str = None,
        request_id: str = None,
    ):
        # The diagnostic ID.
        # 
        # After a diagnostic ID is returned, you can call [GetVpnGatewayDiagnoseResult](https://help.aliyun.com/document_detail/2521963.html) to query the diagnostic report.
        self.diagnose_id = diagnose_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnose_id is not None:
            result['DiagnoseId'] = self.diagnose_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnoseId') is not None:
            self.diagnose_id = m.get('DiagnoseId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

