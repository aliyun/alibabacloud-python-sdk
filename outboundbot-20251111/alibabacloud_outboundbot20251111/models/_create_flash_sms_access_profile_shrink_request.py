# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFlashSmsAccessProfileShrinkRequest(DaraModel):
    def __init__(
        self,
        access_profile_shrink: str = None,
        instance_id: str = None,
        provider_id: str = None,
    ):
        # The access configuration.
        self.access_profile_shrink = access_profile_shrink
        # The instance ID.
        self.instance_id = instance_id
        # The provider ID. Valid values:
        # - Uincall: Beijing Youyin Communication Co., Ltd.
        # - ChuangLan: Beijing Chuanglan Yunzhi Information Co., Ltd.
        # - ChinaMobile: China Mobile.
        # - ShangHaiTianNan: Shanghai Tiannan.
        # - HeDao: Galexes.
        # - DySms: Alibaba Communication.
        self.provider_id = provider_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_profile_shrink is not None:
            result['AccessProfile'] = self.access_profile_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.provider_id is not None:
            result['ProviderId'] = self.provider_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessProfile') is not None:
            self.access_profile_shrink = m.get('AccessProfile')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ProviderId') is not None:
            self.provider_id = m.get('ProviderId')

        return self

