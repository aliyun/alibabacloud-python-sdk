# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSourceLocationRequest(DaraModel):
    def __init__(
        self,
        base_url: str = None,
        enable_segment_delivery: bool = None,
        segment_delivery_url: str = None,
        source_location_name: str = None,
    ):
        # The protocol and hostname of the source location.
        # 
        # This parameter is required.
        self.base_url = base_url
        # Specifies whether to use an independent domain name to access the segments.
        self.enable_segment_delivery = enable_segment_delivery
        # The domain name used to access the segments.
        self.segment_delivery_url = segment_delivery_url
        # The name of the source location.
        # 
        # This parameter is required.
        self.source_location_name = source_location_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        if self.enable_segment_delivery is not None:
            result['EnableSegmentDelivery'] = self.enable_segment_delivery

        if self.segment_delivery_url is not None:
            result['SegmentDeliveryUrl'] = self.segment_delivery_url

        if self.source_location_name is not None:
            result['SourceLocationName'] = self.source_location_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        if m.get('EnableSegmentDelivery') is not None:
            self.enable_segment_delivery = m.get('EnableSegmentDelivery')

        if m.get('SegmentDeliveryUrl') is not None:
            self.segment_delivery_url = m.get('SegmentDeliveryUrl')

        if m.get('SourceLocationName') is not None:
            self.source_location_name = m.get('SourceLocationName')

        return self

