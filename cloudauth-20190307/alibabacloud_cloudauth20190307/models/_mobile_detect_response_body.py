# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class MobileDetectResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.MobileDetectResponseBodyResultObject = None,
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
            temp_model = main_models.MobileDetectResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class MobileDetectResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        charge_count: str = None,
        items: List[main_models.MobileDetectResponseBodyResultObjectItems] = None,
    ):
        # Billing count, the total billing count in one request
        self.charge_count = charge_count
        # Verification results set
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_count is not None:
            result['ChargeCount'] = self.charge_count

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeCount') is not None:
            self.charge_count = m.get('ChargeCount')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.MobileDetectResponseBodyResultObjectItems()
                self.items.append(temp_model.from_map(k1))

        return self

class MobileDetectResponseBodyResultObjectItems(DaraModel):
    def __init__(
        self,
        area: str = None,
        biz_code: str = None,
        isp_name: str = None,
        mobile: str = None,
        sub_code: str = None,
    ):
        # Phone number\\"s area (only for plaintext phone numbers)
        self.area = area
        # Verification result
        # 
        # - 1: Available online 
        # - 2: Not available online
        # - 3: No query result
        self.biz_code = biz_code
        # Operator name
        # 
        # - CMCC: China Mobile 
        # - CUCC: China Unicom 
        # - CTCC: China Telecom
        self.isp_name = isp_name
        # Phone number
        self.mobile = mobile
        # Verification details
        # 
        # - 101: Available number
        # - 102: Empty number
        # - 103: Suspended 
        # - 104: Silent number (inactive small number, new number, non-smartphone user within the last six months) 
        # - 105: Risky number (long-term shutdown or no voice service activated and prone to complaints)
        # - 301: No record found
        self.sub_code = sub_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.sub_code is not None:
            result['SubCode'] = self.sub_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')

        return self

