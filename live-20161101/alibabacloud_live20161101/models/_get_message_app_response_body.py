# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class GetMessageAppResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetMessageAppResponseBodyResult = None,
    ):
        # The ID of the request.
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
            temp_model = main_models.GetMessageAppResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetMessageAppResponseBodyResult(DaraModel):
    def __init__(
        self,
        app_config: Dict[str, str] = None,
        app_id: str = None,
        app_name: str = None,
        create_time: int = None,
        extension: Dict[str, str] = None,
        status: int = None,
    ):
        # The configurations of the application.
        self.app_config = app_config
        # The ID of the interactive messaging application.
        self.app_id = app_id
        # The name of the interactive messaging application.
        self.app_name = app_name
        # The time when the interactive messaging application was created. The time is displayed in UTC.
        self.create_time = create_time
        # The extended field.
        self.extension = extension
        # The status of the interactive message application. A value of 1 indicates that the application is normal.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_config is not None:
            result['AppConfig'] = self.app_config

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.extension is not None:
            result['Extension'] = self.extension

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConfig') is not None:
            self.app_config = m.get('AppConfig')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

