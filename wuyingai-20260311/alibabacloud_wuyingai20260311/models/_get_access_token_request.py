# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAccessTokenRequest(DaraModel):
    def __init__(
        self,
        external_user_id: str = None,
        template_id: str = None,
    ):
        # The unique identifier of the user in the external system.
        self.external_user_id = external_user_id
        # The ID of the agent template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

