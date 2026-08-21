# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDailyPlayRegionStatisRequest(DaraModel):
    def __init__(
        self,
        date: str = None,
        media_region: str = None,
    ):
        # The playback date, in days. Format: yyyy-MM-dd.
        # 
        # > 
        # > - Only daily queries are supported.
        # > - Only data within the past year can be queried.
        # 
        # This parameter is required.
        self.date = date
        # The media asset region ID. Specify this parameter to perform a filtered query for the playback data of all audio and video files in a specified service region. Valid values:
        # 
        # - cn-beijing: China (Beijing)
        # - cn-shanghai: China (Shanghai)
        # - cn-shenzhen: China (Shenzhen)
        # - ap-northeast-1: Japan (Tokyo)
        # - ap-southeast-1: Singapore
        # - ap-southeast-5: Indonesia (Jakarta)
        # - eu-central-1: Germany (Frankfurt)
        # 
        # This parameter is required.
        self.media_region = media_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.media_region is not None:
            result['MediaRegion'] = self.media_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('MediaRegion') is not None:
            self.media_region = m.get('MediaRegion')

        return self

