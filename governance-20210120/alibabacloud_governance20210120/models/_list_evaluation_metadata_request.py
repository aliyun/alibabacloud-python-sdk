# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEvaluationMetadataRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        lens_code: str = None,
        region_id: str = None,
        topic_code: str = None,
    ):
        # The language. The information is returned in the specified language. Valid values:
        # 
        # *   en: English
        # *   zh: Chinese
        self.language = language
        self.lens_code = lens_code
        # The region ID.
        self.region_id = region_id
        self.topic_code = topic_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.lens_code is not None:
            result['LensCode'] = self.lens_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.topic_code is not None:
            result['TopicCode'] = self.topic_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LensCode') is not None:
            self.lens_code = m.get('LensCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TopicCode') is not None:
            self.topic_code = m.get('TopicCode')

        return self

