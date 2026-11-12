# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFirewallTemplateResponseBody(DaraModel):
    def __init__(
        self,
        firewall_template_id: str = None,
        request_id: str = None,
    ):
        # The firewall template ID.
        self.firewall_template_id = firewall_template_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.firewall_template_id is not None:
            result['FirewallTemplateId'] = self.firewall_template_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallTemplateId') is not None:
            self.firewall_template_id = m.get('FirewallTemplateId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

