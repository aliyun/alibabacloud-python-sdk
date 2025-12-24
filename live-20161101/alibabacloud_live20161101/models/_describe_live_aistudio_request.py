# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveAIStudioRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        studio_id: str = None,
        studio_name: str = None,
    ):
        self.owner_id = owner_id
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Valid values: 1 to 50.
        self.page_size = page_size
        self.region_id = region_id
        # The ID of the virtual studio template that you want to query. This parameter is optional.
        self.studio_id = studio_id
        # The name of the virtual studio template.
        self.studio_name = studio_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.studio_id is not None:
            result['StudioId'] = self.studio_id

        if self.studio_name is not None:
            result['StudioName'] = self.studio_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StudioId') is not None:
            self.studio_id = m.get('StudioId')

        if m.get('StudioName') is not None:
            self.studio_name = m.get('StudioName')

        return self

