# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BrowserSessionOut(DaraModel):
    def __init__(
        self,
        browser_id: str = None,
        browser_name: str = None,
        created_at: str = None,
        last_updated_at: str = None,
        session_id: str = None,
        session_idle_timeout_seconds: int = None,
        status: str = None,
    ):
        self.browser_id = browser_id
        self.browser_name = browser_name
        self.created_at = created_at
        self.last_updated_at = last_updated_at
        # This parameter is required.
        self.session_id = session_id
        # 会话空闲超时时间，单位为秒
        self.session_idle_timeout_seconds = session_idle_timeout_seconds
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.browser_id is not None:
            result['browserId'] = self.browser_id

        if self.browser_name is not None:
            result['browserName'] = self.browser_name

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.last_updated_at is not None:
            result['lastUpdatedAt'] = self.last_updated_at

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.session_idle_timeout_seconds is not None:
            result['sessionIdleTimeoutSeconds'] = self.session_idle_timeout_seconds

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('browserId') is not None:
            self.browser_id = m.get('browserId')

        if m.get('browserName') is not None:
            self.browser_name = m.get('browserName')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('lastUpdatedAt') is not None:
            self.last_updated_at = m.get('lastUpdatedAt')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('sessionIdleTimeoutSeconds') is not None:
            self.session_idle_timeout_seconds = m.get('sessionIdleTimeoutSeconds')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

