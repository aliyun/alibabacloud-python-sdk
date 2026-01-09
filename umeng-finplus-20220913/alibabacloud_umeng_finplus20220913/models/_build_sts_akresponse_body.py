# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_umeng_finplus20220913 import models as main_models
from darabonba.model import DaraModel

class BuildStsAKResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.BuildStsAKResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.BuildStsAKResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class BuildStsAKResponseBodyData(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        endpoint: str = None,
        id: str = None,
        path: str = None,
        secret: str = None,
        token: str = None,
    ):
        self.bucket = bucket
        self.endpoint = endpoint
        self.id = id
        self.path = path
        self.secret = secret
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['bucket'] = self.bucket

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.id is not None:
            result['id'] = self.id

        if self.path is not None:
            result['path'] = self.path

        if self.secret is not None:
            result['secret'] = self.secret

        if self.token is not None:
            result['token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('secret') is not None:
            self.secret = m.get('secret')

        if m.get('token') is not None:
            self.token = m.get('token')

        return self

