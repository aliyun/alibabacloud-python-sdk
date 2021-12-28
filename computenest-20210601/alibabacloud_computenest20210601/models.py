# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class ContinueDeployServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        parameters: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        self.client_token = client_token
        self.parameters = parameters
        self.region_id = region_id
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class ContinueDeployServiceInstanceResponseBody(TeaModel):
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


class ContinueDeployServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ContinueDeployServiceInstanceResponseBody = None,
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
            temp_model = ContinueDeployServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceInstanceRequestOperationMetadata(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        resources: str = None,
        service_instance_id: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.resources = resources
        self.service_instance_id = service_instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateServiceInstanceRequestRequestTag(TeaModel):
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


class CreateServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        enable_account_ops: bool = None,
        enable_instance_ops: bool = None,
        operation_metadata: CreateServiceInstanceRequestOperationMetadata = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        request_tag: List[CreateServiceInstanceRequestRequestTag] = None,
        resource_group_id: str = None,
        service_id: str = None,
        service_version: str = None,
        template_name: str = None,
    ):
        self.client_token = client_token
        self.enable_account_ops = enable_account_ops
        self.enable_instance_ops = enable_instance_ops
        self.operation_metadata = operation_metadata
        self.parameters = parameters
        self.region_id = region_id
        self.request_tag = request_tag
        self.resource_group_id = resource_group_id
        self.service_id = service_id
        self.service_version = service_version
        self.template_name = template_name

    def validate(self):
        if self.operation_metadata:
            self.operation_metadata.validate()
        if self.request_tag:
            for k in self.request_tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.enable_account_ops is not None:
            result['EnableAccountOps'] = self.enable_account_ops
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.operation_metadata is not None:
            result['OperationMetadata'] = self.operation_metadata.to_map()
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['RequestTag'] = []
        if self.request_tag is not None:
            for k in self.request_tag:
                result['RequestTag'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EnableAccountOps') is not None:
            self.enable_account_ops = m.get('EnableAccountOps')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('OperationMetadata') is not None:
            temp_model = CreateServiceInstanceRequestOperationMetadata()
            self.operation_metadata = temp_model.from_map(m['OperationMetadata'])
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.request_tag = []
        if m.get('RequestTag') is not None:
            for k in m.get('RequestTag'):
                temp_model = CreateServiceInstanceRequestRequestTag()
                self.request_tag.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class CreateServiceInstanceShrinkRequestOperationMetadata(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        resources: str = None,
        service_instance_id: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.resources = resources
        self.service_instance_id = service_instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateServiceInstanceShrinkRequestRequestTag(TeaModel):
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


class CreateServiceInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        enable_account_ops: bool = None,
        enable_instance_ops: bool = None,
        operation_metadata: CreateServiceInstanceShrinkRequestOperationMetadata = None,
        parameters_shrink: str = None,
        region_id: str = None,
        request_tag: List[CreateServiceInstanceShrinkRequestRequestTag] = None,
        resource_group_id: str = None,
        service_id: str = None,
        service_version: str = None,
        template_name: str = None,
    ):
        self.client_token = client_token
        self.enable_account_ops = enable_account_ops
        self.enable_instance_ops = enable_instance_ops
        self.operation_metadata = operation_metadata
        self.parameters_shrink = parameters_shrink
        self.region_id = region_id
        self.request_tag = request_tag
        self.resource_group_id = resource_group_id
        self.service_id = service_id
        self.service_version = service_version
        self.template_name = template_name

    def validate(self):
        if self.operation_metadata:
            self.operation_metadata.validate()
        if self.request_tag:
            for k in self.request_tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.enable_account_ops is not None:
            result['EnableAccountOps'] = self.enable_account_ops
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.operation_metadata is not None:
            result['OperationMetadata'] = self.operation_metadata.to_map()
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['RequestTag'] = []
        if self.request_tag is not None:
            for k in self.request_tag:
                result['RequestTag'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EnableAccountOps') is not None:
            self.enable_account_ops = m.get('EnableAccountOps')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('OperationMetadata') is not None:
            temp_model = CreateServiceInstanceShrinkRequestOperationMetadata()
            self.operation_metadata = temp_model.from_map(m['OperationMetadata'])
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.request_tag = []
        if m.get('RequestTag') is not None:
            for k in m.get('RequestTag'):
                temp_model = CreateServiceInstanceShrinkRequestRequestTag()
                self.request_tag.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class CreateServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_instance_id: str = None,
        status: str = None,
    ):
        self.request_id = request_id
        self.service_instance_id = service_instance_id
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
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServiceInstanceResponseBody = None,
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
            temp_model = CreateServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceInstancesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_instance_id: List[str] = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class DeleteServiceInstancesResponseBody(TeaModel):
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


class DeleteServiceInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteServiceInstancesResponseBody = None,
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
            temp_model = DeleteServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        self.region_id = region_id
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class GetServiceInstanceResponseBodyServiceServiceInfos(TeaModel):
    def __init__(
        self,
        image: str = None,
        locale: str = None,
        name: str = None,
        short_description: str = None,
    ):
        self.image = image
        self.locale = locale
        self.name = name
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class GetServiceInstanceResponseBodyService(TeaModel):
    def __init__(
        self,
        deploy_metadata: str = None,
        deploy_type: str = None,
        publish_time: str = None,
        service_id: str = None,
        service_infos: List[GetServiceInstanceResponseBodyServiceServiceInfos] = None,
        service_type: str = None,
        status: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        version: str = None,
    ):
        self.deploy_metadata = deploy_metadata
        self.deploy_type = deploy_type
        self.publish_time = publish_time
        self.service_id = service_id
        self.service_infos = service_infos
        self.service_type = service_type
        self.status = status
        self.supplier_name = supplier_name
        self.supplier_url = supplier_url
        self.version = version

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
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = GetServiceInstanceResponseBodyServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        enable_instance_ops: bool = None,
        is_operated: bool = None,
        operated_service_instance_id: str = None,
        operation_end_time: str = None,
        operation_start_time: str = None,
        outputs: str = None,
        parameters: str = None,
        progress: int = None,
        request_id: str = None,
        resources: str = None,
        service: GetServiceInstanceResponseBodyService = None,
        service_instance_id: str = None,
        status: str = None,
        status_detail: str = None,
        template_name: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.enable_instance_ops = enable_instance_ops
        self.is_operated = is_operated
        self.operated_service_instance_id = operated_service_instance_id
        self.operation_end_time = operation_end_time
        self.operation_start_time = operation_start_time
        self.outputs = outputs
        self.parameters = parameters
        self.progress = progress
        self.request_id = request_id
        self.resources = resources
        self.service = service
        self.service_instance_id = service_instance_id
        self.status = status
        self.status_detail = status_detail
        self.template_name = template_name
        self.update_time = update_time

    def validate(self):
        if self.service:
            self.service.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.is_operated is not None:
            result['IsOperated'] = self.is_operated
        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service is not None:
            result['Service'] = self.service.to_map()
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('IsOperated') is not None:
            self.is_operated = m.get('IsOperated')
        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Service') is not None:
            temp_model = GetServiceInstanceResponseBodyService()
            self.service = temp_model.from_map(m['Service'])
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
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


class ListServiceInstanceLogsRequest(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class ListServiceInstanceLogsResponseBodyServiceInstancesLogs(TeaModel):
    def __init__(
        self,
        content: str = None,
        phase: str = None,
        service_instance_id: str = None,
        source: str = None,
        timestamp: str = None,
    ):
        self.content = content
        self.phase = phase
        self.service_instance_id = service_instance_id
        self.source = source
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.source is not None:
            result['Source'] = self.source
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class ListServiceInstanceLogsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        service_instances_logs: List[ListServiceInstanceLogsResponseBodyServiceInstancesLogs] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.service_instances_logs = service_instances_logs

    def validate(self):
        if self.service_instances_logs:
            for k in self.service_instances_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceInstancesLogs'] = []
        if self.service_instances_logs is not None:
            for k in self.service_instances_logs:
                result['ServiceInstancesLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_instances_logs = []
        if m.get('ServiceInstancesLogs') is not None:
            for k in m.get('ServiceInstancesLogs'):
                temp_model = ListServiceInstanceLogsResponseBodyServiceInstancesLogs()
                self.service_instances_logs.append(temp_model.from_map(k))
        return self


class ListServiceInstanceLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServiceInstanceLogsResponseBody = None,
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
            temp_model = ListServiceInstanceLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstanceResourcesRequest(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        service_instance_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class ListServiceInstanceResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        resource_arn: str = None,
    ):
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        return self


class ListServiceInstanceResourcesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        resources: List[ListServiceInstanceResourcesResponseBodyResources] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
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
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListServiceInstanceResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListServiceInstanceResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServiceInstanceResourcesResponseBody = None,
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
            temp_model = ListServiceInstanceResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstancesRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListServiceInstancesRequestRequestTag(TeaModel):
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


class ListServiceInstancesRequest(TeaModel):
    def __init__(
        self,
        filter: List[ListServiceInstancesRequestFilter] = None,
        max_results: str = None,
        next_token: str = None,
        region_id: str = None,
        request_tag: List[ListServiceInstancesRequestRequestTag] = None,
    ):
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.request_tag = request_tag

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.request_tag:
            for k in self.request_tag:
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['RequestTag'] = []
        if self.request_tag is not None:
            for k in self.request_tag:
                result['RequestTag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServiceInstancesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.request_tag = []
        if m.get('RequestTag') is not None:
            for k in m.get('RequestTag'):
                temp_model = ListServiceInstancesRequestRequestTag()
                self.request_tag.append(temp_model.from_map(k))
        return self


class ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos(TeaModel):
    def __init__(
        self,
        image: str = None,
        locale: str = None,
        name: str = None,
        short_description: str = None,
    ):
        self.image = image
        self.locale = locale
        self.name = name
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class ListServiceInstancesResponseBodyServiceInstancesService(TeaModel):
    def __init__(
        self,
        deploy_type: str = None,
        publish_time: str = None,
        service_id: str = None,
        service_infos: List[ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos] = None,
        service_type: str = None,
        status: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        version: str = None,
    ):
        self.deploy_type = deploy_type
        self.publish_time = publish_time
        self.service_id = service_id
        self.service_infos = service_infos
        self.service_type = service_type
        self.status = status
        self.supplier_name = supplier_name
        self.supplier_url = supplier_url
        self.version = version

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
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListServiceInstancesResponseBodyServiceInstances(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        enable_instance_ops: bool = None,
        operated_service_instance_id: str = None,
        operation_end_time: str = None,
        operation_start_time: str = None,
        outputs: str = None,
        parameters: str = None,
        progress: int = None,
        resources: str = None,
        service: ListServiceInstancesResponseBodyServiceInstancesService = None,
        service_instance_id: str = None,
        status: str = None,
        status_detail: str = None,
        template_name: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.enable_instance_ops = enable_instance_ops
        self.operated_service_instance_id = operated_service_instance_id
        self.operation_end_time = operation_end_time
        self.operation_start_time = operation_start_time
        self.outputs = outputs
        self.parameters = parameters
        self.progress = progress
        self.resources = resources
        self.service = service
        self.service_instance_id = service_instance_id
        self.status = status
        self.status_detail = status_detail
        self.template_name = template_name
        self.update_time = update_time

    def validate(self):
        if self.service:
            self.service.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service is not None:
            result['Service'] = self.service.to_map()
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Service') is not None:
            temp_model = ListServiceInstancesResponseBodyServiceInstancesService()
            self.service = temp_model.from_map(m['Service'])
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListServiceInstancesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        service_instances: List[ListServiceInstancesResponseBodyServiceInstances] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.service_instances = service_instances
        self.total_count = total_count

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceInstances'] = []
        if self.service_instances is not None:
            for k in self.service_instances:
                result['ServiceInstances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_instances = []
        if m.get('ServiceInstances') is not None:
            for k in m.get('ServiceInstances'):
                temp_model = ListServiceInstancesResponseBodyServiceInstances()
                self.service_instances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


