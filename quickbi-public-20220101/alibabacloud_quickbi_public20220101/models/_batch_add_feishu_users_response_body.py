# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class BatchAddFeishuUsersResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.BatchAddFeishuUsersResponseBodyResult = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Result of adding members to the user group. Possible values:
        # 
        # - true: Addition successful
        # - false: Addition failed
        self.result = result
        # Whether the request was successful. Possible values:
        # 
        # - true: Request successful
        # - false: Request failed
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.BatchAddFeishuUsersResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class BatchAddFeishuUsersResponseBodyResult(DaraModel):
    def __init__(
        self,
        fail_count: int = None,
        fail_results: List[main_models.BatchAddFeishuUsersResponseBodyResultFailResults] = None,
        ok_count: int = None,
    ):
        # Number of failed validations.
        self.fail_count = fail_count
        # Details of the failures.
        self.fail_results = fail_results
        # Count of successes.
        self.ok_count = ok_count

    def validate(self):
        if self.fail_results:
            for v1 in self.fail_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        result['FailResults'] = []
        if self.fail_results is not None:
            for k1 in self.fail_results:
                result['FailResults'].append(k1.to_map() if k1 else None)

        if self.ok_count is not None:
            result['OkCount'] = self.ok_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        self.fail_results = []
        if m.get('FailResults') is not None:
            for k1 in m.get('FailResults'):
                temp_model = main_models.BatchAddFeishuUsersResponseBodyResultFailResults()
                self.fail_results.append(temp_model.from_map(k1))

        if m.get('OkCount') is not None:
            self.ok_count = m.get('OkCount')

        return self

class BatchAddFeishuUsersResponseBodyResultFailResults(DaraModel):
    def __init__(
        self,
        fail_infos: List[main_models.BatchAddFeishuUsersResponseBodyResultFailResultsFailInfos] = None,
    ):
        # Reasons for errors.
        self.fail_infos = fail_infos

    def validate(self):
        if self.fail_infos:
            for v1 in self.fail_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailInfos'] = []
        if self.fail_infos is not None:
            for k1 in self.fail_infos:
                result['FailInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fail_infos = []
        if m.get('FailInfos') is not None:
            for k1 in m.get('FailInfos'):
                temp_model = main_models.BatchAddFeishuUsersResponseBodyResultFailResultsFailInfos()
                self.fail_infos.append(temp_model.from_map(k1))

        return self

class BatchAddFeishuUsersResponseBodyResultFailResultsFailInfos(DaraModel):
    def __init__(
        self,
        code: str = None,
        code_desc: str = None,
        input: str = None,
    ):
        # Error code.
        self.code = code
        # Description of the error code.
        self.code_desc = code_desc
        # Incorrect input value.
        self.input = input

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.code_desc is not None:
            result['CodeDesc'] = self.code_desc

        if self.input is not None:
            result['Input'] = self.input

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CodeDesc') is not None:
            self.code_desc = m.get('CodeDesc')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        return self

