# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AnchorResponse(DaraModel):
    def __init__(
        self,
        anchor_category: str = None,
        anchor_id: str = None,
        anchor_material_name: str = None,
        anchor_type: str = None,
        cover_height: int = None,
        cover_rate: str = None,
        cover_thumbnail_url: str = None,
        cover_url: str = None,
        cover_weight: int = None,
        digital_human_type: str = None,
        gender: str = None,
        resource_type_desc: str = None,
        status: str = None,
        support_bg_change: int = None,
        use_scene: str = None,
    ):
        self.anchor_category = anchor_category
        self.anchor_id = anchor_id
        self.anchor_material_name = anchor_material_name
        self.anchor_type = anchor_type
        self.cover_height = cover_height
        self.cover_rate = cover_rate
        self.cover_thumbnail_url = cover_thumbnail_url
        self.cover_url = cover_url
        self.cover_weight = cover_weight
        self.digital_human_type = digital_human_type
        self.gender = gender
        self.resource_type_desc = resource_type_desc
        self.status = status
        self.support_bg_change = support_bg_change
        self.use_scene = use_scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor_category is not None:
            result['anchorCategory'] = self.anchor_category

        if self.anchor_id is not None:
            result['anchorId'] = self.anchor_id

        if self.anchor_material_name is not None:
            result['anchorMaterialName'] = self.anchor_material_name

        if self.anchor_type is not None:
            result['anchorType'] = self.anchor_type

        if self.cover_height is not None:
            result['coverHeight'] = self.cover_height

        if self.cover_rate is not None:
            result['coverRate'] = self.cover_rate

        if self.cover_thumbnail_url is not None:
            result['coverThumbnailUrl'] = self.cover_thumbnail_url

        if self.cover_url is not None:
            result['coverUrl'] = self.cover_url

        if self.cover_weight is not None:
            result['coverWeight'] = self.cover_weight

        if self.digital_human_type is not None:
            result['digitalHumanType'] = self.digital_human_type

        if self.gender is not None:
            result['gender'] = self.gender

        if self.resource_type_desc is not None:
            result['resourceTypeDesc'] = self.resource_type_desc

        if self.status is not None:
            result['status'] = self.status

        if self.support_bg_change is not None:
            result['supportBgChange'] = self.support_bg_change

        if self.use_scene is not None:
            result['useScene'] = self.use_scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anchorCategory') is not None:
            self.anchor_category = m.get('anchorCategory')

        if m.get('anchorId') is not None:
            self.anchor_id = m.get('anchorId')

        if m.get('anchorMaterialName') is not None:
            self.anchor_material_name = m.get('anchorMaterialName')

        if m.get('anchorType') is not None:
            self.anchor_type = m.get('anchorType')

        if m.get('coverHeight') is not None:
            self.cover_height = m.get('coverHeight')

        if m.get('coverRate') is not None:
            self.cover_rate = m.get('coverRate')

        if m.get('coverThumbnailUrl') is not None:
            self.cover_thumbnail_url = m.get('coverThumbnailUrl')

        if m.get('coverUrl') is not None:
            self.cover_url = m.get('coverUrl')

        if m.get('coverWeight') is not None:
            self.cover_weight = m.get('coverWeight')

        if m.get('digitalHumanType') is not None:
            self.digital_human_type = m.get('digitalHumanType')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('resourceTypeDesc') is not None:
            self.resource_type_desc = m.get('resourceTypeDesc')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('supportBgChange') is not None:
            self.support_bg_change = m.get('supportBgChange')

        if m.get('useScene') is not None:
            self.use_scene = m.get('useScene')

        return self

