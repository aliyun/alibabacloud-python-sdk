# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSavedSearchRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        logstore: str = None,
        savedsearch_name: str = None,
        search_query: str = None,
        topic: str = None,
    ):
        # The display name.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The name of the Logstore to which the saved search belongs.
        # 
        # This parameter is required.
        self.logstore = logstore
        # The name of the saved search. The name must be 3 to 63 characters in length.
        # 
        # This parameter is required.
        self.savedsearch_name = savedsearch_name
        # The query statement of the saved search. A query statement consists of a search statement and an analytic statement in the `Search statement|Analytic statement` format. For more information, see [Log search overview](https://help.aliyun.com/document_detail/43772.html) and [Log analysis overview](https://help.aliyun.com/document_detail/53608.html).
        # 
        # This parameter is required.
        self.search_query = search_query
        # The topic of the logs.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.savedsearch_name is not None:
            result['savedsearchName'] = self.savedsearch_name

        if self.search_query is not None:
            result['searchQuery'] = self.search_query

        if self.topic is not None:
            result['topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('savedsearchName') is not None:
            self.savedsearch_name = m.get('savedsearchName')

        if m.get('searchQuery') is not None:
            self.search_query = m.get('searchQuery')

        if m.get('topic') is not None:
            self.topic = m.get('topic')

        return self

