# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSearchIndexRequest(DaraModel):
    def __init__(
        self,
        index_config: str = None,
        index_status: str = None,
        index_type: str = None,
        search_lib_name: str = None,
    ):
        self.index_config = index_config
        self.index_status = index_status
        # The category of the index. Valid values:
        # 
        # *   mm: large visual model. You can use this model to describe complex visual features and identify and search for specific actions, movements, and events in videos, such as when athletes score a goal or get injured.
        # 
        # >  This feature is in the public preview phase. You can use this feature for free for 1,000 hours of videos.
        # 
        # *   face: face recognition. You can use the face recognition technology to describe face characteristics and automatically mark or search for faces in videos.
        # *   aiLabel: smart tagging. The smart tagging category is used to describe content such as subtitles and audio in videos. You can use the speech recognition technology to automatically extract, mark, and search for subtitles and dialog content from videos. This helps you quickly locate the video content that is related to specific topics or keywords.
        # 
        # This parameter is required.
        self.index_type = index_type
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

