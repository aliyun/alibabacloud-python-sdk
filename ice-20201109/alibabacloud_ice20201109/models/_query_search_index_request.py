# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySearchIndexRequest(DaraModel):
    def __init__(
        self,
        index_type: str = None,
        search_lib_name: str = None,
    ):
        # The category of the index. Valid values:
        # 
        # *   mm: large visual model.
        # *   face: face recognition.
        # *   aiLabel: smart tagging.
        # 
        # This parameter is required.
        self.index_type = index_type
        # The name of the search library.
        # 
        # *   If you leave this parameter empty, the search index is created in the default search library of Intelligent Media Service (IMS). Default value: ims-default-search-lib.
        # *   To query information about an existing search library, call the [QuerySearchLib](https://help.aliyun.com/document_detail/2584455.html) API operation.
        self.search_lib_name = search_lib_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index_type is not None:
            result['IndexType'] = self.index_type

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        return self

