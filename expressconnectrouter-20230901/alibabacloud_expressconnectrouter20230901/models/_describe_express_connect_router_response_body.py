# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class DescribeExpressConnectRouterResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        ecr_list: List[main_models.DescribeExpressConnectRouterResponseBodyEcrList] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of **DynamicMessage** is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The ECRs.
        self.ecr_list = ecr_list
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The total number of entries returned. Valid values: 1 to 2147483647. Default value: 20.
        self.max_results = max_results
        # The returned message.
        self.message = message
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If NextToken is empty, no next page exists.
        # *   If a value of NextToken is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The total number of ECRs.
        self.total_count = total_count

    def validate(self):
        if self.ecr_list:
            for v1 in self.ecr_list:
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

        result['EcrList'] = []
        if self.ecr_list is not None:
            for k1 in self.ecr_list:
                result['EcrList'].append(k1.to_map() if k1 else None)

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

        self.ecr_list = []
        if m.get('EcrList') is not None:
            for k1 in m.get('EcrList'):
                temp_model = main_models.DescribeExpressConnectRouterResponseBodyEcrList()
                self.ecr_list.append(temp_model.from_map(k1))

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

class DescribeExpressConnectRouterResponseBodyEcrList(DaraModel):
    def __init__(
        self,
        alibaba_side_asn: int = None,
        biz_status: str = None,
        description: str = None,
        ecr_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        name: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.DescribeExpressConnectRouterResponseBodyEcrListTags] = None,
    ):
        # The autonomous system number (ASN) of the ECR.
        self.alibaba_side_asn = alibaba_side_asn
        # The business state of the ECR. Valid values:
        # 
        # *   **Normal:** The ECR is running as expected.
        # *   **FinancialLocked**: The ECR is locked due to overdue payments.
        self.biz_status = biz_status
        # The description of the ECR.
        self.description = description
        # The ECR ID.
        self.ecr_id = ecr_id
        # The time when the ECR was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_create = gmt_create
        # The time when the ECR was modified. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The name of the ECR.
        self.name = name
        # The ID of the Alibaba Cloud account that owns the ECR.
        self.owner_id = owner_id
        # The ID of the resource group to which the ECR belongs.
        self.resource_group_id = resource_group_id
        # The deployment state of the ECR. Valid values:
        # 
        # *   **ACTIVE**: The ECR is created.
        # *   **UPDATING**: The ECR is being modified.
        # *   **ASSOCIATING**: The ECR is being associated with resources.
        # *   **DISSOCIATING**: The resource is being disassociated from resources.
        # *   **LOCKED_ATTACHING**: The ECR is locked because it is being associated with an external system.
        # *   **LOCKED_DETACHING**: The ECR is locked because it is being disassociated from an external system.
        # *   **RECLAIMING**: The ECR is waiting to release resources.
        # *   **DELETING**: The ECR is being deleted.
        self.status = status
        # The tags.
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
        if self.alibaba_side_asn is not None:
            result['AlibabaSideAsn'] = self.alibaba_side_asn

        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status

        if self.description is not None:
            result['Description'] = self.description

        if self.ecr_id is not None:
            result['EcrId'] = self.ecr_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlibabaSideAsn') is not None:
            self.alibaba_side_asn = m.get('AlibabaSideAsn')

        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EcrId') is not None:
            self.ecr_id = m.get('EcrId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeExpressConnectRouterResponseBodyEcrListTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class DescribeExpressConnectRouterResponseBodyEcrListTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

