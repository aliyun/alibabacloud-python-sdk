# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAuditRequest(DaraModel):
    def __init__(
        self,
        audit_content: str = None,
    ):
        # The review results. You can specify the results for a maximum of 20 videos at a time. The value must be converted to a string. For more information about the parameters in AuditContent, see the "AuditContent" section of this topic.
        # 
        # This parameter is required.
        self.audit_content = audit_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_content is not None:
            result['AuditContent'] = self.audit_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditContent') is not None:
            self.audit_content = m.get('AuditContent')

        return self

