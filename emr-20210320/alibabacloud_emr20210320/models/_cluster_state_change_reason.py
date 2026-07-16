# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ClusterStateChangeReason(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The status code for the state change. Valid values:
        # 
        # - UserRequest: A user request triggered the state change.
        # 
        # - OutOfStock: The requested ECS instance type is out of stock.
        # 
        # - NotAuthorized: The operation was denied due to insufficient permission.
        # 
        # - QuotaExceeded: The request exceeded a service quota.
        # 
        # - OperationDenied: The operation was denied.
        # 
        # - AccountException: An account-related exception occurred.
        # 
        # - NodeFailure: An ECS node failed.
        # 
        # - BootstrapFailure: A bootstrap action failed.
        # 
        # - ValidationFail: The request failed business logic validation.
        # 
        # - ServiceFailure: A dependent service failed.
        # 
        # - InternalError: An internal error occurred.
        self.code = code
        # A human-readable message detailing the cluster state change.
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

