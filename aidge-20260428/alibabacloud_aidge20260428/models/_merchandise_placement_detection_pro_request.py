# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MerchandisePlacementDetectionProRequest(DaraModel):
    def __init__(
        self,
        image_url: str = None,
        rule: str = None,
        type: str = None,
    ):
        # The HTTPS URL of the display image to detect.
        # 
        # This parameter is required.
        self.image_url = image_url
        # The detection rule. When non-empty, this value takes priority as the model prompt.
        self.rule = rule
        # The product type. This parameter must be set to Genki Forest when Rule is empty.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

