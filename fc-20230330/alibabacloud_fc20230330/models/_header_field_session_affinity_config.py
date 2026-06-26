# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HeaderFieldSessionAffinityConfig(DaraModel):
    def __init__(
        self,
        affinity_header_field_name: str = None,
        disable_session_id_reuse: bool = None,
        session_concurrency_per_instance: int = None,
        session_idle_timeout_in_seconds: int = None,
        session_ttlin_seconds: int = None,
    ):
        # The name of the HTTP request header that passes the client session identity. The name must be 5 to 40 characters long, start with a letter, and contain only letters, numbers, hyphens (-), and underscores (_). The name cannot start with the x-fc- prefix.
        self.affinity_header_field_name = affinity_header_field_name
        # The default value is False. If set to False, a session ID can be reused in a new request after the original session expires. The system treats this as a new session and attaches it to a new instance. If set to True, an expired session ID cannot be reused.
        self.disable_session_id_reuse = disable_session_id_reuse
        # The maximum number of sessions that a single instance can process simultaneously. The value must be an integer from 1 to 200.
        self.session_concurrency_per_instance = session_concurrency_per_instance
        # The idle timeout period for a session in seconds. A session becomes idle if no operations are performed within this period. The maximum value cannot exceed the session\\"s TTL. The value must be an integer from 0 to 21600.
        self.session_idle_timeout_in_seconds = session_idle_timeout_in_seconds
        # The session\\"s Time to Live (TTL) in seconds. This defines the entire lifecycle of a session, from creation to destruction. After this period expires, Function Compute automatically destroys the session and no longer guarantees affinity. The value must be an integer from 1 to 21600.
        self.session_ttlin_seconds = session_ttlin_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affinity_header_field_name is not None:
            result['affinityHeaderFieldName'] = self.affinity_header_field_name

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
        if m.get('affinityHeaderFieldName') is not None:
            self.affinity_header_field_name = m.get('affinityHeaderFieldName')

        if m.get('disableSessionIdReuse') is not None:
            self.disable_session_id_reuse = m.get('disableSessionIdReuse')

        if m.get('sessionConcurrencyPerInstance') is not None:
            self.session_concurrency_per_instance = m.get('sessionConcurrencyPerInstance')

        if m.get('sessionIdleTimeoutInSeconds') is not None:
            self.session_idle_timeout_in_seconds = m.get('sessionIdleTimeoutInSeconds')

        if m.get('sessionTTLInSeconds') is not None:
            self.session_ttlin_seconds = m.get('sessionTTLInSeconds')

        return self

