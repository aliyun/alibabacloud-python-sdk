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
        # The encoding mode of the `CommandContent` and `Output` response parameters. Valid values:
        # 
        # *   PlainText: returns the original command content and command outputs.
        # *   Base64 (default): returns the Base64-encoded command content and command output.
        self.content_encoding = content_encoding
        # Specifies whether to return the command outputs in the response.
        # 
        # *   true: returns the command outputs. When this parameter is set to true, you must specify `InvokeId`, `InstanceId`, or both.
        # *   false (default)
        self.include_output = include_output
        # The execution ID.
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        # The instance ID.
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

