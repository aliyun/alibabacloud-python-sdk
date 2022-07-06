# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AttachPolicyRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        policy_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.policy_id = policy_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.target_id = target_id
        self.target_type = target_type

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
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class AttachPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachPolicyResponseBody = None,
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
            temp_model = AttachPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePolicyRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        policy_content: str = None,
        policy_desc: str = None,
        policy_name: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        user_type: str = None,
    ):
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.policy_content = policy_content
        self.policy_desc = policy_desc
        self.policy_name = policy_name
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.policy_content is not None:
            result['PolicyContent'] = self.policy_content
        if self.policy_desc is not None:
            result['PolicyDesc'] = self.policy_desc
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyContent') is not None:
            self.policy_content = m.get('PolicyContent')
        if m.get('PolicyDesc') is not None:
            self.policy_desc = m.get('PolicyDesc')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class CreatePolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
        request_id: str = None,
    ):
        self.policy_id = policy_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePolicyResponseBody = None,
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
            temp_model = CreatePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagsRequestTagKeyValueParamListTagValueParamList(TeaModel):
    def __init__(
        self,
        description: str = None,
        value: str = None,
    ):
        self.description = description
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateTagsRequestTagKeyValueParamList(TeaModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
        tag_value_param_list: List[CreateTagsRequestTagKeyValueParamListTagValueParamList] = None,
    ):
        self.description = description
        self.key = key
        self.tag_value_param_list = tag_value_param_list

    def validate(self):
        if self.tag_value_param_list:
            for k in self.tag_value_param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.key is not None:
            result['Key'] = self.key
        result['TagValueParamList'] = []
        if self.tag_value_param_list is not None:
            for k in self.tag_value_param_list:
                result['TagValueParamList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        self.tag_value_param_list = []
        if m.get('TagValueParamList') is not None:
            for k in m.get('TagValueParamList'):
                temp_model = CreateTagsRequestTagKeyValueParamListTagValueParamList()
                self.tag_value_param_list.append(temp_model.from_map(k))
        return self


class CreateTagsRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        tag_key_value_param_list: List[CreateTagsRequestTagKeyValueParamList] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.tag_key_value_param_list = tag_key_value_param_list

    def validate(self):
        if self.tag_key_value_param_list:
            for k in self.tag_key_value_param_list:
                if k:
                    k.validate()

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
        result['TagKeyValueParamList'] = []
        if self.tag_key_value_param_list is not None:
            for k in self.tag_key_value_param_list:
                result['TagKeyValueParamList'].append(k.to_map() if k else None)
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
        self.tag_key_value_param_list = []
        if m.get('TagKeyValueParamList') is not None:
            for k in m.get('TagKeyValueParamList'):
                temp_model = CreateTagsRequestTagKeyValueParamList()
                self.tag_key_value_param_list.append(temp_model.from_map(k))
        return self


class CreateTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTagsResponseBody = None,
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
            temp_model = CreateTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePolicyRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        policy_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.policy_id = policy_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account

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
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class DeletePolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyResponseBody = None,
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
            temp_model = DeletePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        value: str = None,
    ):
        self.key = key
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DeleteTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTagResponseBody = None,
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
            temp_model = DeleteTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.accept_language = accept_language
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
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
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
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
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


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachPolicyRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        policy_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.policy_id = policy_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.target_id = target_id
        self.target_type = target_type

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
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class DetachPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetachPolicyResponseBody = None,
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
            temp_model = DetachPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisablePolicyTypeRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: str = None,
        user_type: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.user_type = user_type

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
        if self.user_type is not None:
            result['UserType'] = self.user_type
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
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DisablePolicyTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisablePolicyTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisablePolicyTypeResponseBody = None,
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
            temp_model = DisablePolicyTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnablePolicyTypeRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: str = None,
        user_type: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.user_type = user_type

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
        if self.user_type is not None:
            result['UserType'] = self.user_type
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
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class EnablePolicyTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnablePolicyTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnablePolicyTypeResponseBody = None,
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
            temp_model = EnablePolicyTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateConfigRuleReportRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        target_id: str = None,
        target_type: str = None,
        user_type: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.target_id = target_id
        self.target_type = target_type
        self.user_type = user_type

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
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.user_type is not None:
            result['UserType'] = self.user_type
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
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GenerateConfigRuleReportResponseBody(TeaModel):
    def __init__(
        self,
        report_id: str = None,
        request_id: str = None,
    ):
        self.report_id = report_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateConfigRuleReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateConfigRuleReportResponseBody = None,
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
            temp_model = GenerateConfigRuleReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigRuleReportRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        target_id: str = None,
        target_type: str = None,
        user_type: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.target_id = target_id
        self.target_type = target_type
        self.user_type = user_type

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
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.user_type is not None:
            result['UserType'] = self.user_type
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
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetConfigRuleReportResponseBodyData(TeaModel):
    def __init__(
        self,
        created_time: int = None,
        report_id: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.created_time = created_time
        self.report_id = report_id
        self.target_id = target_id
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.report_id is not None:
            result['ReportId'] = self.report_id
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class GetConfigRuleReportResponseBody(TeaModel):
    def __init__(
        self,
        data: GetConfigRuleReportResponseBodyData = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetConfigRuleReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetConfigRuleReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConfigRuleReportResponseBody = None,
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
            temp_model = GetConfigRuleReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEffectivePolicyRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.target_id = target_id
        self.target_type = target_type

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
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
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
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class GetEffectivePolicyResponseBody(TeaModel):
    def __init__(
        self,
        effective_policy: str = None,
        request_id: str = None,
    ):
        self.effective_policy = effective_policy
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effective_policy is not None:
            result['EffectivePolicy'] = self.effective_policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectivePolicy') is not None:
            self.effective_policy = m.get('EffectivePolicy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEffectivePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEffectivePolicyResponseBody = None,
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
            temp_model = GetEffectivePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        policy_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.policy_id = policy_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account

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
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class GetPolicyResponseBodyPolicy(TeaModel):
    def __init__(
        self,
        policy_content: str = None,
        policy_desc: str = None,
        policy_name: str = None,
        user_type: str = None,
    ):
        self.policy_content = policy_content
        self.policy_desc = policy_desc
        self.policy_name = policy_name
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_content is not None:
            result['PolicyContent'] = self.policy_content
        if self.policy_desc is not None:
            result['PolicyDesc'] = self.policy_desc
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyContent') is not None:
            self.policy_content = m.get('PolicyContent')
        if m.get('PolicyDesc') is not None:
            self.policy_desc = m.get('PolicyDesc')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetPolicyResponseBody(TeaModel):
    def __init__(
        self,
        policy: GetPolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        self.policy = policy
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = GetPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m['Policy'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPolicyResponseBody = None,
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
            temp_model = GetPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyEnableStatusRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: str = None,
        user_type: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.user_type = user_type

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
        if self.user_type is not None:
            result['UserType'] = self.user_type
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
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetPolicyEnableStatusResponseBodyStatusModels(TeaModel):
    def __init__(
        self,
        status: str = None,
        user_type: str = None,
    ):
        self.status = status
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetPolicyEnableStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status_models: List[GetPolicyEnableStatusResponseBodyStatusModels] = None,
    ):
        self.request_id = request_id
        self.status_models = status_models

    def validate(self):
        if self.status_models:
            for k in self.status_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatusModels'] = []
        if self.status_models is not None:
            for k in self.status_models:
                result['StatusModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.status_models = []
        if m.get('StatusModels') is not None:
            for k in m.get('StatusModels'):
                temp_model = GetPolicyEnableStatusResponseBodyStatusModels()
                self.status_models.append(temp_model.from_map(k))
        return self


class GetPolicyEnableStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPolicyEnableStatusResponseBody = None,
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
            temp_model = GetPolicyEnableStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConfigRulesForTargetRequest(TeaModel):
    def __init__(
        self,
        max_result: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        policy_type: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        tag_key: str = None,
        target_id: str = None,
        target_type: str = None,
        user_type: str = None,
    ):
        self.max_result = max_result
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.policy_type = policy_type
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.tag_key = tag_key
        self.target_id = target_id
        self.target_type = target_type
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class ListConfigRulesForTargetResponseBodyData(TeaModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_id: str = None,
        policy_type: str = None,
        remediation: bool = None,
        tag_key: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.aggregator_id = aggregator_id
        self.config_rule_id = config_rule_id
        self.policy_type = policy_type
        self.remediation = remediation
        self.tag_key = tag_key
        self.target_id = target_id
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.remediation is not None:
            result['Remediation'] = self.remediation
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('Remediation') is not None:
            self.remediation = m.get('Remediation')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListConfigRulesForTargetResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListConfigRulesForTargetResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListConfigRulesForTargetResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListConfigRulesForTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConfigRulesForTargetResponseBody = None,
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
            temp_model = ListConfigRulesForTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPoliciesRequest(TeaModel):
    def __init__(
        self,
        max_result: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        policy_ids: List[str] = None,
        policy_names: List[str] = None,
        region_id: str = None,
        resource_owner_account: str = None,
        user_type: str = None,
    ):
        self.max_result = max_result
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.policy_ids = policy_ids
        self.policy_names = policy_names
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class ListPoliciesResponseBodyPolicyList(TeaModel):
    def __init__(
        self,
        policy_content: str = None,
        policy_desc: str = None,
        policy_id: str = None,
        policy_name: str = None,
        user_type: str = None,
    ):
        self.policy_content = policy_content
        self.policy_desc = policy_desc
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_content is not None:
            result['PolicyContent'] = self.policy_content
        if self.policy_desc is not None:
            result['PolicyDesc'] = self.policy_desc
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyContent') is not None:
            self.policy_content = m.get('PolicyContent')
        if m.get('PolicyDesc') is not None:
            self.policy_desc = m.get('PolicyDesc')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class ListPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        policy_list: List[ListPoliciesResponseBodyPolicyList] = None,
        request_id: str = None,
    ):
        self.next_token = next_token
        self.policy_list = policy_list
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.policy_list:
            for k in self.policy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['PolicyList'] = []
        if self.policy_list is not None:
            for k in self.policy_list:
                result['PolicyList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.policy_list = []
        if m.get('PolicyList') is not None:
            for k in m.get('PolicyList'):
                temp_model = ListPoliciesResponseBodyPolicyList()
                self.policy_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPoliciesResponseBody = None,
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
            temp_model = ListPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPoliciesForTargetRequest(TeaModel):
    def __init__(
        self,
        max_result: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        self.max_result = max_result
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.target_id = target_id
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListPoliciesForTargetResponseBodyData(TeaModel):
    def __init__(
        self,
        policy_content: str = None,
        policy_desc: str = None,
        policy_id: str = None,
        policy_name: str = None,
        user_type: str = None,
    ):
        self.policy_content = policy_content
        self.policy_desc = policy_desc
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_content is not None:
            result['PolicyContent'] = self.policy_content
        if self.policy_desc is not None:
            result['PolicyDesc'] = self.policy_desc
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyContent') is not None:
            self.policy_content = m.get('PolicyContent')
        if m.get('PolicyDesc') is not None:
            self.policy_desc = m.get('PolicyDesc')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class ListPoliciesForTargetResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListPoliciesForTargetResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPoliciesForTargetResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPoliciesForTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPoliciesForTargetResponseBody = None,
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
            temp_model = ListPoliciesForTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesByTagRequestTagFilter(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListResourcesByTagRequest(TeaModel):
    def __init__(
        self,
        tag_filter: ListResourcesByTagRequestTagFilter = None,
        fuzzy_type: str = None,
        include_all_tags: bool = None,
        max_result: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_type: str = None,
    ):
        self.tag_filter = tag_filter
        self.fuzzy_type = fuzzy_type
        self.include_all_tags = include_all_tags
        self.max_result = max_result
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_type = resource_type

    def validate(self):
        if self.tag_filter:
            self.tag_filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_filter is not None:
            result['TagFilter'] = self.tag_filter.to_map()
        if self.fuzzy_type is not None:
            result['FuzzyType'] = self.fuzzy_type
        if self.include_all_tags is not None:
            result['IncludeAllTags'] = self.include_all_tags
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagFilter') is not None:
            temp_model = ListResourcesByTagRequestTagFilter()
            self.tag_filter = temp_model.from_map(m['TagFilter'])
        if m.get('FuzzyType') is not None:
            self.fuzzy_type = m.get('FuzzyType')
        if m.get('IncludeAllTags') is not None:
            self.include_all_tags = m.get('IncludeAllTags')
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListResourcesByTagResponseBodyResourcesTags(TeaModel):
    def __init__(
        self,
        category: str = None,
        key: str = None,
        value: str = None,
    ):
        self.category = category
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListResourcesByTagResponseBodyResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        tags: List[ListResourcesByTagResponseBodyResourcesTags] = None,
    ):
        self.resource_id = resource_id
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListResourcesByTagResponseBodyResourcesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListResourcesByTagResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resources: List[ListResourcesByTagResponseBodyResources] = None,
    ):
        # 表示当前调用返回读取到的位置，空或者空字符串代表数据已经读取完毕
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListResourcesByTagResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListResourcesByTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourcesByTagResponseBody = None,
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
            temp_model = ListResourcesByTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSupportResourceTypesRequest(TeaModel):
    def __init__(
        self,
        max_result: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        product_code: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_tye: str = None,
        show_items: bool = None,
        support_code: str = None,
    ):
        self.max_result = max_result
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.product_code = product_code
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_tye = resource_tye
        self.show_items = show_items
        self.support_code = support_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_tye is not None:
            result['ResourceTye'] = self.resource_tye
        if self.show_items is not None:
            result['ShowItems'] = self.show_items
        if self.support_code is not None:
            result['SupportCode'] = self.support_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceTye') is not None:
            self.resource_tye = m.get('ResourceTye')
        if m.get('ShowItems') is not None:
            self.show_items = m.get('ShowItems')
        if m.get('SupportCode') is not None:
            self.support_code = m.get('SupportCode')
        return self


class ListSupportResourceTypesResponseBodySupportResourceTypesSupportItems(TeaModel):
    def __init__(
        self,
        support: bool = None,
        support_code: str = None,
    ):
        self.support = support
        self.support_code = support_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.support is not None:
            result['Support'] = self.support
        if self.support_code is not None:
            result['SupportCode'] = self.support_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Support') is not None:
            self.support = m.get('Support')
        if m.get('SupportCode') is not None:
            self.support_code = m.get('SupportCode')
        return self


class ListSupportResourceTypesResponseBodySupportResourceTypes(TeaModel):
    def __init__(
        self,
        product_code: str = None,
        resource_type: str = None,
        support_items: List[ListSupportResourceTypesResponseBodySupportResourceTypesSupportItems] = None,
    ):
        self.product_code = product_code
        self.resource_type = resource_type
        self.support_items = support_items

    def validate(self):
        if self.support_items:
            for k in self.support_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['SupportItems'] = []
        if self.support_items is not None:
            for k in self.support_items:
                result['SupportItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.support_items = []
        if m.get('SupportItems') is not None:
            for k in m.get('SupportItems'):
                temp_model = ListSupportResourceTypesResponseBodySupportResourceTypesSupportItems()
                self.support_items.append(temp_model.from_map(k))
        return self


class ListSupportResourceTypesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        support_resource_types: List[ListSupportResourceTypesResponseBodySupportResourceTypes] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.support_resource_types = support_resource_types

    def validate(self):
        if self.support_resource_types:
            for k in self.support_resource_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SupportResourceTypes'] = []
        if self.support_resource_types is not None:
            for k in self.support_resource_types:
                result['SupportResourceTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.support_resource_types = []
        if m.get('SupportResourceTypes') is not None:
            for k in m.get('SupportResourceTypes'):
                temp_model = ListSupportResourceTypesResponseBodySupportResourceTypes()
                self.support_resource_types.append(temp_model.from_map(k))
        return self


class ListSupportResourceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSupportResourceTypesResponseBody = None,
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
            temp_model = ListSupportResourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequestTagFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
    ):
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        tag_filter: ListTagKeysRequestTagFilter = None,
        category: str = None,
        fuzzy_type: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_size: int = None,
        query_type: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_type: str = None,
    ):
        self.tag_filter = tag_filter
        self.category = category
        self.fuzzy_type = fuzzy_type
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_size = page_size
        self.query_type = query_type
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_type = resource_type

    def validate(self):
        if self.tag_filter:
            self.tag_filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_filter is not None:
            result['TagFilter'] = self.tag_filter.to_map()
        if self.category is not None:
            result['Category'] = self.category
        if self.fuzzy_type is not None:
            result['FuzzyType'] = self.fuzzy_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagFilter') is not None:
            temp_model = ListTagKeysRequestTagFilter()
            self.tag_filter = temp_model.from_map(m['TagFilter'])
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('FuzzyType') is not None:
            self.fuzzy_type = m.get('FuzzyType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBodyKeysKey(TeaModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        key: str = None,
    ):
        self.category = category
        self.description = description
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.description is not None:
            result['Description'] = self.description
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Key') is not None:
            self.key = m.get('Key')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        keys: ListTagKeysResponseBodyKeys = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.keys = keys
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.keys:
            self.keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['Keys'] = self.keys.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            temp_model = ListTagKeysResponseBodyKeys()
            self.keys = temp_model.from_map(m['Keys'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagKeysResponseBody = None,
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
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_arn: List[str] = None,
        resource_owner_account: str = None,
        tags: str = None,
    ):
        self.category = category
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_size = page_size
        self.region_id = region_id
        self.resource_arn = resource_arn
        self.resource_owner_account = resource_owner_account
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListTagResourcesResponseBodyTagResourcesTags(TeaModel):
    def __init__(
        self,
        category: str = None,
        key: str = None,
        value: str = None,
    ):
        self.category = category
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagValuesRequestTagFilter(TeaModel):
    def __init__(
        self,
        value: str = None,
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


class ListTagValuesRequest(TeaModel):
    def __init__(
        self,
        tag_filter: ListTagValuesRequestTagFilter = None,
        fuzzy_type: str = None,
        key: str = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_size: int = None,
        query_type: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_type: str = None,
    ):
        self.tag_filter = tag_filter
        self.fuzzy_type = fuzzy_type
        self.key = key
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.page_size = page_size
        self.query_type = query_type
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_type = resource_type

    def validate(self):
        if self.tag_filter:
            self.tag_filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_filter is not None:
            result['TagFilter'] = self.tag_filter.to_map()
        if self.fuzzy_type is not None:
            result['FuzzyType'] = self.fuzzy_type
        if self.key is not None:
            result['Key'] = self.key
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagFilter') is not None:
            temp_model = ListTagValuesRequestTagFilter()
            self.tag_filter = temp_model.from_map(m['TagFilter'])
        if m.get('FuzzyType') is not None:
            self.fuzzy_type = m.get('FuzzyType')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ListTagValuesResponseBody = None,
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
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTargetsForPolicyRequest(TeaModel):
    def __init__(
        self,
        max_result: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        policy_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
    ):
        self.max_result = max_result
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.policy_id = policy_id
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_result is not None:
            result['MaxResult'] = self.max_result
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResult') is not None:
            self.max_result = m.get('MaxResult')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class ListTargetsForPolicyResponseBodyTargets(TeaModel):
    def __init__(
        self,
        target_id: str = None,
        target_type: int = None,
    ):
        self.target_id = target_id
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class ListTargetsForPolicyResponseBody(TeaModel):
    def __init__(
        self,
        is_rd: bool = None,
        next_token: str = None,
        rd_id: str = None,
        request_id: str = None,
        targets: List[ListTargetsForPolicyResponseBodyTargets] = None,
    ):
        self.is_rd = is_rd
        self.next_token = next_token
        self.rd_id = rd_id
        self.request_id = request_id
        self.targets = targets

    def validate(self):
        if self.targets:
            for k in self.targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_rd is not None:
            result['IsRd'] = self.is_rd
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.rd_id is not None:
            result['RdId'] = self.rd_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Targets'] = []
        if self.targets is not None:
            for k in self.targets:
                result['Targets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsRd') is not None:
            self.is_rd = m.get('IsRd')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RdId') is not None:
            self.rd_id = m.get('RdId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.targets = []
        if m.get('Targets') is not None:
            for k in m.get('Targets'):
                temp_model = ListTargetsForPolicyResponseBodyTargets()
                self.targets.append(temp_model.from_map(k))
        return self


class ListTargetsForPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTargetsForPolicyResponseBody = None,
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
            temp_model = ListTargetsForPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPolicyRequest(TeaModel):
    def __init__(
        self,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        policy_content: str = None,
        policy_desc: str = None,
        policy_id: str = None,
        policy_name: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
    ):
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.policy_content = policy_content
        self.policy_desc = policy_desc
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.policy_content is not None:
            result['PolicyContent'] = self.policy_content
        if self.policy_desc is not None:
            result['PolicyDesc'] = self.policy_desc
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PolicyContent') is not None:
            self.policy_content = m.get('PolicyContent')
        if m.get('PolicyDesc') is not None:
            self.policy_desc = m.get('PolicyDesc')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class ModifyPolicyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPolicyResponseBody = None,
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
            temp_model = ModifyPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_arn: List[str] = None,
        resource_owner_account: str = None,
        tags: str = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_arn = resource_arn
        self.resource_owner_account = resource_owner_account
        self.tags = tags

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
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        failed_resources: TagResourcesResponseBodyFailedResources = None,
        request_id: str = None,
    ):
        self.failed_resources = failed_resources
        self.request_id = request_id

    def validate(self):
        if self.failed_resources:
            self.failed_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_resources is not None:
            result['FailedResources'] = self.failed_resources.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedResources') is not None:
            temp_model = TagResourcesResponseBodyFailedResources()
            self.failed_resources = temp_model.from_map(m['FailedResources'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_arn: List[str] = None,
        resource_owner_account: str = None,
        tag_key: List[str] = None,
    ):
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.region_id = region_id
        self.resource_arn = resource_arn
        self.resource_owner_account = resource_owner_account
        self.tag_key = tag_key

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
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        failed_resources: UntagResourcesResponseBodyFailedResources = None,
        request_id: str = None,
    ):
        self.failed_resources = failed_resources
        self.request_id = request_id

    def validate(self):
        if self.failed_resources:
            self.failed_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_resources is not None:
            result['FailedResources'] = self.failed_resources.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedResources') is not None:
            temp_model = UntagResourcesResponseBodyFailedResources()
            self.failed_resources = temp_model.from_map(m['FailedResources'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


