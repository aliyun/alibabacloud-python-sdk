# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTrainPicAvatarRequest(DaraModel):
    def __init__(
        self,
        gender: str = None,
        generate_assets: bool = None,
        image_oss_path: str = None,
        name: str = None,
        template_id: str = None,
        transparent: bool = None,
    ):
        # This parameter is required.
        self.gender = gender
        self.generate_assets = generate_assets
        # This parameter is required.
        self.image_oss_path = image_oss_path
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.template_id = template_id
        self.transparent = transparent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gender is not None:
            result['gender'] = self.gender

        if self.generate_assets is not None:
            result['generateAssets'] = self.generate_assets

        if self.image_oss_path is not None:
            result['imageOssPath'] = self.image_oss_path

        if self.name is not None:
            result['name'] = self.name

        if self.template_id is not None:
            result['templateId'] = self.template_id

        if self.transparent is not None:
            result['transparent'] = self.transparent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('generateAssets') is not None:
            self.generate_assets = m.get('generateAssets')

        if m.get('imageOssPath') is not None:
            self.image_oss_path = m.get('imageOssPath')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')

        if m.get('transparent') is not None:
            self.transparent = m.get('transparent')

        return self

