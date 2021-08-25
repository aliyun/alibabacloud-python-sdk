# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CancelServiceRegistrationRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        registration_id: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.registration_id = registration_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CancelServiceRegistrationResponseBody(TeaModel):
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


class CancelServiceRegistrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelServiceRegistrationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CancelServiceRegistrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequestServiceInfo(TeaModel):
    def __init__(
        self,
        locale: str = None,
        short_description: str = None,
        image: str = None,
        name: str = None,
    ):
        self.locale = locale
        self.short_description = short_description
        self.image = image
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateServiceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        client_token: str = None,
        service_id: str = None,
        deploy_type: str = None,
        deploy_metadata: str = None,
        service_type: str = None,
        service_info: List[CreateServiceRequestServiceInfo] = None,
    ):
        self.region_id = region_id
        self.supplier_name = supplier_name
        self.supplier_url = supplier_url
        self.client_token = client_token
        self.service_id = service_id
        self.deploy_type = deploy_type
        self.deploy_metadata = deploy_metadata
        self.service_type = service_type
        self.service_info = service_info

    def validate(self):
        if self.service_info:
            for k in self.service_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        result['ServiceInfo'] = []
        if self.service_info is not None:
            for k in self.service_info:
                result['ServiceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        self.service_info = []
        if m.get('ServiceInfo') is not None:
            for k in m.get('ServiceInfo'):
                temp_model = CreateServiceRequestServiceInfo()
                self.service_info.append(temp_model.from_map(k))
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
        version: str = None,
        service_id: str = None,
    ):
        self.status = status
        self.request_id = request_id
        self.version = version
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.service_id = service_id
        self.service_version = service_version
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class DeleteServiceResponseBody(TeaModel):
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


class DeleteServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
    ):
        self.region_id = region_id
        self.service_id = service_id
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class GetServiceResponseBodyServiceInfos(TeaModel):
    def __init__(
        self,
        locale: str = None,
        image: str = None,
        name: str = None,
        short_description: str = None,
    ):
        self.locale = locale
        self.image = image
        self.name = name
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class GetServiceResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        deploy_metadata: str = None,
        publish_time: str = None,
        request_id: str = None,
        version: str = None,
        deploy_type: str = None,
        service_id: str = None,
        supplier_url: str = None,
        service_type: str = None,
        supplier_name: str = None,
        service_infos: List[GetServiceResponseBodyServiceInfos] = None,
        commodity_code: str = None,
    ):
        self.status = status
        self.deploy_metadata = deploy_metadata
        self.publish_time = publish_time
        self.request_id = request_id
        self.version = version
        self.deploy_type = deploy_type
        self.service_id = service_id
        self.supplier_url = supplier_url
        self.service_type = service_type
        self.supplier_name = supplier_name
        self.service_infos = service_infos
        self.commodity_code = commodity_code

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = GetServiceResponseBodyServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        return self


class GetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        service_instance_id: str = None,
        region_id: str = None,
    ):
        self.service_instance_id = service_instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetServiceInstanceResponseBodyServiceServiceInfos(TeaModel):
    def __init__(
        self,
        locale: str = None,
        image: str = None,
        name: str = None,
        short_description: str = None,
    ):
        self.locale = locale
        self.image = image
        self.name = name
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class GetServiceInstanceResponseBodyService(TeaModel):
    def __init__(
        self,
        status: str = None,
        publish_time: str = None,
        version: str = None,
        deploy_type: str = None,
        service_id: str = None,
        supplier_url: str = None,
        service_type: str = None,
        supplier_name: str = None,
        service_infos: List[GetServiceInstanceResponseBodyServiceServiceInfos] = None,
        deploy_metadata: str = None,
    ):
        self.status = status
        self.publish_time = publish_time
        self.version = version
        self.deploy_type = deploy_type
        self.service_id = service_id
        self.supplier_url = supplier_url
        self.service_type = service_type
        self.supplier_name = supplier_name
        self.service_infos = service_infos
        self.deploy_metadata = deploy_metadata

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.version is not None:
            result['Version'] = self.version
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = GetServiceInstanceResponseBodyServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        return self


class GetServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_time: str = None,
        request_id: str = None,
        service_instance_id: str = None,
        create_time: str = None,
        user_id: int = None,
        service: GetServiceInstanceResponseBodyService = None,
        parameters: str = None,
        status_detail: str = None,
        progress: int = None,
        template_name: str = None,
    ):
        self.status = status
        self.update_time = update_time
        self.request_id = request_id
        self.service_instance_id = service_instance_id
        self.create_time = create_time
        self.user_id = user_id
        self.service = service
        self.parameters = parameters
        self.status_detail = status_detail
        self.progress = progress
        self.template_name = template_name

    def validate(self):
        if self.service:
            self.service.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.service is not None:
            result['Service'] = self.service.to_map()
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Service') is not None:
            temp_model = GetServiceInstanceResponseBodyService()
            self.service = temp_model.from_map(m['Service'])
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class GetServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetServiceInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSupplierInformationRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetSupplierInformationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        supplier_desc: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.supplier_name = supplier_name
        self.supplier_url = supplier_url
        self.supplier_desc = supplier_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.supplier_desc is not None:
            result['SupplierDesc'] = self.supplier_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('SupplierDesc') is not None:
            self.supplier_desc = m.get('SupplierDesc')
        return self


class GetSupplierInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSupplierInformationResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSupplierInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LaunchServiceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.service_id = service_id
        self.service_version = service_version
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class LaunchServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_id: str = None,
        version: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.service_id = service_id
        self.version = version
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
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.version is not None:
            result['Version'] = self.version
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class LaunchServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LaunchServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LaunchServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstancesRequestFilter(TeaModel):
    def __init__(
        self,
        value: List[str] = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListServiceInstancesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        max_results: str = None,
        next_token: str = None,
        filter: List[ListServiceInstancesRequestFilter] = None,
    ):
        self.region_id = region_id
        self.max_results = max_results
        self.next_token = next_token
        self.filter = filter

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServiceInstancesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        return self


class ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos(TeaModel):
    def __init__(
        self,
        locale: str = None,
        image: str = None,
        name: str = None,
        short_description: str = None,
    ):
        self.locale = locale
        self.image = image
        self.name = name
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class ListServiceInstancesResponseBodyServiceInstancesService(TeaModel):
    def __init__(
        self,
        status: str = None,
        publish_time: str = None,
        version: str = None,
        deploy_type: str = None,
        service_id: str = None,
        supplier_url: str = None,
        service_type: str = None,
        supplier_name: str = None,
        service_infos: List[ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos] = None,
    ):
        self.status = status
        self.publish_time = publish_time
        self.version = version
        self.deploy_type = deploy_type
        self.service_id = service_id
        self.supplier_url = supplier_url
        self.service_type = service_type
        self.supplier_name = supplier_name
        self.service_infos = service_infos

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.version is not None:
            result['Version'] = self.version
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        return self


class ListServiceInstancesResponseBodyServiceInstances(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_time: str = None,
        service_instance_id: str = None,
        create_time: str = None,
        user_id: int = None,
        service: ListServiceInstancesResponseBodyServiceInstancesService = None,
        parameters: str = None,
        status_detail: str = None,
        progress: int = None,
        template_name: str = None,
    ):
        self.status = status
        self.update_time = update_time
        self.service_instance_id = service_instance_id
        self.create_time = create_time
        self.user_id = user_id
        self.service = service
        self.parameters = parameters
        self.status_detail = status_detail
        self.progress = progress
        self.template_name = template_name

    def validate(self):
        if self.service:
            self.service.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.service is not None:
            result['Service'] = self.service.to_map()
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Service') is not None:
            temp_model = ListServiceInstancesResponseBodyServiceInstancesService()
            self.service = temp_model.from_map(m['Service'])
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListServiceInstancesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        max_results: str = None,
        service_instances: List[ListServiceInstancesResponseBodyServiceInstances] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.max_results = max_results
        self.service_instances = service_instances

    def validate(self):
        if self.service_instances:
            for k in self.service_instances:
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ServiceInstances'] = []
        if self.service_instances is not None:
            for k in self.service_instances:
                result['ServiceInstances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.service_instances = []
        if m.get('ServiceInstances') is not None:
            for k in m.get('ServiceInstances'):
                temp_model = ListServiceInstancesResponseBodyServiceInstances()
                self.service_instances.append(temp_model.from_map(k))
        return self


class ListServiceInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServiceInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceRegistrationsRequestFilter(TeaModel):
    def __init__(
        self,
        value: List[str] = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListServiceRegistrationsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        max_results: str = None,
        next_token: str = None,
        filter: List[ListServiceRegistrationsRequestFilter] = None,
    ):
        self.region_id = region_id
        self.max_results = max_results
        self.next_token = next_token
        self.filter = filter

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServiceRegistrationsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        return self


class ListServiceRegistrationsResponseBodyServiceRegistrations(TeaModel):
    def __init__(
        self,
        status: str = None,
        registration_id: str = None,
        finish_time: str = None,
        comment: str = None,
        service_id: str = None,
        submit_time: str = None,
    ):
        self.status = status
        self.registration_id = registration_id
        self.finish_time = finish_time
        self.comment = comment
        self.service_id = service_id
        self.submit_time = submit_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        return self


class ListServiceRegistrationsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
        max_results: int = None,
        service_registrations: List[ListServiceRegistrationsResponseBodyServiceRegistrations] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.max_results = max_results
        self.service_registrations = service_registrations

    def validate(self):
        if self.service_registrations:
            for k in self.service_registrations:
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ServiceRegistrations'] = []
        if self.service_registrations is not None:
            for k in self.service_registrations:
                result['ServiceRegistrations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.service_registrations = []
        if m.get('ServiceRegistrations') is not None:
            for k in m.get('ServiceRegistrations'):
                temp_model = ListServiceRegistrationsResponseBodyServiceRegistrations()
                self.service_registrations.append(temp_model.from_map(k))
        return self


class ListServiceRegistrationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServiceRegistrationsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListServiceRegistrationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequestFilter(TeaModel):
    def __init__(
        self,
        value: List[str] = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListServicesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        max_results: str = None,
        next_token: str = None,
        all_versions: bool = None,
        filter: List[ListServicesRequestFilter] = None,
    ):
        self.region_id = region_id
        self.max_results = max_results
        self.next_token = next_token
        self.all_versions = all_versions
        self.filter = filter

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.all_versions is not None:
            result['AllVersions'] = self.all_versions
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('AllVersions') is not None:
            self.all_versions = m.get('AllVersions')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServicesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        return self


class ListServicesResponseBodyServicesServiceInfos(TeaModel):
    def __init__(
        self,
        locale: str = None,
        image: str = None,
        name: str = None,
        short_description: str = None,
    ):
        self.locale = locale
        self.image = image
        self.name = name
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class ListServicesResponseBodyServices(TeaModel):
    def __init__(
        self,
        status: str = None,
        default_version: bool = None,
        publish_time: str = None,
        version: str = None,
        deploy_type: str = None,
        service_id: str = None,
        supplier_url: str = None,
        service_type: str = None,
        supplier_name: str = None,
        service_infos: List[ListServicesResponseBodyServicesServiceInfos] = None,
        commodity_code: str = None,
    ):
        self.status = status
        self.default_version = default_version
        self.publish_time = publish_time
        self.version = version
        self.deploy_type = deploy_type
        self.service_id = service_id
        self.supplier_url = supplier_url
        self.service_type = service_type
        self.supplier_name = supplier_name
        self.service_infos = service_infos
        self.commodity_code = commodity_code

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.version is not None:
            result['Version'] = self.version
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = ListServicesResponseBodyServicesServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
        max_results: int = None,
        services: List[ListServicesResponseBodyServices] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.max_results = max_results
        self.services = services

    def validate(self):
        if self.services:
            for k in self.services:
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterServiceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        service_id: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.service_id = service_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class RegisterServiceResponseBody(TeaModel):
    def __init__(
        self,
        registration_id: str = None,
        request_id: str = None,
    ):
        self.registration_id = registration_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.registration_id is not None:
            result['RegistrationId'] = self.registration_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegistrationId') is not None:
            self.registration_id = m.get('RegistrationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegisterServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RegisterServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceRequestServiceInfo(TeaModel):
    def __init__(
        self,
        locale: str = None,
        short_description: str = None,
        image: str = None,
        name: str = None,
    ):
        self.locale = locale
        self.short_description = short_description
        self.image = image
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        deploy_type: str = None,
        deploy_metadata: str = None,
        client_token: str = None,
        service_id: str = None,
        service_type: str = None,
        service_info: List[UpdateServiceRequestServiceInfo] = None,
    ):
        self.region_id = region_id
        self.supplier_name = supplier_name
        self.supplier_url = supplier_url
        self.deploy_type = deploy_type
        self.deploy_metadata = deploy_metadata
        self.client_token = client_token
        self.service_id = service_id
        self.service_type = service_type
        self.service_info = service_info

    def validate(self):
        if self.service_info:
            for k in self.service_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        result['ServiceInfo'] = []
        if self.service_info is not None:
            for k in self.service_info:
                result['ServiceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        self.service_info = []
        if m.get('ServiceInfo') is not None:
            for k in m.get('ServiceInfo'):
                temp_model = UpdateServiceRequestServiceInfo()
                self.service_info.append(temp_model.from_map(k))
        return self


class UpdateServiceResponseBody(TeaModel):
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


class UpdateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WithdrawServiceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
        client_token: str = None,
    ):
        self.region_id = region_id
        self.service_id = service_id
        self.service_version = service_version
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class WithdrawServiceResponseBody(TeaModel):
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


class WithdrawServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WithdrawServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = WithdrawServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


