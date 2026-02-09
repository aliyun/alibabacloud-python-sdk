# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class GetMcubeFileTokenResponseBody(DaraModel):
    def __init__(
        self,
        get_file_token_result: main_models.GetMcubeFileTokenResponseBodyGetFileTokenResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.get_file_token_result = get_file_token_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.get_file_token_result:
            self.get_file_token_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.get_file_token_result is not None:
            result['GetFileTokenResult'] = self.get_file_token_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetFileTokenResult') is not None:
            temp_model = main_models.GetMcubeFileTokenResponseBodyGetFileTokenResult()
            self.get_file_token_result = temp_model.from_map(m.get('GetFileTokenResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class GetMcubeFileTokenResponseBodyGetFileTokenResult(DaraModel):
    def __init__(
        self,
        file_token: main_models.GetMcubeFileTokenResponseBodyGetFileTokenResultFileToken = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.file_token = file_token
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.file_token:
            self.file_token.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_token is not None:
            result['FileToken'] = self.file_token.to_map()

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileToken') is not None:
            temp_model = main_models.GetMcubeFileTokenResponseBodyGetFileTokenResultFileToken()
            self.file_token = temp_model.from_map(m.get('FileToken'))

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMcubeFileTokenResponseBodyGetFileTokenResultFileToken(DaraModel):
    def __init__(
        self,
        accessid: str = None,
        dir: str = None,
        expire: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
    ):
        self.accessid = accessid
        self.dir = dir
        self.expire = expire
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
        if self.accessid is not None:
            result['Accessid'] = self.accessid

        if self.dir is not None:
            result['Dir'] = self.dir

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.host is not None:
            result['Host'] = self.host

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.signature is not None:
            result['Signature'] = self.signature

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')

        if m.get('Dir') is not None:
            self.dir = m.get('Dir')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Signature') is not None:
            self.signature = m.get('Signature')

        return self

