# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveAISubtitleRequest(DaraModel):
    def __init__(
        self,
        is_default: bool = None,
        owner_id: int = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
        subtitle_id: str = None,
        subtitle_name: str = None,
    ):
        # Specifies whether to query the default subtitle template. Valid values:
        # 
        # *   true
        # 
        # *   false
        # 
        #     **
        # 
        #     **Note **The default template includes the built-in parameter configurations. You can specify the copyFrom parameter when you call the AddLiveAISubtitle operation to use the default template.
        self.is_default = is_default
        self.owner_id = owner_id
        # The page number. Valid values: [1,100].
        self.page_number = page_number
        # The number of entries per page. Valid values: [1,100].
        self.page_size = page_size
        self.region_id = region_id
        # The ID of the subtitle template.
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
        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.subtitle_id is not None:
            result['SubtitleId'] = self.subtitle_id

        if self.subtitle_name is not None:
            result['SubtitleName'] = self.subtitle_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SubtitleId') is not None:
            self.subtitle_id = m.get('SubtitleId')

        if m.get('SubtitleName') is not None:
            self.subtitle_name = m.get('SubtitleName')

        return self

