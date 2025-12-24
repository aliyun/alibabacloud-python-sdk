# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveCdnDiagnoseInfoRequest(DaraModel):
    def __init__(
        self,
        security_token: str = None,
        app: str = None,
        domain: str = None,
        end_time: int = None,
        interval_type: str = None,
        phase: int = None,
        request_type: str = None,
        start_time: int = None,
        stream_name: str = None,
        stream_suffix: str = None,
    ):
        self.security_token = security_token
        # This parameter is required.
        self.app = app
        # This parameter is required.
        self.domain = domain
        # This parameter is required.
        self.end_time = end_time
        self.interval_type = interval_type
        # This parameter is required.
        self.phase = phase
        self.request_type = request_type
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.stream_name = stream_name
        # This parameter is required.
        self.stream_suffix = stream_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.app is not None:
            result['app'] = self.app

        if self.domain is not None:
            result['domain'] = self.domain

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.interval_type is not None:
            result['intervalType'] = self.interval_type

        if self.phase is not None:
            result['phase'] = self.phase

        if self.request_type is not None:
            result['requestType'] = self.request_type

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.stream_name is not None:
            result['streamName'] = self.stream_name

        if self.stream_suffix is not None:
            result['streamSuffix'] = self.stream_suffix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('app') is not None:
            self.app = m.get('app')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('intervalType') is not None:
            self.interval_type = m.get('intervalType')

        if m.get('phase') is not None:
            self.phase = m.get('phase')

        if m.get('requestType') is not None:
            self.request_type = m.get('requestType')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('streamName') is not None:
            self.stream_name = m.get('streamName')

        if m.get('streamSuffix') is not None:
            self.stream_suffix = m.get('streamSuffix')

        return self

