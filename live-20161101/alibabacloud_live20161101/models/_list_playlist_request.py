# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPlaylistRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        page: int = None,
        page_size: int = None,
        program_id: str = None,
        region_id: str = None,
    ):
        self.owner_id = owner_id
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the episode list. If you set this parameter, only the information about the specified episode lists is returned. If you do not set this parameter, the information about all episode lists that belong to the account is returned. If the episode list was created by calling the [AddPlaylistItems](https://help.aliyun.com/document_detail/2848078.html) operation, check the value of the response parameter ProgramId to obtain the ID.
        self.program_id = program_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.program_id is not None:
            result['ProgramId'] = self.program_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProgramId') is not None:
            self.program_id = m.get('ProgramId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

