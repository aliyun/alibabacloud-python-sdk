# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCdnConditionIPBInfoRequest(DaraModel):
    def __init__(
        self,
        data_id: str = None,
    ):
        # The configuration ID. Valid values:
        # 
        # *   condition_region_config_cn
        # *   condition_region_config_en
        # *   condition_isp_config_cn
        # *   condition_isp_config_en
        # *   condition_country_config_cn
        # *   condition_country_config_en
        # 
        # This parameter is required.
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_id is not None:
            result['DataId'] = self.data_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        return self

