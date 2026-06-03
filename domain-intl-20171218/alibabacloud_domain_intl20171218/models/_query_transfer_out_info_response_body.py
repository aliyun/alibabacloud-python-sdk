# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTransferOutInfoResponseBody(DaraModel):
    def __init__(
        self,
        email: str = None,
        expiration_date: str = None,
        pending_request_date: str = None,
        request_id: str = None,
        result_code: str = None,
        result_msg: str = None,
        status: int = None,
        transfer_authorization_code_send_date: str = None,
    ):
        self.email = email
        self.expiration_date = expiration_date
        self.pending_request_date = pending_request_date
        self.request_id = request_id
        self.result_code = result_code
        self.result_msg = result_msg
        self.status = status
        self.transfer_authorization_code_send_date = transfer_authorization_code_send_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.expiration_date is not None:
            result['ExpirationDate'] = self.expiration_date

        if self.pending_request_date is not None:
            result['PendingRequestDate'] = self.pending_request_date

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.status is not None:
            result['Status'] = self.status

        if self.transfer_authorization_code_send_date is not None:
            result['TransferAuthorizationCodeSendDate'] = self.transfer_authorization_code_send_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('ExpirationDate') is not None:
            self.expiration_date = m.get('ExpirationDate')

        if m.get('PendingRequestDate') is not None:
            self.pending_request_date = m.get('PendingRequestDate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TransferAuthorizationCodeSendDate') is not None:
            self.transfer_authorization_code_send_date = m.get('TransferAuthorizationCodeSendDate')

        return self

