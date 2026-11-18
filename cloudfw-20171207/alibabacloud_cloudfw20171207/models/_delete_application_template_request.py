# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteApplicationTemplateRequest(DaraModel):
    def __init__(
        self,
        application_template_id: str = None,
    ):
        # The ID of the application program template to delete. This parameter is required. If you leave this parameter empty, a parameter fault is returned. The template must exist within the current Alibaba Cloud account. You cannot delete a template if it contains custom application program rules or is referenced by an access control policy of the Internet border, NAT, or virtual private cloud (VPC) firewalls.
        self.application_template_id = application_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')

        return self

