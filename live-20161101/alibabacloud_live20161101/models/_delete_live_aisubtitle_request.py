# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLiveAISubtitleRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        subtitle_id: str = None,
        subtitle_name: str = None,
    ):
        self.owner_id = owner_id
        self.region_id = region_id
        # The ID of the subtitle template.
        # 
        # This parameter is required.
        self.subtitle_id = subtitle_id
        # The name of the subtitle template. The name can contain only digits, letters, and hyphens (-). The name cannot start with a hyphen.
        self.subtitle_name = subtitle_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.subtitle_id is not None:
            result['SubtitleId'] = self.subtitle_id

        if self.subtitle_name is not None:
            result['SubtitleName'] = self.subtitle_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SubtitleId') is not None:
            self.subtitle_id = m.get('SubtitleId')

        if m.get('SubtitleName') is not None:
            self.subtitle_name = m.get('SubtitleName')

        return self

