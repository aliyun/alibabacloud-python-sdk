# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateYaoChiAgentConfirmResponseBody(DaraModel):
    def __init__(
        self,
        approved: bool = None,
        confirmation_id: str = None,
        request_id: str = None,
        status: str = None,
        tool_args_received: bool = None,
    ):
        # The confirmation decision submitted in this request, which is the same as the Approved request parameter. A value of true indicates that the execution is approved, and false indicates that the execution is rejected. This does not indicate whether the tool operation is executed successfully.
        self.approved = approved
        # The identifier of the operation for which the confirmation is submitted, which is the same as the ConfirmationId request parameter.
        self.confirmation_id = confirmation_id
        # The unique identifier of the request, which is used for troubleshooting and log tracing.
        self.request_id = request_id
        # The status string. The example value success refers to the outer success status of the downstream confirmation callback response and is provided only for format demonstration. It does not mean that the Status field of the current operation actually returns this value. In the current version, this field may be empty or not returned. Do not rely on this field to determine whether the execution is approved or whether the tool is executed successfully.
        self.status = status
        # Specifies whether custom tool parameters are received. A value of true indicates that non-null parameters are provided, and false indicates that no parameters are provided. This does not indicate that the parameters are applied or that the tool is executed successfully. In the current version, omit the ToolArgs request parameter, and this field normally returns false.
        self.tool_args_received = tool_args_received

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approved is not None:
            result['Approved'] = self.approved

        if self.confirmation_id is not None:
            result['ConfirmationId'] = self.confirmation_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tool_args_received is not None:
            result['ToolArgsReceived'] = self.tool_args_received

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Approved') is not None:
            self.approved = m.get('Approved')

        if m.get('ConfirmationId') is not None:
            self.confirmation_id = m.get('ConfirmationId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ToolArgsReceived') is not None:
            self.tool_args_received = m.get('ToolArgsReceived')

        return self

