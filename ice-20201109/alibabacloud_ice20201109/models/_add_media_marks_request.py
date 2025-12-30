# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddMediaMarksRequest(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        media_marks: str = None,
    ):
        # The ID of the media asset.
        # 
        # This parameter is required.
        self.media_id = media_id
        # The mark information. The value must be a JSONArray.
        # 
        # This parameter is required.
        self.media_marks = media_marks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_marks is not None:
            result['MediaMarks'] = self.media_marks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaMarks') is not None:
            self.media_marks = m.get('MediaMarks')

        return self

