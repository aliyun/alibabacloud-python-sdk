# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAnchorRequest(DaraModel):
    def __init__(
        self,
        anchor_category: str = None,
        anchor_material_name: str = None,
        cover_url: str = None,
        digital_human_type: str = None,
        gender: str = None,
        use_scene: str = None,
        video_oss_key: str = None,
    ):
        self.anchor_category = anchor_category
        self.anchor_material_name = anchor_material_name
        self.cover_url = cover_url
        self.digital_human_type = digital_human_type
        self.gender = gender
        self.use_scene = use_scene
        self.video_oss_key = video_oss_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor_category is not None:
            result['anchorCategory'] = self.anchor_category

        if self.anchor_material_name is not None:
            result['anchorMaterialName'] = self.anchor_material_name

        if self.cover_url is not None:
            result['coverUrl'] = self.cover_url

        if self.digital_human_type is not None:
            result['digitalHumanType'] = self.digital_human_type

        if self.gender is not None:
            result['gender'] = self.gender

        if self.use_scene is not None:
            result['useScene'] = self.use_scene

        if self.video_oss_key is not None:
            result['videoOssKey'] = self.video_oss_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anchorCategory') is not None:
            self.anchor_category = m.get('anchorCategory')

        if m.get('anchorMaterialName') is not None:
            self.anchor_material_name = m.get('anchorMaterialName')

        if m.get('coverUrl') is not None:
            self.cover_url = m.get('coverUrl')

        if m.get('digitalHumanType') is not None:
            self.digital_human_type = m.get('digitalHumanType')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')

        if m.get('videoOssKey') is not None:
            self.video_oss_key = m.get('videoOssKey')

        return self

