# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_emas_appmonitor20190611 import models as main_models
from darabonba.model import DaraModel

class RequestUploadTokenResponseBody(DaraModel):
    def __init__(
        self,
        args: Dict[str, Any] = None,
        error_code: int = None,
        message: str = None,
        model: main_models.RequestUploadTokenResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Args
        self.args = args
        self.error_code = error_code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.model is not None:
            result['Model'] = self.model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Model') is not None:
            temp_model = main_models.RequestUploadTokenResponseBodyModel()
            self.model = temp_model.from_map(m.get('Model'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class RequestUploadTokenResponseBodyModel(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        endpoint: str = None,
        security_token: str = None,
        upload_bucket: str = None,
        upload_dir: str = None,
    ):
        # OSS AccessKeyId
        self.access_key_id = access_key_id
        # OSS AccessKeySecret
        self.access_key_secret = access_key_secret
        self.endpoint = endpoint
        self.security_token = security_token
        self.upload_bucket = upload_bucket
        self.upload_dir = upload_dir

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.upload_bucket is not None:
            result['UploadBucket'] = self.upload_bucket

        if self.upload_dir is not None:
            result['UploadDir'] = self.upload_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('UploadBucket') is not None:
            self.upload_bucket = m.get('UploadBucket')

        if m.get('UploadDir') is not None:
            self.upload_dir = m.get('UploadDir')

        return self

