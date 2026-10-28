# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyQuotaTemplateServiceStatusRequest(DaraModel):
    def __init__(
        self,
        service_status: int = None,
    ):
        # The status of the quota template. Valid values:
        # 
        # - -1: The quota template is disabled.
        # 
        # - 1: The quota template is enabled.
        # 
        # This parameter is required.
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        return self

