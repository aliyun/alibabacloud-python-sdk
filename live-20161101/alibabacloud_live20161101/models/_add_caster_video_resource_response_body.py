# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCasterVideoResourceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource. This parameter can be used as a request parameter in the API operation that you can call to delete the video source in the production studio or modify the video source in the production studio.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

