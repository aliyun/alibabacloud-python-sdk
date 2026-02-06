# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVideoInfosRequest(DaraModel):
    def __init__(
        self,
        reference_ids: str = None,
        video_ids: str = None,
    ):
        self.reference_ids = reference_ids
        # The list of video IDs. Separate multiple IDs with commas (,). A maximum of 20 IDs can be specified.
        self.video_ids = video_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reference_ids is not None:
            result['ReferenceIds'] = self.reference_ids

        if self.video_ids is not None:
            result['VideoIds'] = self.video_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferenceIds') is not None:
            self.reference_ids = m.get('ReferenceIds')

        if m.get('VideoIds') is not None:
            self.video_ids = m.get('VideoIds')

        return self

