# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWebFilterTemplateRequest(DaraModel):
    def __init__(
        self,
        web_filter_template_id: str = None,
    ):
        # The ID of the web filtering template to delete. This parameter is required. If you leave this parameter empty, a parameter fault is returned. The template must exist within the current Alibaba Cloud account. A template cannot be deleted if it is referenced by an access control policy of the Internet border, NAT firewalls, or virtual private cloud (VPC) firewalls.
        self.web_filter_template_id = web_filter_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.web_filter_template_id is not None:
            result['WebFilterTemplateId'] = self.web_filter_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WebFilterTemplateId') is not None:
            self.web_filter_template_id = m.get('WebFilterTemplateId')

        return self

