# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyFaceRecordRequest(DaraModel):
    def __init__(
        self,
        face_group_code: str = None,
        img_oss_infos: str = None,
    ):
        # This parameter is required.
        self.face_group_code = face_group_code
        # This parameter is required.
        self.img_oss_infos = img_oss_infos

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_group_code is not None:
            result['FaceGroupCode'] = self.face_group_code

        if self.img_oss_infos is not None:
            result['ImgOssInfos'] = self.img_oss_infos

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceGroupCode') is not None:
            self.face_group_code = m.get('FaceGroupCode')

        if m.get('ImgOssInfos') is not None:
            self.img_oss_infos = m.get('ImgOssInfos')

        return self

