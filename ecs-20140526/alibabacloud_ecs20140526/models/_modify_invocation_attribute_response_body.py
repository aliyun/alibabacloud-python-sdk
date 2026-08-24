# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInvocationAttributeResponseBody(DaraModel):
    def __init__(
        self,
        command_id: str = None,
        request_id: str = None,
    ):
        # The command ID.
        #    - A new command is created and the new `CommandId` is returned only when `CommandContent` is changed.
        #    - When `CommandContent` is not changed, no new command is created, and the `CommandId` of the currently executing command is returned.
        #    - If you called [InvokeCommand](https://help.aliyun.com/document_detail/64841.html), or called [RunCommand](https://help.aliyun.com/document_detail/141751.html) with `KeepCommand` set to `true`, the new command is retained. Otherwise, when the execution is completed or the task is manually stopped, all commands associated with the task are deleted.
        self.command_id = command_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

