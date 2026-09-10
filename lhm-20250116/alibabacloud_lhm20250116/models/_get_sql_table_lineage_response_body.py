# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class GetSqlTableLineageResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetSqlTableLineageResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data body returned by the operation. For the field structure, see the child parameters.
        self.data = data
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # The request ID, which is used to locate and troubleshoot issues with the current call.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - true: Successful.
        # - false: Failed. Use errCode and errMessage to troubleshoot the issue.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetSqlTableLineageResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetSqlTableLineageResponseBodyData(DaraModel):
    def __init__(
        self,
        downstream_tables: List[str] = None,
        error_msg: str = None,
        success: bool = None,
        upstream_tables: List[str] = None,
    ):
        # The list of downstream tables.
        self.downstream_tables = downstream_tables
        # The error message.
        self.error_msg = error_msg
        # Indicates whether the call was successful. Valid values:
        # - true: Successful.
        # - false: Failed. Use errCode and errMessage to troubleshoot the issue.
        self.success = success
        # The list of upstream tables.
        self.upstream_tables = upstream_tables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.downstream_tables is not None:
            result['downstreamTables'] = self.downstream_tables

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.success is not None:
            result['success'] = self.success

        if self.upstream_tables is not None:
            result['upstreamTables'] = self.upstream_tables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('downstreamTables') is not None:
            self.downstream_tables = m.get('downstreamTables')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('upstreamTables') is not None:
            self.upstream_tables = m.get('upstreamTables')

        return self

