# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HttpConfig(DaraModel):
    def __init__(
        self,
        cookie: str = None,
        cookie_timeout: int = None,
        idle_timeout: int = None,
        request_timeout: int = None,
        scheduler: str = None,
        server_certificate_id: str = None,
        sticky_session: str = None,
        sticky_session_type: str = None,
        xforwarded_for: str = None,
    ):
        self.cookie = cookie
        self.cookie_timeout = cookie_timeout
        self.idle_timeout = idle_timeout
        self.request_timeout = request_timeout
        self.scheduler = scheduler
        self.server_certificate_id = server_certificate_id
        self.sticky_session = sticky_session
        self.sticky_session_type = sticky_session_type
        self.xforwarded_for = xforwarded_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cookie is not None:
            result['Cookie'] = self.cookie

        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id

        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session

        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type

        if self.xforwarded_for is not None:
            result['XForwardedFor'] = self.xforwarded_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')

        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')

        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')

        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')

        if m.get('XForwardedFor') is not None:
            self.xforwarded_for = m.get('XForwardedFor')

        return self

