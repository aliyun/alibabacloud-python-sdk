# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class SparkAppInfo(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        dbcluster_id: str = None,
        detail: main_models.Detail = None,
        message: str = None,
        priority: str = None,
        state: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.dbcluster_id = dbcluster_id
        self.detail = detail
        self.message = message
        self.priority = priority
        self.state = state

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.detail is not None:
            result['Detail'] = self.detail.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Detail') is not None:
            temp_model = main_models.Detail()
            self.detail = temp_model.from_map(m.get('Detail'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

