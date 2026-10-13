# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class GenerateUploadUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GenerateUploadUrlResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

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
            temp_model = main_models.GenerateUploadUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GenerateUploadUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        expire: int = None,
        folder: str = None,
        host: str = None,
        message: str = None,
        policy: str = None,
        signature: str = None,
        success: bool = None,
    ):
        self.access_id = access_id
        self.expire = expire
        self.folder = folder
        self.host = host
        self.message = message
        self.policy = policy
        self.signature = signature
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.folder is not None:
            result['Folder'] = self.folder

        if self.host is not None:
            result['Host'] = self.host

        if self.message is not None:
            result['Message'] = self.message

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.signature is not None:
            result['Signature'] = self.signature

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('Folder') is not None:
            self.folder = m.get('Folder')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

