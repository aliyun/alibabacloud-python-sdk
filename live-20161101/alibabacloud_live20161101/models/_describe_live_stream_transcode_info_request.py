# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveStreamTranscodeInfoRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_transcode_name: str = None,
        owner_id: int = None,
        region_id: str = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_transcode_name = domain_transcode_name
        self.owner_id = owner_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_transcode_name is not None:
            result['DomainTranscodeName'] = self.domain_transcode_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainTranscodeName') is not None:
            self.domain_transcode_name = m.get('DomainTranscodeName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

