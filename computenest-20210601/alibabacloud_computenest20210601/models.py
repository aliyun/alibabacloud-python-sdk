# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


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
        deploy_metadata: str = None,
        deploy_type: str = None,
        service_id: str = None,
        supplier_url: str = None,
        service_type: str = None,
        supplier_name: str = None,
        service_infos: List[GetServiceInstanceResponseBodyServiceServiceInfos] = None,
    ):
        self.status = status
        self.publish_time = publish_time
        self.version = version
        self.deploy_metadata = deploy_metadata
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
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
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
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
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
        return self


class GetServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        outputs: str = None,
        status: str = None,
        template_name: str = None,
        update_time: str = None,
        progress: int = None,
        parameters: str = None,
        request_id: str = None,
        service_instance_id: str = None,
        create_time: str = None,
        status_detail: str = None,
        resources: str = None,
        service: GetServiceInstanceResponseBodyService = None,
        operation_start_time: str = None,
        operation_end_time: str = None,
        operated_service_instance_id: str = None,
        enable_instance_ops: bool = None,
        is_operated: bool = None,
    ):
        self.outputs = outputs
        self.status = status
        self.template_name = template_name
        self.update_time = update_time
        self.progress = progress
        self.parameters = parameters
        self.request_id = request_id
        self.service_instance_id = service_instance_id
        self.create_time = create_time
        self.status_detail = status_detail
        self.resources = resources
        self.service = service
        self.operation_start_time = operation_start_time
        self.operation_end_time = operation_end_time
        self.operated_service_instance_id = operated_service_instance_id
        self.enable_instance_ops = enable_instance_ops
        self.is_operated = is_operated

    def validate(self):
        if self.service:
            self.service.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.status is not None:
            result['Status'] = self.status
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service is not None:
            result['Service'] = self.service.to_map()
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.is_operated is not None:
            result['IsOperated'] = self.is_operated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Service') is not None:
            temp_model = GetServiceInstanceResponseBodyService()
            self.service = temp_model.from_map(m['Service'])
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('IsOperated') is not None:
            self.is_operated = m.get('IsOperated')
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
        region_id: str = None,
        max_results: str = None,
        next_token: str = None,
        service_instance_id: str = None,
    ):
        self.region_id = region_id
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class ListServiceInstanceLogsResponseBodyServiceInstancesLogs(TeaModel):
    def __init__(
        self,
        timestamp: str = None,
        service_instance_id: str = None,
        source: str = None,
        phase: str = None,
        content: str = None,
    ):
        self.timestamp = timestamp
        self.service_instance_id = service_instance_id
        self.source = source
        self.phase = phase
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.source is not None:
            result['Source'] = self.source
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ListServiceInstanceLogsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        max_results: str = None,
        service_instances_logs: List[ListServiceInstanceLogsResponseBodyServiceInstancesLogs] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.max_results = max_results
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
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ServiceInstancesLogs'] = []
        if self.service_instances_logs is not None:
            for k in self.service_instances_logs:
                result['ServiceInstancesLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
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


class CreateServiceInstanceRequestOperationMetadata(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        resources: str = None,
        service_instance_id: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.resources = resources
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class CreateServiceInstanceRequestRequestTags(TeaModel):
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
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
        parameters: Dict[str, Any] = None,
        client_token: str = None,
        enable_instance_ops: bool = None,
        enable_account_ops: bool = None,
        template_name: str = None,
        operation_metadata: CreateServiceInstanceRequestOperationMetadata = None,
        request_tags: List[CreateServiceInstanceRequestRequestTags] = None,
    ):
        self.region_id = region_id
        self.service_id = service_id
        self.service_version = service_version
        self.parameters = parameters
        self.client_token = client_token
        self.enable_instance_ops = enable_instance_ops
        self.enable_account_ops = enable_account_ops
        self.template_name = template_name
        self.operation_metadata = operation_metadata
        self.request_tags = request_tags

    def validate(self):
        if self.operation_metadata:
            self.operation_metadata.validate()
        if self.request_tags:
            for k in self.request_tags:
                if k:
                    k.validate()

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
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.enable_account_ops is not None:
            result['EnableAccountOps'] = self.enable_account_ops
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.operation_metadata is not None:
            result['OperationMetadata'] = self.operation_metadata.to_map()
        result['RequestTags'] = []
        if self.request_tags is not None:
            for k in self.request_tags:
                result['RequestTags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('EnableAccountOps') is not None:
            self.enable_account_ops = m.get('EnableAccountOps')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('OperationMetadata') is not None:
            temp_model = CreateServiceInstanceRequestOperationMetadata()
            self.operation_metadata = temp_model.from_map(m['OperationMetadata'])
        self.request_tags = []
        if m.get('RequestTags') is not None:
            for k in m.get('RequestTags'):
                temp_model = CreateServiceInstanceRequestRequestTags()
                self.request_tags.append(temp_model.from_map(k))
        return self


class CreateServiceInstanceShrinkRequestOperationMetadata(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        resources: str = None,
        service_instance_id: str = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.resources = resources
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class CreateServiceInstanceShrinkRequestRequestTags(TeaModel):
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
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
        parameters_shrink: str = None,
        client_token: str = None,
        enable_instance_ops: bool = None,
        enable_account_ops: bool = None,
        template_name: str = None,
        operation_metadata: CreateServiceInstanceShrinkRequestOperationMetadata = None,
        request_tags: List[CreateServiceInstanceShrinkRequestRequestTags] = None,
    ):
        self.region_id = region_id
        self.service_id = service_id
        self.service_version = service_version
        self.parameters_shrink = parameters_shrink
        self.client_token = client_token
        self.enable_instance_ops = enable_instance_ops
        self.enable_account_ops = enable_account_ops
        self.template_name = template_name
        self.operation_metadata = operation_metadata
        self.request_tags = request_tags

    def validate(self):
        if self.operation_metadata:
            self.operation_metadata.validate()
        if self.request_tags:
            for k in self.request_tags:
                if k:
                    k.validate()

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
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.enable_account_ops is not None:
            result['EnableAccountOps'] = self.enable_account_ops
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.operation_metadata is not None:
            result['OperationMetadata'] = self.operation_metadata.to_map()
        result['RequestTags'] = []
        if self.request_tags is not None:
            for k in self.request_tags:
                result['RequestTags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('EnableAccountOps') is not None:
            self.enable_account_ops = m.get('EnableAccountOps')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('OperationMetadata') is not None:
            temp_model = CreateServiceInstanceShrinkRequestOperationMetadata()
            self.operation_metadata = temp_model.from_map(m['OperationMetadata'])
        self.request_tags = []
        if m.get('RequestTags') is not None:
            for k in m.get('RequestTags'):
                temp_model = CreateServiceInstanceShrinkRequestRequestTags()
                self.request_tags.append(temp_model.from_map(k))
        return self


class CreateServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
        service_instance_id: str = None,
    ):
        self.status = status
        self.request_id = request_id
        self.service_instance_id = service_instance_id

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
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
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


class ContinueDeployServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        service_instance_id: str = None,
        region_id: str = None,
        parameters: str = None,
    ):
        self.client_token = client_token
        self.service_instance_id = service_instance_id
        self.region_id = region_id
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
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


class DisableOperationServiceInstanceRequest(TeaModel):
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


class DisableOperationServiceInstanceResponseBody(TeaModel):
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


class DisableOperationServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableOperationServiceInstanceResponseBody = None,
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
            temp_model = DisableOperationServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        service_instance_id: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.service_instance_id = service_instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeployServiceInstanceResponseBody(TeaModel):
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


class DeployServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeployServiceInstanceResponseBody = None,
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
            temp_model = DeployServiceInstanceResponseBody()
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


class ListServiceInstancesRequestRequestTags(TeaModel):
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
        region_id: str = None,
        max_results: str = None,
        next_token: str = None,
        filter: List[ListServiceInstancesRequestFilter] = None,
        request_tags: List[ListServiceInstancesRequestRequestTags] = None,
    ):
        self.region_id = region_id
        self.max_results = max_results
        self.next_token = next_token
        self.filter = filter
        self.request_tags = request_tags

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.request_tags:
            for k in self.request_tags:
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
        result['RequestTags'] = []
        if self.request_tags is not None:
            for k in self.request_tags:
                result['RequestTags'].append(k.to_map() if k else None)
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
        self.request_tags = []
        if m.get('RequestTags') is not None:
            for k in m.get('RequestTags'):
                temp_model = ListServiceInstancesRequestRequestTags()
                self.request_tags.append(temp_model.from_map(k))
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
        outputs: str = None,
        update_time: str = None,
        parameters: str = None,
        service_instance_id: str = None,
        create_time: str = None,
        status_detail: str = None,
        progress: int = None,
        resources: str = None,
        template_name: str = None,
        operated_service_instance_id: str = None,
        service: ListServiceInstancesResponseBodyServiceInstancesService = None,
        operation_start_time: str = None,
        operation_end_time: str = None,
        enable_instance_ops: bool = None,
    ):
        self.status = status
        self.outputs = outputs
        self.update_time = update_time
        self.parameters = parameters
        self.service_instance_id = service_instance_id
        self.create_time = create_time
        self.status_detail = status_detail
        self.progress = progress
        self.resources = resources
        self.template_name = template_name
        self.operated_service_instance_id = operated_service_instance_id
        self.service = service
        self.operation_start_time = operation_start_time
        self.operation_end_time = operation_end_time
        self.enable_instance_ops = enable_instance_ops

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
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id
        if self.service is not None:
            result['Service'] = self.service.to_map()
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')
        if m.get('Service') is not None:
            temp_model = ListServiceInstancesResponseBodyServiceInstancesService()
            self.service = temp_model.from_map(m['Service'])
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
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


class ListPoliciesRequest(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        region_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListPoliciesResponseBodyPolicies(TeaModel):
    def __init__(
        self,
        description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        policy_document: str = None,
    ):
        self.description = description
        self.policy_name = policy_name
        self.policy_type = policy_type
        self.policy_document = policy_document

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        return self


class ListPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_token: str = None,
        policies: List[ListPoliciesResponseBodyPolicies] = None,
        max_results: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        # NextToken
        self.next_token = next_token
        self.policies = policies
        self.max_results = max_results

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPoliciesResponseBody = None,
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
            temp_model = ListPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInuseServicesRequestFilter(TeaModel):
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


class ListInuseServicesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        max_results: str = None,
        next_token: str = None,
        filter: List[ListInuseServicesRequestFilter] = None,
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
                temp_model = ListInuseServicesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        return self


class ListInuseServicesResponseBodyServicesServiceInfos(TeaModel):
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


class ListInuseServicesResponseBodyServices(TeaModel):
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
        service_infos: List[ListInuseServicesResponseBodyServicesServiceInfos] = None,
        commodity_code: str = None,
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
                temp_model = ListInuseServicesResponseBodyServicesServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        return self


class ListInuseServicesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
        max_results: str = None,
        services: List[ListInuseServicesResponseBodyServices] = None,
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
                temp_model = ListInuseServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        return self


class ListInuseServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInuseServicesResponseBody = None,
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
            temp_model = ListInuseServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
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


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableOperationServiceInstanceRequest(TeaModel):
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


class EnableOperationServiceInstanceResponseBody(TeaModel):
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


class EnableOperationServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableOperationServiceInstanceResponseBody = None,
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
            temp_model = EnableOperationServiceInstanceResponseBody()
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
        is_support_operated: bool = None,
        policy_names: str = None,
        duration: int = None,
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
        self.is_support_operated = is_support_operated
        self.policy_names = policy_names
        self.duration = duration

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
        if self.is_support_operated is not None:
            result['IsSupportOperated'] = self.is_support_operated
        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names
        if self.duration is not None:
            result['Duration'] = self.duration
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
        if m.get('IsSupportOperated') is not None:
            self.is_support_operated = m.get('IsSupportOperated')
        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
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


