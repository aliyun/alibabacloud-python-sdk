# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CookieSessionAffinityConfig(DaraModel):
    def __init__(
        self,
        disable_session_id_reuse: bool = None,
        session_concurrency_per_instance: int = None,
        session_idle_timeout_in_seconds: int = None,
        session_ttlin_seconds: int = None,
    ):
        # The default value is \\`false\\`. When set to \\`false\\`, a request with the same session ID can be sent after the session expires. The system treats this as a new session and attaches it to a new instance. When set to \\`true\\`, the session ID cannot be reused after the session expires.
        self.disable_session_id_reuse = disable_session_id_reuse
        # The maximum number of sessions that a single instance can process at the same time. The value must be an integer from 1 to 200.
        self.session_concurrency_per_instance = session_concurrency_per_instance
        # The duration in seconds that a session can remain idle. If a user is inactive for this period, the session is considered idle. The maximum duration is limited by the session\\"s lifecycle. The value must be between 0 and 21,600.
        self.session_idle_timeout_in_seconds = session_idle_timeout_in_seconds
        # The total lifecycle of a session in seconds, from creation to destruction. After this period, Function Compute automatically destroys the session and no longer guarantees affinity. The value must be an integer from 1 to 21,600.
        self.session_ttlin_seconds = session_ttlin_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable_session_id_reuse is not None:
            result['disableSessionIdReuse'] = self.disable_session_id_reuse

        if self.session_concurrency_per_instance is not None:
            result['sessionConcurrencyPerInstance'] = self.session_concurrency_per_instance

        if self.session_idle_timeout_in_seconds is not None:
            result['sessionIdleTimeoutInSeconds'] = self.session_idle_timeout_in_seconds

        if self.session_ttlin_seconds is not None:
            result['sessionTTLInSeconds'] = self.session_ttlin_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disableSessionIdReuse') is not None:
            self.disable_session_id_reuse = m.get('disableSessionIdReuse')

        if m.get('sessionConcurrencyPerInstance') is not None:
            self.session_concurrency_per_instance = m.get('sessionConcurrencyPerInstance')

        if m.get('sessionIdleTimeoutInSeconds') is not None:
            self.session_idle_timeout_in_seconds = m.get('sessionIdleTimeoutInSeconds')

        if m.get('sessionTTLInSeconds') is not None:
            self.session_ttlin_seconds = m.get('sessionTTLInSeconds')

        return self

