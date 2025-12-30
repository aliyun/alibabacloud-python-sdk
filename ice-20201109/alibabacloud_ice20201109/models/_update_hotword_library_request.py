# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class UpdateHotwordLibraryRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        hotword_library_id: str = None,
        hotwords: List[main_models.Hotword] = None,
        name: str = None,
    ):
        # The description of the hotword library. It can be up to 200 characters in length.
        self.description = description
        # The ID of the hotword library.
        # 
        # This parameter is required.
        self.hotword_library_id = hotword_library_id
        # The hotword list. You can add up to 300 hotword entries to a single library.
        self.hotwords = hotwords
        # The name of the hotword library. It can be up to 100 characters in length.
        self.name = name

    def validate(self):
        if self.hotwords:
            for v1 in self.hotwords:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.hotword_library_id is not None:
            result['HotwordLibraryId'] = self.hotword_library_id

        result['Hotwords'] = []
        if self.hotwords is not None:
            for k1 in self.hotwords:
                result['Hotwords'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HotwordLibraryId') is not None:
            self.hotword_library_id = m.get('HotwordLibraryId')

        self.hotwords = []
        if m.get('Hotwords') is not None:
            for k1 in m.get('Hotwords'):
                temp_model = main_models.Hotword()
                self.hotwords.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

