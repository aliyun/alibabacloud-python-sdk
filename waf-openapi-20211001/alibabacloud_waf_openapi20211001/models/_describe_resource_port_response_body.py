# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeResourcePortResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_ports: List[str] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # An array of HTTP and HTTPS listener ports that are added to the WAF instance.
        self.resource_ports = resource_ports

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_ports is not None:
            result['ResourcePorts'] = self.resource_ports

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourcePorts') is not None:
            self.resource_ports = m.get('ResourcePorts')

        return self

