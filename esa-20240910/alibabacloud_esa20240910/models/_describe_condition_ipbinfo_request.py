# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeConditionIPBInfoRequest(DaraModel):
    def __init__(
        self,
        data_id: str = None,
    ):
        # The configuration ID. Valid values:
        # - condition_region_config_cn: provides a mapping list of region Chinese names and their corresponding codes.
        # - condition_region_config_en: provides a mapping list of region English names and their corresponding codes.
        # - condition_isp_config_cn: provides a mapping list of ISP Chinese names and their corresponding codes.
        # - condition_isp_config_en: provides a mapping list of ISP English names and their corresponding codes.
        # - condition_country_config_cn: provides a mapping list of country Chinese names and their corresponding codes.
        # - condition_country_config_en: provides a mapping list of country English names and their corresponding codes.
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

