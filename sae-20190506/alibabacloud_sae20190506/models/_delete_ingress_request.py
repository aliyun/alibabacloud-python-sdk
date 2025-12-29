# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteIngressRequest(DaraModel):
    def __init__(
        self,
        ingress_id: int = None,
    ):
        # The ID of the routing rule that you want to delete. You can call the [ListIngresses](https://help.aliyun.com/document_detail/153934.html) operation to obtain the ID of a routing rule.
        # 
        # This parameter is required.
        self.ingress_id = ingress_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')

        return self

