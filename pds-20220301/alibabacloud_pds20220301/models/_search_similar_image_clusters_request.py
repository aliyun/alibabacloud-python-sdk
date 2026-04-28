# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchSimilarImageClustersRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        image_thumbnail_process: str = None,
        limit: int = None,
        marker: str = None,
        order: str = None,
    ):
        # This parameter is required.
        self.drive_id = drive_id
        self.image_thumbnail_process = image_thumbnail_process
        self.limit = limit
        self.marker = marker
        self.order = order

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

        if self.order is not None:
            result['order'] = self.order

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

        if m.get('order') is not None:
            self.order = m.get('order')

        return self

