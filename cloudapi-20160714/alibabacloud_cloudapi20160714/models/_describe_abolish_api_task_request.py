# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAbolishApiTaskRequest(DaraModel):
    def __init__(
        self,
        operation_uid: str = None,
        security_token: str = None,
    ):
        # The ID of the unpublishing operation.
        # 
        # This parameter is required.
        self.operation_uid = operation_uid
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_uid is not None:
            result['OperationUid'] = self.operation_uid

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationUid') is not None:
            self.operation_uid = m.get('OperationUid')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

