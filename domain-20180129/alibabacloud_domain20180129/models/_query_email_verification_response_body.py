# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryEmailVerificationResponseBody(DaraModel):
    def __init__(
        self,
        confirm_ip: str = None,
        email: str = None,
        email_verification_no: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        request_id: str = None,
        send_ip: str = None,
        token_send_time: str = None,
        user_id: str = None,
        verification_status: int = None,
        verification_time: str = None,
    ):
        self.confirm_ip = confirm_ip
        self.email = email
        self.email_verification_no = email_verification_no
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.request_id = request_id
        self.send_ip = send_ip
        self.token_send_time = token_send_time
        self.user_id = user_id
        self.verification_status = verification_status
        self.verification_time = verification_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confirm_ip is not None:
            result['ConfirmIp'] = self.confirm_ip

        if self.email is not None:
            result['Email'] = self.email

        if self.email_verification_no is not None:
            result['EmailVerificationNo'] = self.email_verification_no

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.send_ip is not None:
            result['SendIp'] = self.send_ip

        if self.token_send_time is not None:
            result['TokenSendTime'] = self.token_send_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status

        if self.verification_time is not None:
            result['VerificationTime'] = self.verification_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfirmIp') is not None:
            self.confirm_ip = m.get('ConfirmIp')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EmailVerificationNo') is not None:
            self.email_verification_no = m.get('EmailVerificationNo')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SendIp') is not None:
            self.send_ip = m.get('SendIp')

        if m.get('TokenSendTime') is not None:
            self.token_send_time = m.get('TokenSendTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')

        if m.get('VerificationTime') is not None:
            self.verification_time = m.get('VerificationTime')

        return self

