# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateChangeSetResponseBody(DaraModel):
    def __init__(
        self,
        change_set_id: str = None,
        request_id: str = None,
        stack_id: str = None,
    ):
        # The ID of the change set.
        self.change_set_id = change_set_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the stack.
        self.stack_id = stack_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_set_id is not None:
            result['ChangeSetId'] = self.change_set_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stack_id is not None:
            result['StackId'] = self.stack_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeSetId') is not None:
            self.change_set_id = m.get('ChangeSetId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')

        return self

