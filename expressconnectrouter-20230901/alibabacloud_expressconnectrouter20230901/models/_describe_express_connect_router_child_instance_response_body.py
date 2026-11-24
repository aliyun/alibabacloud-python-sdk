# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class DescribeExpressConnectRouterChildInstanceResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        child_instance_list: List[main_models.DescribeExpressConnectRouterChildInstanceResponseBodyChildInstanceList] = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
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
        # The list of child instances.
        self.child_instance_list = child_instance_list
        # The status code that indicates whether the call was successful. A value of 200 indicates that the attachment was successful. Other values indicate that the attachment failed. For more information about the causes of failures, see the error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message, which is used to replace `%s` in the **ErrMessage** error message.
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, it indicates that the **DtsJobId** request parameter is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The maximum number of entries returned. Valid values: 1 to 2147483647. Default value: 20.
        self.max_results = max_results
        # The message returned by the operation.
        self.message = message
        # The token for the next query. Valid values:
        # 
        # - If NextToken is empty, no next query is required.
        # - If NextToken is returned, the value indicates the token for the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - **True**: successful.
        # - **False**: failed.
        self.success = success
        # The total number of associated resources.
        self.total_count = total_count

    def validate(self):
        if self.child_instance_list:
            for v1 in self.child_instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['ChildInstanceList'] = []
        if self.child_instance_list is not None:
            for k1 in self.child_instance_list:
                result['ChildInstanceList'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

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

        self.child_instance_list = []
        if m.get('ChildInstanceList') is not None:
            for k1 in m.get('ChildInstanceList'):
                temp_model = main_models.DescribeExpressConnectRouterChildInstanceResponseBodyChildInstanceList()
                self.child_instance_list.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

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

class DescribeExpressConnectRouterChildInstanceResponseBodyChildInstanceList(DaraModel):
    def __init__(
        self,
        association_id: str = None,
        child_instance_id: str = None,
        child_instance_name: str = None,
        child_instance_owner_id: int = None,
        child_instance_region_id: str = None,
        child_instance_type: str = None,
        description: str = None,
        ecr_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        owner_id: int = None,
        region_id: str = None,
        status: str = None,
    ):
        # The ID used to associate the Express Connect Router (ECR) with the VBR.
        self.association_id = association_id
        # The instance ID of the border router for routing.
        self.child_instance_id = child_instance_id
        # The name of the child instance.
        self.child_instance_name = child_instance_name
        # The Alibaba Cloud account ID to which the child instance belongs.
        self.child_instance_owner_id = child_instance_owner_id
        # The region where the child instance resides.
        self.child_instance_region_id = child_instance_region_id
        # The type of the child instance. Valid values: **VBR**: virtual border router.
        self.child_instance_type = child_instance_type
        # The description of the child instance.
        self.description = description
        # The instance ID of the Express Connect Router (ECR).
        self.ecr_id = ecr_id
        # The time when the association was created. The time is displayed in UTC and follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
        self.gmt_create = gmt_create
        # The time when the association was modified. The time is displayed in UTC and follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
        self.gmt_modified = gmt_modified
        # The Alibaba Cloud account ID to which the border router for routing belongs.
        self.owner_id = owner_id
        # The region where the VBR resides.
        self.region_id = region_id
        # The deployment status of the associated resource. Valid values:
        # 
        # - **CREATING**: creating.
        # 
        # - **ACTIVE**: created.
        # 
        # - **ASSOCIATING**: associating.
        # 
        # - **DISSOCIATING**: dissociating.
        # 
        # - **UPDATING**: updating.
        # 
        # - **DELETING**: deleting.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_id is not None:
            result['AssociationId'] = self.association_id

        if self.child_instance_id is not None:
            result['ChildInstanceId'] = self.child_instance_id

        if self.child_instance_name is not None:
            result['ChildInstanceName'] = self.child_instance_name

        if self.child_instance_owner_id is not None:
            result['ChildInstanceOwnerId'] = self.child_instance_owner_id

        if self.child_instance_region_id is not None:
            result['ChildInstanceRegionId'] = self.child_instance_region_id

        if self.child_instance_type is not None:
            result['ChildInstanceType'] = self.child_instance_type

        if self.description is not None:
            result['Description'] = self.description

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')

        if m.get('ChildInstanceId') is not None:
            self.child_instance_id = m.get('ChildInstanceId')

        if m.get('ChildInstanceName') is not None:
            self.child_instance_name = m.get('ChildInstanceName')

        if m.get('ChildInstanceOwnerId') is not None:
            self.child_instance_owner_id = m.get('ChildInstanceOwnerId')

        if m.get('ChildInstanceRegionId') is not None:
            self.child_instance_region_id = m.get('ChildInstanceRegionId')

        if m.get('ChildInstanceType') is not None:
            self.child_instance_type = m.get('ChildInstanceType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

