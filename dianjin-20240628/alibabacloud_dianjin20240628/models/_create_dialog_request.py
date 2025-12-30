# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from darabonba.model import DaraModel

class CreateDialogRequest(DaraModel):
    def __init__(
        self,
        channel: str = None,
        enable_library: bool = None,
        meta_data: Dict[str, Any] = None,
        play_code: str = None,
        qa_library_list: List[str] = None,
        request_id: str = None,
        self_directed: bool = None,
    ):
        # This parameter is required.
        self.channel = channel
        self.enable_library = enable_library
        self.meta_data = meta_data
        # This parameter is required.
        self.play_code = play_code
        self.qa_library_list = qa_library_list
        # This parameter is required.
        self.request_id = request_id
        self.self_directed = self_directed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['channel'] = self.channel

        if self.enable_library is not None:
            result['enableLibrary'] = self.enable_library

        if self.meta_data is not None:
            result['metaData'] = self.meta_data

        if self.play_code is not None:
            result['playCode'] = self.play_code

        if self.qa_library_list is not None:
            result['qaLibraryList'] = self.qa_library_list

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.self_directed is not None:
            result['selfDirected'] = self.self_directed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('enableLibrary') is not None:
            self.enable_library = m.get('enableLibrary')

        if m.get('metaData') is not None:
            self.meta_data = m.get('metaData')

        if m.get('playCode') is not None:
            self.play_code = m.get('playCode')

        if m.get('qaLibraryList') is not None:
            self.qa_library_list = m.get('qaLibraryList')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('selfDirected') is not None:
            self.self_directed = m.get('selfDirected')

        return self

