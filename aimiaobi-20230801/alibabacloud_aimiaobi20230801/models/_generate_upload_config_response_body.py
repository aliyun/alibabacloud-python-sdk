# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GenerateUploadConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GenerateUploadConfigResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The business data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The unique ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. \\`true\\` indicates success. \\`false\\` indicates failure.
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
            temp_model = main_models.GenerateUploadConfigResponseBodyData()
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

class GenerateUploadConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        file_key: str = None,
        form_datas: Dict[str, str] = None,
        post_url: str = None,
    ):
        # The unique identifier of the file. You can use this value as a URL for AI Writing Assistant.
        self.file_key = file_key
        # The credentials for uploading the file to OSS.
        # 
        # ```json
        # {
        #   "OSSAccessKeyId": "xxx",
        #   "Signature": "xxx+xxx=",
        #   "MaxSize": 31457280,
        #   "key": "aimiaobi/dataset/2_2/xx.txt",
        #   "policy": "xxx=="
        # }
        # ```
        self.form_datas = form_datas
        # The address for uploading the file to OSS. This is a dedicated OSS domain name for AI Writing Assistant. The value is fixed to \\`https\\://aimiaobi-service-prod.oss-cn-beijing.aliyuncs.com/\\`.
        self.post_url = post_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.form_datas is not None:
            result['FormDatas'] = self.form_datas

        if self.post_url is not None:
            result['PostUrl'] = self.post_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('FormDatas') is not None:
            self.form_datas = m.get('FormDatas')

        if m.get('PostUrl') is not None:
            self.post_url = m.get('PostUrl')

        return self

