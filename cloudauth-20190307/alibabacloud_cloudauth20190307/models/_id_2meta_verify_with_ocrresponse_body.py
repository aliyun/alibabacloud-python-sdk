# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class Id2MetaVerifyWithOCRResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result_object: main_models.Id2MetaVerifyWithOCRResponseBodyResultObject = None,
    ):
        # Return code: 200 indicates success, any other value indicates failure.
        # **Important**
        # - This parameter indicates whether the API was called correctly. For detailed return code explanations, please refer to the error codes.
        # - Check the business verification results through the fields in ResultObject.
        self.code = code
        # API call return message.
        # **Important**
        # This parameter only indicates if there was an exception with the API call.
        self.message = message
        # Request ID.
        self.request_id = request_id
        # Result object
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
            temp_model = main_models.Id2MetaVerifyWithOCRResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class Id2MetaVerifyWithOCRResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        biz_code: str = None,
        card_info: str = None,
    ):
        # Identity verification result:
        # - 1: Consistent
        # - 2: Inconsistent
        # - 3: No record found
        self.biz_code = biz_code
        # {"address":"Zhejiang Province, Hangzhou City, Yu*****","birthDate":"19901226","certName":"Zhang San","certNo":"1234561990122*****","nationality":"Han","authority":"xxx Public Security Bureau","startDate":"20201130","endDate":"20301130"}
        self.card_info = card_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_code is not None:
            result['BizCode'] = self.biz_code

        if self.card_info is not None:
            result['CardInfo'] = self.card_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizCode') is not None:
            self.biz_code = m.get('BizCode')

        if m.get('CardInfo') is not None:
            self.card_info = m.get('CardInfo')

        return self

