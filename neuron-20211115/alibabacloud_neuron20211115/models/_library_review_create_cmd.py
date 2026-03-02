# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LibraryReviewCreateCmd(DaraModel):
    def __init__(
        self,
        library_id: int = None,
        library_url: str = None,
        market_id: int = None,
        reviewer_id: str = None,
    ):
        self.library_id = library_id
        self.library_url = library_url
        self.market_id = market_id
        self.reviewer_id = reviewer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.library_url is not None:
            result['libraryUrl'] = self.library_url

        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.reviewer_id is not None:
            result['reviewerId'] = self.reviewer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('libraryUrl') is not None:
            self.library_url = m.get('libraryUrl')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('reviewerId') is not None:
            self.reviewer_id = m.get('reviewerId')

        return self

