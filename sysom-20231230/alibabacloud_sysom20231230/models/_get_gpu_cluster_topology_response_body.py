# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetGpuClusterTopologyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetGpuClusterTopologyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The result code. Valid values: Success, Sysom.ServerError, Sysom.InvalidParameter.
        self.code = code
        # The data returned by the operation.
        self.data = data
        # The error message returned when the code is not Success.
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetGpuClusterTopologyResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGpuClusterTopologyResponseBodyData(DaraModel):
    def __init__(
        self,
        data: main_models.GetGpuClusterTopologyResponseBodyDataData = None,
        total: int = None,
    ):
        # The cluster topology data structure.
        self.data = data
        # The number of GPU cards returned.
        self.total = total

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetGpuClusterTopologyResponseBodyDataData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class GetGpuClusterTopologyResponseBodyDataData(DaraModel):
    def __init__(
        self,
        edges: Any = None,
        nodes: Any = None,
    ):
        # The edge data in the topology structure.
        self.edges = edges
        # The node data in the topology structure.
        self.nodes = nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edges is not None:
            result['edges'] = self.edges

        if self.nodes is not None:
            result['nodes'] = self.nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edges') is not None:
            self.edges = m.get('edges')

        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')

        return self

