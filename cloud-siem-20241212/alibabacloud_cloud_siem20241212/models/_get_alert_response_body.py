# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class GetAlertResponseBody(DaraModel):
    def __init__(
        self,
        alert: main_models.GetAlertResponseBodyAlert = None,
        request_id: str = None,
    ):
        # If this value is true, the minor engine version is not the latest version.
        # 
        # > If the minor engine version of your server is not the latest version, the sampling logs may be inaccurate, which causes inaccurate IP statistics. We recommend that you upgrade the minor engine version at your earliest convenience.
        self.alert = alert
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.alert:
            self.alert.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert is not None:
            result['Alert'] = self.alert.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alert') is not None:
            temp_model = main_models.GetAlertResponseBodyAlert()
            self.alert = temp_model.from_map(m.get('Alert'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAlertResponseBodyAlert(DaraModel):
    def __init__(
        self,
        alert_record: str = None,
        alert_uuid: str = None,
    ):
        # The alert content.
        self.alert_record = alert_record
        # The alert UUID.
        self.alert_uuid = alert_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_record is not None:
            result['AlertRecord'] = self.alert_record

        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertRecord') is not None:
            self.alert_record = m.get('AlertRecord')

        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')

        return self

