# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QueryPhoneNoAByTrackNoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: List[main_models.QueryPhoneNoAByTrackNoResponseBodyModule] = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   Other status codes indicate that the request failed. For more information, see [Error codes](https://help.aliyun.com/document_detail/109196.html).
        self.code = code
        # The returned message.
        self.message = message
        # The information returned after the phone numbers were bound.
        self.module = module
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.module:
            for v1 in self.module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        result['Module'] = []
        if self.module is not None:
            for k1 in self.module:
                result['Module'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.module = []
        if m.get('Module') is not None:
            for k1 in m.get('Module'):
                temp_model = main_models.QueryPhoneNoAByTrackNoResponseBodyModule()
                self.module.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryPhoneNoAByTrackNoResponseBodyModule(DaraModel):
    def __init__(
        self,
        extension: str = None,
        phone_no_a: str = None,
        phone_no_x: str = None,
    ):
        # The extension of phone number X.
        self.extension = extension
        # Phone number A.
        self.phone_no_a = phone_no_a
        # The private number, that is, phone number X.
        self.phone_no_x = phone_no_x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extension is not None:
            result['Extension'] = self.extension

        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a

        if self.phone_no_x is not None:
            result['PhoneNoX'] = self.phone_no_x

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')

        if m.get('PhoneNoX') is not None:
            self.phone_no_x = m.get('PhoneNoX')

        return self

