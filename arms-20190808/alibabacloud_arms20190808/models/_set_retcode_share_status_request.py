# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetRetcodeShareStatusRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        pid: str = None,
        status: bool = None,
    ):
        # The name of the application that is monitored by Browser Monitoring.
        self.app_name = app_name
        # The process identifier (PID) of the application. 
        # 
        # Log on to the **ARMS console**. In the left-side navigation pane, choose **Browser Monitoring** > **Browser Monitoring**. On the Browser Monitoring page, click the name of an application. The URL in the address bar contains the process ID (PID) of the application. The PID is indicated in the `pid=xxx` format. The PID is usually percent encoded as `xxx%40xxx`. You must modify this value to remove the percent encoding. For example, if the PID in the URL is `eb4zdose6v%409781be0f44d****`, you must replace `%40` with @ to obtain `eb4zdose6v@9781be0f44d****`.
        self.pid = pid
        # Specifies whether to turn on or turn off the logon-free sharing switch. Valid values:
        # 
        # *   `true`: Turn on the switch.
        # *   `false`: Turn off the switch.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

