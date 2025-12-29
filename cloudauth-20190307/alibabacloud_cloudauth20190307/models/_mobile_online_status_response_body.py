# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class MobileOnlineStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.MobileOnlineStatusResponseBodyResultObject = None,
    ):
        # Return code: 200 for success, others for failure.
        self.code = code
        # Return message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned result information
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
            temp_model = main_models.MobileOnlineStatusResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class MobileOnlineStatusResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        isp_name: str = None,
        sub_code: str = None,
    ):
        # Verification result
        # 
        # - 1: Available online 
        # - 2: Not available online (see subCode for details)
        # - 3: No query result
        self.biz_code = biz_code
        # ISP name
        # 
        # - CMCC: China Mobile 
        # - CUCC: China Unicom 
        # - CTCC: China Telecom
        self.isp_name = isp_name
        # Verification details
        # 
        # - 101: Available online 
        # - 201: Suspended 
        # - 202: Disconnected 
        # - 203: Online but not available 
        # - 204: Not online 
        # - 301: No record found
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

