# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDynamicImageRequest(DaraModel):
    def __init__(
        self,
        dynamic_image_ids: str = None,
        video_id: str = None,
    ):
        # The IDs of the animated stickers.
        # 
        # - Separate multiple IDs with commas (,). You can specify a maximum of 10 IDs.
        # - If you do not set this parameter, the system finds the video specified by the VideoId parameter and deletes the information about the animated stickers associated with the video. If more than 10 animated stickers are associated with the video specified by the VideoId parameter, the deletion request is denied.
        self.dynamic_image_ids = dynamic_image_ids
        # The ID of the video associated with the animated stickers whose information you want to delete.
        # 
        # This parameter is required.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_image_ids is not None:
            result['DynamicImageIds'] = self.dynamic_image_ids

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicImageIds') is not None:
            self.dynamic_image_ids = m.get('DynamicImageIds')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

