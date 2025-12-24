# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAllCustomTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        custom_templates: str = None,
        request_id: str = None,
    ):
        # The template names and template configurations returned.
        self.custom_templates = custom_templates
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_templates is not None:
            result['CustomTemplates'] = self.custom_templates

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomTemplates') is not None:
            self.custom_templates = m.get('CustomTemplates')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

