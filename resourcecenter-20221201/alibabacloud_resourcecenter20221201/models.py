# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class DisableMultiAccountResourceCenterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class DisableMultiAccountResourceCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableMultiAccountResourceCenterResponseBody = None,
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
            temp_model = DisableMultiAccountResourceCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableResourceCenterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
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


class DisableResourceCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableResourceCenterResponseBody = None,
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
            temp_model = DisableResourceCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableMultiAccountResourceCenterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The status of the feature. Valid values:
        # 
        # *   Pending: The feature is being enabled.
        # *   Enabled: The feature is enabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class EnableMultiAccountResourceCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableMultiAccountResourceCenterResponseBody = None,
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
            temp_model = EnableMultiAccountResourceCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableResourceCenterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The activation status of the service. Valid values:
        # 
        # *   Pending: The service is being activated.
        # *   Enabled: The service is activated.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class EnableResourceCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableResourceCenterResponseBody = None,
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
            temp_model = EnableResourceCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMultiAccountResourceCenterServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        initial_status: str = None,
        request_id: str = None,
        service_status: str = None,
    ):
        # The initialization status of the feature. Valid values:
        # 
        # *   Pending: The feature is being initialized.
        # *   Finished: The feature is initialized.
        self.initial_status = initial_status
        # The ID of the request.
        self.request_id = request_id
        # The status of the feature. Valid values:
        # 
        # *   Enabled: The feature is enabled.
        # *   Disabled: The feature is disabled.
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initial_status is not None:
            result['InitialStatus'] = self.initial_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitialStatus') is not None:
            self.initial_status = m.get('InitialStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class GetMultiAccountResourceCenterServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMultiAccountResourceCenterServiceStatusResponseBody = None,
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
            temp_model = GetMultiAccountResourceCenterServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMultiAccountResourceConfigurationRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        resource_id: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the management account or member of the resource directory.
        self.account_id = account_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The region ID of the resource.
        self.resource_region_id = resource_region_id
        # The type of the resource.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetMultiAccountResourceConfigurationResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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


class GetMultiAccountResourceConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        configuration: Dict[str, Any] = None,
        create_time: str = None,
        ip_addresses: List[str] = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tags: List[GetMultiAccountResourceConfigurationResponseBodyTags] = None,
        zone_id: str = None,
    ):
        # The ID of the management account or member of the resource directory.
        self.account_id = account_id
        # The configurations of the resource.
        self.configuration = configuration
        # The time when the resource was created.
        self.create_time = create_time
        # The IP addresses.
        # 
        # > Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.ip_addresses = ip_addresses
        # The region ID of the resource.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group to which the resource belongs.
        self.resource_group_id = resource_group_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The name of the resource.
        self.resource_name = resource_name
        # The type of the resource.
        self.resource_type = resource_type
        # The tags of the resource.
        self.tags = tags
        # The zone ID of the resource.
        self.zone_id = zone_id

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
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetMultiAccountResourceConfigurationResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetMultiAccountResourceConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMultiAccountResourceConfigurationResponseBody = None,
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
            temp_model = GetMultiAccountResourceConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceCenterServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        initial_status: str = None,
        request_id: str = None,
        service_status: str = None,
    ):
        # The initialization status of the service. Valid values:
        # 
        # *   Pending: The service being initialized.
        # *   Finished: The service is initialized.
        self.initial_status = initial_status
        # The ID of the request.
        self.request_id = request_id
        # The status of the service. Valid values:
        # 
        # *   Enabled: The service is activated.
        # *   Disabled: The service is deactivated.
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initial_status is not None:
            result['InitialStatus'] = self.initial_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitialStatus') is not None:
            self.initial_status = m.get('InitialStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class GetResourceCenterServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceCenterServiceStatusResponseBody = None,
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
            temp_model = GetResourceCenterServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceConfigurationRequest(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the resource.
        self.resource_id = resource_id
        # The region ID of the resource.
        self.resource_region_id = resource_region_id
        # The type of the resource.
        # 
        # For more information about the resource types supported by Resource Center, see [Services that work with Resource Center](~~477798~~).
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetResourceConfigurationResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class GetResourceConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        configuration: Dict[str, Any] = None,
        create_time: str = None,
        ip_addresses: List[str] = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tags: List[GetResourceConfigurationResponseBodyTags] = None,
        zone_id: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.account_id = account_id
        # The configurations of the resource.
        self.configuration = configuration
        # The time when the resource was created.
        self.create_time = create_time
        # The IP addresses.
        # 
        # > Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.ip_addresses = ip_addresses
        # The region ID of the resource.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group to which the resource belongs.
        self.resource_group_id = resource_group_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The name of the resource.
        self.resource_name = resource_name
        # The type of the resource.
        self.resource_type = resource_type
        # The tags of the resource.
        self.tags = tags
        # The zone ID of the resource.
        self.zone_id = zone_id

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
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetResourceConfigurationResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetResourceConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceConfigurationResponseBody = None,
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
            temp_model = GetResourceConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceCountsRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: List[str] = None,
    ):
        # The key of the filter condition. For more information, see `Supported filter parameters`.
        self.key = key
        # The matching mode.
        # 
        # The value Equals indicates an equal match.
        self.match_type = match_type
        # The values of the filter condition.
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
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetResourceCountsRequest(TeaModel):
    def __init__(
        self,
        filter: List[GetResourceCountsRequestFilter] = None,
        group_by_key: str = None,
    ):
        # The filter conditions.
        self.filter = filter
        # The dimension by which resources are queried. Valid values:
        # 
        # *   ResourceType
        # *   Region
        # *   ResourceGroupId
        # *   TagKey
        # *   TagValue
        self.group_by_key = group_by_key

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
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.group_by_key is not None:
            result['GroupByKey'] = self.group_by_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = GetResourceCountsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('GroupByKey') is not None:
            self.group_by_key = m.get('GroupByKey')
        return self


class GetResourceCountsResponseBodyFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The key of the filter condition.
        self.key = key
        # The values of the filter condition.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetResourceCountsResponseBodyResourceCounts(TeaModel):
    def __init__(
        self,
        count: int = None,
        group_name: str = None,
    ):
        # The number of resources.
        self.count = count
        # The group name.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class GetResourceCountsResponseBody(TeaModel):
    def __init__(
        self,
        filters: List[GetResourceCountsResponseBodyFilters] = None,
        group_by_key: str = None,
        request_id: str = None,
        resource_counts: List[GetResourceCountsResponseBodyResourceCounts] = None,
    ):
        # The filter conditions.
        self.filters = filters
        # The dimension by which resources are queried.
        self.group_by_key = group_by_key
        # The request ID.
        self.request_id = request_id
        # The numbers of resources.
        self.resource_counts = resource_counts

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()
        if self.resource_counts:
            for k in self.resource_counts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.group_by_key is not None:
            result['GroupByKey'] = self.group_by_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceCounts'] = []
        if self.resource_counts is not None:
            for k in self.resource_counts:
                result['ResourceCounts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = GetResourceCountsResponseBodyFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('GroupByKey') is not None:
            self.group_by_key = m.get('GroupByKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_counts = []
        if m.get('ResourceCounts') is not None:
            for k in m.get('ResourceCounts'):
                temp_model = GetResourceCountsResponseBodyResourceCounts()
                self.resource_counts.append(temp_model.from_map(k))
        return self


class GetResourceCountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceCountsResponseBody = None,
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
            temp_model = GetResourceCountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMultiAccountResourceGroupsRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_ids: List[str] = None,
    ):
        # The ID of the management account or member of the resource directory.
        self.account_id = account_id
        # The maximum number of entries to return on each page.
        # 
        # Maximum value: 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The IDs of resource groups.
        self.resource_group_ids = resource_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')
        return self


class ListMultiAccountResourceGroupsResponseBodyResourceGroups(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        status: str = None,
    ):
        # The ID of the management account or member of the resource directory.
        self.account_id = account_id
        # The time when the resource group was created.
        self.create_date = create_date
        # The display name of the resource group.
        self.display_name = display_name
        # The ID of the resource group.
        self.id = id
        # The unique identifier of the resource group.
        self.name = name
        # The status of the resource group. Valid values:
        # 
        # *   Creating: The resource group is being created.
        # *   OK: The resource group is created.
        # *   PendingDelete: The resource group is waiting to be deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListMultiAccountResourceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resource_groups: List[ListMultiAccountResourceGroupsResponseBodyResourceGroups] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information about the resource groups.
        self.resource_groups = resource_groups

    def validate(self):
        if self.resource_groups:
            for k in self.resource_groups:
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
        result['ResourceGroups'] = []
        if self.resource_groups is not None:
            for k in self.resource_groups:
                result['ResourceGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_groups = []
        if m.get('ResourceGroups') is not None:
            for k in m.get('ResourceGroups'):
                temp_model = ListMultiAccountResourceGroupsResponseBodyResourceGroups()
                self.resource_groups.append(temp_model.from_map(k))
        return self


class ListMultiAccountResourceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMultiAccountResourceGroupsResponseBody = None,
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
            temp_model = ListMultiAccountResourceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMultiAccountTagKeysRequest(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        max_results: int = None,
        next_token: str = None,
        scope: str = None,
        tag_key: str = None,
    ):
        # The matching mode. Valid values:
        # 
        # *   Equals: equal match
        # *   Prefix: match by prefix
        self.match_type = match_type
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the `token` to initiate another request and obtain the remaining entries.
        self.next_token = next_token
        # The search scope. You can set the value to one of the following items:
        # 
        # *   ID of a resource directory: Resources within the management account and all members of the resource directory are searched. You can call the [GetResourceDirectory](~~159995~~) operation to obtain the ID.
        # *   ID of the Root folder: Resources within all members in the Root folder and the subfolders of the Root folder are searched. You can call the [ListFoldersForParent](~~159997~~) operation to obtain the ID.
        # *   ID of a folder: Resources within all members in the folder are searched. You can call the [ListFoldersForParent](~~159997~~) operation to obtain the ID.
        # *   ID of a member: Resources within the member are searched. You can call the [ListAccounts](~~160016~~) operation to obtain the ID.
        self.scope = scope
        # The tag key.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListMultiAccountTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_keys: List[str] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The tag keys.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class ListMultiAccountTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMultiAccountTagKeysResponseBody = None,
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
            temp_model = ListMultiAccountTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMultiAccountTagValuesRequest(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        max_results: int = None,
        next_token: str = None,
        scope: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The matching mode. Valid values:
        # 
        # *   Equals: equal match
        # *   Prefix: match by prefix
        self.match_type = match_type
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the `token` to initiate another request and obtain the remaining entries.
        self.next_token = next_token
        # The search scope. You can set the value to one of the following items:
        # 
        # *   ID of a resource directory: Resources within the management account and all members of the resource directory are searched. You can call the [GetResourceDirectory](~~159995~~) operation to obtain the ID.
        # *   ID of the Root folder: Resources within all members in the Root folder and the subfolders of the Root folder are searched. You can call the [ListFoldersForParent](~~159997~~) operation to obtain the ID.
        # *   ID of a folder: Resources within all members in the folder are searched. You can call the [ListFoldersForParent](~~159997~~) operation to obtain the ID.
        # *   ID of a member: Resources within the member are searched. You can call the [ListAccounts](~~160016~~) operation to obtain the ID.
        self.scope = scope
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListMultiAccountTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_values: List[str] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The tag values.
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        return self


class ListMultiAccountTagValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMultiAccountTagValuesResponseBody = None,
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
            temp_model = ListMultiAccountTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceTypesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        query: List[str] = None,
        resource_type: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US: English
        self.accept_language = accept_language
        # The query conditions.
        self.query = query
        # The resource type.
        # 
        # For more information about the resource types that are supported by Resource Center, see [Services that work with Resource Center](~~477798~~).
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.query is not None:
            result['Query'] = self.query
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListResourceTypesResponseBodyResourceTypes(TeaModel):
    def __init__(
        self,
        filter_keys: List[str] = None,
        product_name: str = None,
        resource_type: str = None,
        resource_type_name: str = None,
    ):
        # The supported filter conditions.
        self.filter_keys = filter_keys
        # The name of the Alibaba Cloud service.
        self.product_name = product_name
        # The resource type.
        self.resource_type = resource_type
        # The name of the resource type.
        self.resource_type_name = resource_type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_keys is not None:
            result['FilterKeys'] = self.filter_keys
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_type_name is not None:
            result['ResourceTypeName'] = self.resource_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterKeys') is not None:
            self.filter_keys = m.get('FilterKeys')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceTypeName') is not None:
            self.resource_type_name = m.get('ResourceTypeName')
        return self


class ListResourceTypesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_types: List[ListResourceTypesResponseBodyResourceTypes] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the resource types.
        self.resource_types = resource_types

    def validate(self):
        if self.resource_types:
            for k in self.resource_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceTypes'] = []
        if self.resource_types is not None:
            for k in self.resource_types:
                result['ResourceTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_types = []
        if m.get('ResourceTypes') is not None:
            for k in m.get('ResourceTypes'):
                temp_model = ListResourceTypesResponseBodyResourceTypes()
                self.resource_types.append(temp_model.from_map(k))
        return self


class ListResourceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceTypesResponseBody = None,
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
            temp_model = ListResourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        max_results: int = None,
        next_token: str = None,
        tag_key: str = None,
    ):
        # The matching mode. Valid values:
        # 
        # *   Equals: equal match
        # *   Prefix: match by prefix
        self.match_type = match_type
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the `token` to initiate another request and obtain the remaining entries.
        self.next_token = next_token
        # The tag key.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_keys: List[str] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The tag keys.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
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


class ListTagValuesRequest(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        max_results: int = None,
        next_token: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The matching mode. Valid values:
        # 
        # *   Equals: equal match
        # *   Prefix: match by prefix
        self.match_type = match_type
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the `token` to initiate another request and obtain the remaining entries.
        self.next_token = next_token
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_values: List[str] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The tag values.
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
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


class SearchMultiAccountResourcesRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: List[str] = None,
    ):
        # The key of the filter condition. For more information, see `Supported filter parameters`.
        self.key = key
        # The matching mode.
        # 
        # The value Equals indicates an equal match.
        self.match_type = match_type
        # The values of the filter condition.
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
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchMultiAccountResourcesRequestSortCriterion(TeaModel):
    def __init__(
        self,
        key: str = None,
        order: str = None,
    ):
        # The attribute based on which the entries are sorted.
        # 
        # The value CreateTime indicates the creation time of resources.
        self.key = key
        # The order in which the entries are sorted. Valid values:
        # 
        # *   ASC: The entries are sorted in ascending order. This value is the default value.
        # *   DESC: The entries are sorted in descending order.
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class SearchMultiAccountResourcesRequest(TeaModel):
    def __init__(
        self,
        filter: List[SearchMultiAccountResourcesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        scope: str = None,
        sort_criterion: SearchMultiAccountResourcesRequestSortCriterion = None,
    ):
        # The filter conditions.
        self.filter = filter
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the token to initiate another request and obtain the remaining entries.``
        self.next_token = next_token
        # The search scope. You can set the value to one of the following items:
        # 
        # *   ID of a resource directory: Resources within the management account and all members of the resource directory are searched. You can call the [GetResourceDirectory](~~159995~~) operation to obtain the ID.
        # *   ID of the Root folder: Resources within all members in the Root folder and the subfolders of the Root folder are searched. You can call the [ListFoldersForParent](~~159997~~) operation to obtain the ID.
        # *   ID of a folder: Resources within all members in the folder are searched. You can call the [ListFoldersForParent](~~159997~~) operation to obtain the ID.
        # *   ID of a member: Resources within the member are searched. You can call the [ListAccounts](~~160016~~) operation to obtain the ID.
        self.scope = scope
        # The method that is used to sort the entries returned.
        self.sort_criterion = sort_criterion

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.sort_criterion:
            self.sort_criterion.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.sort_criterion is not None:
            result['SortCriterion'] = self.sort_criterion.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = SearchMultiAccountResourcesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SortCriterion') is not None:
            temp_model = SearchMultiAccountResourcesRequestSortCriterion()
            self.sort_criterion = temp_model.from_map(m['SortCriterion'])
        return self


class SearchMultiAccountResourcesResponseBodyFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        values: List[str] = None,
    ):
        # The key of the filter condition.
        self.key = key
        # The matching mode.
        self.match_type = match_type
        # The values of the filter condition.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class SearchMultiAccountResourcesResponseBodyResourcesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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


class SearchMultiAccountResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_time: str = None,
        ip_addresses: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tags: List[SearchMultiAccountResourcesResponseBodyResourcesTags] = None,
        zone_id: str = None,
    ):
        # The ID of the management account or member of the resource directory.
        self.account_id = account_id
        # The time when the resource was created.
        # 
        # > Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.create_time = create_time
        # The IP addresses.
        # 
        # > Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.ip_addresses = ip_addresses
        # The region ID of the resource.
        self.region_id = region_id
        # The ID of the resource group to which the resource belongs.
        self.resource_group_id = resource_group_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The name of the resource.
        self.resource_name = resource_name
        # The type of the resource.
        self.resource_type = resource_type
        # The tags of the resource.
        self.tags = tags
        # The zone ID of the resource.
        # 
        # > Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.zone_id = zone_id

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
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses
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
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')
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
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = SearchMultiAccountResourcesResponseBodyResourcesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class SearchMultiAccountResourcesResponseBody(TeaModel):
    def __init__(
        self,
        filters: List[SearchMultiAccountResourcesResponseBodyFilters] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resources: List[SearchMultiAccountResourcesResponseBodyResources] = None,
        scope: str = None,
    ):
        # The filter conditions.
        self.filters = filters
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information about the resources.
        self.resources = resources
        # The search scope.
        # 
        # *   ID of a resource directory: Resources within the management account and all members of the resource directory are searched.
        # *   ID of the Root folder: Resources within all members in the Root folder and the subfolders of the Root folder are searched.
        # *   ID of a folder: Resources within all members in the folder are searched.
        # *   ID of a member: Resources within the member are searched.
        self.scope = scope

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = SearchMultiAccountResourcesResponseBodyFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = SearchMultiAccountResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class SearchMultiAccountResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchMultiAccountResourcesResponseBody = None,
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
            temp_model = SearchMultiAccountResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchResourcesRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: List[str] = None,
    ):
        # The key of the filter condition. For more information, see `Supported filter parameters`.
        self.key = key
        # The matching mode.
        # 
        # The value Equals indicates an equal match.
        self.match_type = match_type
        # The values of the filter condition.
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
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchResourcesRequestSortCriterion(TeaModel):
    def __init__(
        self,
        key: str = None,
        order: str = None,
    ):
        # The attribute based on which the entries are sorted.
        # 
        # The value CreateTime indicates the creation time of resources.
        self.key = key
        # The order in which the entries are sorted. Valid values:
        # 
        # *   ASC: The entries are sorted in ascending order. This value is the default value.
        # *   DESC: The entries are sorted in descending order.
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class SearchResourcesRequest(TeaModel):
    def __init__(
        self,
        filter: List[SearchResourcesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        sort_criterion: SearchResourcesRequestSortCriterion = None,
    ):
        # The filter conditions.
        self.filter = filter
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the `token` to initiate another request and obtain the remaining entries.
        self.next_token = next_token
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The method that is used to sort the entries returned.
        self.sort_criterion = sort_criterion

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.sort_criterion:
            self.sort_criterion.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sort_criterion is not None:
            result['SortCriterion'] = self.sort_criterion.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = SearchResourcesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SortCriterion') is not None:
            temp_model = SearchResourcesRequestSortCriterion()
            self.sort_criterion = temp_model.from_map(m['SortCriterion'])
        return self


class SearchResourcesResponseBodyFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        values: List[str] = None,
    ):
        # The key of the filter condition.
        self.key = key
        # The matching mode.
        self.match_type = match_type
        # The values of the filter condition.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class SearchResourcesResponseBodyResourcesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class SearchResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_time: str = None,
        ip_addresses: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tags: List[SearchResourcesResponseBodyResourcesTags] = None,
        zone_id: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.account_id = account_id
        # The time when the resource was created.
        # 
        # > Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.create_time = create_time
        # The IP addresses.
        # 
        # > Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.ip_addresses = ip_addresses
        # The region ID of the resource.
        self.region_id = region_id
        # The ID of the resource group to which the resource belongs.
        self.resource_group_id = resource_group_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The name of the resource.
        self.resource_name = resource_name
        # The type of the resource.
        self.resource_type = resource_type
        # The tags of the resource.
        self.tags = tags
        # The zone ID of the resource.
        # 
        # > Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.zone_id = zone_id

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
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses
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
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')
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
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = SearchResourcesResponseBodyResourcesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class SearchResourcesResponseBody(TeaModel):
    def __init__(
        self,
        filters: List[SearchResourcesResponseBodyFilters] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resources: List[SearchResourcesResponseBodyResources] = None,
    ):
        # The filter conditions.
        self.filters = filters
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information about the resources.
        self.resources = resources

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
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
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = SearchResourcesResponseBodyFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = SearchResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class SearchResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchResourcesResponseBody = None,
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
            temp_model = SearchResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


