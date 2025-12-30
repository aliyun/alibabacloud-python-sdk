# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AlterSearchIndexRequest(DaraModel):
    def __init__(
        self,
        index_config: str = None,
        index_status: str = None,
        index_type: str = None,
        search_lib_name: str = None,
    ):
        # The configurations of the index.
        # 
        # >  You must specify either IndexStatus or IndexConfig.
        self.index_config = index_config
        # The state of the index. Valid values:
        # 
        # *   active (default): the index is enabled.
        # *   Deactive: the index is not enabled.
        # 
        # >  You must specify either IndexStatus or IndexConfig.
        self.index_status = index_status
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
        if self.index_config is not None:
            result['IndexConfig'] = self.index_config

        if self.index_status is not None:
            result['IndexStatus'] = self.index_status

        if self.index_type is not None:
            result['IndexType'] = self.index_type

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexConfig') is not None:
            self.index_config = m.get('IndexConfig')

        if m.get('IndexStatus') is not None:
            self.index_status = m.get('IndexStatus')

        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        return self

