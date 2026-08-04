# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class QueryDeleteTaskCheckDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_check_data_dto_list: List[main_models.QueryDeleteTaskCheckDataResponseBodyTaskCheckDataDtoList] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_check_data_dto_list = task_check_data_dto_list

    def validate(self):
        if self.task_check_data_dto_list:
            for v1 in self.task_check_data_dto_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        result['TaskCheckDataDtoList'] = []
        if self.task_check_data_dto_list is not None:
            for k1 in self.task_check_data_dto_list:
                result['TaskCheckDataDtoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        self.task_check_data_dto_list = []
        if m.get('TaskCheckDataDtoList') is not None:
            for k1 in m.get('TaskCheckDataDtoList'):
                temp_model = main_models.QueryDeleteTaskCheckDataResponseBodyTaskCheckDataDtoList()
                self.task_check_data_dto_list.append(temp_model.from_map(k1))

        return self

class QueryDeleteTaskCheckDataResponseBodyTaskCheckDataDtoList(DaraModel):
    def __init__(
        self,
        checker_desc: str = None,
        checker_name: str = None,
        checker_uni_key: str = None,
        dependency_level: str = None,
    ):
        self.checker_desc = checker_desc
        self.checker_name = checker_name
        self.checker_uni_key = checker_uni_key
        self.dependency_level = dependency_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checker_desc is not None:
            result['CheckerDesc'] = self.checker_desc

        if self.checker_name is not None:
            result['CheckerName'] = self.checker_name

        if self.checker_uni_key is not None:
            result['CheckerUniKey'] = self.checker_uni_key

        if self.dependency_level is not None:
            result['DependencyLevel'] = self.dependency_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckerDesc') is not None:
            self.checker_desc = m.get('CheckerDesc')

        if m.get('CheckerName') is not None:
            self.checker_name = m.get('CheckerName')

        if m.get('CheckerUniKey') is not None:
            self.checker_uni_key = m.get('CheckerUniKey')

        if m.get('DependencyLevel') is not None:
            self.dependency_level = m.get('DependencyLevel')

        return self

