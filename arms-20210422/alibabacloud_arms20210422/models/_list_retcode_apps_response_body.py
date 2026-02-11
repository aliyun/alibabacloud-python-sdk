# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20210422 import models as main_models
from darabonba.model import DaraModel

class ListRetcodeAppsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        retcode_apps: List[main_models.ListRetcodeAppsResponseBodyRetcodeApps] = None,
    ):
        self.request_id = request_id
        self.retcode_apps = retcode_apps

    def validate(self):
        if self.retcode_apps:
            for v1 in self.retcode_apps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RetcodeApps'] = []
        if self.retcode_apps is not None:
            for k1 in self.retcode_apps:
                result['RetcodeApps'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.retcode_apps = []
        if m.get('RetcodeApps') is not None:
            for k1 in m.get('RetcodeApps'):
                temp_model = main_models.ListRetcodeAppsResponseBodyRetcodeApps()
                self.retcode_apps.append(temp_model.from_map(k1))

        return self

class ListRetcodeAppsResponseBodyRetcodeApps(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        pid: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.pid is not None:
            result['Pid'] = self.pid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        return self

