# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchMediaByFaceRequest(DaraModel):
    def __init__(
        self,
        custom_filters: str = None,
        entity_id: str = None,
        face_search_token: str = None,
        media_type: str = None,
        namespace: str = None,
        page_no: int = None,
        page_size: int = None,
        person_image_url: str = None,
        search_lib_name: str = None,
        utc_create: str = None,
    ):
        self.custom_filters = custom_filters
        # The ID of the entity.
        self.entity_id = entity_id
        # The token that is used to identify the query. You can use this parameter in the SearchMediaClipByFace operation to specify the same query conditions.
        # 
        # This parameter is required.
        self.face_search_token = face_search_token
        # The type of the media asset. Valid values:
        # 
        # *   image
        # *   video
        self.media_type = media_type
        self.namespace = namespace
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The URL of the face image.
        # 
        # This parameter is required.
        self.person_image_url = person_image_url
        # The name of the search library.
        self.search_lib_name = search_lib_name
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

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.face_search_token is not None:
            result['FaceSearchToken'] = self.face_search_token

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.person_image_url is not None:
            result['PersonImageUrl'] = self.person_image_url

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomFilters') is not None:
            self.custom_filters = m.get('CustomFilters')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('FaceSearchToken') is not None:
            self.face_search_token = m.get('FaceSearchToken')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PersonImageUrl') is not None:
            self.person_image_url = m.get('PersonImageUrl')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')

        return self

