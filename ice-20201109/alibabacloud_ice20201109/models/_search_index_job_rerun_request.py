# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchIndexJobRerunRequest(DaraModel):
    def __init__(
        self,
        media_ids: str = None,
        namespace: str = None,
        search_lib_name: str = None,
        task: str = None,
    ):
        # The ID of the media asset. Separate multiple IDs with commas (,).
        # 
        # This parameter is required.
        self.media_ids = media_ids
        self.namespace = namespace
        # The search library.
        self.search_lib_name = search_lib_name
        # The type of the job. Separate multiple types with commas (,).
        # 
        # *   aiLabel: smart tagging.
        # *   face: face recognition.
        # *   mm: large visual model.
        self.task = task

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_ids is not None:
            result['MediaIds'] = self.media_ids

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        if self.task is not None:
            result['Task'] = self.task

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaIds') is not None:
            self.media_ids = m.get('MediaIds')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        if m.get('Task') is not None:
            self.task = m.get('Task')

        return self

