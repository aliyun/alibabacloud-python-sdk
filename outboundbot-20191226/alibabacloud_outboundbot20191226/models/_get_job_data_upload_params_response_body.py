# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class GetJobDataUploadParamsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        upload_params: main_models.GetJobDataUploadParamsResponseBodyUploadParams = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.upload_params = upload_params

    def validate(self):
        if self.upload_params:
            self.upload_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.upload_params is not None:
            result['UploadParams'] = self.upload_params.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UploadParams') is not None:
            temp_model = main_models.GetJobDataUploadParamsResponseBodyUploadParams()
            self.upload_params = temp_model.from_map(m.get('UploadParams'))

        return self

class GetJobDataUploadParamsResponseBodyUploadParams(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        expire: int = None,
        folder: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
    ):
        self.access_id = access_id
        self.expire = expire
        self.folder = folder
        self.host = host
        self.policy = policy
        self.signature = signature

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

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.signature is not None:
            result['Signature'] = self.signature

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

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        return self

