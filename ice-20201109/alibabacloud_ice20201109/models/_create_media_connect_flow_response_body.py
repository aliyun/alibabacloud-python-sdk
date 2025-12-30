# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class CreateMediaConnectFlowResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.CreateMediaConnectFlowResponseBodyContent = None,
        description: str = None,
        request_id: str = None,
        ret_code: int = None,
    ):
        # The response body.
        self.content = content
        # The returned message.
        self.description = description
        # The ID of the request.
        self.request_id = request_id
        # The returned error code. A value of 0 indicates the call is successful.
        self.ret_code = ret_code

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ret_code is not None:
            result['RetCode'] = self.ret_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.CreateMediaConnectFlowResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')

        return self

class CreateMediaConnectFlowResponseBodyContent(DaraModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        # The flow ID.
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        return self

