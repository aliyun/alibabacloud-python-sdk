# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SavedSearch(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        logstore: str = None,
        savedsearch_name: str = None,
        search_query: str = None,
        topic: str = None,
    ):
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.logstore = logstore
        # This parameter is required.
        self.savedsearch_name = savedsearch_name
        # This parameter is required.
        self.search_query = search_query
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

