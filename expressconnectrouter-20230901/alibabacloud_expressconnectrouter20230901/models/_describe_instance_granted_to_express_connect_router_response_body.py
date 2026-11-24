# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceGrantedToExpressConnectRouterResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        ecr_granted_instance_list: List[main_models.DescribeInstanceGrantedToExpressConnectRouterResponseBodyEcrGrantedInstanceList] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The status code. A value of 200 indicates that the call was successful. Other values indicate that the call failed. For more information about the failure causes, see the error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message, which is used to replace `%s` in the **ErrMessage** error message.
        # 
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, it indicates that the **DtsJobId** request parameter is invalid.
        self.dynamic_message = dynamic_message
        # The list of instances authorized to the ECR.
        self.ecr_granted_instance_list = ecr_granted_instance_list
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The maximum number of entries returned. Valid values: 1 to 2147483647. Default value: 20.
        self.max_results = max_results
        # The message returned by the operation.
        self.message = message
        # The pagination token. Valid values:
        # 
        # - If **NextToken** is empty, no next query is available.
        # - If **NextToken** returns a value, the value indicates the token for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - **True**: The call was successful.
        # - **False**: The call failed.
        self.success = success
        # The total number of network instances for which authorization is granted to the Express Connect Router (ECR).
        self.total_count = total_count

    def validate(self):
        if self.ecr_granted_instance_list:
            for v1 in self.ecr_granted_instance_list:
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

        result['EcrGrantedInstanceList'] = []
        if self.ecr_granted_instance_list is not None:
            for k1 in self.ecr_granted_instance_list:
                result['EcrGrantedInstanceList'].append(k1.to_map() if k1 else None)

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

        self.ecr_granted_instance_list = []
        if m.get('EcrGrantedInstanceList') is not None:
            for k1 in m.get('EcrGrantedInstanceList'):
                temp_model = main_models.DescribeInstanceGrantedToExpressConnectRouterResponseBodyEcrGrantedInstanceList()
                self.ecr_granted_instance_list.append(temp_model.from_map(k1))

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

class DescribeInstanceGrantedToExpressConnectRouterResponseBodyEcrGrantedInstanceList(DaraModel):
    def __init__(
        self,
        ecr_id: str = None,
        ecr_owner_ali_uid: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        grant_id: str = None,
        node_id: str = None,
        node_owner_bid: str = None,
        node_owner_uid: int = None,
        node_region_id: str = None,
        node_type: str = None,
        status: str = None,
    ):
        # The instance ID of the Express Connect Router (ECR).
        self.ecr_id = ecr_id
        # The ID of the Alibaba Cloud account to which the Express Connect Router (ECR) instance that receives the authorization belongs.
        self.ecr_owner_ali_uid = ecr_owner_ali_uid
        # The time when the instance was created.
        self.gmt_create = gmt_create
        # The time when the instance was modified.
        self.gmt_modified = gmt_modified
        # The ID of the authorization.
        self.grant_id = grant_id
        # The instance ID of the authorization.
        self.node_id = node_id
        # The ID of the Alibaba Cloud enterprise account to which the instance belongs.
        self.node_owner_bid = node_owner_bid
        # The ID of the Alibaba Cloud account to which the instance belongs.
        self.node_owner_uid = node_owner_uid
        # The ID of the region to which the authorized instance belongs.
        self.node_region_id = node_region_id
        # The type of the network instance. Valid values:
        # - **VBR**: VBR instance.
        # - **VPC**: VPC instance.
        self.node_type = node_type
        # The status of the authorized network instance.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.ecr_owner_ali_uid is not None:
            result['EcrOwnerAliUid'] = self.ecr_owner_ali_uid

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.grant_id is not None:
            result['GrantId'] = self.grant_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_owner_bid is not None:
            result['NodeOwnerBid'] = self.node_owner_bid

        if self.node_owner_uid is not None:
            result['NodeOwnerUid'] = self.node_owner_uid

        if self.node_region_id is not None:
            result['NodeRegionId'] = self.node_region_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('EcrOwnerAliUid') is not None:
            self.ecr_owner_ali_uid = m.get('EcrOwnerAliUid')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GrantId') is not None:
            self.grant_id = m.get('GrantId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeOwnerBid') is not None:
            self.node_owner_bid = m.get('NodeOwnerBid')

        if m.get('NodeOwnerUid') is not None:
            self.node_owner_uid = m.get('NodeOwnerUid')

        if m.get('NodeRegionId') is not None:
            self.node_region_id = m.get('NodeRegionId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

