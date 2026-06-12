# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMetricStoreMeteringModeRequest(DaraModel):
    def __init__(
        self,
        metering_mode: str = None,
    ):
        # The billing mode to which you want to switch. Valid values: ChargeByFunction and ChargeByDataIngest. ChargeByFunction specifies the [pay-by-feature](https://help.aliyun.com/document_detail/48220.html) mode. ChargeByDataIngest specifies the [pay-by-ingested-data](https://help.aliyun.com/document_detail/2365756.html) mode.
        # 
        # This parameter is required.
        self.metering_mode = metering_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metering_mode is not None:
            result['meteringMode'] = self.metering_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('meteringMode') is not None:
            self.metering_mode = m.get('meteringMode')

        return self

