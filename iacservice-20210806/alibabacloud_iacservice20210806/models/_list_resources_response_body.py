# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListResourcesResponseBody(DaraModel):
    def __init__(
        self,
        resources: List[main_models.ListResourcesResponseBodyResources] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.resources = resources
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.ListResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListResourcesResponseBodyResources(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        create_time: str = None,
        depends_on_resource_ids: List[str] = None,
        product_code: str = None,
        properties: Dict[str, Any] = None,
        property_variables: Dict[str, Any] = None,
        region_id: str = None,
        resource_arn: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_page_url: str = None,
        resource_type: str = None,
        status: str = None,
        tags: List[main_models.ListResourcesResponseBodyResourcesTags] = None,
        terraform_arn: str = None,
        terraform_code: str = None,
        zone_id: str = None,
    ):
        self.account_id = account_id
        self.create_time = create_time
        self.depends_on_resource_ids = depends_on_resource_ids
        self.product_code = product_code
        self.properties = properties
        self.property_variables = property_variables
        self.region_id = region_id
        self.resource_arn = resource_arn
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_page_url = resource_page_url
        self.resource_type = resource_type
        self.status = status
        self.tags = tags
        # terraform arn
        self.terraform_arn = terraform_arn
        # terraform code
        self.terraform_code = terraform_code
        self.zone_id = zone_id

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
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.depends_on_resource_ids is not None:
            result['dependsOnResourceIds'] = self.depends_on_resource_ids

        if self.product_code is not None:
            result['productCode'] = self.product_code

        if self.properties is not None:
            result['properties'] = self.properties

        if self.property_variables is not None:
            result['propertyVariables'] = self.property_variables

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_arn is not None:
            result['resourceArn'] = self.resource_arn

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.resource_page_url is not None:
            result['resourcePageUrl'] = self.resource_page_url

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.status is not None:
            result['status'] = self.status

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.terraform_arn is not None:
            result['terraformArn'] = self.terraform_arn

        if self.terraform_code is not None:
            result['terraformCode'] = self.terraform_code

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dependsOnResourceIds') is not None:
            self.depends_on_resource_ids = m.get('dependsOnResourceIds')

        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('propertyVariables') is not None:
            self.property_variables = m.get('propertyVariables')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceArn') is not None:
            self.resource_arn = m.get('resourceArn')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourcePageUrl') is not None:
            self.resource_page_url = m.get('resourcePageUrl')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListResourcesResponseBodyResourcesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('terraformArn') is not None:
            self.terraform_arn = m.get('terraformArn')

        if m.get('terraformCode') is not None:
            self.terraform_code = m.get('terraformCode')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class ListResourcesResponseBodyResourcesTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

