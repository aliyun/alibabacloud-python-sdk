# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeFlowLogsRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        flow_log_id: str = None,
        flow_log_name: str = None,
        log_store_name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        project_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        status: str = None,
        tags: List[main_models.DescribeFlowLogsRequestTags] = None,
        traffic_type: str = None,
        vpc_id: str = None,
    ):
        # The description of the flow log.
        # 
        # The description must be 1 to 256 characters long and cannot start with `http://` or `https://`.
        self.description = description
        # The ID of the flow log.
        self.flow_log_id = flow_log_id
        # The name of the flow log.
        # 
        # The name must be 1 to 128 characters long and cannot start with `http://` or `https://`.
        self.flow_log_name = flow_log_name
        # The Logstore that stores the captured traffic.
        self.log_store_name = log_store_name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number, with a default value of **1**.
        self.page_number = page_number
        # The number of items per page in a paginated query, with a maximum value of **50** and a default value of **20**.
        self.page_size = page_size
        # The Project that manages the captured traffic.
        self.project_name = project_name
        # The region ID of the flow log.
        # 
        # You can obtain the region ID by calling the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) interface.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID of the flow log.
        self.resource_group_id = resource_group_id
        # The resource ID of the traffic to capture.
        self.resource_id = resource_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource type of the traffic to capture. Values:
        # - **NetworkInterface**: Elastic Network Interface (ENI).
        # - **VSwitch**: All ENIs within a VSwitch.
        # - **VPC**: All ENIs within a VPC.
        self.resource_type = resource_type
        # The status of the flow log. Values:
        # - **Active**: The flow log is in an active state.
        # - **Activating**: The flow log is being created.
        # - **Inactive**: The flow log is in an inactive state.
        self.status = status
        # The list of tags.
        self.tags = tags
        # The type of traffic to collect. Values:
        # - **All**: All traffic.
        # - **Allow**: Traffic allowed by access control.
        # - **Drop**: Traffic denied by access control.
        self.traffic_type = traffic_type
        # The ID of the VPC for which you want to view the flow log.
        self.vpc_id = vpc_id

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
        if self.description is not None:
            result['Description'] = self.description

        if self.flow_log_id is not None:
            result['FlowLogId'] = self.flow_log_id

        if self.flow_log_name is not None:
            result['FlowLogName'] = self.flow_log_name

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.traffic_type is not None:
            result['TrafficType'] = self.traffic_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FlowLogId') is not None:
            self.flow_log_id = m.get('FlowLogId')

        if m.get('FlowLogName') is not None:
            self.flow_log_name = m.get('FlowLogName')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeFlowLogsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TrafficType') is not None:
            self.traffic_type = m.get('TrafficType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeFlowLogsRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. Up to 20 tag keys are supported. If you need to pass this value, it cannot be an empty string.
        # 
        # A tag key can have up to 128 characters and cannot start with `aliyun` or `acs:`. It also cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag. Up to 20 tag values are supported. If you need to pass this value, it can be an empty string.
        # 
        # A tag value can have up to 128 characters and cannot start with `aliyun` or `acs:`. It also cannot contain `http://` or `https://`.
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

