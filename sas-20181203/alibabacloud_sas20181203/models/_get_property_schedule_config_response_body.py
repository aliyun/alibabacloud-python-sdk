# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetPropertyScheduleConfigResponseBody(DaraModel):
    def __init__(
        self,
        property_schedule_config: main_models.GetPropertyScheduleConfigResponseBodyPropertyScheduleConfig = None,
        request_id: str = None,
    ):
        # The configurations for the collection frequency of asset fingerprints.
        self.property_schedule_config = property_schedule_config
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.property_schedule_config:
            self.property_schedule_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.property_schedule_config is not None:
            result['PropertyScheduleConfig'] = self.property_schedule_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PropertyScheduleConfig') is not None:
            temp_model = main_models.GetPropertyScheduleConfigResponseBodyPropertyScheduleConfig()
            self.property_schedule_config = temp_model.from_map(m.get('PropertyScheduleConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPropertyScheduleConfigResponseBodyPropertyScheduleConfig(DaraModel):
    def __init__(
        self,
        next_schedule_time: int = None,
        schedule_time: str = None,
        type: str = None,
    ):
        # The timestamp when the next collection of asset fingerprints starts. Unit: milliseconds.
        self.next_schedule_time = next_schedule_time
        # The collection frequency of asset fingerprints. Valid values:
        # 
        # *   **0**: disabled, which indicates that the asset fingerprints are not automatically or periodically collected.
        # *   **1**: collects asset fingerprints once an hour.
        # *   **3**: collects asset fingerprints once every 3 hours.
        # *   **12**: collects asset fingerprints once every 12 hours.
        # *   **24**: collects asset fingerprints once a day.
        # *   **168**: collects asset fingerprints once every 7 days.
        self.schedule_time = schedule_time
        # The type of the asset fingerprints. Valid values:
        # 
        # *   **scheduler_port_period**: listening port
        # *   **scheduler_process_period**: running process
        # *   **scheduler_account_period**: account
        # *   **scheduler_software_period**: software
        # *   **scheduler_cron_period**: scheduled task
        # *   **scheduler_sca_period**: middleware
        # *   **scheduler_autorun_period**: startup item
        # *   **scheduler_lkm_period**: kernel module
        # *   **scheduler_sca_proxy_period**: website
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_schedule_time is not None:
            result['NextScheduleTime'] = self.next_schedule_time

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextScheduleTime') is not None:
            self.next_schedule_time = m.get('NextScheduleTime')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

