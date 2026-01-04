# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExportImageRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        ossbucket: str = None,
        ossprefix: str = None,
        ossregion_id: str = None,
        role_name: str = None,
    ):
        # The ID of the image.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The OSS bucket to which you want to export the image.
        # 
        # This parameter is required.
        self.ossbucket = ossbucket
        # The prefix of the object as which you want to store the image in the OSS bucket. The prefix must be 1 to 30 characters in length and can contain digits and letters.
        self.ossprefix = ossprefix
        # The region ID.
        # 
        # This parameter is required.
        self.ossregion_id = ossregion_id
        # The name of the Resource Access Management (RAM) role.
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket

        if self.ossprefix is not None:
            result['OSSPrefix'] = self.ossprefix

        if self.ossregion_id is not None:
            result['OSSRegionId'] = self.ossregion_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')

        if m.get('OSSPrefix') is not None:
            self.ossprefix = m.get('OSSPrefix')

        if m.get('OSSRegionId') is not None:
            self.ossregion_id = m.get('OSSRegionId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

