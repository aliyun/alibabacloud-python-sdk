# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeFlowLogsResponseBody(DaraModel):
    def __init__(
        self,
        flow_logs: main_models.DescribeFlowLogsResponseBodyFlowLogs = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        success: str = None,
        total_count: str = None,
    ):
        # List of flow logs.
        self.flow_logs = flow_logs
        # The page number.
        self.page_number = page_number
        # The number of items per page in a paginated query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Values:
        # - **true**: The call was successful.
        # - **false**: The call failed.
        self.success = success
        # The number of entries in the queried flow log list.
        self.total_count = total_count

    def validate(self):
        if self.flow_logs:
            self.flow_logs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_logs is not None:
            result['FlowLogs'] = self.flow_logs.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowLogs') is not None:
            temp_model = main_models.DescribeFlowLogsResponseBodyFlowLogs()
            self.flow_logs = temp_model.from_map(m.get('FlowLogs'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

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
        flow_log: List[main_models.DescribeFlowLogsResponseBodyFlowLogsFlowLog] = None,
    ):
        self.flow_log = flow_log

    def validate(self):
        if self.flow_log:
            for v1 in self.flow_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FlowLog'] = []
        if self.flow_log is not None:
            for k1 in self.flow_log:
                result['FlowLog'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_log = []
        if m.get('FlowLog') is not None:
            for k1 in m.get('FlowLog'):
                temp_model = main_models.DescribeFlowLogsResponseBodyFlowLogsFlowLog()
                self.flow_log.append(temp_model.from_map(k1))

        return self

class DescribeFlowLogsResponseBodyFlowLogsFlowLog(DaraModel):
    def __init__(
        self,
        aggregation_interval: int = None,
        business_status: str = None,
        creation_time: str = None,
        description: str = None,
        flow_log_deliver_error_message: str = None,
        flow_log_deliver_status: str = None,
        flow_log_id: str = None,
        flow_log_name: str = None,
        ip_version: str = None,
        log_store_name: str = None,
        project_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        service_type: str = None,
        status: str = None,
        tags: main_models.DescribeFlowLogsResponseBodyFlowLogsFlowLogTags = None,
        traffic_path: main_models.DescribeFlowLogsResponseBodyFlowLogsFlowLogTrafficPath = None,
        traffic_type: str = None,
    ):
        # The sampling interval of the flow log. Unit: minutes.
        self.aggregation_interval = aggregation_interval
        # The business status. Values:
        # 
        # - **Normal**: Normal status.
        # - **FinancialLocked**: Locked due to unpaid bills.
        self.business_status = business_status
        # The creation time of the flow log.
        self.creation_time = creation_time
        # The description of the flow log.
        self.description = description
        # When log delivery fails, you can troubleshoot based on the error messages. Possible error messages include:
        # - **UnavaliableTarget**: The Logstore of the Log Service SLS is unavailable and cannot receive logs. It is recommended to check if the corresponding Logstore actually exists and is accessible. 
        # - **ProjectNotExist**: The Project of the Log Service SLS does not exist. It is suggested to delete the original flow log and create a new one pointing to an existing Project. 
        # - **UnknownError**: An internal error has occurred. Please try again later.
        self.flow_log_deliver_error_message = flow_log_deliver_error_message
        # The delivery status of the flow log, with values:
        # - **SUCCESS**: Delivery succeeded. 
        # - **FAILED**: Delivery failed.
        self.flow_log_deliver_status = flow_log_deliver_status
        # The ID of the flow log.
        self.flow_log_id = flow_log_id
        # The name of the flow log.
        self.flow_log_name = flow_log_name
        # The type of IP address for collecting flow log traffic.
        self.ip_version = ip_version
        # The Logstore where the captured traffic is stored.
        self.log_store_name = log_store_name
        # The Project that manages the captured traffic.
        self.project_name = project_name
        # The region ID to which the flow log belongs.
        self.region_id = region_id
        # The ID of the resource group to which the flow log belongs.
        self.resource_group_id = resource_group_id
        # The resource ID of the traffic captured by the flow log.
        self.resource_id = resource_id
        # The resource type of the traffic captured by the flow log:
        # 
        # - **NetworkInterface**: Elastic network interface.
        # - **VSwitch**: All elastic network interfaces within a VSwitch.
        # - **VPC**: All elastic network interfaces within a VPC.
        self.resource_type = resource_type
        # The hosting type of the cloud service.
        # - It can be empty, indicating that the flow log was created by the user. 
        # - When not empty, the only supported value is: **sls**, indicating that the flow log was created through the Log Service console.
        # > Flow log instances created through the Log Service console can be displayed in the VPC list, but they cannot be modified, started, stopped, or deleted within the VPC. If you need to perform these operations on the flow log, you can log in to the [Log Service console](https://sls.console.aliyun.com) to modify, start, stop, or delete it.
        self.service_type = service_type
        # The status of the flow log. Values:
        # - **Active**: The flow log is in an active state.
        # 
        # - **Activating**: The flow log is being created.
        # 
        # - **Inactive**: The flow log is in an inactive state.
        self.status = status
        # List of tags
        self.tags = tags
        # The path of the captured traffic. Values:
        # 
        # - **all**: Indicates full collection.
        # - **internetGateway**: Indicates public network traffic collection.
        self.traffic_path = traffic_path
        # The type of traffic captured by the flow log. Values:
        # 
        # - **All**: All traffic.
        # - **Allow**: Traffic allowed by access control.
        # - **Drop**: Traffic denied by access control.
        self.traffic_type = traffic_type

    def validate(self):
        if self.tags:
            self.tags.validate()
        if self.traffic_path:
            self.traffic_path.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregation_interval is not None:
            result['AggregationInterval'] = self.aggregation_interval

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.flow_log_deliver_error_message is not None:
            result['FlowLogDeliverErrorMessage'] = self.flow_log_deliver_error_message

        if self.flow_log_deliver_status is not None:
            result['FlowLogDeliverStatus'] = self.flow_log_deliver_status

        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id

        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.traffic_path is not None:
            result['TrafficPath'] = self.traffic_path.to_map()

        if self.traffic_type is not None:
            result['TrafficType'] = self.traffic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregationInterval') is not None:
            self.aggregation_interval = m.get('AggregationInterval')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FlowLogDeliverErrorMessage') is not None:
            self.flow_log_deliver_error_message = m.get('FlowLogDeliverErrorMessage')

        if m.get('FlowLogDeliverStatus') is not None:
            self.flow_log_deliver_status = m.get('FlowLogDeliverStatus')

        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')

        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeFlowLogsResponseBodyFlowLogsFlowLogTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TrafficPath') is not None:
            temp_model = main_models.DescribeFlowLogsResponseBodyFlowLogsFlowLogTrafficPath()
            self.traffic_path = temp_model.from_map(m.get('TrafficPath'))

        if m.get('TrafficType') is not None:
            self.traffic_type = m.get('TrafficType')

        return self

class DescribeFlowLogsResponseBodyFlowLogsFlowLogTrafficPath(DaraModel):
    def __init__(
        self,
        traffic_path_list: List[str] = None,
    ):
        self.traffic_path_list = traffic_path_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.traffic_path_list is not None:
            result['TrafficPathList'] = self.traffic_path_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrafficPathList') is not None:
            self.traffic_path_list = m.get('TrafficPathList')

        return self

class DescribeFlowLogsResponseBodyFlowLogsFlowLogTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeFlowLogsResponseBodyFlowLogsFlowLogTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeFlowLogsResponseBodyFlowLogsFlowLogTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeFlowLogsResponseBodyFlowLogsFlowLogTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key.
        self.key = key
        # Tag value.
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

