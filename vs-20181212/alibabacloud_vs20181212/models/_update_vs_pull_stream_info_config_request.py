# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVsPullStreamInfoConfigRequest(DaraModel):
    def __init__(
        self,
        always: str = None,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        source_url: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        self.always = always
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.domain_name = domain_name
        self.end_time = end_time
        self.owner_id = owner_id
        # This parameter is required.
        self.source_url = source_url
        self.start_time = start_time
        # This parameter is required.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.always is not None:
            result['Always'] = self.always

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.source_url is not None:
            result['SourceUrl'] = self.source_url

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Always') is not None:
            self.always = m.get('Always')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SourceUrl') is not None:
            self.source_url = m.get('SourceUrl')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

