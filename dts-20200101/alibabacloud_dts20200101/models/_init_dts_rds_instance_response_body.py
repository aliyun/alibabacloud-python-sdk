# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitDtsRdsInstanceResponseBody(DaraModel):
    def __init__(
        self,
        admin_account: str = None,
        admin_password: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The built-in account that is used by DTS to connect to the node.
        self.admin_account = admin_account
        # The password of the built-in account.
        self.admin_password = admin_password
        # The error code returned if the request fails.
        self.err_code = err_code
        # The error message returned if the request fails.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_account is not None:
            result['AdminAccount'] = self.admin_account

        if self.admin_password is not None:
            result['AdminPassword'] = self.admin_password

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminAccount') is not None:
            self.admin_account = m.get('AdminAccount')

        if m.get('AdminPassword') is not None:
            self.admin_password = m.get('AdminPassword')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

