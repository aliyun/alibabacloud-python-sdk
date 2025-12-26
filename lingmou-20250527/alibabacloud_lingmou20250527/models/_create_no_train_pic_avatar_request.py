# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNoTrainPicAvatarRequest(DaraModel):
    def __init__(
        self,
        expressiveness: str = None,
        gender: str = None,
        generate_assets: bool = None,
        image_oss_path: str = None,
        jwt_token: str = None,
        name: str = None,
        transparent: bool = None,
    ):
        self.expressiveness = expressiveness
        self.gender = gender
        self.generate_assets = generate_assets
        self.image_oss_path = image_oss_path
        self.jwt_token = jwt_token
        self.name = name
        self.transparent = transparent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expressiveness is not None:
            result['expressiveness'] = self.expressiveness

        if self.gender is not None:
            result['gender'] = self.gender

        if self.generate_assets is not None:
            result['generateAssets'] = self.generate_assets

        if self.image_oss_path is not None:
            result['imageOssPath'] = self.image_oss_path

        if self.jwt_token is not None:
            result['jwtToken'] = self.jwt_token

        if self.name is not None:
            result['name'] = self.name

        if self.transparent is not None:
            result['transparent'] = self.transparent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expressiveness') is not None:
            self.expressiveness = m.get('expressiveness')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('generateAssets') is not None:
            self.generate_assets = m.get('generateAssets')

        if m.get('imageOssPath') is not None:
            self.image_oss_path = m.get('imageOssPath')

        if m.get('jwtToken') is not None:
            self.jwt_token = m.get('jwtToken')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('transparent') is not None:
            self.transparent = m.get('transparent')

        return self

