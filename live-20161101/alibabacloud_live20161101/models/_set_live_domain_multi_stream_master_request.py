# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLiveDomainMultiStreamMasterRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain: str = None,
        owner_id: int = None,
        stream_name: str = None,
        upstream_sequence: str = None,
    ):
        # The name of the application to which the live stream belongs.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        self.owner_id = owner_id
        # The name of the live stream.
        # 
        # This parameter is required.
        self.stream_name = stream_name
        # The unique identifier of the stream ingest.
        # 
        # This parameter is required.
        self.upstream_sequence = upstream_sequence

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.upstream_sequence is not None:
            result['UpstreamSequence'] = self.upstream_sequence

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('UpstreamSequence') is not None:
            self.upstream_sequence = m.get('UpstreamSequence')

        return self

