# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_clickhouse20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeDBInstanceConfigChangeLogResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDBInstanceConfigChangeLogResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeDBInstanceConfigChangeLogResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBInstanceConfigChangeLogResponseBodyData(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        param_change_logs: List[main_models.DescribeDBInstanceConfigChangeLogResponseBodyDataParamChangeLogs] = None,
    ):
        self.dbinstance_id = dbinstance_id
        self.param_change_logs = param_change_logs

    def validate(self):
        if self.param_change_logs:
            for v1 in self.param_change_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        result['ParamChangeLogs'] = []
        if self.param_change_logs is not None:
            for k1 in self.param_change_logs:
                result['ParamChangeLogs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        self.param_change_logs = []
        if m.get('ParamChangeLogs') is not None:
            for k1 in m.get('ParamChangeLogs'):
                temp_model = main_models.DescribeDBInstanceConfigChangeLogResponseBodyDataParamChangeLogs()
                self.param_change_logs.append(temp_model.from_map(k1))

        return self

class DescribeDBInstanceConfigChangeLogResponseBodyDataParamChangeLogs(DaraModel):
    def __init__(
        self,
        applied: bool = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        new_value: str = None,
        old_value: str = None,
    ):
        self.applied = applied
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        self.new_value = new_value
        self.old_value = old_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applied is not None:
            result['Applied'] = self.applied

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['ID'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.new_value is not None:
            result['NewValue'] = self.new_value

        if self.old_value is not None:
            result['OldValue'] = self.old_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Applied') is not None:
            self.applied = m.get('Applied')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ID') is not None:
            self.id = m.get('ID')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')

        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')

        return self

