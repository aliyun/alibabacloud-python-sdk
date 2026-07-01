# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddFavoritePublicMediaResponseBody(DaraModel):
    def __init__(
        self,
        ignored_list: List[str] = None,
        request_id: str = None,
    ):
        # A list of Media Asset IDs that were not added to your Favorites. This happens if a Media Asset does not exist or is already in your Favorites.
        self.ignored_list = ignored_list
        # The Request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignored_list is not None:
            result['IgnoredList'] = self.ignored_list

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoredList') is not None:
            self.ignored_list = m.get('IgnoredList')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

