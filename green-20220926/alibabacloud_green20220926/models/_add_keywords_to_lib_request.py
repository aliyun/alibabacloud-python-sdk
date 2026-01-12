# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddKeywordsToLibRequest(DaraModel):
    def __init__(
        self,
        keywords: str = None,
        keywords_object: str = None,
        lib_id: str = None,
        region_id: str = None,
    ):
        # The keyword to be added.
        self.keywords = keywords
        # The name of the keyword file.
        self.keywords_object = keywords_object
        # The id of the keyword library.
        self.lib_id = lib_id
        # Region ID
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.keywords_object is not None:
            result['KeywordsObject'] = self.keywords_object

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('KeywordsObject') is not None:
            self.keywords_object = m.get('KeywordsObject')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

