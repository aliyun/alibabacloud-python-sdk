# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDeviceAutoUpgradePolicyResponseBody(DaraModel):
    def __init__(
        self,
        cron_expression: str = None,
        duration: str = None,
        jitter: str = None,
        request_id: str = None,
        serial_number: str = None,
        smart_agid: str = None,
        time_zone: str = None,
        upgrade_type: str = None,
    ):
        # The time when upgrades start. The time was configured by using a cron expression.
        # 
        # Example value: `0 0 4 1/1 * ?`. The example value indicates that upgrades start at 04:00:00 (UTC+8) on the first day of each month.
        self.cron_expression = cron_expression
        # The time period during which upgrades are performed.
        # 
        # Valid values: **30 to 120**.
        # 
        # Unit: minutes.
        self.duration = duration
        # The time differences between upgrades. Unit: minutes.
        self.jitter = jitter
        # The ID of the request.
        self.request_id = request_id
        # The serial number of the SAG instance.
        self.serial_number = serial_number
        # The ID of the SAG instance.
        self.smart_agid = smart_agid
        # The time zone in which the trigger period takes effect.
        self.time_zone = time_zone
        # The update type. Valid values:
        # 
        # *   **scheduled**: scheduled upgrade.
        # *   **boot**: automatic upgrade upon instance startup.
        # *   **manual**: manual upgrade.
        self.upgrade_type = upgrade_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.jitter is not None:
            result['Jitter'] = self.jitter

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        if self.upgrade_type is not None:
            result['UpgradeType'] = self.upgrade_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Jitter') is not None:
            self.jitter = m.get('Jitter')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        if m.get('UpgradeType') is not None:
            self.upgrade_type = m.get('UpgradeType')

        return self

