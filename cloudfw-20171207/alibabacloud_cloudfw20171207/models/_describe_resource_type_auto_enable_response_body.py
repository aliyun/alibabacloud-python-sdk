# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class DescribeResourceTypeAutoEnableResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_type_auto_enable: Dict[str, bool] = None,
    ):
        self.request_id = request_id
        self.resource_type_auto_enable = resource_type_auto_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_type_auto_enable is not None:
            result['ResourceTypeAutoEnable'] = self.resource_type_auto_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceTypeAutoEnable') is not None:
            self.resource_type_auto_enable = m.get('ResourceTypeAutoEnable')

        return self

