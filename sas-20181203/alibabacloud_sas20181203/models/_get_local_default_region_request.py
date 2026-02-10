# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLocalDefaultRegionRequest(DaraModel):
    def __init__(
        self,
        vendor: str = None,
    ):
        # The cloud service provider. Valid values:
        # 
        # *   **Tencent**: Tencent Cloud.
        # *   **HUAWEICLOUD**: Huawei Cloud.
        # *   **Azure**: Microsoft Azure.
        # *   **AWS**: Amazon Web Services (AWS).
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

