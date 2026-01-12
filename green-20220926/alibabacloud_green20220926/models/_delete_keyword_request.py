# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteKeywordRequest(DaraModel):
    def __init__(
        self,
        keyword_id_list: str = None,
        keyword_ids: str = None,
        lib_id: str = None,
        region_id: str = None,
    ):
        # The ids\\" list of keywords.
        self.keyword_id_list = keyword_id_list
        # The ids of keywords.
        self.keyword_ids = keyword_ids
        # Library id
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
        if self.keyword_id_list is not None:
            result['KeywordIdList'] = self.keyword_id_list

        if self.keyword_ids is not None:
            result['KeywordIds'] = self.keyword_ids

        if self.lib_id is not None:
            result['LibId'] = self.lib_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeywordIdList') is not None:
            self.keyword_id_list = m.get('KeywordIdList')

        if m.get('KeywordIds') is not None:
            self.keyword_ids = m.get('KeywordIds')

        if m.get('LibId') is not None:
            self.lib_id = m.get('LibId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

