# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLiveShrinkRequest(DaraModel):
    def __init__(
        self,
        cover_url: str = None,
        introduction: str = None,
        live_id: str = None,
        pre_end_time: int = None,
        pre_start_time: int = None,
        tenant_context_shrink: str = None,
        title: str = None,
    ):
        self.cover_url = cover_url
        self.introduction = introduction
        # This parameter is required.
        self.live_id = live_id
        # This parameter is required.
        self.pre_end_time = pre_end_time
        # This parameter is required.
        self.pre_start_time = pre_start_time
        self.tenant_context_shrink = tenant_context_shrink
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        if self.introduction is not None:
            result['Introduction'] = self.introduction

        if self.live_id is not None:
            result['LiveId'] = self.live_id

        if self.pre_end_time is not None:
            result['PreEndTime'] = self.pre_end_time

        if self.pre_start_time is not None:
            result['PreStartTime'] = self.pre_start_time

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')

        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')

        if m.get('PreEndTime') is not None:
            self.pre_end_time = m.get('PreEndTime')

        if m.get('PreStartTime') is not None:
            self.pre_start_time = m.get('PreStartTime')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

