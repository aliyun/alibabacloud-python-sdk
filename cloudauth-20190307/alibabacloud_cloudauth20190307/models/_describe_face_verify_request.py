# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFaceVerifyRequest(DaraModel):
    def __init__(
        self,
        certify_id: str = None,
        picture_return_type: str = None,
        scene_id: int = None,
    ):
        # Unique identifier for real-person authentication.
        self.certify_id = certify_id
        # Image return type.
        self.picture_return_type = picture_return_type
        # Authentication scene ID.
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id

        if self.picture_return_type is not None:
            result['PictureReturnType'] = self.picture_return_type

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')

        if m.get('PictureReturnType') is not None:
            self.picture_return_type = m.get('PictureReturnType')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        return self

