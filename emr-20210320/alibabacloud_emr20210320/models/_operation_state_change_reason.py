# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperationStateChangeReason(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The operation status code. Valid values:
        # 
        # - `UserRequest`: The operation was initiated by a user.
        # 
        # - `OutOfStock`: The requested ECS instance type is out of stock.
        # 
        # - `NotAuthorized`: You are not authorized to perform the operation.
        # 
        # - `QuotaExceeded`: A resource quota was exceeded.
        # 
        # - `OperationDenied`: The operation was denied.
        # 
        # - `AccountException`: An account exception occurred.
        # 
        # - `NodeFailure`: An ECS node failed.
        # 
        # - `BootstrapFailure`: A bootstrap action failed.
        # 
        # - `ValidationFail`: The business logic validation failed.
        # 
        # - `ServiceFailure`: A dependent service failed.
        # 
        # - `InternalError`: An internal error occurred.
        self.code = code
        # A human-readable message that provides details about the state change.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

