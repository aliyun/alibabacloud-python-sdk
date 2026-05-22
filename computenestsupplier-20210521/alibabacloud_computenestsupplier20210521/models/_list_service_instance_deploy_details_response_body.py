# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListServiceInstanceDeployDetailsResponseBody(DaraModel):
    def __init__(
        self,
        deploy_details: List[main_models.ListServiceInstanceDeployDetailsResponseBodyDeployDetails] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the service instance deployment.
        self.deploy_details = deploy_details
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.deploy_details:
            for v1 in self.deploy_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeployDetails'] = []
        if self.deploy_details is not None:
            for k1 in self.deploy_details:
                result['DeployDetails'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deploy_details = []
        if m.get('DeployDetails') is not None:
            for k1 in m.get('DeployDetails'):
                temp_model = main_models.ListServiceInstanceDeployDetailsResponseBodyDeployDetails()
                self.deploy_details.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListServiceInstanceDeployDetailsResponseBodyDeployDetails(DaraModel):
    def __init__(
        self,
        count: str = None,
        create_time: str = None,
        cycle: str = None,
        deploy_succeeded: str = None,
        error_code: str = None,
        error_detail: str = None,
        error_type: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_name_chn: str = None,
        service_name_eng: str = None,
        service_type: str = None,
        service_version: str = None,
        timestamp: str = None,
        user_id: str = None,
    ):
        # The total number of entries that meet the specified conditions.
        self.count = count
        # The time when the service instance was created.
        self.create_time = create_time
        # The period over which data is aggregated.
        self.cycle = cycle
        # The indicates whether the deployment was successful.
        self.deploy_succeeded = deploy_succeeded
        # The error code.
        self.error_code = error_code
        # The error description.
        self.error_detail = error_detail
        # The type of error that caused the deployment to fail.
        self.error_type = error_type
        # The service ID.
        self.service_id = service_id
        # The service instance ID.
        self.service_instance_id = service_instance_id
        # The name of the service in Chinese.
        self.service_name_chn = service_name_chn
        # The name of the service in English.
        self.service_name_eng = service_name_eng
        # The type of service. 
        # 
        # Possible values:
        # 
        # - private: Deployed under the user\\"s account.
        # - managed: Hosted under the service provider\\"s account.
        # - operation: Managed operation service.
        self.service_type = service_type
        # The service version.
        self.service_version = service_version
        # The timestamp when the response is returned.
        self.timestamp = timestamp
        # The aliuid of user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cycle is not None:
            result['Cycle'] = self.cycle

        if self.deploy_succeeded is not None:
            result['DeploySucceeded'] = self.deploy_succeeded

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_detail is not None:
            result['ErrorDetail'] = self.error_detail

        if self.error_type is not None:
            result['ErrorType'] = self.error_type

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.service_name_chn is not None:
            result['ServiceNameChn'] = self.service_name_chn

        if self.service_name_eng is not None:
            result['ServiceNameEng'] = self.service_name_eng

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')

        if m.get('DeploySucceeded') is not None:
            self.deploy_succeeded = m.get('DeploySucceeded')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorDetail') is not None:
            self.error_detail = m.get('ErrorDetail')

        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('ServiceNameChn') is not None:
            self.service_name_chn = m.get('ServiceNameChn')

        if m.get('ServiceNameEng') is not None:
            self.service_name_eng = m.get('ServiceNameEng')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

