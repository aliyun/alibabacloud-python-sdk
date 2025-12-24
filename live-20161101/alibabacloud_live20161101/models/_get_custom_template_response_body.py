# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCustomTemplateResponseBody(DaraModel):
    def __init__(
        self,
        custom_template: str = None,
        request_id: str = None,
        template: str = None,
    ):
        # The configurations of the template.
        self.custom_template = custom_template
        # The request ID.
        self.request_id = request_id
        # The name of the template.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_template is not None:
            result['CustomTemplate'] = self.custom_template

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template is not None:
            result['Template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomTemplate') is not None:
            self.custom_template = m.get('CustomTemplate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

