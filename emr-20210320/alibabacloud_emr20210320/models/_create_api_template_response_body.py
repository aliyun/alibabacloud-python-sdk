# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateApiTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        success: str = None,
        template_id: str = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Template ID (to be deprecated).
        self.success = success
        # Template ID (it is recommended to use the parameter TemplateId).
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

