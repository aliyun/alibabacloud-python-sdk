# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetImageSceneLabelListConfRequest(DaraModel):
    def __init__(
        self,
        image_service_code: str = None,
        region_id: str = None,
    ):
        # Service code.
        self.image_service_code = image_service_code
        # Region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_service_code is not None:
            result['ImageServiceCode'] = self.image_service_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageServiceCode') is not None:
            self.image_service_code = m.get('ImageServiceCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

