# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCheckDetailRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        lang: str = None,
        region_id: str = None,
    ):
        # The ID of the check item.
        # 
        # >  You can call the [ListCheckResult](~~ListCheckResult~~) operation to query the IDs of check items.
        # 
        # This parameter is required.
        self.check_id = check_id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese.
        # *   **en**: English.
        self.lang = lang
        # The region ID of the instance.
        # 
        # >  You can call the [ListCloudAssetInstances](~~ListCloudAssetInstances~~) operation to query the region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

