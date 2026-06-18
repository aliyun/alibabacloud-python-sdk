# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInvocationsRequest(DaraModel):
    def __init__(
        self,
        content_encoding: str = None,
        include_output: bool = None,
        invoke_id: str = None,
        node_id: str = None,
    ):
        # The encoding mode of the `CommandContent` and `Output` fields in the response. Valid values:
        # 
        # - PlainText: Returns the original command content and output.
        # 
        # - Base64 (default): Returns the Base64-encoded command content and output.
        self.content_encoding = content_encoding
        # Specifies whether to include the command output in the response.
        # 
        # - true: Returns the output. You must specify the `InvokeId` or `NodeId` parameter.
        # 
        # - false (default): Does not return the output.
        self.include_output = include_output
        # The ID of the command execution.
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        # The ID of the instance.
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.include_output is not None:
            result['IncludeOutput'] = self.include_output

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('IncludeOutput') is not None:
            self.include_output = m.get('IncludeOutput')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

