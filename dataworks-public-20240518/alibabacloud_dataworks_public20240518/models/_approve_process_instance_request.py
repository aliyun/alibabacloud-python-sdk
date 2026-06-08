# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApproveProcessInstanceRequest(DaraModel):
    def __init__(
        self,
        approval_action: str = None,
        approval_comment: str = None,
        client_token: str = None,
        process_instance_id: str = None,
    ):
        # This parameter is required.
        self.approval_action = approval_action
        # This parameter is required.
        self.approval_comment = approval_comment
        self.client_token = client_token
        # This parameter is required.
        self.process_instance_id = process_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_action is not None:
            result['ApprovalAction'] = self.approval_action

        if self.approval_comment is not None:
            result['ApprovalComment'] = self.approval_comment

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalAction') is not None:
            self.approval_action = m.get('ApprovalAction')

        if m.get('ApprovalComment') is not None:
            self.approval_comment = m.get('ApprovalComment')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')

        return self

