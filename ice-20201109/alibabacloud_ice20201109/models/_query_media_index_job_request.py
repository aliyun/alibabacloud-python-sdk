# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMediaIndexJobRequest(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        search_lib_name: str = None,
    ):
        # The ID of the media asset.
        # 
        # This parameter is required.
        self.media_id = media_id
        # The name of the search library. Default value: ims-default-search-lib.
        self.search_lib_name = search_lib_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        return self

