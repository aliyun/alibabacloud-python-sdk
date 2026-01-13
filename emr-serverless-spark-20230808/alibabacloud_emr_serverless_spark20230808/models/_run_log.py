# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunLog(DaraModel):
    def __init__(
        self,
        driver_startup: str = None,
        driver_std_error: str = None,
        driver_std_out: str = None,
        driver_syslog: str = None,
    ):
        self.driver_startup = driver_startup
        self.driver_std_error = driver_std_error
        self.driver_std_out = driver_std_out
        self.driver_syslog = driver_syslog

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.driver_startup is not None:
            result['driverStartup'] = self.driver_startup

        if self.driver_std_error is not None:
            result['driverStdError'] = self.driver_std_error

        if self.driver_std_out is not None:
            result['driverStdOut'] = self.driver_std_out

        if self.driver_syslog is not None:
            result['driverSyslog'] = self.driver_syslog

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('driverStartup') is not None:
            self.driver_startup = m.get('driverStartup')

        if m.get('driverStdError') is not None:
            self.driver_std_error = m.get('driverStdError')

        if m.get('driverStdOut') is not None:
            self.driver_std_out = m.get('driverStdOut')

        if m.get('driverSyslog') is not None:
            self.driver_syslog = m.get('driverSyslog')

        return self

