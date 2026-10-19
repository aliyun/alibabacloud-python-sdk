# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAccountAttributesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        log_enabled: bool = None,
        log_store_name: str = None,
        message_trace_enabled: bool = None,
        project_name: str = None,
    ):
        # Ensures the idempotence of the request. Generate a parameter value from your client to ensure that the value is unique across different requests. ClientToken supports only ASCII characters and cannot exceed 64 characters in length. For more information, see How to ensure idempotence.
        self.client_token = client_token
        # Specifies whether to enable the log management feature.
        self.log_enabled = log_enabled
        # The name of the Simple Log Service Logstore.
        self.log_store_name = log_store_name
        # Specifies whether to enable the message trace feature.
        self.message_trace_enabled = message_trace_enabled
        # The name of the Simple Log Service project.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.log_enabled is not None:
            result['LogEnabled'] = self.log_enabled

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.message_trace_enabled is not None:
            result['MessageTraceEnabled'] = self.message_trace_enabled

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('LogEnabled') is not None:
            self.log_enabled = m.get('LogEnabled')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('MessageTraceEnabled') is not None:
            self.message_trace_enabled = m.get('MessageTraceEnabled')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

