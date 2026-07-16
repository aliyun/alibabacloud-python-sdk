# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateStackTemplateByResourcesResponseBody(DaraModel):
    def __init__(
        self,
        new_template_body: str = None,
        old_template_body: str = None,
        request_id: str = None,
    ):
        # The template content after correction.
        self.new_template_body = new_template_body
        # The template content before correction.
        self.old_template_body = old_template_body
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_template_body is not None:
            result['NewTemplateBody'] = self.new_template_body

        if self.old_template_body is not None:
            result['OldTemplateBody'] = self.old_template_body

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewTemplateBody') is not None:
            self.new_template_body = m.get('NewTemplateBody')

        if m.get('OldTemplateBody') is not None:
            self.old_template_body = m.get('OldTemplateBody')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

