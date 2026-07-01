# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySmsSignResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        create_date: str = None,
        message: str = None,
        reason: str = None,
        request_id: str = None,
        sign_name: str = None,
        sign_status: int = None,
    ):
        # The status code of the request.
        # 
        # - `OK` indicates that the request was successful.
        # 
        # - For other error codes, see [Error codes](https://help.aliyun.com/document_detail/101346.html).
        self.code = code
        # The date and time when the SMS signature was created.
        self.create_date = create_date
        # The description of the status code.
        self.message = message
        # The review reason.
        # 
        # - If the review status is **Approved** or **Pending Review**, this parameter is empty.
        # 
        # - If the review status is **Rejected**, this parameter provides the reason for the rejection.
        self.reason = reason
        # The request ID.
        self.request_id = request_id
        # The SMS signature.
        self.sign_name = sign_name
        # The review status of the SMS signature. Valid values:
        # 
        # - **0**: Pending Review.
        # 
        # - **1**: Approved.
        # 
        # - **2**: Rejected. For details, see the `Reason` parameter.
        # 
        # - **10**: Canceled.
        self.sign_status = sign_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.message is not None:
            result['Message'] = self.message

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.sign_status is not None:
            result['SignStatus'] = self.sign_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('SignStatus') is not None:
            self.sign_status = m.get('SignStatus')

        return self

