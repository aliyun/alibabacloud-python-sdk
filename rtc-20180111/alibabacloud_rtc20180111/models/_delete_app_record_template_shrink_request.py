# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAppRecordTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        client_token: str = None,
        template_shrink: str = None,
    ):
        # The application ID. You can create and query the ID in the console. Only a single ID is supported.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The idempotency parameter.
        self.client_token = client_token
        # The template information.
        # 
        # This parameter is required.
        self.template_shrink = template_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.template_shrink is not None:
            result['Template'] = self.template_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Template') is not None:
            self.template_shrink = m.get('Template')

        return self

