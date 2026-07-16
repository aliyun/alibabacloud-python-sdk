# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTemplateScratchResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        template_scratch_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource scenario.
        self.template_scratch_id = template_scratch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')

        return self

