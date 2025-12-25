# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetDataExportPreCheckDetailResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        pre_check_result: main_models.GetDataExportPreCheckDetailResponseBodyPreCheckResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # Indicates the result of the precheck task.
        self.pre_check_result = pre_check_result
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.pre_check_result:
            self.pre_check_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.pre_check_result is not None:
            result['PreCheckResult'] = self.pre_check_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('PreCheckResult') is not None:
            temp_model = main_models.GetDataExportPreCheckDetailResponseBodyPreCheckResult()
            self.pre_check_result = temp_model.from_map(m.get('PreCheckResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataExportPreCheckDetailResponseBodyPreCheckResult(DaraModel):
    def __init__(
        self,
        ignore_affect_rows: bool = None,
        pre_check_detail_list: main_models.GetDataExportPreCheckDetailResponseBodyPreCheckResultPreCheckDetailList = None,
    ):
        # Specifies whether to skip verification. Valid values:
        # 
        # - true
        # - false
        self.ignore_affect_rows = ignore_affect_rows
        # The list of pre-check details.
        self.pre_check_detail_list = pre_check_detail_list

    def validate(self):
        if self.pre_check_detail_list:
            self.pre_check_detail_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignore_affect_rows is not None:
            result['IgnoreAffectRows'] = self.ignore_affect_rows

        if self.pre_check_detail_list is not None:
            result['PreCheckDetailList'] = self.pre_check_detail_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreAffectRows') is not None:
            self.ignore_affect_rows = m.get('IgnoreAffectRows')

        if m.get('PreCheckDetailList') is not None:
            temp_model = main_models.GetDataExportPreCheckDetailResponseBodyPreCheckResultPreCheckDetailList()
            self.pre_check_detail_list = temp_model.from_map(m.get('PreCheckDetailList'))

        return self

class GetDataExportPreCheckDetailResponseBodyPreCheckResultPreCheckDetailList(DaraModel):
    def __init__(
        self,
        pre_check_detail_list: List[main_models.GetDataExportPreCheckDetailResponseBodyPreCheckResultPreCheckDetailListPreCheckDetailList] = None,
    ):
        self.pre_check_detail_list = pre_check_detail_list

    def validate(self):
        if self.pre_check_detail_list:
            for v1 in self.pre_check_detail_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PreCheckDetailList'] = []
        if self.pre_check_detail_list is not None:
            for k1 in self.pre_check_detail_list:
                result['PreCheckDetailList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pre_check_detail_list = []
        if m.get('PreCheckDetailList') is not None:
            for k1 in m.get('PreCheckDetailList'):
                temp_model = main_models.GetDataExportPreCheckDetailResponseBodyPreCheckResultPreCheckDetailListPreCheckDetailList()
                self.pre_check_detail_list.append(temp_model.from_map(k1))

        return self

class GetDataExportPreCheckDetailResponseBodyPreCheckResultPreCheckDetailListPreCheckDetailList(DaraModel):
    def __init__(
        self,
        affect_rows: int = None,
        sql: str = None,
    ):
        # The estimated number of data rows to be affected.
        self.affect_rows = affect_rows
        # The SQL statement.
        self.sql = sql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows

        if self.sql is not None:
            result['SQL'] = self.sql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')

        if m.get('SQL') is not None:
            self.sql = m.get('SQL')

        return self

