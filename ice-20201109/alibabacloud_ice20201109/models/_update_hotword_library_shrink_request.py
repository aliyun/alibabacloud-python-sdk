# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateHotwordLibraryShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        hotword_library_id: str = None,
        hotwords_shrink: str = None,
        name: str = None,
    ):
        # The description of the hotword library. It can be up to 200 characters in length.
        self.description = description
        # The ID of the hotword library.
        # 
        # This parameter is required.
        self.hotword_library_id = hotword_library_id
        # The hotword list. You can add up to 300 hotword entries to a single library.
        self.hotwords_shrink = hotwords_shrink
        # The name of the hotword library. It can be up to 100 characters in length.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.hotword_library_id is not None:
            result['HotwordLibraryId'] = self.hotword_library_id

        if self.hotwords_shrink is not None:
            result['Hotwords'] = self.hotwords_shrink

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HotwordLibraryId') is not None:
            self.hotword_library_id = m.get('HotwordLibraryId')

        if m.get('Hotwords') is not None:
            self.hotwords_shrink = m.get('Hotwords')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

