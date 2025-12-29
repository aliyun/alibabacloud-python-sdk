# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class VehicleMetaVerifyV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.VehicleMetaVerifyV2ResponseBodyResultObject = None,
    ):
        # Return code, **200** indicates successful API response.
        self.code = code
        # Return message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Returned result
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
            temp_model = main_models.VehicleMetaVerifyV2ResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class VehicleMetaVerifyV2ResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        vehicle_info: str = None,
    ):
        # Verification result code:
        # - **1**: Verification consistent.
        # - **2**: Verification inconsistent.
        # - **3**: No record found.
        self.biz_code = biz_code
        # Detailed vehicle information.
        self.vehicle_info = vehicle_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.vehicle_info is not None:
            result['VehicleInfo'] = self.vehicle_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('VehicleInfo') is not None:
            self.vehicle_info = m.get('VehicleInfo')

        return self

