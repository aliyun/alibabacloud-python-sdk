# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeImportOASTaskResponseBody(DaraModel):
    def __init__(
        self,
        api_results: main_models.DescribeImportOASTaskResponseBodyApiResults = None,
        model_results: main_models.DescribeImportOASTaskResponseBodyModelResults = None,
        request_id: str = None,
        task_status: str = None,
    ):
        # The execution status of the subtask. Valid values:
        # 
        # *   RUNNING
        # *   WAIT
        # *   OVER
        # *   FAIL
        # *   CANCEL
        self.api_results = api_results
        # The execution status of the subtask. Valid values:
        # 
        # *   RUNNING
        # *   WAIT
        # *   OVER
        # *   FAIL
        # *   CANCEL
        self.model_results = model_results
        # The request ID.
        self.request_id = request_id
        # The status of the import task. Valid values:
        # 
        # *   Running
        # *   Finished
        self.task_status = task_status

    def validate(self):
        if self.api_results:
            self.api_results.validate()
        if self.model_results:
            self.model_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_results is not None:
            result['ApiResults'] = self.api_results.to_map()

        if self.model_results is not None:
            result['ModelResults'] = self.model_results.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiResults') is not None:
            temp_model = main_models.DescribeImportOASTaskResponseBodyApiResults()
            self.api_results = temp_model.from_map(m.get('ApiResults'))

        if m.get('ModelResults') is not None:
            temp_model = main_models.DescribeImportOASTaskResponseBodyModelResults()
            self.model_results = temp_model.from_map(m.get('ModelResults'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

class DescribeImportOASTaskResponseBodyModelResults(DaraModel):
    def __init__(
        self,
        model_result: List[main_models.DescribeImportOASTaskResponseBodyModelResultsModelResult] = None,
    ):
        self.model_result = model_result

    def validate(self):
        if self.model_result:
            for v1 in self.model_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModelResult'] = []
        if self.model_result is not None:
            for k1 in self.model_result:
                result['ModelResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.model_result = []
        if m.get('ModelResult') is not None:
            for k1 in m.get('ModelResult'):
                temp_model = main_models.DescribeImportOASTaskResponseBodyModelResultsModelResult()
                self.model_result.append(temp_model.from_map(k1))

        return self

class DescribeImportOASTaskResponseBodyModelResultsModelResult(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        group_id: str = None,
        model_id: str = None,
        model_name: str = None,
        update_status: str = None,
    ):
        # The cause of the failure if the model fails to be imported.
        self.error_message = error_message
        # The API group ID.
        self.group_id = group_id
        # The ID of the imported model.
        self.model_id = model_id
        # The model name.
        self.model_name = model_name
        # The execution status of the subtask. Valid values:
        # 
        # *   RUNNING
        # *   WAIT
        # *   OVER
        # *   FAIL
        # *   CANCEL
        self.update_status = update_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.update_status is not None:
            result['UpdateStatus'] = self.update_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('UpdateStatus') is not None:
            self.update_status = m.get('UpdateStatus')

        return self

class DescribeImportOASTaskResponseBodyApiResults(DaraModel):
    def __init__(
        self,
        api_result: List[main_models.DescribeImportOASTaskResponseBodyApiResultsApiResult] = None,
    ):
        self.api_result = api_result

    def validate(self):
        if self.api_result:
            for v1 in self.api_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiResult'] = []
        if self.api_result is not None:
            for k1 in self.api_result:
                result['ApiResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_result = []
        if m.get('ApiResult') is not None:
            for k1 in m.get('ApiResult'):
                temp_model = main_models.DescribeImportOASTaskResponseBodyApiResultsApiResult()
                self.api_result.append(temp_model.from_map(k1))

        return self

class DescribeImportOASTaskResponseBodyApiResultsApiResult(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        description: str = None,
        error_message: str = None,
        group_id: str = None,
        method: str = None,
        path: str = None,
        update_status: str = None,
    ):
        # The API ID.
        self.api_id = api_id
        # The API name.
        self.api_name = api_name
        # The API description.
        self.description = description
        # The cause of the failure if the API fails to be imported.
        self.error_message = error_message
        # The API group ID.
        self.group_id = group_id
        # The HTTP request HTTP method of the API.
        self.method = method
        # The request path of the API.
        self.path = path
        # The execution status of the subtask. Valid values:
        # 
        # *   RUNNING
        # *   WAIT
        # *   OVER
        # *   FAIL
        # *   CANCEL
        self.update_status = update_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.description is not None:
            result['Description'] = self.description

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.method is not None:
            result['Method'] = self.method

        if self.path is not None:
            result['Path'] = self.path

        if self.update_status is not None:
            result['UpdateStatus'] = self.update_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('UpdateStatus') is not None:
            self.update_status = m.get('UpdateStatus')

        return self

