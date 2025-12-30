# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchPublicMediaInfoRequest(DaraModel):
    def __init__(
        self,
        authorized: bool = None,
        dynamic_meta_data_match_fields: str = None,
        entity_id: str = None,
        favorite: bool = None,
        media_ids: str = None,
        page_no: int = None,
        page_size: int = None,
        sort_by: str = None,
    ):
        self.authorized = authorized
        self.dynamic_meta_data_match_fields = dynamic_meta_data_match_fields
        self.entity_id = entity_id
        self.favorite = favorite
        self.media_ids = media_ids
        self.page_no = page_no
        self.page_size = page_size
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorized is not None:
            result['Authorized'] = self.authorized

        if self.dynamic_meta_data_match_fields is not None:
            result['DynamicMetaDataMatchFields'] = self.dynamic_meta_data_match_fields

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.favorite is not None:
            result['Favorite'] = self.favorite

        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorized') is not None:
            self.authorized = m.get('Authorized')

        if m.get('DynamicMetaDataMatchFields') is not None:
            self.dynamic_meta_data_match_fields = m.get('DynamicMetaDataMatchFields')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('Favorite') is not None:
            self.favorite = m.get('Favorite')

        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

