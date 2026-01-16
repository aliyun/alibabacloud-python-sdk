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
        self.affinity_header_field_name = affinity_header_field_name
        self.disable_session_id_reuse = disable_session_id_reuse
        self.session_concurrency_per_instance = session_concurrency_per_instance
        self.session_idle_timeout_in_seconds = session_idle_timeout_in_seconds
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

