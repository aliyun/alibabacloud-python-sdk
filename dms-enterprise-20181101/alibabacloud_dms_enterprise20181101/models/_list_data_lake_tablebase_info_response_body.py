# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListDataLakeTablebaseInfoResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        tablebase_info_list: List[main_models.DLTablebaseInfo] = None,
        total_count: str = None,
    ):
        # The error code returned if the request fails.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The list of tables in the data lake.
        self.tablebase_info_list = tablebase_info_list
        # The number of tables that meet the conditions.
        self.total_count = total_count

    def validate(self):
        if self.tablebase_info_list:
            for v1 in self.tablebase_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['TablebaseInfoList'] = []
        if self.tablebase_info_list is not None:
            for k1 in self.tablebase_info_list:
                result['TablebaseInfoList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.tablebase_info_list = []
        if m.get('TablebaseInfoList') is not None:
            for k1 in m.get('TablebaseInfoList'):
                temp_model = main_models.DLTablebaseInfo()
                self.tablebase_info_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

