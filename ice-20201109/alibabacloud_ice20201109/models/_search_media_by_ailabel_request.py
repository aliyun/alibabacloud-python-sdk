# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchMediaByAILabelRequest(DaraModel):
    def __init__(
        self,
        custom_filters: str = None,
        matching_mode: str = None,
        media_id: str = None,
        media_type: str = None,
        multimodal_search_type: str = None,
        namespace: str = None,
        page_no: int = None,
        page_size: int = None,
        search_lib_name: str = None,
        sort_by: str = None,
        specific_search: bool = None,
        text: str = None,
        utc_create: str = None,
    ):
        self.custom_filters = custom_filters
        self.matching_mode = matching_mode
        # The ID of the media asset. This parameter is required if you want to query media asset clips.
        self.media_id = media_id
        # The type of the media assets. Valid values:
        # 
        # *   image
        # *   video
        # *   audio
        self.media_type = media_type
        # The type of query. Valid values:
        # 
        # *   PersonName: queries media assets based on character names.
        # *   Ocr: queries media assets based on subtitles.
        # *   AiCategory: queries media assets based on AI categories.
        # *   FullSearch (default): queries all media assets.
        self.multimodal_search_type = multimodal_search_type
        self.namespace = namespace
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The name of the search library.
        self.search_lib_name = search_lib_name
        # The sorting method of the results. Valid values:
        # 
        # *   CreationTime:Desc (default): sorts results in reverse chronological order.
        # *   CreationTime:Asc: sorts results in chronological order.
        self.sort_by = sort_by
        # Specifies whether to query media asset clips. Valid values:
        # 
        # *   true
        # *   false
        self.specific_search = specific_search
        # The content that you want to query.
        self.text = text
        self.utc_create = utc_create

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_filters is not None:
            result['CustomFilters'] = self.custom_filters

        if self.matching_mode is not None:
            result['MatchingMode'] = self.matching_mode

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.multimodal_search_type is not None:
            result['MultimodalSearchType'] = self.multimodal_search_type

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.specific_search is not None:
            result['SpecificSearch'] = self.specific_search

        if self.text is not None:
            result['Text'] = self.text

        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomFilters') is not None:
            self.custom_filters = m.get('CustomFilters')

        if m.get('MatchingMode') is not None:
            self.matching_mode = m.get('MatchingMode')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('MultimodalSearchType') is not None:
            self.multimodal_search_type = m.get('MultimodalSearchType')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SpecificSearch') is not None:
            self.specific_search = m.get('SpecificSearch')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')

        return self

