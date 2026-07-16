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
        # The data after it is masked. The data is a string in JSON format and includes the following fields:
        # 
        # - **dataHeaderList**: The column names of the masked data.
        # 
        # - **dataList**: The masked data. The order of the fields corresponds to the order of the column names.
        # 
        # - **ruleList**: The sensitive data type IDs. Each ID corresponds to the unique ID of a sensitive data type that is returned by the [DescribeRules](https://help.aliyun.com/document_detail/410141.html) operation.
        self.data = data
        # The ID of the request. Alibaba Cloud generates a unique ID for each request. You can use this ID to troubleshoot issues.
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

