# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetBackupAutoConfigStatusResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetBackupAutoConfigStatusResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
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
            temp_model = main_models.GetBackupAutoConfigStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetBackupAutoConfigStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        can_config_auto: bool = None,
    ):
        # Indicates whether the anti-ransomware policy for servers can be automatically configured by the managed anti-ransomware feature. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.can_config_auto = can_config_auto

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_config_auto is not None:
            result['CanConfigAuto'] = self.can_config_auto

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanConfigAuto') is not None:
            self.can_config_auto = m.get('CanConfigAuto')

        return self

