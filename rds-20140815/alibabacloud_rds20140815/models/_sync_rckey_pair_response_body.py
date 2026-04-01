# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class SyncRCKeyPairResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SyncRCKeyPairResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the result.
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
            temp_model = main_models.SyncRCKeyPairResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SyncRCKeyPairResponseBodyData(DaraModel):
    def __init__(
        self,
        is_sync_info: bool = None,
    ):
        # Indicates whether the synchronization succeeded. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_sync_info = is_sync_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_sync_info is not None:
            result['IsSyncInfo'] = self.is_sync_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSyncInfo') is not None:
            self.is_sync_info = m.get('IsSyncInfo')

        return self

