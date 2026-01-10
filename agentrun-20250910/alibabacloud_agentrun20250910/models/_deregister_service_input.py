# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeregisterServiceInput(DaraModel):
    def __init__(
        self,
        service_name: str = None,
    ):
        # 要注销的服务名称（UUID格式）
        # 
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_name is not None:
            result['serviceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        return self

