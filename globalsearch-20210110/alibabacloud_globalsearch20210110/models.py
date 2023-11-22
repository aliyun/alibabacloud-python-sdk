# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class CountProductResourcesRequestRequestFilter(TeaModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_value: str = None,
        operation: str = None,
    ):
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class CountProductResourcesRequestRequest(TeaModel):
    def __init__(
        self,
        aggregators: List[str] = None,
        filter: List[CountProductResourcesRequestRequestFilter] = None,
        keyword: str = None,
        max_items: str = None,
        product: str = None,
        resource_type: str = None,
    ):
        self.aggregators = aggregators
        self.filter = filter
        self.keyword = keyword
        self.max_items = max_items
        self.product = product
        self.resource_type = resource_type

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregators is not None:
            result['Aggregators'] = self.aggregators
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregators') is not None:
            self.aggregators = m.get('Aggregators')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = CountProductResourcesRequestRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class CountProductResourcesRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        released: str = None,
        request: List[CountProductResourcesRequestRequest] = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.keyword = keyword
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.released = released
        self.request = request
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.request:
            for k in self.request:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.released is not None:
            result['Released'] = self.released
        result['Request'] = []
        if self.request is not None:
            for k in self.request:
                result['Request'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Released') is not None:
            self.released = m.get('Released')
        self.request = []
        if m.get('Request') is not None:
            for k in m.get('Request'):
                temp_model = CountProductResourcesRequestRequest()
                self.request.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CountProductResourcesResponseBodyResourcesResourceAggregationsAggregation(TeaModel):
    def __init__(
        self,
        count: str = None,
        keys: str = None,
    ):
        self.count = count
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class CountProductResourcesResponseBodyResourcesResourceAggregations(TeaModel):
    def __init__(
        self,
        aggregation: List[CountProductResourcesResponseBodyResourcesResourceAggregationsAggregation] = None,
    ):
        self.aggregation = aggregation

    def validate(self):
        if self.aggregation:
            for k in self.aggregation:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Aggregation'] = []
        if self.aggregation is not None:
            for k in self.aggregation:
                result['Aggregation'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregation = []
        if m.get('Aggregation') is not None:
            for k in m.get('Aggregation'):
                temp_model = CountProductResourcesResponseBodyResourcesResourceAggregationsAggregation()
                self.aggregation.append(temp_model.from_map(k))
        return self


class CountProductResourcesResponseBodyResourcesResource(TeaModel):
    def __init__(
        self,
        aggregations: CountProductResourcesResponseBodyResourcesResourceAggregations = None,
        product: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        total: str = None,
    ):
        self.aggregations = aggregations
        self.product = product
        self.resource_group_id = resource_group_id
        self.resource_type = resource_type
        self.total = total

    def validate(self):
        if self.aggregations:
            self.aggregations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregations is not None:
            result['Aggregations'] = self.aggregations.to_map()
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregations') is not None:
            temp_model = CountProductResourcesResponseBodyResourcesResourceAggregations()
            self.aggregations = temp_model.from_map(m['Aggregations'])
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class CountProductResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        resource: List[CountProductResourcesResponseBodyResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = CountProductResourcesResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k))
        return self


class CountProductResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resources: CountProductResourcesResponseBodyResources = None,
    ):
        self.request_id = request_id
        self.resources = resources

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            temp_model = CountProductResourcesResponseBodyResources()
            self.resources = temp_model.from_map(m['Resources'])
        return self


class CountProductResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CountProductResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CountProductResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeReleasedResourcesRequestFilter(TeaModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_value: str = None,
        operation: str = None,
    ):
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class DescribeReleasedResourcesRequestTagFilter(TeaModel):
    def __init__(
        self,
        operation: str = None,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        self.operation = operation
        self.tag_key = tag_key
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        return self


class DescribeReleasedResourcesRequest(TeaModel):
    def __init__(
        self,
        detail_attribute_names: List[str] = None,
        filter: List[DescribeReleasedResourcesRequestFilter] = None,
        global_: str = None,
        keyword: str = None,
        marker: str = None,
        max_items: int = None,
        owner_account: str = None,
        owner_id: int = None,
        product: str = None,
        region_id: str = None,
        region_no: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag_filter: List[DescribeReleasedResourcesRequestTagFilter] = None,
    ):
        self.detail_attribute_names = detail_attribute_names
        self.filter = filter
        self.global_ = global_
        self.keyword = keyword
        self.marker = marker
        self.max_items = max_items
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.product = product
        self.region_id = region_id
        self.region_no = region_no
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.tag_filter = tag_filter

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.tag_filter:
            for k in self.tag_filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail_attribute_names is not None:
            result['DetailAttributeNames'] = self.detail_attribute_names
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.global_ is not None:
            result['Global'] = self.global_
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['TagFilter'] = []
        if self.tag_filter is not None:
            for k in self.tag_filter:
                result['TagFilter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DetailAttributeNames') is not None:
            self.detail_attribute_names = m.get('DetailAttributeNames')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = DescribeReleasedResourcesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('Global') is not None:
            self.global_ = m.get('Global')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag_filter = []
        if m.get('TagFilter') is not None:
            for k in m.get('TagFilter'):
                temp_model = DescribeReleasedResourcesRequestTagFilter()
                self.tag_filter.append(temp_model.from_map(k))
        return self


class DescribeReleasedResourcesResponseBodyResourcesResource(TeaModel):
    def __init__(
        self,
        arn: str = None,
        create_time: str = None,
        detail: Dict[str, Any] = None,
        matched_attributes: str = None,
        product: str = None,
        public_ip: str = None,
        region_id: str = None,
        release_time: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        update_time: str = None,
    ):
        self.arn = arn
        self.create_time = create_time
        self.detail = detail
        self.matched_attributes = matched_attributes
        self.product = product
        self.public_ip = public_ip
        self.region_id = region_id
        self.release_time = release_time
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.matched_attributes is not None:
            result['MatchedAttributes'] = self.matched_attributes
        if self.product is not None:
            result['Product'] = self.product
        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('MatchedAttributes') is not None:
            self.matched_attributes = m.get('MatchedAttributes')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeReleasedResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        resource: List[DescribeReleasedResourcesResponseBodyResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = DescribeReleasedResourcesResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k))
        return self


class DescribeReleasedResourcesResponseBody(TeaModel):
    def __init__(
        self,
        estimated_total: int = None,
        marker: str = None,
        request_id: str = None,
        resources: DescribeReleasedResourcesResponseBodyResources = None,
        truncated: bool = None,
    ):
        self.estimated_total = estimated_total
        self.marker = marker
        self.request_id = request_id
        self.resources = resources
        self.truncated = truncated

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_total is not None:
            result['EstimatedTotal'] = self.estimated_total
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.truncated is not None:
            result['Truncated'] = self.truncated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EstimatedTotal') is not None:
            self.estimated_total = m.get('EstimatedTotal')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            temp_model = DescribeReleasedResourcesResponseBodyResources()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('Truncated') is not None:
            self.truncated = m.get('Truncated')
        return self


class DescribeReleasedResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeReleasedResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeReleasedResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceAggregationsRequestFilter(TeaModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_value: str = None,
        operation: str = None,
    ):
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class DescribeResourceAggregationsRequestTagFilter(TeaModel):
    def __init__(
        self,
        operation: str = None,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        self.operation = operation
        self.tag_key = tag_key
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        return self


class DescribeResourceAggregationsRequest(TeaModel):
    def __init__(
        self,
        agg_action: str = None,
        aggregators: List[str] = None,
        filter: List[DescribeResourceAggregationsRequestFilter] = None,
        global_: str = None,
        keyword: str = None,
        marker: str = None,
        max_items: int = None,
        owner_account: str = None,
        owner_id: int = None,
        product: str = None,
        region_id: str = None,
        region_no: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag_filter: List[DescribeResourceAggregationsRequestTagFilter] = None,
    ):
        self.agg_action = agg_action
        self.aggregators = aggregators
        self.filter = filter
        self.global_ = global_
        self.keyword = keyword
        self.marker = marker
        self.max_items = max_items
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.product = product
        self.region_id = region_id
        self.region_no = region_no
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.tag_filter = tag_filter

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.tag_filter:
            for k in self.tag_filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agg_action is not None:
            result['AggAction'] = self.agg_action
        if self.aggregators is not None:
            result['Aggregators'] = self.aggregators
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.global_ is not None:
            result['Global'] = self.global_
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['TagFilter'] = []
        if self.tag_filter is not None:
            for k in self.tag_filter:
                result['TagFilter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggAction') is not None:
            self.agg_action = m.get('AggAction')
        if m.get('Aggregators') is not None:
            self.aggregators = m.get('Aggregators')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = DescribeResourceAggregationsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('Global') is not None:
            self.global_ = m.get('Global')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag_filter = []
        if m.get('TagFilter') is not None:
            for k in m.get('TagFilter'):
                temp_model = DescribeResourceAggregationsRequestTagFilter()
                self.tag_filter.append(temp_model.from_map(k))
        return self


class DescribeResourceAggregationsResponseBodyAggregationsAggregation(TeaModel):
    def __init__(
        self,
        count: str = None,
        keys: str = None,
        name: str = None,
        value: str = None,
    ):
        self.count = count
        self.keys = keys
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeResourceAggregationsResponseBodyAggregations(TeaModel):
    def __init__(
        self,
        aggregation: List[DescribeResourceAggregationsResponseBodyAggregationsAggregation] = None,
    ):
        self.aggregation = aggregation

    def validate(self):
        if self.aggregation:
            for k in self.aggregation:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Aggregation'] = []
        if self.aggregation is not None:
            for k in self.aggregation:
                result['Aggregation'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aggregation = []
        if m.get('Aggregation') is not None:
            for k in m.get('Aggregation'):
                temp_model = DescribeResourceAggregationsResponseBodyAggregationsAggregation()
                self.aggregation.append(temp_model.from_map(k))
        return self


class DescribeResourceAggregationsResponseBody(TeaModel):
    def __init__(
        self,
        aggregations: DescribeResourceAggregationsResponseBodyAggregations = None,
        request_id: str = None,
    ):
        self.aggregations = aggregations
        self.request_id = request_id

    def validate(self):
        if self.aggregations:
            self.aggregations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregations is not None:
            result['Aggregations'] = self.aggregations.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregations') is not None:
            temp_model = DescribeResourceAggregationsResponseBodyAggregations()
            self.aggregations = temp_model.from_map(m['Aggregations'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeResourceAggregationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResourceAggregationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeResourceAggregationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceFilterAttributesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        product: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.product = product
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeResourceFilterAttributesResponseBodyFilterAttributesFilterAttributeSupportOperations(TeaModel):
    def __init__(
        self,
        support_operation: List[str] = None,
    ):
        self.support_operation = support_operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.support_operation is not None:
            result['SupportOperation'] = self.support_operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportOperation') is not None:
            self.support_operation = m.get('SupportOperation')
        return self


class DescribeResourceFilterAttributesResponseBodyFilterAttributesFilterAttributeValues(TeaModel):
    def __init__(
        self,
        value: List[str] = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeResourceFilterAttributesResponseBodyFilterAttributesFilterAttribute(TeaModel):
    def __init__(
        self,
        name: str = None,
        support_operations: DescribeResourceFilterAttributesResponseBodyFilterAttributesFilterAttributeSupportOperations = None,
        type: str = None,
        values: DescribeResourceFilterAttributesResponseBodyFilterAttributesFilterAttributeValues = None,
    ):
        self.name = name
        self.support_operations = support_operations
        self.type = type
        self.values = values

    def validate(self):
        if self.support_operations:
            self.support_operations.validate()
        if self.values:
            self.values.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.support_operations is not None:
            result['SupportOperations'] = self.support_operations.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SupportOperations') is not None:
            temp_model = DescribeResourceFilterAttributesResponseBodyFilterAttributesFilterAttributeSupportOperations()
            self.support_operations = temp_model.from_map(m['SupportOperations'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Values') is not None:
            temp_model = DescribeResourceFilterAttributesResponseBodyFilterAttributesFilterAttributeValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class DescribeResourceFilterAttributesResponseBodyFilterAttributes(TeaModel):
    def __init__(
        self,
        filter_attribute: List[DescribeResourceFilterAttributesResponseBodyFilterAttributesFilterAttribute] = None,
    ):
        self.filter_attribute = filter_attribute

    def validate(self):
        if self.filter_attribute:
            for k in self.filter_attribute:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FilterAttribute'] = []
        if self.filter_attribute is not None:
            for k in self.filter_attribute:
                result['FilterAttribute'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter_attribute = []
        if m.get('FilterAttribute') is not None:
            for k in m.get('FilterAttribute'):
                temp_model = DescribeResourceFilterAttributesResponseBodyFilterAttributesFilterAttribute()
                self.filter_attribute.append(temp_model.from_map(k))
        return self


class DescribeResourceFilterAttributesResponseBody(TeaModel):
    def __init__(
        self,
        filter_attributes: DescribeResourceFilterAttributesResponseBodyFilterAttributes = None,
        request_id: str = None,
    ):
        self.filter_attributes = filter_attributes
        self.request_id = request_id

    def validate(self):
        if self.filter_attributes:
            self.filter_attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_attributes is not None:
            result['FilterAttributes'] = self.filter_attributes.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterAttributes') is not None:
            temp_model = DescribeResourceFilterAttributesResponseBodyFilterAttributes()
            self.filter_attributes = temp_model.from_map(m['FilterAttributes'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeResourceFilterAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResourceFilterAttributesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeResourceFilterAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourceRecommendFiltersRequest(TeaModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_value: str = None,
        global_: str = None,
        max_items: int = None,
        owner_account: str = None,
        owner_id: int = None,
        product: str = None,
        region_id: str = None,
        region_no: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
    ):
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value
        self.global_ = global_
        self.max_items = max_items
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.product = product
        self.region_id = region_id
        self.region_no = region_no
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        if self.global_ is not None:
            result['Global'] = self.global_
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        if m.get('Global') is not None:
            self.global_ = m.get('Global')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeResourceRecommendFiltersResponseBodyRecommendFiltersRecommendFilter(TeaModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_value: str = None,
        product: str = None,
        resource_type: str = None,
    ):
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value
        self.product = product
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeResourceRecommendFiltersResponseBodyRecommendFilters(TeaModel):
    def __init__(
        self,
        recommend_filter: List[DescribeResourceRecommendFiltersResponseBodyRecommendFiltersRecommendFilter] = None,
    ):
        self.recommend_filter = recommend_filter

    def validate(self):
        if self.recommend_filter:
            for k in self.recommend_filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RecommendFilter'] = []
        if self.recommend_filter is not None:
            for k in self.recommend_filter:
                result['RecommendFilter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recommend_filter = []
        if m.get('RecommendFilter') is not None:
            for k in m.get('RecommendFilter'):
                temp_model = DescribeResourceRecommendFiltersResponseBodyRecommendFiltersRecommendFilter()
                self.recommend_filter.append(temp_model.from_map(k))
        return self


class DescribeResourceRecommendFiltersResponseBody(TeaModel):
    def __init__(
        self,
        recommend_filters: DescribeResourceRecommendFiltersResponseBodyRecommendFilters = None,
        request_id: str = None,
    ):
        self.recommend_filters = recommend_filters
        self.request_id = request_id

    def validate(self):
        if self.recommend_filters:
            self.recommend_filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recommend_filters is not None:
            result['RecommendFilters'] = self.recommend_filters.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecommendFilters') is not None:
            temp_model = DescribeResourceRecommendFiltersResponseBodyRecommendFilters()
            self.recommend_filters = temp_model.from_map(m['RecommendFilters'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeResourceRecommendFiltersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResourceRecommendFiltersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeResourceRecommendFiltersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourcesRequestFilter(TeaModel):
    def __init__(
        self,
        attribute_name: str = None,
        attribute_value: str = None,
        operation: str = None,
    ):
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name
        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value
        if self.operation is not None:
            result['Operation'] = self.operation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')
        if m.get('AttributeValue') is not None:
            self.attribute_value = m.get('AttributeValue')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        return self


class DescribeResourcesRequestTagFilter(TeaModel):
    def __init__(
        self,
        operation: str = None,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        self.operation = operation
        self.tag_key = tag_key
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        return self


class DescribeResourcesRequest(TeaModel):
    def __init__(
        self,
        detail: bool = None,
        detail_attribute_names: List[str] = None,
        filter: List[DescribeResourcesRequestFilter] = None,
        global_: str = None,
        keyword: str = None,
        marker: str = None,
        max_items: int = None,
        owner_account: str = None,
        owner_id: int = None,
        page: int = None,
        product: str = None,
        region_id: str = None,
        region_no: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        tag_filter: List[DescribeResourcesRequestTagFilter] = None,
    ):
        self.detail = detail
        self.detail_attribute_names = detail_attribute_names
        self.filter = filter
        self.global_ = global_
        self.keyword = keyword
        self.marker = marker
        self.max_items = max_items
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page = page
        self.product = product
        self.region_id = region_id
        self.region_no = region_no
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.resource_type = resource_type
        self.tag_filter = tag_filter

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.tag_filter:
            for k in self.tag_filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.detail_attribute_names is not None:
            result['DetailAttributeNames'] = self.detail_attribute_names
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.global_ is not None:
            result['Global'] = self.global_
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_items is not None:
            result['MaxItems'] = self.max_items
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page is not None:
            result['Page'] = self.page
        if self.product is not None:
            result['Product'] = self.product
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['TagFilter'] = []
        if self.tag_filter is not None:
            for k in self.tag_filter:
                result['TagFilter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('DetailAttributeNames') is not None:
            self.detail_attribute_names = m.get('DetailAttributeNames')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = DescribeResourcesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('Global') is not None:
            self.global_ = m.get('Global')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag_filter = []
        if m.get('TagFilter') is not None:
            for k in m.get('TagFilter'):
                temp_model = DescribeResourcesRequestTagFilter()
                self.tag_filter.append(temp_model.from_map(k))
        return self


class DescribeResourcesResponseBodyResourcesResource(TeaModel):
    def __init__(
        self,
        arn: str = None,
        create_time: str = None,
        detail: Dict[str, Any] = None,
        matched_attributes: Dict[str, Any] = None,
        product: str = None,
        public_ip: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        resource_url: str = None,
        update_time: str = None,
    ):
        self.arn = arn
        self.create_time = create_time
        self.detail = detail
        self.matched_attributes = matched_attributes
        self.product = product
        self.public_ip = public_ip
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.resource_url = resource_url
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arn is not None:
            result['Arn'] = self.arn
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.matched_attributes is not None:
            result['MatchedAttributes'] = self.matched_attributes
        if self.product is not None:
            result['Product'] = self.product
        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_url is not None:
            result['ResourceUrl'] = self.resource_url
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('MatchedAttributes') is not None:
            self.matched_attributes = m.get('MatchedAttributes')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceUrl') is not None:
            self.resource_url = m.get('ResourceUrl')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        resource: List[DescribeResourcesResponseBodyResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = DescribeResourcesResponseBodyResourcesResource()
                self.resource.append(temp_model.from_map(k))
        return self


class DescribeResourcesResponseBody(TeaModel):
    def __init__(
        self,
        estimated_total: int = None,
        marker: str = None,
        request_id: str = None,
        resources: DescribeResourcesResponseBodyResources = None,
        truncated: bool = None,
    ):
        self.estimated_total = estimated_total
        self.marker = marker
        self.request_id = request_id
        self.resources = resources
        self.truncated = truncated

    def validate(self):
        if self.resources:
            self.resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.estimated_total is not None:
            result['EstimatedTotal'] = self.estimated_total
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources.to_map()
        if self.truncated is not None:
            result['Truncated'] = self.truncated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EstimatedTotal') is not None:
            self.estimated_total = m.get('EstimatedTotal')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            temp_model = DescribeResourcesResponseBodyResources()
            self.resources = temp_model.from_map(m['Resources'])
        if m.get('Truncated') is not None:
            self.truncated = m.get('Truncated')
        return self


class DescribeResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSupportedProductsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DescribeSupportedProductsResponseBodyProductsProductResourceTypesResourceType(TeaModel):
    def __init__(
        self,
        name: str = None,
        resource_type: str = None,
        support_released: str = None,
    ):
        self.name = name
        self.resource_type = resource_type
        self.support_released = support_released

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.support_released is not None:
            result['SupportReleased'] = self.support_released
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SupportReleased') is not None:
            self.support_released = m.get('SupportReleased')
        return self


class DescribeSupportedProductsResponseBodyProductsProductResourceTypes(TeaModel):
    def __init__(
        self,
        resource_type: List[DescribeSupportedProductsResponseBodyProductsProductResourceTypesResourceType] = None,
    ):
        self.resource_type = resource_type

    def validate(self):
        if self.resource_type:
            for k in self.resource_type:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceType'] = []
        if self.resource_type is not None:
            for k in self.resource_type:
                result['ResourceType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_type = []
        if m.get('ResourceType') is not None:
            for k in m.get('ResourceType'):
                temp_model = DescribeSupportedProductsResponseBodyProductsProductResourceTypesResourceType()
                self.resource_type.append(temp_model.from_map(k))
        return self


class DescribeSupportedProductsResponseBodyProductsProduct(TeaModel):
    def __init__(
        self,
        name: str = None,
        policy: str = None,
        product: str = None,
        resource_types: DescribeSupportedProductsResponseBodyProductsProductResourceTypes = None,
    ):
        self.name = name
        self.policy = policy
        self.product = product
        self.resource_types = resource_types

    def validate(self):
        if self.resource_types:
            self.resource_types.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.product is not None:
            result['Product'] = self.product
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('Product') is not None:
            self.product = m.get('Product')
        if m.get('ResourceTypes') is not None:
            temp_model = DescribeSupportedProductsResponseBodyProductsProductResourceTypes()
            self.resource_types = temp_model.from_map(m['ResourceTypes'])
        return self


class DescribeSupportedProductsResponseBodyProducts(TeaModel):
    def __init__(
        self,
        product: List[DescribeSupportedProductsResponseBodyProductsProduct] = None,
    ):
        self.product = product

    def validate(self):
        if self.product:
            for k in self.product:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Product'] = []
        if self.product is not None:
            for k in self.product:
                result['Product'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product = []
        if m.get('Product') is not None:
            for k in m.get('Product'):
                temp_model = DescribeSupportedProductsResponseBodyProductsProduct()
                self.product.append(temp_model.from_map(k))
        return self


class DescribeSupportedProductsResponseBody(TeaModel):
    def __init__(
        self,
        products: DescribeSupportedProductsResponseBodyProducts = None,
        request_id: str = None,
    ):
        self.products = products
        self.request_id = request_id

    def validate(self):
        if self.products:
            self.products.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.products is not None:
            result['Products'] = self.products.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Products') is not None:
            temp_model = DescribeSupportedProductsResponseBodyProducts()
            self.products = temp_model.from_map(m['Products'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSupportedProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSupportedProductsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSupportedProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


