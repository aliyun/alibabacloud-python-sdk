# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteHotwordLibraryRequest(DaraModel):
    def __init__(
        self,
        hotword_library_id: str = None,
    ):
        # The ID of the hotword library that you want to delete.
        self.hotword_library_id = hotword_library_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotword_library_id is not None:
            result['HotwordLibraryId'] = self.hotword_library_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotwordLibraryId') is not None:
            self.hotword_library_id = m.get('HotwordLibraryId')

        return self

