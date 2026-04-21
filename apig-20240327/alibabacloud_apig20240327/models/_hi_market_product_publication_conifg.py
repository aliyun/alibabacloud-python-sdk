# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HiMarketProductPublicationConifg(DaraModel):
    def __init__(
        self,
        publication_id: str = None,
    ):
        self.publication_id = publication_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.publication_id is not None:
            result['publicationId'] = self.publication_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('publicationId') is not None:
            self.publication_id = m.get('publicationId')

        return self

