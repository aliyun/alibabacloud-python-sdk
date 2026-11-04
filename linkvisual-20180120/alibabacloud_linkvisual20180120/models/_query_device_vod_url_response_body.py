# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class QueryDeviceVodUrlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryDeviceVodUrlResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. Valid values:
        # 
        # - **200**: The call was successful.
        # - Other values: The call failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/145071.html).
        self.code = code
        # The query result.
        self.data = data
        # The error message returned if the call fails.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - **true**: The call was successful.
        # - **false**: The call failed.
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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

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
            temp_model = main_models.QueryDeviceVodUrlResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryDeviceVodUrlResponseBodyData(DaraModel):
    def __init__(
        self,
        decrypt_key: str = None,
        stun_info: str = None,
        vod_url: str = None,
    ):
        # The decryption key.
        # A decryption key is generated when the **ShouldEncrypt** parameter is set to **true**.
        self.decrypt_key = decrypt_key
        self.stun_info = stun_info
        # The URL of the local recording.
        self.vod_url = vod_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.decrypt_key is not None:
            result['DecryptKey'] = self.decrypt_key

        if self.stun_info is not None:
            result['StunInfo'] = self.stun_info

        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DecryptKey') is not None:
            self.decrypt_key = m.get('DecryptKey')

        if m.get('StunInfo') is not None:
            self.stun_info = m.get('StunInfo')

        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')

        return self

