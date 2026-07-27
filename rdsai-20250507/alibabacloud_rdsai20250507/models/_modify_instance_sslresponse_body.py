# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceSSLResponseBody(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.branch_name = branch_name
        # The instance ID of the AI application.
        self.instance_name = instance_name
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

