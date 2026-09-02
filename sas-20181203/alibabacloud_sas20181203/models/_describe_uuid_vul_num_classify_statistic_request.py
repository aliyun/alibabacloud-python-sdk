# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUuidVulNumClassifyStatisticRequest(DaraModel):
    def __init__(
        self,
        image_vul: bool = None,
        uuids: str = None,
    ):
        self.image_vul = image_vul
        # This parameter is required.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_vul is not None:
            result['ImageVul'] = self.image_vul

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageVul') is not None:
            self.image_vul = m.get('ImageVul')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

