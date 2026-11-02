# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServiceLinkedRoleTemplateRequest(DaraModel):
    def __init__(
        self,
        service_name: str = None,
    ):
        # The cloud service name.
        # 
        # For more information, see the **Cloud service identity** column in [Cloud services that support service-linked roles](https://help.aliyun.com/document_detail/461722.html).
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

