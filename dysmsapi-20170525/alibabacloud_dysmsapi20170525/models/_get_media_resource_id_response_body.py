# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class GetMediaResourceIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetMediaResourceIdResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 请求状态码。
        # 
        # - 返回OK代表请求成功。
        # - 其他错误码，请参见[错误码列表](https://help.aliyun.com/document_detail/101346.html)。
        self.code = code
        # 返回数据。
        self.data = data
        # 请求ID。
        self.request_id = request_id
        # 调用接口是否成功。取值：
        # 
        # - **true**：调用成功。
        # 
        # - **false**：调用失败。
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
            temp_model = main_models.GetMediaResourceIdResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetMediaResourceIdResponseBodyData(DaraModel):
    def __init__(
        self,
        res_url_download: str = None,
        resource_id: int = None,
    ):
        # 资源下载地址。
        self.res_url_download = res_url_download
        # 资源ID。
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.res_url_download is not None:
            result['ResUrlDownload'] = self.res_url_download

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResUrlDownload') is not None:
            self.res_url_download = m.get('ResUrlDownload')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

