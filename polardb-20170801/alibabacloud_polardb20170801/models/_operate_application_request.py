# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateApplicationRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        operation: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The operation type. Valid values:
        # 
        # * **restart**: restart
        # * **stop**: stop
        # * **start**: start.
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.operation is not None:
            result['Operation'] = self.operation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        return self

