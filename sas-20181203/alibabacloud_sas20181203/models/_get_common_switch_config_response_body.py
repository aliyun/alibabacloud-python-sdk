# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCommonSwitchConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetCommonSwitchConfigResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
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
            temp_model = main_models.GetCommonSwitchConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCommonSwitchConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        target_default: str = None,
        target_sync_status: str = None,
    ):
        # Specifies whether to turn on the switch for newly added servers. Valid values:
        # 
        # *   **add**: By default, the switch is turned on for newly added servers.
        # *   **del**: By default, the switch is turned off for newly added servers.
        self.target_default = target_default
        # The status of the synchronization. Valid values:
        # 
        # *   **sync**: The modifications are being synchronized.
        # *   **valid**: The modifications has taken effect.
        self.target_sync_status = target_sync_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_default is not None:
            result['TargetDefault'] = self.target_default

        if self.target_sync_status is not None:
            result['TargetSyncStatus'] = self.target_sync_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetDefault') is not None:
            self.target_default = m.get('TargetDefault')

        if m.get('TargetSyncStatus') is not None:
            self.target_sync_status = m.get('TargetSyncStatus')

        return self

