# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class SaveTraceAppConfigRequest(DaraModel):
    def __init__(
        self,
        pid: str = None,
        settings: List[main_models.SaveTraceAppConfigRequestSettings] = None,
    ):
        # The process ID (PID) of the application.
        # 
        # Log on to the ARMS console. In the left-side navigation pane, choose **Application Monitoring** > **Application List**. On the Application List page, click the name of an application. The URL in the address bar contains the PID of the application. The PID is indicated in the pid=xxx format. The PID is usually percent encoded as xxx%40xxx. You must modify this value to remove the percent encoding. For example, if the PID in the URL is xxx%4074xxx, you must replace %40 with an at sign (@) to obtain xxx@74xxx.
        # 
        # This parameter is required.
        self.pid = pid
        # The settings of Application Monitoring.
        self.settings = settings

    def validate(self):
        if self.settings:
            for v1 in self.settings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pid is not None:
            result['Pid'] = self.pid

        result['Settings'] = []
        if self.settings is not None:
            for k1 in self.settings:
                result['Settings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        self.settings = []
        if m.get('Settings') is not None:
            for k1 in m.get('Settings'):
                temp_model = main_models.SaveTraceAppConfigRequestSettings()
                self.settings.append(temp_model.from_map(k1))

        return self

class SaveTraceAppConfigRequestSettings(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the settings that you want to modify. For more information about the supported settings, see the following sections.
        # 
        # *   Trace sampling settings
        # *   Agent switch settings
        # *   Threshold settings
        # *   Advanced settings
        # *   Thread settings
        # *   Memory snapshot settings
        # *   URL convergence settings
        # *   Business log association settings
        self.key = key
        # The value of the settings that you want to modify. For more information about the supported settings, see the following sections.
        # 
        # *   Trace sampling settings
        # *   Agent switch settings
        # *   Threshold settings
        # *   Advanced settings
        # *   Thread settings
        # *   Memory snapshot settings
        # *   URL convergence settings
        # *   Business log association settings
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

