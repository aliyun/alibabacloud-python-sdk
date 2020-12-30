# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        owner_account: str = None,
        region_id: str = None,
        next_token: str = None,
        page_size: int = None,
        category: str = None,
        resource_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.owner_account = owner_account
        self.region_id = region_id
        self.next_token = next_token
        self.page_size = page_size
        self.category = category
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.category is not None:
            result['Category'] = self.category
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBodyKeysKey(TeaModel):
    def __init__(
        self,
        key: str = None,
        category: str = None,
    ):
        self.key = key
        self.category = category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.category is not None:
            result['Category'] = self.category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        return self


class ListTagKeysResponseBodyKeys(TeaModel):
    def __init__(
        self,
        key: List[ListTagKeysResponseBodyKeysKey] = None,
    ):
        self.key = key

    def validate(self):
        if self.key:
            for k in self.key:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Key'] = []
        if self.key is not None:
            for k in self.key:
                result['Key'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key = []
        if m.get('Key') is not None:
            for k in m.get('Key'):
                temp_model = ListTagKeysResponseBodyKeysKey()
                self.key.append(temp_model.from_map(k))
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        keys: ListTagKeysResponseBodyKeys = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.keys = keys

    def validate(self):
        if self.keys:
            self.keys.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Keys') is not None:
            temp_model = ListTagKeysResponseBodyKeys()
            self.keys = temp_model.from_map(m['Keys'])
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagKeysResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        owner_account: str = None,
        region_id: str = None,
        next_token: str = None,
        page_size: int = None,
        tags: str = None,
        category: str = None,
        resource_arn: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.owner_account = owner_account
        self.region_id = region_id
        self.next_token = next_token
        self.page_size = page_size
        self.tags = tags
        self.category = category
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.category is not None:
            result['Category'] = self.category
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        return self


class ListTagResourcesResponseBodyTagResourcesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        category: str = None,
    ):
        self.key = key
        self.value = value
        self.category = category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        if self.category is not None:
            result['Category'] = self.category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
        tags: List[ListTagResourcesResponseBodyTagResourcesTags] = None,
    ):
        self.resource_arn = resource_arn
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagValuesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        owner_account: str = None,
        region_id: str = None,
        key: str = None,
        next_token: str = None,
        page_size: int = None,
        resource_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.owner_account = owner_account
        self.region_id = region_id
        self.key = key
        self.next_token = next_token
        self.page_size = page_size
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.key is not None:
            result['Key'] = self.key
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagValuesResponseBodyValues(TeaModel):
    def __init__(
        self,
        value: List[str] = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        values: ListTagValuesResponseBodyValues = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.values = values

    def validate(self):
        if self.values:
            self.values.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.values is not None:
            result['Values'] = self.values.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Values') is not None:
            temp_model = ListTagValuesResponseBodyValues()
            self.values = temp_model.from_map(m['Values'])
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagValuesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        owner_account: str = None,
        region_id: str = None,
        tags: str = None,
        resource_arn: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.owner_account = owner_account
        self.region_id = region_id
        self.tags = tags
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        return self


class TagResourcesResponseBodyFailedResourcesFailedResourceResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class TagResourcesResponseBodyFailedResourcesFailedResource(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
        result: TagResourcesResponseBodyFailedResourcesFailedResourceResult = None,
    ):
        self.resource_arn = resource_arn
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        if m.get('Result') is not None:
            temp_model = TagResourcesResponseBodyFailedResourcesFailedResourceResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class TagResourcesResponseBodyFailedResources(TeaModel):
    def __init__(
        self,
        failed_resource: List[TagResourcesResponseBodyFailedResourcesFailedResource] = None,
    ):
        self.failed_resource = failed_resource

    def validate(self):
        if self.failed_resource:
            for k in self.failed_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['FailedResource'] = []
        if self.failed_resource is not None:
            for k in self.failed_resource:
                result['FailedResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_resource = []
        if m.get('FailedResource') is not None:
            for k in m.get('FailedResource'):
                temp_model = TagResourcesResponseBodyFailedResourcesFailedResource()
                self.failed_resource.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        failed_resources: TagResourcesResponseBodyFailedResources = None,
    ):
        self.request_id = request_id
        self.failed_resources = failed_resources

    def validate(self):
        if self.failed_resources:
            self.failed_resources.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.failed_resources is not None:
            result['FailedResources'] = self.failed_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FailedResources') is not None:
            temp_model = TagResourcesResponseBodyFailedResources()
            self.failed_resources = temp_model.from_map(m['FailedResources'])
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        owner_account: str = None,
        region_id: str = None,
        resource_arn: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.owner_account = owner_account
        self.region_id = region_id
        self.resource_arn = resource_arn
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBodyFailedResourcesFailedResourceResult(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UntagResourcesResponseBodyFailedResourcesFailedResource(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
        result: UntagResourcesResponseBodyFailedResourcesFailedResourceResult = None,
    ):
        self.resource_arn = resource_arn
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        if m.get('Result') is not None:
            temp_model = UntagResourcesResponseBodyFailedResourcesFailedResourceResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class UntagResourcesResponseBodyFailedResources(TeaModel):
    def __init__(
        self,
        failed_resource: List[UntagResourcesResponseBodyFailedResourcesFailedResource] = None,
    ):
        self.failed_resource = failed_resource

    def validate(self):
        if self.failed_resource:
            for k in self.failed_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['FailedResource'] = []
        if self.failed_resource is not None:
            for k in self.failed_resource:
                result['FailedResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_resource = []
        if m.get('FailedResource') is not None:
            for k in m.get('FailedResource'):
                temp_model = UntagResourcesResponseBodyFailedResourcesFailedResource()
                self.failed_resource.append(temp_model.from_map(k))
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        failed_resources: UntagResourcesResponseBodyFailedResources = None,
    ):
        self.request_id = request_id
        self.failed_resources = failed_resources

    def validate(self):
        if self.failed_resources:
            self.failed_resources.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.failed_resources is not None:
            result['FailedResources'] = self.failed_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FailedResources') is not None:
            temp_model = UntagResourcesResponseBodyFailedResources()
            self.failed_resources = temp_model.from_map(m['FailedResources'])
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


