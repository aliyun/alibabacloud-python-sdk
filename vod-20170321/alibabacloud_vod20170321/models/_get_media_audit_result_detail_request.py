# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMediaAuditResultDetailRequest(DaraModel):
    def __init__(
        self,
        media_id: str = None,
        page_no: int = None,
    ):
        # The ID of the video.
        # 
        # This parameter is required.
        self.media_id = media_id
        # The page number. The default value is **1**. A maximum of **20** records can be returned on each page.
        # 
        # This parameter is required.
        self.page_no = page_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        return self

