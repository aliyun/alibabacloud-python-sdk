# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveContactTemplateResponseBody(DaraModel):
    def __init__(
        self,
        contact_template_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.contact_template_id = contact_template_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_template_id is not None:
            result['ContactTemplateId'] = self.contact_template_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactTemplateId') is not None:
            self.contact_template_id = m.get('ContactTemplateId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

