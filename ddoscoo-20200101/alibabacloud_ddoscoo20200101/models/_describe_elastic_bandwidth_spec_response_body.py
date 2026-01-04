# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeElasticBandwidthSpecResponseBody(DaraModel):
    def __init__(
        self,
        elastic_bandwidth_spec: List[str] = None,
        request_id: str = None,
    ):
        # An array that consists of the available burstable protection bandwidths. Unit: Gbit/s.
        self.elastic_bandwidth_spec = elastic_bandwidth_spec
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_bandwidth_spec is not None:
            result['ElasticBandwidthSpec'] = self.elastic_bandwidth_spec

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticBandwidthSpec') is not None:
            self.elastic_bandwidth_spec = m.get('ElasticBandwidthSpec')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

