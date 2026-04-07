# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetSensitiveDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sensitive_data: Dict[str, Any] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the sensitive data returned. The information includes totalCount and sensDatas. sensDatas includes the following parameters:
        # 
        # *   guid: the ID of the metadata of the tenant. For example, the ID of the metadata in the MaxCompute compute engine is in the Project name.Table name.Column name format.
        # *   sensType: the type of the sensitive data.
        # *   sensLevel: the sensitivity level of the sensitive data
        self.sensitive_data = sensitive_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sensitive_data is not None:
            result['SensitiveData'] = self.sensitive_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SensitiveData') is not None:
            self.sensitive_data = m.get('SensitiveData')

        return self

