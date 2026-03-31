# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCloudResourceResponseBody(DaraModel):
    def __init__(
        self,
        cloud_resource: str = None,
        request_id: str = None,
    ):
        # The ID of the resource that is added to WAF.
        self.cloud_resource = cloud_resource
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_resource is not None:
            result['CloudResource'] = self.cloud_resource

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudResource') is not None:
            self.cloud_resource = m.get('CloudResource')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

