# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_wyota20210420 import models as main_models
from darabonba.model import DaraModel

class GetTerminalCountResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTerminalCountResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. 200 is returned if the call is successful. An error code is returned if the call fails.
        self.code = code
        # The terminal count statistics information.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message. This parameter is empty if the call is successful.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetTerminalCountResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTerminalCountResponseBodyData(DaraModel):
    def __init__(
        self,
        bind_user_count: int = None,
        in_manage_count: int = None,
        not_in_manage_count: int = None,
        total_count: int = None,
    ):
        # The number of hardware terminals that are bound to users. This parameter is returned only when ClientType is set to 1.
        self.bind_user_count = bind_user_count
        # The number of managed terminals.
        self.in_manage_count = in_manage_count
        # The number of unmanaged terminals.
        self.not_in_manage_count = not_in_manage_count
        # The total number of terminals.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bind_user_count is not None:
            result['BindUserCount'] = self.bind_user_count

        if self.in_manage_count is not None:
            result['InManageCount'] = self.in_manage_count

        if self.not_in_manage_count is not None:
            result['NotInManageCount'] = self.not_in_manage_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindUserCount') is not None:
            self.bind_user_count = m.get('BindUserCount')

        if m.get('InManageCount') is not None:
            self.in_manage_count = m.get('InManageCount')

        if m.get('NotInManageCount') is not None:
            self.not_in_manage_count = m.get('NotInManageCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

