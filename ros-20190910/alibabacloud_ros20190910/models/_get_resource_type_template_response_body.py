# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetResourceTypeTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        template_body: Dict[str, Any] = None,
        template_content: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The structure that contains the template body. The template body must be 1 to 51,200 bytes in length. For more information, see [Template syntax](https://help.aliyun.com/document_detail/28857.html).
        # 
        # > We recommend that use TemplateContent instead of TemplateBody.
        self.template_body = template_body
        # The JSON-formatted structure of the template body. For more information, see [Template syntax](https://help.aliyun.com/document_detail/28857.html).
        self.template_content = template_content

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

        if self.template_content is not None:
            result['TemplateContent'] = self.template_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')

        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')

        return self

