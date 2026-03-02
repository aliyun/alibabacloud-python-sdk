# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcReviewCreateCmd(DaraModel):
    def __init__(
        self,
        market_id: int = None,
        pbc_url: str = None,
        pbc_version_id: int = None,
        reviewer_id: int = None,
    ):
        # This parameter is required.
        self.market_id = market_id
        # This parameter is required.
        self.pbc_url = pbc_url
        # This parameter is required.
        self.pbc_version_id = pbc_version_id
        # This parameter is required.
        self.reviewer_id = reviewer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.market_id is not None:
            result['marketId'] = self.market_id

        if self.pbc_url is not None:
            result['pbcUrl'] = self.pbc_url

        if self.pbc_version_id is not None:
            result['pbcVersionId'] = self.pbc_version_id

        if self.reviewer_id is not None:
            result['reviewerId'] = self.reviewer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        if m.get('pbcUrl') is not None:
            self.pbc_url = m.get('pbcUrl')

        if m.get('pbcVersionId') is not None:
            self.pbc_version_id = m.get('pbcVersionId')

        if m.get('reviewerId') is not None:
            self.reviewer_id = m.get('reviewerId')

        return self

