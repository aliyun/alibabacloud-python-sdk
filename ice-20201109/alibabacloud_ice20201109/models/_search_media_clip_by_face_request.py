# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchMediaClipByFaceRequest(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        face_search_token: str = None,
        media_id: str = None,
        page_no: int = None,
        page_size: int = None,
        search_lib_name: str = None,
    ):
        # The ID of the entity.
        self.entity_id = entity_id
        # The value of this parameter is the same as that of the FaceSearchToken parameter in the SearchMediaByFace request. This specifies to return media asset clips that meet the same query conditions.
        # 
        # This parameter is required.
        self.face_search_token = face_search_token
        # The ID of the media asset.
        # 
        # This parameter is required.
        self.media_id = media_id
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The name of the search library.
        self.search_lib_name = search_lib_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.face_search_token is not None:
            result['FaceSearchToken'] = self.face_search_token

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('FaceSearchToken') is not None:
            self.face_search_token = m.get('FaceSearchToken')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        return self

