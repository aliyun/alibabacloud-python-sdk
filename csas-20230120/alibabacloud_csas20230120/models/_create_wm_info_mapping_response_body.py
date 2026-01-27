# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreateWmInfoMappingResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateWmInfoMappingResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateWmInfoMappingResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateWmInfoMappingResponseBodyData(DaraModel):
    def __init__(
        self,
        wm_info_uint: int = None,
    ):
        self.wm_info_uint = wm_info_uint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.wm_info_uint is not None:
            result['WmInfoUint'] = self.wm_info_uint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WmInfoUint') is not None:
            self.wm_info_uint = m.get('WmInfoUint')

        return self

