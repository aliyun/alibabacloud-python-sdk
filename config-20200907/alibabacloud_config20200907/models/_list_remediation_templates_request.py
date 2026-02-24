# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRemediationTemplatesRequest(DaraModel):
    def __init__(
        self,
        managed_rule_identifier: str = None,
        page_number: int = None,
        page_size: int = None,
        remediation_type: str = None,
    ):
        self.managed_rule_identifier = managed_rule_identifier
        self.page_number = page_number
        self.page_size = page_size
        self.remediation_type = remediation_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remediation_type is not None:
            result['RemediationType'] = self.remediation_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RemediationType') is not None:
            self.remediation_type = m.get('RemediationType')

        return self

