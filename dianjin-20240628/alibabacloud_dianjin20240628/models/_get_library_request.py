# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLibraryRequest(DaraModel):
    def __init__(
        self,
        library_id: str = None,
    ):
        # This parameter is required.
        self.library_id = library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.library_id is not None:
            result['libraryId'] = self.library_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        return self

