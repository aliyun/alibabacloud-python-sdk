# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateChatSessionRequest(DaraModel):
    def __init__(
        self,
        model: str = None,
        session_id: str = None,
        tenant_id: str = None,
        title: str = None,
    ):
        # The abstract model name (model tier). If not specified, the current model of the session is not modified.
        self.model = model
        # The session ID.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The new session title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model is not None:
            result['model'] = self.model

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

