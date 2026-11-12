# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetImageDistributeInfoRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        version_id: str = None,
    ):
        # The ID of the image whose region distribution information you want to query.
        self.image_id = image_id
        # The ID of the image version. If this parameter is not specified, the online version of the image is queried.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

