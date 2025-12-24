# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateImageComponentResponseBody(DaraModel):
    def __init__(
        self,
        image_component_id: str = None,
        request_id: str = None,
    ):
        # The ID of the image component.
        self.image_component_id = image_component_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_component_id is not None:
            result['ImageComponentId'] = self.image_component_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageComponentId') is not None:
            self.image_component_id = m.get('ImageComponentId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

