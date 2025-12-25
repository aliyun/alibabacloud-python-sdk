# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetOpLogResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        op_log_details: main_models.GetOpLogResponseBodyOpLogDetails = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The details of the operation log.
        self.op_log_details = op_log_details
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The total number of operation logs that are returned.
        self.total_count = total_count

    def validate(self):
        if self.op_log_details:
            self.op_log_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.op_log_details is not None:
            result['OpLogDetails'] = self.op_log_details.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('OpLogDetails') is not None:
            temp_model = main_models.GetOpLogResponseBodyOpLogDetails()
            self.op_log_details = temp_model.from_map(m.get('OpLogDetails'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetOpLogResponseBodyOpLogDetails(DaraModel):
    def __init__(
        self,
        op_log_detail: List[main_models.GetOpLogResponseBodyOpLogDetailsOpLogDetail] = None,
    ):
        self.op_log_detail = op_log_detail

    def validate(self):
        if self.op_log_detail:
            for v1 in self.op_log_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OpLogDetail'] = []
        if self.op_log_detail is not None:
            for k1 in self.op_log_detail:
                result['OpLogDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.op_log_detail = []
        if m.get('OpLogDetail') is not None:
            for k1 in m.get('OpLogDetail'):
                temp_model = main_models.GetOpLogResponseBodyOpLogDetailsOpLogDetail()
                self.op_log_detail.append(temp_model.from_map(k1))

        return self

class GetOpLogResponseBodyOpLogDetailsOpLogDetail(DaraModel):
    def __init__(
        self,
        database: str = None,
        module: str = None,
        op_content: str = None,
        op_time: str = None,
        op_user_id: int = None,
        order_id: int = None,
        user_id: str = None,
        user_nick: str = None,
    ):
        # The endpoint of the database instance.
        # 
        # > 
        # 
        # *   This parameter is valid only for database instances of the LocalInstance type.
        # 
        # *   This parameter is valid only for operations on the functional modules related to tasks.
        self.database = database
        # The functional module for which the operation log is queried.
        self.module = module
        # The details of the operation.
        self.op_content = op_content
        # The time when the operation was performed.
        self.op_time = op_time
        # The ID of the user who performed the operation.
        self.op_user_id = op_user_id
        # The ID of the ticket or task.
        # 
        # >  This parameter is valid only for operations on the functional modules related to tasks and the task management module in system management.
        self.order_id = order_id
        # The ID of the Alibaba Cloud account.
        self.user_id = user_id
        # The display name of the user.
        self.user_nick = user_nick

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database is not None:
            result['Database'] = self.database

        if self.module is not None:
            result['Module'] = self.module

        if self.op_content is not None:
            result['OpContent'] = self.op_content

        if self.op_time is not None:
            result['OpTime'] = self.op_time

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_nick is not None:
            result['UserNick'] = self.user_nick

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('OpContent') is not None:
            self.op_content = m.get('OpContent')

        if m.get('OpTime') is not None:
            self.op_time = m.get('OpTime')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')

        return self

