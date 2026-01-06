# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class GetSparkReplSessionResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSparkReplSessionResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
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
            temp_model = main_models.GetSparkReplSessionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetSparkReplSessionResponseBodyData(DaraModel):
    def __init__(
        self,
        active: str = None,
        aliyun_uid: str = None,
        attempt_id: str = None,
        error: str = None,
        session_id: int = None,
        state: str = None,
        web_ui_address: str = None,
    ):
        # Indicates whether the session is active. Valid values:
        # 
        # *   true
        # *   false
        self.active = active
        # The ID of the Alibaba Cloud account that owns the cluster.
        self.aliyun_uid = aliyun_uid
        # The attempt ID of the Spark application.
        self.attempt_id = attempt_id
        # The error message.
        self.error = error
        # The ID of the session that executes the code.
        self.session_id = session_id
        # The status of the session. Valid values:
        # 
        # *   IDLE
        # *   BUSY
        # *   DEAD
        self.state = state
        # The URL of the web UI for the Spark application.
        self.web_ui_address = web_ui_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.attempt_id is not None:
            result['AttemptId'] = self.attempt_id

        if self.error is not None:
            result['Error'] = self.error

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.state is not None:
            result['State'] = self.state

        if self.web_ui_address is not None:
            result['WebUiAddress'] = self.web_ui_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('AttemptId') is not None:
            self.attempt_id = m.get('AttemptId')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('WebUiAddress') is not None:
            self.web_ui_address = m.get('WebUiAddress')

        return self

