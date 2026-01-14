# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecDatamaskResponseBody(DaraModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        # The de-identified data, which is described in a JSON string. The JSON string contains the following parameters:
        # 
        # *   **dataHeaderList**: the names of columns that contain the de-identified data.
        # *   **dataList**: the de-identified data. The column order of the de-identified data is the same as that indicated by the dataHeaderList parameter.
        # *   **ruleList**: the IDs of sensitive data detection rules.
        self.data = data
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

