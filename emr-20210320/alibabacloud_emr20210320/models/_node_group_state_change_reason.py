# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NodeGroupStateChangeReason(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The status code for the state change. Valid values include:
        # 
        # - `UserRequest`: A user request triggered the change.
        # 
        # - `OutOfStock`: The requested ECS instance type is out of stock.
        # 
        # - `NotAuthorized`: The request lacks the required permissions.
        # 
        # - `QuotaExceeded`: The request exceeds the resource quota.
        # 
        # - `OperationDenied`: The system denied the operation.
        # 
        # - `AccountException`: An account exception occurred.
        # 
        # - `NodeFailure`: An ECS node failed.
        # 
        # - `BootstrapFailure`: The bootstrap process failed.
        # 
        # - `ValidationFail`: The request parameters failed validation.
        # 
        # - `ServiceFailure`: A dependent service failed.
        # 
        # - `InternalError`: An unexpected internal error occurred.
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

