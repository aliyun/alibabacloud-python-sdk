# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dyplsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CreatePickUpWaybillResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreatePickUpWaybillResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The status code description.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreatePickUpWaybillResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreatePickUpWaybillResponseBodyData(DaraModel):
    def __init__(
        self,
        cp_code: str = None,
        error_code: str = None,
        error_msg: str = None,
        got_code: str = None,
        mail_no: str = None,
        success: str = None,
    ):
        # The express delivery company code.
        self.cp_code = cp_code
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The pickup code.
        self.got_code = got_code
        # The waybill number.
        self.mail_no = mail_no
        # Indicates whether the API call is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.got_code is not None:
            result['GotCode'] = self.got_code

        if self.mail_no is not None:
            result['MailNo'] = self.mail_no

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('GotCode') is not None:
            self.got_code = m.get('GotCode')

        if m.get('MailNo') is not None:
            self.mail_no = m.get('MailNo')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

