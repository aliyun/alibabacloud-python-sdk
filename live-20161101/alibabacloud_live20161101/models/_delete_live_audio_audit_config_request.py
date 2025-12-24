# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLiveAudioAuditConfigRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        owner_id: int = None,
        region_id: str = None,
        stream_name: str = None,
    ):
        # The name of the application to which the live stream belongs.
        # 
        # >  A value of asterisk (\\*) specifies all applications under the domain name.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        self.region_id = region_id
        # The name of the live stream.
        # 
        # >  A value of asterisk (\\*) specifies all live streams in the application.
        # 
        # This parameter is required.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

