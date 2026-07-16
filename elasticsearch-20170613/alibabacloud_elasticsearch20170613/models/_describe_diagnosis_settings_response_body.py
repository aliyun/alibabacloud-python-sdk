# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class DescribeDiagnosisSettingsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribeDiagnosisSettingsResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.DescribeDiagnosisSettingsResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class DescribeDiagnosisSettingsResponseBodyResult(DaraModel):
    def __init__(
        self,
        authorization_status: bool = None,
        daily_limit: int = None,
        daily_schedule_enabled: bool = None,
        diagnosis_mode: str = None,
        scene: str = None,
        selected_items: List[str] = None,
        update_time: int = None,
    ):
        self.authorization_status = authorization_status
        self.daily_limit = daily_limit
        self.daily_schedule_enabled = daily_schedule_enabled
        self.diagnosis_mode = diagnosis_mode
        # The scenario of intelligent O&M.
        self.scene = scene
        self.selected_items = selected_items
        # The timestamp when the intelligent O&M scenario was last updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_status is not None:
            result['authorizationStatus'] = self.authorization_status

        if self.daily_limit is not None:
            result['dailyLimit'] = self.daily_limit

        if self.daily_schedule_enabled is not None:
            result['dailyScheduleEnabled'] = self.daily_schedule_enabled

        if self.diagnosis_mode is not None:
            result['diagnosisMode'] = self.diagnosis_mode

        if self.scene is not None:
            result['scene'] = self.scene

        if self.selected_items is not None:
            result['selectedItems'] = self.selected_items

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authorizationStatus') is not None:
            self.authorization_status = m.get('authorizationStatus')

        if m.get('dailyLimit') is not None:
            self.daily_limit = m.get('dailyLimit')

        if m.get('dailyScheduleEnabled') is not None:
            self.daily_schedule_enabled = m.get('dailyScheduleEnabled')

        if m.get('diagnosisMode') is not None:
            self.diagnosis_mode = m.get('diagnosisMode')

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        if m.get('selectedItems') is not None:
            self.selected_items = m.get('selectedItems')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

