# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fnf20190315 import models as main_models
from darabonba.model import DaraModel

class ListFlowVersionsResponseBody(DaraModel):
    def __init__(
        self,
        flow_versions: List[main_models.ListFlowVersionsResponseBodyFlowVersions] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.flow_versions = flow_versions
        # list token
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.flow_versions:
            for v1 in self.flow_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FlowVersions'] = []
        if self.flow_versions is not None:
            for k1 in self.flow_versions:
                result['FlowVersions'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_versions = []
        if m.get('FlowVersions') is not None:
            for k1 in m.get('FlowVersions'):
                temp_model = main_models.ListFlowVersionsResponseBodyFlowVersions()
                self.flow_versions.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFlowVersionsResponseBodyFlowVersions(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        version: str = None,
    ):
        self.created_time = created_time
        self.description = description
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

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

