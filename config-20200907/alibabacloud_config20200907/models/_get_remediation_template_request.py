# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRemediationTemplateRequest(DaraModel):
    def __init__(
        self,
        template_identifier: str = None,
    ):
        # The ID of the automatic remediation template.
        # 
        # For more information about how to obtain the ID of a remediation template, see [Compliance library](https://help.aliyun.com/document_detail/2337741.html).
        self.template_identifier = template_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_identifier is not None:
            result['TemplateIdentifier'] = self.template_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateIdentifier') is not None:
            self.template_identifier = m.get('TemplateIdentifier')

        return self

