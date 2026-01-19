# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeDeployApiTaskResponseBody(DaraModel):
    def __init__(
        self,
        deployed_results: main_models.DescribeDeployApiTaskResponseBodyDeployedResults = None,
        request_id: str = None,
    ):
        # The returned result.
        self.deployed_results = deployed_results
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.deployed_results:
            self.deployed_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployed_results is not None:
            result['DeployedResults'] = self.deployed_results.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployedResults') is not None:
            temp_model = main_models.DescribeDeployApiTaskResponseBodyDeployedResults()
            self.deployed_results = temp_model.from_map(m.get('DeployedResults'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDeployApiTaskResponseBodyDeployedResults(DaraModel):
    def __init__(
        self,
        deployed_result: List[main_models.DescribeDeployApiTaskResponseBodyDeployedResultsDeployedResult] = None,
    ):
        self.deployed_result = deployed_result

    def validate(self):
        if self.deployed_result:
            for v1 in self.deployed_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeployedResult'] = []
        if self.deployed_result is not None:
            for k1 in self.deployed_result:
                result['DeployedResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployed_result = []
        if m.get('DeployedResult') is not None:
            for k1 in m.get('DeployedResult'):
                temp_model = main_models.DescribeDeployApiTaskResponseBodyDeployedResultsDeployedResult()
                self.deployed_result.append(temp_model.from_map(k1))

        return self

class DescribeDeployApiTaskResponseBodyDeployedResultsDeployedResult(DaraModel):
    def __init__(
        self,
        api_uid: str = None,
        deployed_status: str = None,
        error_msg: str = None,
        group_id: str = None,
        stage_name: str = None,
    ):
        # The ID of the API.
        self.api_uid = api_uid
        # The deployment status of the API.
        self.deployed_status = deployed_status
        # The error message.
        self.error_msg = error_msg
        # The ID of the API group.
        self.group_id = group_id
        # The runtime environment of the API. Valid values:
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
        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid

        if self.deployed_status is not None:
            result['DeployedStatus'] = self.deployed_status

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')

        if m.get('DeployedStatus') is not None:
            self.deployed_status = m.get('DeployedStatus')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        return self

