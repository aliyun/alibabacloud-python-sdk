# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeAbolishApiTaskResponseBody(DaraModel):
    def __init__(
        self,
        api_abolish_results: main_models.DescribeAbolishApiTaskResponseBodyApiAbolishResults = None,
        request_id: str = None,
    ):
        # The result returned.
        self.api_abolish_results = api_abolish_results
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.api_abolish_results:
            self.api_abolish_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_abolish_results is not None:
            result['ApiAbolishResults'] = self.api_abolish_results.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiAbolishResults') is not None:
            temp_model = main_models.DescribeAbolishApiTaskResponseBodyApiAbolishResults()
            self.api_abolish_results = temp_model.from_map(m.get('ApiAbolishResults'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAbolishApiTaskResponseBodyApiAbolishResults(DaraModel):
    def __init__(
        self,
        api_abolish_result: List[main_models.DescribeAbolishApiTaskResponseBodyApiAbolishResultsApiAbolishResult] = None,
    ):
        self.api_abolish_result = api_abolish_result

    def validate(self):
        if self.api_abolish_result:
            for v1 in self.api_abolish_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiAbolishResult'] = []
        if self.api_abolish_result is not None:
            for k1 in self.api_abolish_result:
                result['ApiAbolishResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_abolish_result = []
        if m.get('ApiAbolishResult') is not None:
            for k1 in m.get('ApiAbolishResult'):
                temp_model = main_models.DescribeAbolishApiTaskResponseBodyApiAbolishResultsApiAbolishResult()
                self.api_abolish_result.append(temp_model.from_map(k1))

        return self

class DescribeAbolishApiTaskResponseBodyApiAbolishResultsApiAbolishResult(DaraModel):
    def __init__(
        self,
        abolish_status: str = None,
        api_name: str = None,
        api_uid: str = None,
        error_msg: str = None,
        group_id: str = None,
        group_name: str = None,
        stage_id: str = None,
        stage_name: str = None,
    ):
        # The unpublishing status.
        self.abolish_status = abolish_status
        # The name of the API.
        self.api_name = api_name
        # The ID of the API.
        self.api_uid = api_uid
        # The error message.
        self.error_msg = error_msg
        # The ID of the API group.
        self.group_id = group_id
        # The name of the API group.
        self.group_name = group_name
        # The ID of the runtime environment.
        self.stage_id = stage_id
        # The name of the runtime environment. Valid values:
        # 
        # *   **RELEASE**
        # *   **TEST**
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abolish_status is not None:
            result['AbolishStatus'] = self.abolish_status

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbolishStatus') is not None:
            self.abolish_status = m.get('AbolishStatus')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')

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

        return self

