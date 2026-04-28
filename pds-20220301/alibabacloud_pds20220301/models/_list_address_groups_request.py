# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAddressGroupsRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        image_thumbnail_process: str = None,
        limit: int = None,
        marker: str = None,
        video_thumbnail_process: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The method that is used to generate a thumbnail of an image.
        self.image_thumbnail_process = image_thumbnail_process
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is left empty.
        self.marker = marker
        # The method that is used to generate a thumbnail of a video.
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process

        if self.limit is not None:
            result['limit'] = self.limit

        if self.marker is not None:
            result['marker'] = self.marker

        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')

        return self

