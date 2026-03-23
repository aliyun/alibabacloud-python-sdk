# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEdgeFunctionResponseBody(DaraModel):
    def __init__(
        self,
        edge_function_name: str = None,
        instance_name: str = None,
        request_id: str = None,
    ):
        # The name of the edge function.
        self.edge_function_name = edge_function_name
        # The ID of the RDS Supabase instance.
        self.instance_name = instance_name
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edge_function_name is not None:
            result['EdgeFunctionName'] = self.edge_function_name

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EdgeFunctionName') is not None:
            self.edge_function_name = m.get('EdgeFunctionName')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

