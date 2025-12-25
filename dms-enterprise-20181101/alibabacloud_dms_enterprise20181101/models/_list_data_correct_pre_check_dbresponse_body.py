# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListDataCorrectPreCheckDBResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        pre_check_dblist: List[main_models.ListDataCorrectPreCheckDBResponseBodyPreCheckDBList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The information about the databases that are involved in the precheck.
        self.pre_check_dblist = pre_check_dblist
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.pre_check_dblist:
            for v1 in self.pre_check_dblist:
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

        result['PreCheckDBList'] = []
        if self.pre_check_dblist is not None:
            for k1 in self.pre_check_dblist:
                result['PreCheckDBList'].append(k1.to_map() if k1 else None)

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

        self.pre_check_dblist = []
        if m.get('PreCheckDBList') is not None:
            for k1 in m.get('PreCheckDBList'):
                temp_model = main_models.ListDataCorrectPreCheckDBResponseBodyPreCheckDBList()
                self.pre_check_dblist.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataCorrectPreCheckDBResponseBodyPreCheckDBList(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        search_name: str = None,
        sql_num: int = None,
    ):
        # The ID of the database.
        self.db_id = db_id
        # The name of the database.
        self.search_name = search_name
        # The number of SQL statements.
        self.sql_num = sql_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        if self.sql_num is not None:
            result['SqlNum'] = self.sql_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('SqlNum') is not None:
            self.sql_num = m.get('SqlNum')

        return self

