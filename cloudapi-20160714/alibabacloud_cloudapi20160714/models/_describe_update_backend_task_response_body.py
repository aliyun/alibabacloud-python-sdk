# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeUpdateBackendTaskResponseBody(DaraModel):
    def __init__(
        self,
        api_update_backend_results: main_models.DescribeUpdateBackendTaskResponseBodyApiUpdateBackendResults = None,
        request_id: str = None,
    ):
        self.api_update_backend_results = api_update_backend_results
        self.request_id = request_id

    def validate(self):
        if self.api_update_backend_results:
            self.api_update_backend_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_update_backend_results is not None:
            result['ApiUpdateBackendResults'] = self.api_update_backend_results.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiUpdateBackendResults') is not None:
            temp_model = main_models.DescribeUpdateBackendTaskResponseBodyApiUpdateBackendResults()
            self.api_update_backend_results = temp_model.from_map(m.get('ApiUpdateBackendResults'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUpdateBackendTaskResponseBodyApiUpdateBackendResults(DaraModel):
    def __init__(
        self,
        api_update_backend_result: List[main_models.DescribeUpdateBackendTaskResponseBodyApiUpdateBackendResultsApiUpdateBackendResult] = None,
    ):
        self.api_update_backend_result = api_update_backend_result

    def validate(self):
        if self.api_update_backend_result:
            for v1 in self.api_update_backend_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiUpdateBackendResult'] = []
        if self.api_update_backend_result is not None:
            for k1 in self.api_update_backend_result:
                result['ApiUpdateBackendResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_update_backend_result = []
        if m.get('ApiUpdateBackendResult') is not None:
            for k1 in m.get('ApiUpdateBackendResult'):
                temp_model = main_models.DescribeUpdateBackendTaskResponseBodyApiUpdateBackendResultsApiUpdateBackendResult()
                self.api_update_backend_result.append(temp_model.from_map(k1))

        return self

class DescribeUpdateBackendTaskResponseBodyApiUpdateBackendResultsApiUpdateBackendResult(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        api_uid: str = None,
        backend_id: str = None,
        error_msg: str = None,
        group_id: str = None,
        group_name: str = None,
        stage_id: str = None,
        stage_name: str = None,
        update_status: str = None,
    ):
        self.api_name = api_name
        self.api_uid = api_uid
        self.backend_id = backend_id
        self.error_msg = error_msg
        self.group_id = group_id
        self.group_name = group_name
        self.stage_id = stage_id
        self.stage_name = stage_name
        self.update_status = update_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid

        if self.backend_id is not None:
            result['BackendId'] = self.backend_id

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.update_status is not None:
            result['UpdateStatus'] = self.update_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')

        if m.get('BackendId') is not None:
            self.backend_id = m.get('BackendId')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('UpdateStatus') is not None:
            self.update_status = m.get('UpdateStatus')

        return self

