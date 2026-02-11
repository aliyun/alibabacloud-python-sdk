# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_arms20210422 import models as main_models
from darabonba.model import DaraModel

class CreateRetcodeAppResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        retcode_app_data_bean: main_models.CreateRetcodeAppResponseBodyRetcodeAppDataBean = None,
    ):
        self.request_id = request_id
        self.retcode_app_data_bean = retcode_app_data_bean

    def validate(self):
        if self.retcode_app_data_bean:
            self.retcode_app_data_bean.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.retcode_app_data_bean is not None:
            result['RetcodeAppDataBean'] = self.retcode_app_data_bean.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RetcodeAppDataBean') is not None:
            temp_model = main_models.CreateRetcodeAppResponseBodyRetcodeAppDataBean()
            self.retcode_app_data_bean = temp_model.from_map(m.get('RetcodeAppDataBean'))

        return self

class CreateRetcodeAppResponseBodyRetcodeAppDataBean(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        pid: str = None,
    ):
        self.app_id = app_id
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

        if self.pid is not None:
            result['Pid'] = self.pid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        return self

