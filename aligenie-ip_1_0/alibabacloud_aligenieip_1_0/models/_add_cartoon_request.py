# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCartoonRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        start_video_md_5: str = None,
        start_video_url: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.start_video_md_5 = start_video_md_5
        # This parameter is required.
        self.start_video_url = start_video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.start_video_md_5 is not None:
            result['StartVideoMd5'] = self.start_video_md_5

        if self.start_video_url is not None:
            result['StartVideoUrl'] = self.start_video_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('StartVideoMd5') is not None:
            self.start_video_md_5 = m.get('StartVideoMd5')

        if m.get('StartVideoUrl') is not None:
            self.start_video_url = m.get('StartVideoUrl')

        return self

