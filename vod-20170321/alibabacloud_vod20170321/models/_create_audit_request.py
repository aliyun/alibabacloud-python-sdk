# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAuditRequest(DaraModel):
    def __init__(
        self,
        audit_content: str = None,
    ):
        # The array of review content.
        # 
        # A maximum of **100** audio or video entries can be reviewed at a time. Convert the array to a string before passing it as the parameter value.
        # 
        # For the specific parameter structure, see the **AuditContent** table below.
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

