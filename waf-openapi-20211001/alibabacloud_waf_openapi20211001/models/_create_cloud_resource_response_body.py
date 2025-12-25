# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudResourceResponseBody(DaraModel):
    def __init__(
        self,
        cloud_resource_id: str = None,
        request_id: str = None,
    ):
        # The ID of the resource that is added to WAF. The ID is automatically generated.
        self.cloud_resource_id = cloud_resource_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_resource_id is not None:
            result['CloudResourceId'] = self.cloud_resource_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudResourceId') is not None:
            self.cloud_resource_id = m.get('CloudResourceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

