# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLibraryInstructionRequest(DaraModel):
    def __init__(
        self,
        company_id: int = None,
        document: str = None,
        id: int = None,
        library_id: str = None,
        market_id: int = None,
    ):
        self.company_id = company_id
        self.document = document
        self.id = id
        self.library_id = library_id
        self.market_id = market_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.document is not None:
            result['document'] = self.document

        if self.id is not None:
            result['id'] = self.id

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.market_id is not None:
            result['marketId'] = self.market_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('document') is not None:
            self.document = m.get('document')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('marketId') is not None:
            self.market_id = m.get('marketId')

        return self

