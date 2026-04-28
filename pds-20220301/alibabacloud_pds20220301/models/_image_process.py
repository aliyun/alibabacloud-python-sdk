# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageProcess(DaraModel):
    def __init__(
        self,
        image_thumbnail_process: str = None,
        office_thumbnail_process: str = None,
        video_thumbnail_process: str = None,
    ):
        # The thumbnail processing rules for images. For more information, see the "IMG implementation modes" topic of Object Storage Service (OSS). Default value: image/resize,m_fill,h_128,w_128,limit_0.
        self.image_thumbnail_process = image_thumbnail_process
        # The thumbnail processing rules for documents. For a document, the snapshot of one of the pages in the document is used as the thumbnail. This parameter takes effect on this snapshot. Default value: image/resize,m_fill,h_128,w_128,limit_0.
        self.office_thumbnail_process = office_thumbnail_process
        # The thumbnail processing rules for videos. For more information, see the "Video snapshots" topic of OSS. Default value: video/snapshot,t_1000,f_jpg,w_0,h_0,m_fast,ar_auto.
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process

        if self.office_thumbnail_process is not None:
            result['office_thumbnail_process'] = self.office_thumbnail_process

        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')

        if m.get('office_thumbnail_process') is not None:
            self.office_thumbnail_process = m.get('office_thumbnail_process')

        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')

        return self

