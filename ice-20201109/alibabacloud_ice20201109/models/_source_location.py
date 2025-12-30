# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SourceLocation(DaraModel):
    def __init__(
        self,
        arn: str = None,
        base_url: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        segment_delivery_configurations: str = None,
        source_location_name: str = None,
        state: int = None,
    ):
        self.arn = arn
        self.base_url = base_url
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.segment_delivery_configurations = segment_delivery_configurations
        self.source_location_name = source_location_name
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.base_url is not None:
            result['BaseUrl'] = self.base_url

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.segment_delivery_configurations is not None:
            result['SegmentDeliveryConfigurations'] = self.segment_delivery_configurations

        if self.source_location_name is not None:
            result['SourceLocationName'] = self.source_location_name

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('BaseUrl') is not None:
            self.base_url = m.get('BaseUrl')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('SegmentDeliveryConfigurations') is not None:
            self.segment_delivery_configurations = m.get('SegmentDeliveryConfigurations')

        if m.get('SourceLocationName') is not None:
            self.source_location_name = m.get('SourceLocationName')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

