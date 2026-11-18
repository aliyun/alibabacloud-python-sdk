# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class RunAppInstanceCommandResponseBody(DaraModel):
    def __init__(
        self,
        command_result_model: main_models.RunAppInstanceCommandResponseBodyCommandResultModel = None,
        request_id: str = None,
    ):
        # The command issuance result.
        self.command_result_model = command_result_model
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.command_result_model:
            self.command_result_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_result_model is not None:
            result['CommandResultModel'] = self.command_result_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandResultModel') is not None:
            temp_model = main_models.RunAppInstanceCommandResponseBodyCommandResultModel()
            self.command_result_model = temp_model.from_map(m.get('CommandResultModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RunAppInstanceCommandResponseBodyCommandResultModel(DaraModel):
    def __init__(
        self,
        invocation_id: str = None,
    ):
        # The command execution ID. When commands are issued in batches to multiple delivery groups, only one execution ID is returned. You can use this ID to call the ListCommandInvocationResults operation to query the command execution results on each session.
        self.invocation_id = invocation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')

        return self

