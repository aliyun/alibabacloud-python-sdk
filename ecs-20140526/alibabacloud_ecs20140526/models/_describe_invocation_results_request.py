# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInvocationResultsRequest(DaraModel):
    def __init__(
        self,
        command_id: str = None,
        content_encoding: str = None,
        include_history: bool = None,
        instance_id: str = None,
        invoke_id: str = None,
        invoke_record_status: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tag: List[main_models.DescribeInvocationResultsRequestTag] = None,
    ):
        # $.parameters[11].schema.example
        self.command_id = command_id
        # <DescribeInvocationResultsResponse>
        #     <RequestId>473469C7-AA6F-4DC5-B3DB-A3DC0DE*****</RequestId>
        #     <Invocation>
        #         <InvocationResults>
        #             <InvocationResult>
        #                 <Dropped>0</Dropped>
        #                 <InvocationStatus>Success</InvocationStatus>
        #                 <InstanceId>i-bp1i7gg30r52z2em****</InstanceId>
        #                 <ExitCode>0</ExitCode>
        #                 <ErrorInfo>the specified instance does not exists</ErrorInfo>
        #                 <StartTime>2019-12-20T06:15:55Z</StartTime>
        #                 <Repeats>0</Repeats>
        #                 <InvokeRecordStatus>Running</InvokeRecordStatus>
        #                 <FinishedTime>2019-12-20T06:15:56Z</FinishedTime>
        #                 <Output>MTU6MzA6MDEK</Output>
        #                 <CommandId>c-hz0jdfwcsr****</CommandId>
        #                 <ErrorCode>InstanceNotExists</ErrorCode>
        #                 <InvokeId>t-hz0jdfwd9f****</InvokeId>
        #                 <StopTime>2020-01-19T09:15:47Z</StopTime>
        #                 <ContainerId>ab141ddfbacfe02d9dbc25966ed971536124527097398d419a6746873fea****</ContainerId>
        #                 <ContainerName>test-container</ContainerName>
        #                 <Tags>
        #                     <TagKey>owner</TagKey>
        #                     <TagValue>zhangsan</TagValue>
        #                 </Tags>
        #             </InvocationResult>
        #         </InvocationResults>
        #         <TotalCount>1</TotalCount>
        #         <PageSize>1</PageSize>
        #         <PageNumber>1</PageNumber>
        #     </Invocation>
        # </DescribeInvocationResultsResponse>
        self.content_encoding = content_encoding
        # {
        #   "RequestId" : "473469C7-AA6F-4DC5-B3DB-A3DC0DE*****",
        #   "Invocation" : {
        #     "InvocationResults" : {
        #       "InvocationResult" : [ {
        #         "Dropped" : 0,
        #         "InvocationStatus" : "Success",
        #         "InstanceId" : "i-bp1i7gg30r52z2em****",
        #         "ExitCode" : 0,
        #         "ErrorInfo" : "the specified instance does not exists",
        #         "StartTime" : "2019-12-20T06:15:55Z",
        #         "Repeats" : 0,
        #         "InvokeRecordStatus" : "Running",
        #         "FinishedTime" : "2019-12-20T06:15:56Z",
        #         "Output" : "MTU6MzA6MDEK",
        #         "CommandId" : "c-hz0jdfwcsr****",
        #         "ErrorCode" : "InstanceNotExists",
        #         "InvokeId" : "t-hz0jdfwd9f****",
        #         "StopTime" : "2020-01-19T09:15:47Z",
        #         "ContainerId":"ab141ddfbacfe02d9dbc25966ed971536124527097398d419a6746873fea****",
        #         "ContainerName":"test-container",      
        #         "Tags": [
        #                     {
        #                         "TagKey": "owner",
        #                         "TagValue": "zhangsan"
        #                     }
        #                 ]
        #       } ]
        #     },
        #     "TotalCount" : 1,
        #     "PageSize" : 1,
        #     "PageNumber" : 1
        #   }
        # }
        self.include_history = include_history
        # $.parameters[11].schema.description
        self.instance_id = instance_id
        # $.parameters[11].schema.items.enumValueTitles
        self.invoke_id = invoke_id
        # $.parameters[11].schema.enumValueTitles
        self.invoke_record_status = invoke_record_status
        # FEATUREecsXZ3H4M
        self.max_results = max_results
        # dubbo
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # acs:ecs:{#regionId}:{#accountId}:command/*
        self.page_number = page_number
        # acs:ecs:{#regionId}:{#accountId}:instance/*
        self.page_size = page_size
        # $.parameters[11].schema.items.description
        # 
        # This parameter is required.
        self.region_id = region_id
        # $.parameters[11].schema.items.example
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The region ID of the command. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
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
        if self.command_id is not None:
            result['CommandId'] = self.command_id

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.include_history is not None:
            result['IncludeHistory'] = self.include_history

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.invoke_record_status is not None:
            result['InvokeRecordStatus'] = self.invoke_record_status

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('IncludeHistory') is not None:
            self.include_history = m.get('IncludeHistory')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('InvokeRecordStatus') is not None:
            self.invoke_record_status = m.get('InvokeRecordStatus')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeInvocationResultsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeInvocationResultsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The ID of the instance.
        self.key = key
        # The ID of the command task. You can call the [DescribeInvocations](https://help.aliyun.com/document_detail/64840.html) operation to query the IDs of all command tasks.
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

