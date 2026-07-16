# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class GetBdrcServiceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetBdrcServiceResponseBodyData = None,
        request_id: str = None,
    ):
        # The data that is returned if the call is successful.
        self.data = data
        # The unique identity of the request.
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
            temp_model = main_models.GetBdrcServiceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetBdrcServiceResponseBodyData(DaraModel):
    def __init__(
        self,
        open_time: int = None,
        protection_score_updated_time: int = None,
        service_initialize_status: str = None,
        service_status: str = None,
    ):
        # The time when the service was enabled (UNIX timestamp).
        self.open_time = open_time
        # The time when the data protection score was updated (UNIX timestamp).
        self.protection_score_updated_time = protection_score_updated_time
        # The initialization status of the service.
        self.service_initialize_status = service_initialize_status
        # The enabling status of the service.
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_time is not None:
            result['OpenTime'] = self.open_time

        if self.protection_score_updated_time is not None:
            result['ProtectionScoreUpdatedTime'] = self.protection_score_updated_time

        if self.service_initialize_status is not None:
            result['ServiceInitializeStatus'] = self.service_initialize_status

        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')

        if m.get('ProtectionScoreUpdatedTime') is not None:
            self.protection_score_updated_time = m.get('ProtectionScoreUpdatedTime')

        if m.get('ServiceInitializeStatus') is not None:
            self.service_initialize_status = m.get('ServiceInitializeStatus')

        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')

        return self

