# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchMediaByHybridRequest(DaraModel):
    def __init__(
        self,
        custom_filters: str = None,
        media_id: str = None,
        media_type: str = None,
        namespace: str = None,
        page_no: int = None,
        page_size: int = None,
        search_lib_name: str = None,
        text: str = None,
        utc_create: str = None,
    ):
        # Custom filters. A JSON string. Supported backing fields include integer field intField1 and string fields strField1 and strField2. Only one matching condition can be applied per field, and filters across different fields are combined with a logical AND relationship.
        # 
        # - Exact match example: {"intField1":12,"strField1":"abc"}
        # 
        # - Multi-value example: {"intField1":[12,13],"strField1":["abc","cd"]}
        # 
        # - Range example: {"intField1":{"gte":12,"lte":13}}
        self.custom_filters = custom_filters
        # The ID of the media asset. If provided, the details of the media asset are returned.
        self.media_id = media_id
        # The type of media assets. Valid values:
        # 
        # - image
        # 
        # - video
        self.media_type = media_type
        # The namespace.
        self.namespace = namespace
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Valid values: 1 to 50. Default value: 10.
        self.page_size = page_size
        # The name of the search library
        self.search_lib_name = search_lib_name
        # The natural language search query.
        self.text = text
        # Creation time, in milliseconds UNIX timestamp. gte means greater than or equal to, and lte means less than or equal to.
        # 
        # - Range example: {"gte":1761205662998,"lte":1771205662998}
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

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        if self.text is not None:
            result['Text'] = self.text

        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomFilters') is not None:
            self.custom_filters = m.get('CustomFilters')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')

        return self

