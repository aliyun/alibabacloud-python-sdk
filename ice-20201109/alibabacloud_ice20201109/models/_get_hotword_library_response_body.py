# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetHotwordLibraryResponseBody(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        hotword_library_id: str = None,
        hotwords: List[main_models.Hotword] = None,
        name: str = None,
        request_id: str = None,
        usage_scenario: str = None,
    ):
        # The time when the hotword library was created.
        self.creation_time = creation_time
        # The description of the hotword library.
        self.description = description
        # The ID of the hotword library.
        self.hotword_library_id = hotword_library_id
        # The hotword list.
        self.hotwords = hotwords
        # The name of the hotword library.
        self.name = name
        # The ID of the request.
        self.request_id = request_id
        # The usage scenario of the hotword library.
        self.usage_scenario = usage_scenario

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
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.usage_scenario is not None:
            result['UsageScenario'] = self.usage_scenario

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UsageScenario') is not None:
            self.usage_scenario = m.get('UsageScenario')

        return self

