# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class CreateKyuubiServiceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateKyuubiServiceResponseBodyData = None,
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
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.CreateKyuubiServiceResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreateKyuubiServiceResponseBodyData(DaraModel):
    def __init__(
        self,
        kyuubi_service_id: str = None,
    ):
        # Kyuubi Service ID。
        self.kyuubi_service_id = kyuubi_service_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kyuubi_service_id is not None:
            result['kyuubiServiceId'] = self.kyuubi_service_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kyuubiServiceId') is not None:
            self.kyuubi_service_id = m.get('kyuubiServiceId')

        return self

