# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudcallcenter20200701 import models as main_models
from darabonba.model import DaraModel

class GetHistoricalCampaignReportResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetHistoricalCampaignReportResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetHistoricalCampaignReportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetHistoricalCampaignReportResponseBodyData(DaraModel):
    def __init__(
        self,
        abandoned_rate: float = None,
        calls_abandoned: int = None,
        calls_connected: int = None,
        calls_dialed: int = None,
        connected_rate: float = None,
        occupancy_rate: float = None,
    ):
        self.abandoned_rate = abandoned_rate
        self.calls_abandoned = calls_abandoned
        self.calls_connected = calls_connected
        self.calls_dialed = calls_dialed
        self.connected_rate = connected_rate
        self.occupancy_rate = occupancy_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abandoned_rate is not None:
            result['AbandonedRate'] = self.abandoned_rate

        if self.calls_abandoned is not None:
            result['CallsAbandoned'] = self.calls_abandoned

        if self.calls_connected is not None:
            result['CallsConnected'] = self.calls_connected

        if self.calls_dialed is not None:
            result['CallsDialed'] = self.calls_dialed

        if self.connected_rate is not None:
            result['ConnectedRate'] = self.connected_rate

        if self.occupancy_rate is not None:
            result['OccupancyRate'] = self.occupancy_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonedRate') is not None:
            self.abandoned_rate = m.get('AbandonedRate')

        if m.get('CallsAbandoned') is not None:
            self.calls_abandoned = m.get('CallsAbandoned')

        if m.get('CallsConnected') is not None:
            self.calls_connected = m.get('CallsConnected')

        if m.get('CallsDialed') is not None:
            self.calls_dialed = m.get('CallsDialed')

        if m.get('ConnectedRate') is not None:
            self.connected_rate = m.get('ConnectedRate')

        if m.get('OccupancyRate') is not None:
            self.occupancy_rate = m.get('OccupancyRate')

        return self

