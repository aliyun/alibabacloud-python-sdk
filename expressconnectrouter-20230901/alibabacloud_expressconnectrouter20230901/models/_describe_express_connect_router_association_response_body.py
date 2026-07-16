# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class DescribeExpressConnectRouterAssociationResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        association_list: List[main_models.DescribeExpressConnectRouterAssociationResponseBodyAssociationList] = None,
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
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The associated resources.
        self.association_list = association_list
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed. For more information, see Error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic part in the error message. This parameter is used to replace the `%s` variable in **ErrMessage**.
        # 
        # >  For example, if the value of **ErrMessage** is **The Value of Input Parameter %s is not valid** and the value of DynamicMessage is **DtsJobId**, the request parameter **DtsJobId** is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The total number of entries returned. Valid values: 1 to 2147483647. Default value: 20.
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
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success
        # The total number of associated resources.
        self.total_count = total_count

    def validate(self):
        if self.association_list:
            for v1 in self.association_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['AssociationList'] = []
        if self.association_list is not None:
            for k1 in self.association_list:
                result['AssociationList'].append(k1.to_map() if k1 else None)

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

        self.association_list = []
        if m.get('AssociationList') is not None:
            for k1 in m.get('AssociationList'):
                temp_model = main_models.DescribeExpressConnectRouterAssociationResponseBodyAssociationList()
                self.association_list.append(temp_model.from_map(k1))

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

class DescribeExpressConnectRouterAssociationResponseBodyAssociationList(DaraModel):
    def __init__(
        self,
        allowed_prefixes: List[str] = None,
        allowed_prefixes_mode: str = None,
        association_id: str = None,
        association_node_type: str = None,
        cen_id: str = None,
        description: str = None,
        ecr_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        owner_id: int = None,
        region_id: str = None,
        status: str = None,
        tags: List[main_models.DescribeExpressConnectRouterAssociationResponseBodyAssociationListTags] = None,
        transit_router_id: str = None,
        transit_router_name: str = None,
        transit_router_owner_id: int = None,
        vpc_id: str = None,
        vpc_name: str = None,
        vpc_owner_id: int = None,
    ):
        # The allowed route prefixes.
        self.allowed_prefixes = allowed_prefixes
        # The prefix route mode. Valid values:
        # 
        # *   MatchMode
        # *   IncrementalMode
        self.allowed_prefixes_mode = allowed_prefixes_mode
        # The ID of the association between the ECR and the VPC or TR.
        self.association_id = association_id
        # The type of the associated resource. Valid values:
        # 
        # *   **VPC**
        # *   **TR**
        self.association_node_type = association_node_type
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The description of the associated resource.
        self.description = description
        # The ECR ID.
        self.ecr_id = ecr_id
        # The time when the association was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_create = gmt_create
        # The time when the association was modified. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.gmt_modified = gmt_modified
        # The ID of the Alibaba Cloud account that owns the resource.
        self.owner_id = owner_id
        # The region ID of the resource.
        self.region_id = region_id
        # The deployment state of the associated resource. Valid values:
        # 
        # *   **CREATING**: The resource is being created.
        # *   **ACTIVE**: The resource is created.
        # *   **INACTIVE**: The TR is pending to be associated with the ECR.
        # *   **ASSOCIATING**: The resource is being associated.
        # *   **DISSOCIATING**: The resource is being disassociated.
        # *   **UPDATING**: The resource is being modified.
        # *   **DELETING**: The resource is being deleted.
        self.status = status
        self.tags = tags
        # The TR ID.
        self.transit_router_id = transit_router_id
        self.transit_router_name = transit_router_name
        # The ID of the Alibaba Cloud account that owns the TR.
        self.transit_router_owner_id = transit_router_owner_id
        # The VPC ID.
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name
        # The ID of the Alibaba Cloud account to which the VPC belongs.
        self.vpc_owner_id = vpc_owner_id

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
        if self.allowed_prefixes is not None:
            result['AllowedPrefixes'] = self.allowed_prefixes

        if self.allowed_prefixes_mode is not None:
            result['AllowedPrefixesMode'] = self.allowed_prefixes_mode

        if self.association_id is not None:
            result['AssociationId'] = self.association_id

        if self.association_node_type is not None:
            result['AssociationNodeType'] = self.association_node_type

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

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

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_name is not None:
            result['TransitRouterName'] = self.transit_router_name

        if self.transit_router_owner_id is not None:
            result['TransitRouterOwnerId'] = self.transit_router_owner_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        if self.vpc_owner_id is not None:
            result['VpcOwnerId'] = self.vpc_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedPrefixes') is not None:
            self.allowed_prefixes = m.get('AllowedPrefixes')

        if m.get('AllowedPrefixesMode') is not None:
            self.allowed_prefixes_mode = m.get('AllowedPrefixesMode')

        if m.get('AssociationId') is not None:
            self.association_id = m.get('AssociationId')

        if m.get('AssociationNodeType') is not None:
            self.association_node_type = m.get('AssociationNodeType')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

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

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeExpressConnectRouterAssociationResponseBodyAssociationListTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterName') is not None:
            self.transit_router_name = m.get('TransitRouterName')

        if m.get('TransitRouterOwnerId') is not None:
            self.transit_router_owner_id = m.get('TransitRouterOwnerId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        if m.get('VpcOwnerId') is not None:
            self.vpc_owner_id = m.get('VpcOwnerId')

        return self

class DescribeExpressConnectRouterAssociationResponseBodyAssociationListTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

