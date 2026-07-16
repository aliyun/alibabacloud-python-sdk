# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableCheckResourceRequest(DaraModel):
    def __init__(
        self,
        resource_arn: str = None,
    ):
        # Unique resource identity
        # 
        # This parameter is required.
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        return self

