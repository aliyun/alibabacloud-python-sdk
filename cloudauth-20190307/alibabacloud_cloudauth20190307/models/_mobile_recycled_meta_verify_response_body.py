# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class MobileRecycledMetaVerifyResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.MobileRecycledMetaVerifyResponseBodyResultObject = None,
    ):
        # The return code. A value of 200 indicates success, and other values indicate failure.
        # Important
        # - This parameter indicates whether the API operation was called successfully. For detailed return code descriptions, see Error codes.
        # - To view the business verification result, check the fields in ResultObject.
        self.code = code
        # The returned message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The returned result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

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

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.MobileRecycledMetaVerifyResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class MobileRecycledMetaVerifyResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        isp_name: str = None,
        sub_code: str = None,
    ):
        # The query result. Valid values:
        # 
        # - 1: A query result is returned.
        # - 3: No query result is returned.
        self.biz_code = biz_code
        # The ISP name. Valid values: China Mobile - CMCC, China Unicom - CUCC, and China Telecom - CTCC.
        self.isp_name = isp_name
        # The detailed verification result. Valid values:
        # 
        # - 101: The registration time is later than or equal to the activation time of the mobile phone number.
        # - 102: The registration time is earlier than the activation time of the mobile phone number.
        # - 103: The newly activated user is not synchronized.
        # - 301: Data exception or disconnected user.
        self.sub_code = sub_code

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

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        return self

