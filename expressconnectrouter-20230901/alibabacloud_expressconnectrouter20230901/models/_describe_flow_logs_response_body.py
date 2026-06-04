# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class DescribeFlowLogsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        flow_logs: List[main_models.DescribeFlowLogsResponseBodyFlowLogs] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The queried information about the request denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The information about the flow logs.
        self.flow_logs = flow_logs
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The total number of entries returned. Valid values: 1 to 2147483647. Default value: 10.
        self.max_results = max_results
        # The returned message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - **True**
        # - **False**
        self.success = success
        # The total number of records that meet the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.flow_logs:
            for v1 in self.flow_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        result['FlowLogs'] = []
        if self.flow_logs is not None:
            for k1 in self.flow_logs:
                result['FlowLogs'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        self.flow_logs = []
        if m.get('FlowLogs') is not None:
            for k1 in m.get('FlowLogs'):
                temp_model = main_models.DescribeFlowLogsResponseBodyFlowLogs()
                self.flow_logs.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeFlowLogsResponseBodyFlowLogs(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        ecr_id: str = None,
        flow_log_id: str = None,
        flow_log_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        interval: int = None,
        log_store_name: str = None,
        project_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        sampling_rate: str = None,
        sls_region_id: str = None,
        status: str = None,
        tags: List[main_models.DescribeFlowLogsResponseBodyFlowLogsTags] = None,
    ):
        # The time when the flow log was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
        self.creation_time = creation_time
        # The description of the flow log.
        self.description = description
        # The ECR ID.
        self.ecr_id = ecr_id
        # The ID of the flow log.
        self.flow_log_id = flow_log_id
        # The name of the flow log.
        self.flow_log_name = flow_log_name
        # The ID of the network instance.
        self.instance_id = instance_id
        # The type of the network instance. Valid values:
        # 
        # - **VBR**: virtual border router (VBR)
        self.instance_type = instance_type
        # The time window for collecting log data. Unit: seconds. Valid values:
        # 
        # - **60**
        # - **600**
        # 
        # Default value: **600**.
        self.interval = interval
        # The Logstore that stores the captured traffic data.
        self.log_store_name = log_store_name
        # The name of the project that stores the captured traffic data.
        self.project_name = project_name
        # The region ID of the flow log.
        self.region_id = region_id
        # The ID of the resource group to which the ECR belongs.
        self.resource_group_id = resource_group_id
        # The sampling proportion. Valid values:
        # 
        # - **1:4096**
        # - **1:2048**
        # - **1:1024**
        # 
        # Default value: **1:4096**.
        self.sampling_rate = sampling_rate
        # The ID of the region where Log Service is deployed.
        self.sls_region_id = sls_region_id
        # The status of the flow log. Valid values:
        # 
        # *   **Active**
        # 
        # *   **Inactive**
        self.status = status
        # The tag key.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id

        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate

        if self.sls_region_id is not None:
            result['SlsRegionId'] = self.sls_region_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')

        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')

        if m.get('SlsRegionId') is not None:
            self.sls_region_id = m.get('SlsRegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeFlowLogsResponseBodyFlowLogsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeFlowLogsResponseBodyFlowLogsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N of the instance. The tag key cannot be an empty string.
        # 
        # > It can be up to 64 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value.
        # 
        # > It can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`. The tag value can be an empty string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

