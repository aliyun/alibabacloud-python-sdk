# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeServiceMirrorResponseBody(DaraModel):
    def __init__(
        self,
        ratio: str = None,
        request_id: str = None,
        service_name: str = None,
        target: str = None,
    ):
        # The percentage of traffic that you want to mirror. Valid values: 0 to 100.
        self.ratio = ratio
        # The request ID.
        self.request_id = request_id
        # The service name.
        self.service_name = service_name
        # The destination services to which you want to mirror traffic.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ratio is not None:
            result['Ratio'] = self.ratio

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

