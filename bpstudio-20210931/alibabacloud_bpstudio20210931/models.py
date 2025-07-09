# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AppFailBackRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
    ):
        # The application ID.
        self.application_id = application_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        return self


class AppFailBackResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # The disaster recovery switchback task ID.
        self.data = data
        # The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppFailBackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AppFailBackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AppFailBackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppFailOverRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        fail_zone: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The destination zone to which you want to switch the disaster recovery application.
        self.fail_zone = fail_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.fail_zone is not None:
            result['FailZone'] = self.fail_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('FailZone') is not None:
            self.fail_zone = m.get('FailZone')
        return self


class AppFailOverResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # The disaster recovery switchover task ID.
        self.data = data
        # The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppFailOverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AppFailOverResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AppFailOverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the new resource group.
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        # The ID of the resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource for which you want to change the resource group. Valid values: APPLICATION and TEMPLATE.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code. A value of 200 indicates that the request is successful. Other values indicate that the request failed.
        self.code = code
        # No business data is returned for this parameter.
        self.data = data
        # The error message returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequestInstances(TeaModel):
    def __init__(
        self,
        id: str = None,
        node_name: str = None,
        node_type: str = None,
    ):
        # The ID of the instance.
        self.id = id
        # The name of the instance.
        self.node_name = node_name
        # The type of the instance.
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(
        self,
        area_id: str = None,
        client_token: str = None,
        configuration: Dict[str, str] = None,
        instances: List[CreateApplicationRequestInstances] = None,
        name: str = None,
        process_variables: Dict[str, Any] = None,
        resource_group_id: str = None,
        template_id: str = None,
        variables: Dict[str, Any] = None,
    ):
        # The ID of the region.
        self.area_id = area_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The parameters that are used to configure the application you want to create. For example, enableMonitor specifies whether to automatically create a CloudMonitor task for the application, and enableReport specifies whether to generate reports.
        self.configuration = configuration
        # The instances in which you want to create the application. You can create applications in an existing virtual private cloud (VPC).
        self.instances = instances
        # The name of the application.
        # 
        # *   The application name must be unique. You can call the [ListApplication](https://www.alibabacloud.com/help/en/bp-studio/latest/api-bpstudio-2021-09-31-listapplication) operation to query the existing applications.
        # *   The application name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http:// or https://`. The name can contain letters, digits, underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.name = name
        self.process_variables = process_variables
        # The ID of the resource group to which the application you want to create belongs.
        self.resource_group_id = resource_group_id
        # The ID of the template.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The parameter values that are contained in the template. If the template contains no parameter values, the default values are used.
        self.variables = variables

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.process_variables is not None:
            result['ProcessVariables'] = self.process_variables
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.variables is not None:
            result['Variables'] = self.variables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = CreateApplicationRequestInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProcessVariables') is not None:
            self.process_variables = m.get('ProcessVariables')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        return self


class CreateApplicationShrinkRequest(TeaModel):
    def __init__(
        self,
        area_id: str = None,
        client_token: str = None,
        configuration_shrink: str = None,
        instances_shrink: str = None,
        name: str = None,
        process_variables_shrink: str = None,
        resource_group_id: str = None,
        template_id: str = None,
        variables_shrink: str = None,
    ):
        # The ID of the region.
        self.area_id = area_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The parameters that are used to configure the application you want to create. For example, enableMonitor specifies whether to automatically create a CloudMonitor task for the application, and enableReport specifies whether to generate reports.
        self.configuration_shrink = configuration_shrink
        # The instances in which you want to create the application. You can create applications in an existing virtual private cloud (VPC).
        self.instances_shrink = instances_shrink
        # The name of the application.
        # 
        # *   The application name must be unique. You can call the [ListApplication](https://www.alibabacloud.com/help/en/bp-studio/latest/api-bpstudio-2021-09-31-listapplication) operation to query the existing applications.
        # *   The application name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http:// or https://`. The name can contain letters, digits, underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.name = name
        self.process_variables_shrink = process_variables_shrink
        # The ID of the resource group to which the application you want to create belongs.
        self.resource_group_id = resource_group_id
        # The ID of the template.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The parameter values that are contained in the template. If the template contains no parameter values, the default values are used.
        self.variables_shrink = variables_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configuration_shrink is not None:
            result['Configuration'] = self.configuration_shrink
        if self.instances_shrink is not None:
            result['Instances'] = self.instances_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.process_variables_shrink is not None:
            result['ProcessVariables'] = self.process_variables_shrink
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.variables_shrink is not None:
            result['Variables'] = self.variables_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Configuration') is not None:
            self.configuration_shrink = m.get('Configuration')
        if m.get('Instances') is not None:
            self.instances_shrink = m.get('Instances')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProcessVariables') is not None:
            self.process_variables_shrink = m.get('ProcessVariables')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Variables') is not None:
            self.variables_shrink = m.get('Variables')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The ID of the application.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeleteApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        client_token: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DeployApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data of the application.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeployApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeployApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteOperationASyncRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        attributes: Dict[str, Any] = None,
        client_token: str = None,
        operation: str = None,
        resource_group_id: str = None,
        service_type: str = None,
    ):
        # The ID of the Cloud Architect Design Tools (CADT) application.
        self.application_id = application_id
        # The parameters related to the action. Specify the parameters based on the value of Operation. The parameters are passed in the map format. The following examples show how to specify the parameters if you want to change the specifications of an Elastic Compute Service (ECS) instance:
        # 
        # *   The following common parameters are required: change_type, regionId, instanceId, appId
        # *   Example values for changing the instance type of the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_instance_type","instance_type":"ecs.hfr7.2xlarge","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # *   Example values for stopping the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_status","status":"Stopped","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # *   Example values for starting the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_status","status":"Running","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # *   Example values for restarting the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_status","status":"Restart","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # 
        # Example of enumerating more than one set of parameters:
        # 
        # *   { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{\\\\"change_type\\\\":\\\\"modify_instance_type\\\\",\\\\"instance_type\\\\":\\\\"ecs.hfr7.2xlarge\\\\",\\\\"instanceId\\\\":\\\\"i-xxxxxxxxx\\\\",\\\\"regionId\\\\":\\\\"cn-beijing\\\\",\\\\"appId\\\\":\\\\"xxxxxxxxxxxxx\\\\"}" }
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{\\\\"change_type\\\\":\\\\"modify_instance_type\\\\",\\\\"instance_type\\\\":\\\\"ecs.hfr7.2xlarge\\\\",\\\\"instanceId\\\\":\\\\"i-xxxxxxxxx\\\\",\\\\"regionId\\\\":\\\\"cn-beijing\\\\",\\\\"appId\\\\":\\\\"xxxxxxxxxxxxx\\\\"}" }
        # 
        #     <!-- -->
        self.attributes = attributes
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # This operation type is the operation type of modifying the product, some operation types are generic, and some are used alone. The following is an example of ECS deployment:
        # - The name of the ECS: rename
        # - Specification of ecs: modifyInstanceType
        # - Startup of ecs: modifyInstanceType
        # - Stop of ecs: modifyInstanceType
        # - Restart of ecs: modifyInstanceType
        # - Ecs Tag: addTags
        # - Deletion of ecs: ecsDelete
        # - Paid type for ecs: modifyPayType
        # 
        # This parameter is required.
        self.operation = operation
        # Resource group ID, which is used to verify the permissions of the resource group
        self.resource_group_id = resource_group_id
        # The type of the service. If you want to perform operations on an Elastic Compute Service (ECS) instance, set ServiceType to ecs.
        # 
        # This parameter is required.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ExecuteOperationASyncShrinkRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        attributes_shrink: str = None,
        client_token: str = None,
        operation: str = None,
        resource_group_id: str = None,
        service_type: str = None,
    ):
        # The ID of the Cloud Architect Design Tools (CADT) application.
        self.application_id = application_id
        # The parameters related to the action. Specify the parameters based on the value of Operation. The parameters are passed in the map format. The following examples show how to specify the parameters if you want to change the specifications of an Elastic Compute Service (ECS) instance:
        # 
        # *   The following common parameters are required: change_type, regionId, instanceId, appId
        # *   Example values for changing the instance type of the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_instance_type","instance_type":"ecs.hfr7.2xlarge","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # *   Example values for stopping the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_status","status":"Stopped","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # *   Example values for starting the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_status","status":"Running","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # *   Example values for restarting the ECS instance: { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{"change_type":"modify_status","status":"Restart","instanceId":"i-xxxxxxxxx","regionId":"cn-beijing","appId":"xxxxxxxxxxxxx"}" }
        # 
        # Example of enumerating more than one set of parameters:
        # 
        # *   { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{\\\\"change_type\\\\":\\\\"modify_instance_type\\\\",\\\\"instance_type\\\\":\\\\"ecs.hfr7.2xlarge\\\\",\\\\"instanceId\\\\":\\\\"i-xxxxxxxxx\\\\",\\\\"regionId\\\\":\\\\"cn-beijing\\\\",\\\\"appId\\\\":\\\\"xxxxxxxxxxxxx\\\\"}" }
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     { "ServiceType": "ecs", "Operation": "modifyInstanceType", "Attributes": "{\\\\"change_type\\\\":\\\\"modify_instance_type\\\\",\\\\"instance_type\\\\":\\\\"ecs.hfr7.2xlarge\\\\",\\\\"instanceId\\\\":\\\\"i-xxxxxxxxx\\\\",\\\\"regionId\\\\":\\\\"cn-beijing\\\\",\\\\"appId\\\\":\\\\"xxxxxxxxxxxxx\\\\"}" }
        # 
        #     <!-- -->
        self.attributes_shrink = attributes_shrink
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # This operation type is the operation type of modifying the product, some operation types are generic, and some are used alone. The following is an example of ECS deployment:
        # - The name of the ECS: rename
        # - Specification of ecs: modifyInstanceType
        # - Startup of ecs: modifyInstanceType
        # - Stop of ecs: modifyInstanceType
        # - Restart of ecs: modifyInstanceType
        # - Ecs Tag: addTags
        # - Deletion of ecs: ecsDelete
        # - Paid type for ecs: modifyPayType
        # 
        # This parameter is required.
        self.operation = operation
        # Resource group ID, which is used to verify the permissions of the resource group
        self.resource_group_id = resource_group_id
        # The type of the service. If you want to perform operations on an Elastic Compute Service (ECS) instance, set ServiceType to ecs.
        # 
        # This parameter is required.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ExecuteOperationASyncResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # Result code, 200 for success; Other representatives fail.
        self.code = code
        # The operation ID. You can call the GetExecuteOperationResult operation to asynchronously query the result of an operation. The ID expires after one hour.
        self.data = data
        # Error message
        self.message = message
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExecuteOperationASyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteOperationASyncResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ExecuteOperationASyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteOperationSyncRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        attributes: Dict[str, Any] = None,
        client_token: str = None,
        operation: str = None,
        resource_group_id: str = None,
        service_type: str = None,
    ):
        self.application_id = application_id
        self.attributes = attributes
        self.client_token = client_token
        # This parameter is required.
        self.operation = operation
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ExecuteOperationSyncShrinkRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        attributes_shrink: str = None,
        client_token: str = None,
        operation: str = None,
        resource_group_id: str = None,
        service_type: str = None,
    ):
        self.application_id = application_id
        self.attributes_shrink = attributes_shrink
        self.client_token = client_token
        # This parameter is required.
        self.operation = operation
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.attributes_shrink is not None:
            result['Attributes'] = self.attributes_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Attributes') is not None:
            self.attributes_shrink = m.get('Attributes')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ExecuteOperationSyncResponseBodyData(TeaModel):
    def __init__(
        self,
        arguments: str = None,
        message: str = None,
        operation_id: str = None,
        status: str = None,
    ):
        self.arguments = arguments
        self.message = message
        self.operation_id = operation_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        if self.message is not None:
            result['Message'] = self.message
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ExecuteOperationSyncResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ExecuteOperationSyncResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ExecuteOperationSyncResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExecuteOperationSyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteOperationSyncResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ExecuteOperationSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the request.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetApplicationResponseBodyDataChecklist(TeaModel):
    def __init__(
        self,
        lifecycle: str = None,
        region: str = None,
        remark: str = None,
        resource_code: str = None,
        resource_name: str = None,
        result: str = None,
        specification: str = None,
    ):
        # The resource tag.
        self.lifecycle = lifecycle
        # The region in which the instance resides.
        self.region = region
        # The message returned for verification.
        self.remark = remark
        # The service code.
        self.resource_code = resource_code
        # The name of the instance.
        self.resource_name = resource_name
        # The verification result.
        self.result = result
        # The resource specifications.
        self.specification = specification

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.region is not None:
            result['Region'] = self.region
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.result is not None:
            result['Result'] = self.result
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class GetApplicationResponseBodyDataComplianceListRules(TeaModel):
    def __init__(
        self,
        rule_detail: str = None,
        rule_id: str = None,
    ):
        self.rule_detail = rule_detail
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_detail is not None:
            result['ruleDetail'] = self.rule_detail
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleDetail') is not None:
            self.rule_detail = m.get('ruleDetail')
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class GetApplicationResponseBodyDataComplianceList(TeaModel):
    def __init__(
        self,
        resource_code: str = None,
        resource_name: str = None,
        rules: List[GetApplicationResponseBodyDataComplianceListRules] = None,
    ):
        self.resource_code = resource_code
        self.resource_name = resource_name
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetApplicationResponseBodyDataComplianceListRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetApplicationResponseBodyDataPriceList(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        count: int = None,
        instance_name: str = None,
        lifecycle: str = None,
        one_price: float = None,
        original_price: float = None,
        period: int = None,
        price: float = None,
        price_unit: str = None,
        region: str = None,
        remark: str = None,
        resource_code: str = None,
        specification: str = None,
        type: str = None,
    ):
        # The billing method.
        self.charge_type = charge_type
        # The quantity.
        self.count = count
        # The name of the instance.
        self.instance_name = instance_name
        # Resource Fill Labels.
        self.lifecycle = lifecycle
        # The unit price of the instance.
        self.one_price = one_price
        # The original price of the instance.
        self.original_price = original_price
        # The service duration.
        self.period = period
        # The total price.
        self.price = price
        # Unit: USD per hour
        self.price_unit = price_unit
        # The region in which the instance resides.
        self.region = region
        # The error message that is returned when a price query fails.
        self.remark = remark
        # Product code
        self.resource_code = resource_code
        # The instance type. This parameter indicates the information about the instance type. For example, 192.168.0.0/16 may be returned for a Virtual Private Cloud (VPC) instance, ecs.g5.large may be returned for an Elastic Compute Service (ECS) instance, and slb.s1.small may be returned for a Server Load Balancer (SLB) instance. If the resource does not have a specific type, an empty value is returned.
        self.specification = specification
        # The creation mode. Valid values:\\
        # 1: creates a new instance.\\
        # 2: imports an instance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.count is not None:
            result['Count'] = self.count
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.one_price is not None:
            result['OnePrice'] = self.one_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.period is not None:
            result['Period'] = self.period
        if self.price is not None:
            result['Price'] = self.price
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.region is not None:
            result['Region'] = self.region
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('OnePrice') is not None:
            self.one_price = m.get('OnePrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetApplicationResponseBodyDataResourceList(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        lifecycle: str = None,
        node_label: str = None,
        remark: str = None,
        resource_code: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        status: str = None,
    ):
        # The billing method.
        self.charge_type = charge_type
        # The resource tag.
        self.lifecycle = lifecycle
        self.node_label = node_label
        # The deployment result.
        self.remark = remark
        # The service code.
        self.resource_code = resource_code
        # The instance ID.
        self.resource_id = resource_id
        # The name of the instance.
        self.resource_name = resource_name
        # The type of the resource.
        self.resource_type = resource_type
        # The resource deployment result.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle
        if self.node_label is not None:
            result['NodeLabel'] = self.node_label
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')
        if m.get('NodeLabel') is not None:
            self.node_label = m.get('NodeLabel')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        checklist: List[GetApplicationResponseBodyDataChecklist] = None,
        compliance_list: List[GetApplicationResponseBodyDataComplianceList] = None,
        create_time: str = None,
        deploy_percent: float = None,
        description: str = None,
        error: str = None,
        image_url: str = None,
        name: str = None,
        price_list: List[GetApplicationResponseBodyDataPriceList] = None,
        resource_group_id: str = None,
        resource_list: List[GetApplicationResponseBodyDataResourceList] = None,
        status: str = None,
        template_id: str = None,
    ):
        # App ID
        self.application_id = application_id
        # The resource tag.
        self.checklist = checklist
        self.compliance_list = compliance_list
        # The time when the app was created
        self.create_time = create_time
        self.deploy_percent = deploy_percent
        # Application description
        self.description = description
        # The resource type.
        self.error = error
        # The URL of the image in the database.
        self.image_url = image_url
        # App name
        self.name = name
        # The billing results.
        self.price_list = price_list
        # The ID of the resource group to which the app belongs
        self.resource_group_id = resource_group_id
        # The resource specification.
        self.resource_list = resource_list
        # Verification passed
        self.status = status
        # The ID of the template associated with the application
        self.template_id = template_id

    def validate(self):
        if self.checklist:
            for k in self.checklist:
                if k:
                    k.validate()
        if self.compliance_list:
            for k in self.compliance_list:
                if k:
                    k.validate()
        if self.price_list:
            for k in self.price_list:
                if k:
                    k.validate()
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        result['Checklist'] = []
        if self.checklist is not None:
            for k in self.checklist:
                result['Checklist'].append(k.to_map() if k else None)
        result['ComplianceList'] = []
        if self.compliance_list is not None:
            for k in self.compliance_list:
                result['ComplianceList'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_percent is not None:
            result['DeployPercent'] = self.deploy_percent
        if self.description is not None:
            result['Description'] = self.description
        if self.error is not None:
            result['Error'] = self.error
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        result['PriceList'] = []
        if self.price_list is not None:
            for k in self.price_list:
                result['PriceList'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        self.checklist = []
        if m.get('Checklist') is not None:
            for k in m.get('Checklist'):
                temp_model = GetApplicationResponseBodyDataChecklist()
                self.checklist.append(temp_model.from_map(k))
        self.compliance_list = []
        if m.get('ComplianceList') is not None:
            for k in m.get('ComplianceList'):
                temp_model = GetApplicationResponseBodyDataComplianceList()
                self.compliance_list.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployPercent') is not None:
            self.deploy_percent = m.get('DeployPercent')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.price_list = []
        if m.get('PriceList') is not None:
            for k in m.get('PriceList'):
                temp_model = GetApplicationResponseBodyDataPriceList()
                self.price_list.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = GetApplicationResponseBodyDataResourceList()
                self.resource_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetApplicationResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # The details of the application.
        self.data = data
        # Reason for the request failure
        self.message = message
        # Request ID
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationVariablesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetApplicationVariablesResponseBodyDataVariableList(TeaModel):
    def __init__(
        self,
        value: str = None,
        variable: str = None,
    ):
        self.value = value
        self.variable = variable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.variable is not None:
            result['Variable'] = self.variable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Variable') is not None:
            self.variable = m.get('Variable')
        return self


class GetApplicationVariablesResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        variable_list: List[GetApplicationVariablesResponseBodyDataVariableList] = None,
    ):
        self.instance_id = instance_id
        self.variable_list = variable_list

    def validate(self):
        if self.variable_list:
            for k in self.variable_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['VariableList'] = []
        if self.variable_list is not None:
            for k in self.variable_list:
                result['VariableList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.variable_list = []
        if m.get('VariableList') is not None:
            for k in m.get('VariableList'):
                temp_model = GetApplicationVariablesResponseBodyDataVariableList()
                self.variable_list.append(temp_model.from_map(k))
        return self


class GetApplicationVariablesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetApplicationVariablesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetApplicationVariablesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApplicationVariablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApplicationVariablesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetApplicationVariablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationVariables4FailRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetApplicationVariables4FailResponseBodyData(TeaModel):
    def __init__(
        self,
        attribute: str = None,
        default_value: str = None,
        place_holder: str = None,
        region: str = None,
        value: str = None,
        variable: str = None,
    ):
        self.attribute = attribute
        self.default_value = default_value
        self.place_holder = place_holder
        self.region = region
        self.value = value
        self.variable = variable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute is not None:
            result['Attribute'] = self.attribute
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.place_holder is not None:
            result['PlaceHolder'] = self.place_holder
        if self.region is not None:
            result['Region'] = self.region
        if self.value is not None:
            result['Value'] = self.value
        if self.variable is not None:
            result['Variable'] = self.variable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('PlaceHolder') is not None:
            self.place_holder = m.get('PlaceHolder')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Variable') is not None:
            self.variable = m.get('Variable')
        return self


class GetApplicationVariables4FailResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetApplicationVariables4FailResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetApplicationVariables4FailResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApplicationVariables4FailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApplicationVariables4FailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetApplicationVariables4FailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExecuteOperationResultRequest(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the operation.
        # 
        # This parameter is required.
        self.operation_id = operation_id
        # The ID of the resource group. This parameter is specified to verify the permissions on the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetExecuteOperationResultResponseBodyData(TeaModel):
    def __init__(
        self,
        arguments: str = None,
        message: str = None,
        operation_id: str = None,
        status: str = None,
    ):
        # The output of the operation.
        self.arguments = arguments
        # The returned message.
        self.message = message
        # The ID of the operation.
        self.operation_id = operation_id
        # The status of the operation.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        if self.message is not None:
            result['Message'] = self.message
        if self.operation_id is not None:
            result['OperationId'] = self.operation_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OperationId') is not None:
            self.operation_id = m.get('OperationId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetExecuteOperationResultResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetExecuteOperationResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code. A value of 200 indicates that the request is successful.
        self.code = code
        # The detailed result of the queried operation.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetExecuteOperationResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetExecuteOperationResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExecuteOperationResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetExecuteOperationResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFoTaskStatusRequest(TeaModel):
    def __init__(
        self,
        task_id: int = None,
    ):
        # The disaster recovery switchover task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetFoTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # The status of the switchover task.
        self.data = data
        # The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFoTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFoTaskStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetFoTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPotentialFailZonesRequest(TeaModel):
    def __init__(
        self,
        is_plan_id: bool = None,
        object_id: str = None,
    ):
        # Specifies whether the value of this parameter is the ID of a disaster recovery set.
        self.is_plan_id = is_plan_id
        # If you set IsPlanId to false, specify the ID of a disaster recovery application. If you set IsPlanId to true, specify the ID of a disaster recovery set.
        self.object_id = object_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_plan_id is not None:
            result['IsPlanId'] = self.is_plan_id
        if self.object_id is not None:
            result['ObjectId'] = self.object_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsPlanId') is not None:
            self.is_plan_id = m.get('IsPlanId')
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')
        return self


class GetPotentialFailZonesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[str] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # The zones where the current disaster recovery service can be switched.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPotentialFailZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPotentialFailZonesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetPotentialFailZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResource4ModifyRecordRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        max_results: int = None,
        next_token: int = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class GetResource4ModifyRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        attribute: str = None,
        error: str = None,
        modify_time: str = None,
        resource_id: str = None,
        status: str = None,
        type: str = None,
    ):
        self.attribute = attribute
        self.error = error
        self.modify_time = modify_time
        self.resource_id = resource_id
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute is not None:
            result['Attribute'] = self.attribute
        if self.error is not None:
            result['Error'] = self.error
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetResource4ModifyRecordResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[GetResource4ModifyRecordResponseBodyData] = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetResource4ModifyRecordResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetResource4ModifyRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResource4ModifyRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetResource4ModifyRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResult4QueryInstancePrice4ModifyRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        task_id: str = None,
    ):
        self.application_id = application_id
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetResult4QueryInstancePrice4ModifyResponseBodyDataPriceList(TeaModel):
    def __init__(
        self,
        discount_amount: float = None,
        error: str = None,
        node_type: str = None,
        original_amount: float = None,
        price_unit: str = None,
        promotion_name: str = None,
        trade_amount: float = None,
    ):
        self.discount_amount = discount_amount
        self.error = error
        self.node_type = node_type
        self.original_amount = original_amount
        self.price_unit = price_unit
        self.promotion_name = promotion_name
        self.trade_amount = trade_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.error is not None:
            result['Error'] = self.error
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class GetResult4QueryInstancePrice4ModifyResponseBodyData(TeaModel):
    def __init__(
        self,
        price_list: List[GetResult4QueryInstancePrice4ModifyResponseBodyDataPriceList] = None,
        status: str = None,
        task_id: str = None,
    ):
        self.price_list = price_list
        self.status = status
        self.task_id = task_id

    def validate(self):
        if self.price_list:
            for k in self.price_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PriceList'] = []
        if self.price_list is not None:
            for k in self.price_list:
                result['PriceList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.price_list = []
        if m.get('PriceList') is not None:
            for k in m.get('PriceList'):
                temp_model = GetResult4QueryInstancePrice4ModifyResponseBodyDataPriceList()
                self.price_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetResult4QueryInstancePrice4ModifyResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetResult4QueryInstancePrice4ModifyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetResult4QueryInstancePrice4ModifyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResult4QueryInstancePrice4ModifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResult4QueryInstancePrice4ModifyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetResult4QueryInstancePrice4ModifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        region: str = None,
        resource_group_id: str = None,
        template_id: str = None,
    ):
        # Template Area
        self.region = region
        # ResourceGroup ID
        self.resource_group_id = resource_group_id
        # Template ID
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetTemplateResponseBodyDataVariables(TeaModel):
    def __init__(
        self,
        attribute: str = None,
        data_type: str = None,
        default_value: str = None,
        options: str = None,
        variable: str = None,
    ):
        # The name of the variable.
        self.attribute = attribute
        # The type of the variable.
        self.data_type = data_type
        # The default value of the variable.
        self.default_value = default_value
        self.options = options
        # The value of the variable.
        self.variable = variable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute is not None:
            result['Attribute'] = self.attribute
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.options is not None:
            result['Options'] = self.options
        if self.variable is not None:
            result['Variable'] = self.variable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            self.attribute = m.get('Attribute')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('Variable') is not None:
            self.variable = m.get('Variable')
        return self


class GetTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        image_url: str = None,
        name: str = None,
        resource_group_id: str = None,
        template_id: str = None,
        variables: List[GetTemplateResponseBodyDataVariables] = None,
    ):
        # The time when the template was created.
        self.create_time = create_time
        # Template Description
        self.description = description
        # The path to the template schema image file
        self.image_url = image_url
        # The name of the template
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Template ID
        self.template_id = template_id
        # The details of the template variables.
        self.variables = variables

    def validate(self):
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = GetTemplateResponseBodyDataVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The details of the template.
        self.data = data
        # The interface returns information
        self.message = message
        # Request ID
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
    ):
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        bucket: str = None,
        endpoint: str = None,
        security_token: str = None,
        snapshot_bucket: str = None,
    ):
        # The AccessKey ID that is used to access OSS.
        self.access_key_id = access_key_id
        # The AccessKey secret used to access OSS.
        self.access_key_secret = access_key_secret
        # The OSS bucket that is used to store the architecture image.
        self.bucket = bucket
        # The OSS endpoint.
        self.endpoint = endpoint
        # The token that is used to access the Object Storage Service (OSS) bucket that stores the architecture image.
        self.security_token = security_token
        # The OSS bucket that is used to save data snapshots.
        self.snapshot_bucket = snapshot_bucket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.snapshot_bucket is not None:
            result['SnapshotBucket'] = self.snapshot_bucket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SnapshotBucket') is not None:
            self.snapshot_bucket = m.get('SnapshotBucket')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTokenResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The information about the token.
        self.data = data
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitAppFailOverRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
    ):
        # The application ID.
        self.application_id = application_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        return self


class InitAppFailOverResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # The switchover task ID.
        self.data = data
        # The returned message. If the request was successful, a success message is returned. If the request failed, an error message is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InitAppFailOverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitAppFailOverResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = InitAppFailOverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: int = None,
        order_type: int = None,
        resource_group_id: str = None,
        resource_id: str = None,
        show_hide: bool = None,
        status: str = None,
        template_id: str = None,
    ):
        # Keywords in the app name
        self.keyword = keyword
        # The pagination size of the resulting value cannot be less than the minimum value of 1 and cannot be greater than the maximum value of 50.
        # 
        # This parameter is required.
        self.max_results = max_results
        # The pagination page number of the resulting value cannot be less than the minimum value of 1 and cannot be greater than the maximum value of 10000.
        # 
        # This parameter is required.
        self.next_token = next_token
        # 1 update time,<br>2 creation time
        self.order_type = order_type
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # Resource Id
        self.resource_id = resource_id
        self.show_hide = show_hide
        # The status of the applications to be returned.
        self.status = status
        # Template Id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.show_hide is not None:
            result['ShowHide'] = self.show_hide
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ShowHide') is not None:
            self.show_hide = m.get('ShowHide')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ListApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        create_time: str = None,
        image_url: str = None,
        name: str = None,
        resource_group_id: str = None,
        status: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The time when the application was created.
        self.create_time = create_time
        # The URL of the application architecture image.
        self.image_url = image_url
        # The name of the application.
        self.name = name
        # The ID of the resource group to which the application belongs.
        self.resource_group_id = resource_group_id
        # The status of the application.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListApplicationResponseBodyData] = None,
        message: str = None,
        next_token: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The HTTP status code.
        self.code = code
        # App listing information
        self.data = data
        # The interface returns information
        self.message = message
        # The query token returned in this call.
        self.next_token = next_token
        # The ID of the application.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListApplicationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFoCreatedAppsResponseBodyData(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        report_url: str = None,
        status: str = None,
        title: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The URL of the error report.
        self.report_url = report_url
        # The state of the application.
        self.status = status
        # The title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.report_url is not None:
            result['ReportUrl'] = self.report_url
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ReportUrl') is not None:
            self.report_url = m.get('ReportUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListFoCreatedAppsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListFoCreatedAppsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The templates.
        self.data = data
        # The returned error message.
        self.message = message
        # The request ID.
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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListFoCreatedAppsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFoCreatedAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFoCreatedAppsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListFoCreatedAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs. You can specify a maximum number of 50 IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags. A maximum of 20 tags are supported.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The ID of the resource.
        self.resource_id = resource_id
        # The resource type. Valid values: application and template.
        self.resource_type = resource_type
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        # The HTTP status code. A value of 200 indicates that the request is successful.
        self.code = code
        # The error message returned if the request failed.
        self.message = message
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. If the NextToken parameter is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The tags that are added to the resources.
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
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
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


class ListTemplateRequestTag(TeaModel):
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


class ListTemplateRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: int = None,
        order_type: int = None,
        resource_group_id: str = None,
        tag: List[ListTemplateRequestTag] = None,
        tag_list: int = None,
        type: str = None,
    ):
        # The keyword that is used to search for templates.
        self.keyword = keyword
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.max_results = max_results
        # The number of the page to return.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The criterion by which the returned templates are sorted. Valid values:
        # 
        # *   1: The templates are sorted by the time when they are updated.
        # *   2: The templates are sorted by the time when they are created.
        # *   3: The templates are sorted by the system.
        # *   4: The templates are sorted by the number of times that they are used.
        # *   If you specify an integer other than 1, 2, 3, and 4 or do not specify any value, the templates are sorted by the system.
        self.order_type = order_type
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.tag = tag
        # The tag that you want to use to query templates.
        self.tag_list = tag_list
        # The type of the templates to be returned. Valid values: public and private
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.tag_list is not None:
            result['TagList'] = self.tag_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTemplateRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: int = None,
        order_type: int = None,
        resource_group_id: str = None,
        tag_shrink: str = None,
        tag_list: int = None,
        type: str = None,
    ):
        # The keyword that is used to search for templates.
        self.keyword = keyword
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.max_results = max_results
        # The number of the page to return.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The criterion by which the returned templates are sorted. Valid values:
        # 
        # *   1: The templates are sorted by the time when they are updated.
        # *   2: The templates are sorted by the time when they are created.
        # *   3: The templates are sorted by the system.
        # *   4: The templates are sorted by the number of times that they are used.
        # *   If you specify an integer other than 1, 2, 3, and 4 or do not specify any value, the templates are sorted by the system.
        self.order_type = order_type
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.tag_shrink = tag_shrink
        # The tag that you want to use to query templates.
        self.tag_list = tag_list
        # The type of the templates to be returned. Valid values: public and private
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink
        if self.tag_list is not None:
            result['TagList'] = self.tag_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')
        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        image_url: str = None,
        name: str = None,
        resource_group_id: str = None,
        tag_id: int = None,
        tag_name: str = None,
        template_id: str = None,
    ):
        # The time when the template was created.
        self.create_time = create_time
        # The URL of the architecture image.
        self.image_url = image_url
        # The name of the template.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the tag that is added to the template.
        self.tag_id = tag_id
        # The name of the tag that is added to the template.
        self.tag_name = tag_name
        # The ID of the template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.image_url is not None:
            result['ImageURL'] = self.image_url
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ImageURL') is not None:
            self.image_url = m.get('ImageURL')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ListTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[ListTemplateResponseBodyData] = None,
        message: str = None,
        next_token: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The HTTP status code.
        self.code = code
        # The details about templates.
        self.data = data
        # The returned message.
        self.message = message
        # The page number of the returned page.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTemplateResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyApplicationSpecRequestInstanceSpec(TeaModel):
    def __init__(
        self,
        configuration: Dict[str, Any] = None,
        instance_id: str = None,
    ):
        self.configuration = configuration
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ModifyApplicationSpecRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        instance_spec: List[ModifyApplicationSpecRequestInstanceSpec] = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.instance_spec = instance_spec

    def validate(self):
        if self.instance_spec:
            for k in self.instance_spec:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        result['InstanceSpec'] = []
        if self.instance_spec is not None:
            for k in self.instance_spec:
                result['InstanceSpec'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        self.instance_spec = []
        if m.get('InstanceSpec') is not None:
            for k in m.get('InstanceSpec'):
                temp_model = ModifyApplicationSpecRequestInstanceSpec()
                self.instance_spec.append(temp_model.from_map(k))
        return self


class ModifyApplicationSpecShrinkRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        instance_spec_shrink: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.instance_spec_shrink = instance_spec_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_spec_shrink is not None:
            result['InstanceSpec'] = self.instance_spec_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec_shrink = m.get('InstanceSpec')
        return self


class ModifyApplicationSpecResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyApplicationSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyApplicationSpecResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ModifyApplicationSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInstancePrice4ModifyRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        configuration: Dict[str, Any] = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.configuration = configuration
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QueryInstancePrice4ModifyShrinkRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        configuration_shrink: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.configuration_shrink = configuration_shrink
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.configuration_shrink is not None:
            result['Configuration'] = self.configuration_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('Configuration') is not None:
            self.configuration_shrink = m.get('Configuration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QueryInstancePrice4ModifyResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        # taskId
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryInstancePrice4ModifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryInstancePrice4ModifyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryInstancePrice4ModifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInstanceSpec4ModifyRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        instance_id: str = None,
        method_name: str = None,
        parameters: Dict[str, Any] = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        # This parameter is required.
        self.instance_id = instance_id
        self.method_name = method_name
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.method_name is not None:
            result['MethodName'] = self.method_name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class QueryInstanceSpec4ModifyShrinkRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        instance_id: str = None,
        method_name: str = None,
        parameters_shrink: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        # This parameter is required.
        self.instance_id = instance_id
        self.method_name = method_name
        self.parameters_shrink = parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.method_name is not None:
            result['MethodName'] = self.method_name
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MethodName') is not None:
            self.method_name = m.get('MethodName')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        return self


class QueryInstanceSpec4ModifyResponseBodyDataOptionalValues(TeaModel):
    def __init__(
        self,
        label: str = None,
        max: float = None,
        min: float = None,
        step: float = None,
        value: str = None,
    ):
        self.label = label
        self.max = max
        self.min = min
        self.step = step
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.max is not None:
            result['Max'] = self.max
        if self.min is not None:
            result['Min'] = self.min
        if self.step is not None:
            result['Step'] = self.step
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Max') is not None:
            self.max = m.get('Max')
        if m.get('Min') is not None:
            self.min = m.get('Min')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryInstanceSpec4ModifyResponseBodyData(TeaModel):
    def __init__(
        self,
        optional_values: List[QueryInstanceSpec4ModifyResponseBodyDataOptionalValues] = None,
    ):
        self.optional_values = optional_values

    def validate(self):
        if self.optional_values:
            for k in self.optional_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OptionalValues'] = []
        if self.optional_values is not None:
            for k in self.optional_values:
                result['OptionalValues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.optional_values = []
        if m.get('OptionalValues') is not None:
            for k in m.get('OptionalValues'):
                temp_model = QueryInstanceSpec4ModifyResponseBodyDataOptionalValues()
                self.optional_values.append(temp_model.from_map(k))
        return self


class QueryInstanceSpec4ModifyResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: QueryInstanceSpec4ModifyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryInstanceSpec4ModifyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryInstanceSpec4ModifyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryInstanceSpec4ModifyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryInstanceSpec4ModifyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReConfigApplicationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        variables: str = None,
    ):
        self.app_id = app_id
        self.variables = variables

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.variables is not None:
            result['Variables'] = self.variables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        return self


class ReConfigApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReConfigApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReConfigApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ReConfigApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        client_token: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ReleaseApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The return value.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReleaseApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ReleaseApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        client_token: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ValidateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data of the application.
        self.data = data
        # The error message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ValidateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ValidateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValuateApplicationRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        client_token: str = None,
        resource_group_id: str = None,
    ):
        # The operation that you want to perform. Set the value to ValuateApplication.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The ID of the resource group to which the application you want to query belongs.
        self.client_token = client_token
        # The ID of the resource group.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ValuateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The code of the query task.
        self.code = code
        # The ID of the request.
        self.data = data
        # Idempotent notation
        self.message = message
        # The returned message.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ValuateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValuateApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ValuateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValuateTemplateRequestInstances(TeaModel):
    def __init__(
        self,
        id: str = None,
        node_name: str = None,
        node_type: str = None,
    ):
        # The instance ID.
        self.id = id
        # The name of the application instance that is displayed on the diagram.
        self.node_name = node_name
        # The instance type.
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class ValuateTemplateRequest(TeaModel):
    def __init__(
        self,
        area_id: str = None,
        client_token: str = None,
        instances: List[ValuateTemplateRequestInstances] = None,
        resource_group_id: str = None,
        template_id: str = None,
        variables: Dict[str, Any] = None,
    ):
        # The region ID.
        self.area_id = area_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The instances to be replaced.
        self.instances = instances
        # The ID of the resource group to which the application belongs.
        self.resource_group_id = resource_group_id
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The parameter values that are contained in the template. If the template contains no parameter values, the default values are used.
        self.variables = variables

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.variables is not None:
            result['Variables'] = self.variables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ValuateTemplateRequestInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Variables') is not None:
            self.variables = m.get('Variables')
        return self


class ValuateTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        area_id: str = None,
        client_token: str = None,
        instances_shrink: str = None,
        resource_group_id: str = None,
        template_id: str = None,
        variables_shrink: str = None,
    ):
        # The region ID.
        self.area_id = area_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The instances to be replaced.
        self.instances_shrink = instances_shrink
        # The ID of the resource group to which the application belongs.
        self.resource_group_id = resource_group_id
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The parameter values that are contained in the template. If the template contains no parameter values, the default values are used.
        self.variables_shrink = variables_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.area_id is not None:
            result['AreaId'] = self.area_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instances_shrink is not None:
            result['Instances'] = self.instances_shrink
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.variables_shrink is not None:
            result['Variables'] = self.variables_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Instances') is not None:
            self.instances_shrink = m.get('Instances')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Variables') is not None:
            self.variables_shrink = m.get('Variables')
        return self


class ValuateTemplateResponseBodyDataResourceListPriceList(TeaModel):
    def __init__(
        self,
        discount_amount: float = None,
        error: str = None,
        node_type: str = None,
        original_price: float = None,
        price_unit: str = None,
        promotion_name: str = None,
        resource_id: str = None,
        trade_price: float = None,
        type: str = None,
    ):
        # The discount amount.
        self.discount_amount = discount_amount
        # The error message that is returned.
        self.error = error
        # The resource type.
        self.node_type = node_type
        # The original price.
        self.original_price = original_price
        # The pricing unit.
        self.price_unit = price_unit
        # The discount information.
        self.promotion_name = promotion_name
        # The resource ID.
        self.resource_id = resource_id
        # The price at which the transaction is made.
        self.trade_price = trade_price
        # Indicates whether the instance is newly created. Valid values:\\
        # 1: The instance is newly created.\\
        # 2: The instance already exists.\\
        # 0: The price of the instance is not included.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.error is not None:
            result['Error'] = self.error
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ValuateTemplateResponseBodyDataResourceList(TeaModel):
    def __init__(
        self,
        discount_amount: float = None,
        error: str = None,
        node_type: str = None,
        original_price: float = None,
        price_list: List[ValuateTemplateResponseBodyDataResourceListPriceList] = None,
        price_unit: str = None,
        promotion_name: str = None,
        trade_price: float = None,
    ):
        # The discount amount.
        self.discount_amount = discount_amount
        # The error message that is returned.
        self.error = error
        # The resource type.
        self.node_type = node_type
        # The original price.
        self.original_price = original_price
        # The information about the price.
        self.price_list = price_list
        # The pricing unit.
        self.price_unit = price_unit
        # The discount information.
        self.promotion_name = promotion_name
        # The price at which the transaction is made.
        self.trade_price = trade_price

    def validate(self):
        if self.price_list:
            for k in self.price_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.error is not None:
            result['Error'] = self.error
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['PriceList'] = []
        if self.price_list is not None:
            for k in self.price_list:
                result['PriceList'].append(k.to_map() if k else None)
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        self.price_list = []
        if m.get('PriceList') is not None:
            for k in m.get('PriceList'):
                temp_model = ValuateTemplateResponseBodyDataResourceListPriceList()
                self.price_list.append(temp_model.from_map(k))
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class ValuateTemplateResponseBodyData(TeaModel):
    def __init__(
        self,
        resource_list: List[ValuateTemplateResponseBodyDataResourceList] = None,
    ):
        # The result set of the inquiry.
        self.resource_list = resource_list

    def validate(self):
        if self.resource_list:
            for k in self.resource_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceList'] = []
        if self.resource_list is not None:
            for k in self.resource_list:
                result['ResourceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_list = []
        if m.get('ResourceList') is not None:
            for k in m.get('ResourceList'):
                temp_model = ValuateTemplateResponseBodyDataResourceList()
                self.resource_list.append(temp_model.from_map(k))
        return self


class ValuateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ValuateTemplateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The result of the inquiry.
        self.data = data
        # The error message returned if the request failed.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ValuateTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ValuateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValuateTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ValuateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


