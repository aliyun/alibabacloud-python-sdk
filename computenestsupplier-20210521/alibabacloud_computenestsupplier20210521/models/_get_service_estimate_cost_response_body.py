# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetServiceEstimateCostResponseBody(DaraModel):
    def __init__(
        self,
        commodity: Dict[str, Any] = None,
        request_id: str = None,
        resources: Dict[str, Any] = None,
    ):
        # The subscription duration information about the purchase order of Alibaba Cloud Marketplace.
        self.commodity = commodity
        # The request ID.
        self.request_id = request_id
        # The list of resources.
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity is not None:
            result['Commodity'] = self.commodity

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resources is not None:
            result['Resources'] = self.resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commodity') is not None:
            self.commodity = m.get('Commodity')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        return self

