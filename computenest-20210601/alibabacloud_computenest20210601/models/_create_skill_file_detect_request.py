# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSkillFileDetectRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        oss_url: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.oss_url = oss_url
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

