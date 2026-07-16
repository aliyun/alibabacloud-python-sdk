# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth_intl20220809 import models as main_models
from darabonba.model import DaraModel

class Mobile2MetaVerifyIntlResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: main_models.Mobile2MetaVerifyIntlResponseBodyResult = None,
    ):
        # The return code.
        self.code = code
        # The return message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The returned result.
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
            temp_model = main_models.Mobile2MetaVerifyIntlResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class Mobile2MetaVerifyIntlResponseBodyResult(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        isp_name: str = None,
    ):
        # The verification result code. Valid values:
        # - 1: Consistent.
        # - 2: Inconsistent.
        # - 3: No record found.
        self.biz_code = biz_code
        # The name of the telecommunications service provider. Valid values:
        # 
        # - CMCC: China Mobile
        # - CUCC: China Unicom
        # - CTCC: China Telecom.
        self.isp_name = isp_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        return self

