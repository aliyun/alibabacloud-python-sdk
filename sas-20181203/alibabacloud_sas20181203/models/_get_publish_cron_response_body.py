# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetPublishCronResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetPublishCronResponseBodyData = None,
        request_id: str = None,
    ):
        # The publish scheduling configuration.
        self.data = data
        # The request ID. Alibaba Cloud generates a unique identifier for each request. You can use the ID to troubleshoot issues.
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
            temp_model = main_models.GetPublishCronResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPublishCronResponseBodyData(DaraModel):
    def __init__(
        self,
        cron: str = None,
        cron_day: str = None,
        cron_time: int = None,
        cron_type: str = None,
        duration: int = None,
    ):
        # The cron expression for the upgrade start time.
        self.cron = cron
        # The day of the week for the upgrade. Valid values:
        # - **MON**: Monday
        # - **TUE**: Tuesday
        # - **WED**: Wednesday
        # - **THU**: Thursday
        # - **FRI**: Friday
        # - **SAT**: Saturday
        # - **SUN**: Sunday.
        self.cron_day = cron_day
        # The publish start timestamp. Unit: milliseconds.
        self.cron_time = cron_time
        # The upgrade start cycle type. Valid values:
        # - **day**: every day
        # - **week**: every week.
        self.cron_type = cron_type
        # The upgrade duration. Unit: hours.
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['Cron'] = self.cron

        if self.cron_day is not None:
            result['CronDay'] = self.cron_day

        if self.cron_time is not None:
            result['CronTime'] = self.cron_time

        if self.cron_type is not None:
            result['CronType'] = self.cron_type

        if self.duration is not None:
            result['Duration'] = self.duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')

        if m.get('CronDay') is not None:
            self.cron_day = m.get('CronDay')

        if m.get('CronTime') is not None:
            self.cron_time = m.get('CronTime')

        if m.get('CronType') is not None:
            self.cron_type = m.get('CronType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        return self

