# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        template_body: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The content of the template.
        # 
        # For more information about the template syntax, see [Structure of Terraform templates](https://help.aliyun.com/document_detail/184397.html).
        self.template_body = template_body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.template_body is not None:
            result['TemplateBody'] = self.template_body

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        return self

