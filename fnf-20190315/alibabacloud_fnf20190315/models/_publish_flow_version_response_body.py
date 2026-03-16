# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PublishFlowVersionResponseBody(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        flow_name: str = None,
        request_id: str = None,
        version: str = None,
    ):
        self.created_time = created_time
        self.description = description
        self.flow_name = flow_name
        # Id of the request
        self.request_id = request_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

