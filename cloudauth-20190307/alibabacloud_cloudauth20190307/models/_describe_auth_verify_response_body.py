# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeAuthVerifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.DescribeAuthVerifyResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.DescribeAuthVerifyResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class DescribeAuthVerifyResponseBodyResult(DaraModel):
    def __init__(
        self,
        material_info: str = None,
        spoof_back_info: str = None,
        spoof_info: str = None,
        sub_code: str = None,
    ):
        self.material_info = material_info
        self.spoof_back_info = spoof_back_info
        self.spoof_info = spoof_info
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.material_info is not None:
            result['MaterialInfo'] = self.material_info

        if self.spoof_back_info is not None:
            result['SpoofBackInfo'] = self.spoof_back_info

        if self.spoof_info is not None:
            result['SpoofInfo'] = self.spoof_info

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaterialInfo') is not None:
            self.material_info = m.get('MaterialInfo')

        if m.get('SpoofBackInfo') is not None:
            self.spoof_back_info = m.get('SpoofBackInfo')

        if m.get('SpoofInfo') is not None:
            self.spoof_info = m.get('SpoofInfo')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        return self

