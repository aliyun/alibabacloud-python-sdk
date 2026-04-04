# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppAssistantAgentSsoLoginRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        platform_type: str = None,
        target_url: str = None,
    ):
        self.biz_id = biz_id
        self.platform_type = platform_type
        self.target_url = target_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.platform_type is not None:
            result['PlatformType'] = self.platform_type

        if self.target_url is not None:
            result['TargetUrl'] = self.target_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('PlatformType') is not None:
            self.platform_type = m.get('PlatformType')

        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')

        return self

