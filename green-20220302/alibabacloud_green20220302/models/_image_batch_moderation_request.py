# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageBatchModerationRequest(DaraModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        # The detection types supported by Image Moderation Enhanced Edition. Separate multiple values with commas. Valid values:
        # - baselineCheck: general baseline check
        # - baselineCheck_pro: general baseline check professional edition
        # - tonalityImprove: content governance detection
        # - aigcCheck: AIGC image detection
        self.service = service
        # The parameter set for the content moderation object.
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service is not None:
            result['Service'] = self.service

        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')

        return self

