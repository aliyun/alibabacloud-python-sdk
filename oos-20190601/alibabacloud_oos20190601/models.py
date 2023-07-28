# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CancelExecutionRequest(TeaModel):
    def __init__(
        self,
        execution_id: str = None,
        region_id: str = None,
    ):
        self.execution_id = execution_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CancelExecutionResponseBody(TeaModel):
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


class CancelExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelExecutionResponseBody = None,
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
            temp_model = CancelExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the resource group to which the cloud resource is to be moved. You can use resource groups to manage resources owned by your Alibaba Cloud account. Resource groups simplify the resource and permission management of your Alibaba Cloud account. For more information, see [What is Resource Management?](~~94475~~)
        self.new_resource_group_id = new_resource_group_id
        # The ID of the region.
        self.region_id = region_id
        # The ID of the cloud resource that you want to move to another resource group.
        # 
        # *   If the ResourceType parameter is set to template, set the ResourceId parameter to the name of the template.
        # *   If the ResourceType parameter is set to parameter, set the ResourceId parameter to the name of the parameter.
        # *   If the ResourceType parameter is set to secretparameter, set the ResourceId parameter to the name of the encryption parameter.
        # *   If the ResourceType parameter is set to stateconfiguration, set the ResourceId parameter to the ID of the desired-state configuration.
        # *   If the ResourceType parameter is set to application, set the ResourceId parameter to the name of the application.
        self.resource_id = resource_id
        # The type of the cloud resource. Valid values:
        # 
        # *   template: template
        # *   parameter: parameter
        # *   secretparameter: encryption parameter
        # *   stateconfiguration: desired-state configuration
        # *   application: application
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContinueDeployApplicationGroupRequest(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        deploy_parameters: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # The name of the application.
        self.application_name = application_name
        # The deployment information about the application group.
        self.deploy_parameters = deploy_parameters
        # The name of the application group.
        self.name = name
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.deploy_parameters is not None:
            result['DeployParameters'] = self.deploy_parameters
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('DeployParameters') is not None:
            self.deploy_parameters = m.get('DeployParameters')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ContinueDeployApplicationGroupResponseBody(TeaModel):
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


class ContinueDeployApplicationGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ContinueDeployApplicationGroupResponseBody = None,
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
            temp_model = ContinueDeployApplicationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequestAlarmConfig(TeaModel):
    def __init__(
        self,
        contact_groups: List[str] = None,
        health_check_url: str = None,
        template_ids: List[str] = None,
    ):
        self.contact_groups = contact_groups
        self.health_check_url = health_check_url
        self.template_ids = template_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(
        self,
        alarm_config: CreateApplicationRequestAlarmConfig = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: Dict[str, Any] = None,
    ):
        self.alarm_config = alarm_config
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The description of the application.
        self.description = description
        # The application name.
        self.name = name
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags = tags

    def validate(self):
        if self.alarm_config:
            self.alarm_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_config is not None:
            result['AlarmConfig'] = self.alarm_config.to_map()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmConfig') is not None:
            temp_model = CreateApplicationRequestAlarmConfig()
            self.alarm_config = temp_model.from_map(m['AlarmConfig'])
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class CreateApplicationShrinkRequest(TeaModel):
    def __init__(
        self,
        alarm_config_shrink: str = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags_shrink: str = None,
    ):
        self.alarm_config_shrink = alarm_config_shrink
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The description of the application.
        self.description = description
        # The application name.
        self.name = name
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_config_shrink is not None:
            result['AlarmConfig'] = self.alarm_config_shrink
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmConfig') is not None:
            self.alarm_config_shrink = m.get('AlarmConfig')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class CreateApplicationResponseBodyApplication(TeaModel):
    def __init__(
        self,
        create_date: str = None,
        description: str = None,
        name: str = None,
        tags: Dict[str, str] = None,
        update_date: str = None,
    ):
        # The time when the application was created.
        self.create_date = create_date
        # The description of the application.
        self.description = description
        # The application name.
        self.name = name
        # The tags.
        self.tags = tags
        # The time when the application was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        application: CreateApplicationResponseBodyApplication = None,
        request_id: str = None,
    ):
        # The information about the application.
        self.application = application
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = CreateApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
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
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationGroupRequest(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        client_token: str = None,
        cms_group_id: str = None,
        deploy_region_id: str = None,
        description: str = None,
        import_tag_key: str = None,
        import_tag_value: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # The application name.
        self.application_name = application_name
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The ID of the application group in CloudMonitor.
        self.cms_group_id = cms_group_id
        # The ID of the region in which the related sources reside.
        self.deploy_region_id = deploy_region_id
        # The description of the application group.
        self.description = description
        # The key of the tag. You must set both the ImportTagKey and the ImportTagValue parameters, or leave both of them empty. If you do not set the ImportTagKey and ImportTagValue parameters, the application name is used for this parameter by default.
        self.import_tag_key = import_tag_key
        # The value of the tag. You must set both the ImportTagKey and the ImportTagValue parameters, or leave both of them empty. If you do not set the ImportTagKey and ImportTagValue parameters, the application group name is used for this parameter by default.
        self.import_tag_value = import_tag_value
        # The name of the application group.
        self.name = name
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cms_group_id is not None:
            result['CmsGroupId'] = self.cms_group_id
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.import_tag_key is not None:
            result['ImportTagKey'] = self.import_tag_key
        if self.import_tag_value is not None:
            result['ImportTagValue'] = self.import_tag_value
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CmsGroupId') is not None:
            self.cms_group_id = m.get('CmsGroupId')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImportTagKey') is not None:
            self.import_tag_key = m.get('ImportTagKey')
        if m.get('ImportTagValue') is not None:
            self.import_tag_value = m.get('ImportTagValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateApplicationGroupResponseBodyApplicationGroup(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        cms_group_id: str = None,
        create_date: str = None,
        deploy_region_id: str = None,
        description: str = None,
        import_tag_key: str = None,
        import_tag_value: str = None,
        name: str = None,
        update_date: str = None,
    ):
        # The application name.
        self.application_name = application_name
        # The ID of the application group in CloudMonitor.
        self.cms_group_id = cms_group_id
        # The time when the application group was created.
        self.create_date = create_date
        # The ID of the region in which the related sources reside.
        self.deploy_region_id = deploy_region_id
        # The description of the application group.
        self.description = description
        # The key of the tag.
        self.import_tag_key = import_tag_key
        # The value of the tag.
        self.import_tag_value = import_tag_value
        # The name of the application group.
        self.name = name
        # The time when the application group was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.cms_group_id is not None:
            result['CmsGroupId'] = self.cms_group_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.import_tag_key is not None:
            result['ImportTagKey'] = self.import_tag_key
        if self.import_tag_value is not None:
            result['ImportTagValue'] = self.import_tag_value
        if self.name is not None:
            result['Name'] = self.name
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('CmsGroupId') is not None:
            self.cms_group_id = m.get('CmsGroupId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImportTagKey') is not None:
            self.import_tag_key = m.get('ImportTagKey')
        if m.get('ImportTagValue') is not None:
            self.import_tag_value = m.get('ImportTagValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateApplicationGroupResponseBody(TeaModel):
    def __init__(
        self,
        application_group: CreateApplicationGroupResponseBodyApplicationGroup = None,
        request_id: str = None,
    ):
        # The information about the application group.
        self.application_group = application_group
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application_group:
            self.application_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_group is not None:
            result['ApplicationGroup'] = self.application_group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationGroup') is not None:
            temp_model = CreateApplicationGroupResponseBodyApplicationGroup()
            self.application_group = temp_model.from_map(m['ApplicationGroup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateApplicationGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateApplicationGroupResponseBody = None,
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
            temp_model = CreateApplicationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOpsItemRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        client_token: str = None,
        dedup_string: str = None,
        description: str = None,
        priority: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resources: str = None,
        severity: str = None,
        solutions: str = None,
        source: str = None,
        tags: Dict[str, Any] = None,
        title: str = None,
    ):
        self.category = category
        self.client_token = client_token
        self.dedup_string = dedup_string
        self.description = description
        self.priority = priority
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resources = resources
        self.severity = severity
        self.solutions = solutions
        self.source = source
        self.tags = tags
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedup_string is not None:
            result['DedupString'] = self.dedup_string
        if self.description is not None:
            result['Description'] = self.description
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.solutions is not None:
            result['Solutions'] = self.solutions
        if self.source is not None:
            result['Source'] = self.source
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedupString') is not None:
            self.dedup_string = m.get('DedupString')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateOpsItemShrinkRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        client_token: str = None,
        dedup_string: str = None,
        description: str = None,
        priority: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resources: str = None,
        severity: str = None,
        solutions: str = None,
        source: str = None,
        tags_shrink: str = None,
        title: str = None,
    ):
        self.category = category
        self.client_token = client_token
        self.dedup_string = dedup_string
        self.description = description
        self.priority = priority
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resources = resources
        self.severity = severity
        self.solutions = solutions
        self.source = source
        self.tags_shrink = tags_shrink
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedup_string is not None:
            result['DedupString'] = self.dedup_string
        if self.description is not None:
            result['Description'] = self.description
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.solutions is not None:
            result['Solutions'] = self.solutions
        if self.source is not None:
            result['Source'] = self.source
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedupString') is not None:
            self.dedup_string = m.get('DedupString')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateOpsItemResponseBodyOpsItem(TeaModel):
    def __init__(
        self,
        attributes: str = None,
        category: str = None,
        create_date: str = None,
        created_by: str = None,
        description: str = None,
        last_modified_by: str = None,
        ops_item_id: str = None,
        priority: int = None,
        resource_group_id: str = None,
        resources: str = None,
        severity: str = None,
        solutions: str = None,
        source: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        title: str = None,
        update_date: str = None,
    ):
        self.attributes = attributes
        self.category = category
        self.create_date = create_date
        self.created_by = created_by
        self.description = description
        self.last_modified_by = last_modified_by
        self.ops_item_id = ops_item_id
        self.priority = priority
        self.resource_group_id = resource_group_id
        self.resources = resources
        self.severity = severity
        self.solutions = solutions
        self.source = source
        self.status = status
        self.tags = tags
        self.title = title
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.category is not None:
            result['Category'] = self.category
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.description is not None:
            result['Description'] = self.description
        if self.last_modified_by is not None:
            result['LastModifiedBy'] = self.last_modified_by
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.solutions is not None:
            result['Solutions'] = self.solutions
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LastModifiedBy') is not None:
            self.last_modified_by = m.get('LastModifiedBy')
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class CreateOpsItemResponseBody(TeaModel):
    def __init__(
        self,
        ops_item: CreateOpsItemResponseBodyOpsItem = None,
        request_id: str = None,
    ):
        self.ops_item = ops_item
        self.request_id = request_id

    def validate(self):
        if self.ops_item:
            self.ops_item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ops_item is not None:
            result['OpsItem'] = self.ops_item.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpsItem') is not None:
            temp_model = CreateOpsItemResponseBodyOpsItem()
            self.ops_item = temp_model.from_map(m['OpsItem'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOpsItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOpsItemResponseBody = None,
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
            temp_model = CreateOpsItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateParameterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        constraints: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        value: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). For more information, see "How to ensure idempotence".
        self.client_token = client_token
        # The constraints of the common parameter. By default, this parameter is null. Valid values:
        # 
        # *   AllowedValues: The value that is allowed for the common parameter. It must be an array string.
        # *   AllowedPattern: The pattern that is allowed for the common parameter. It must be a regular expression.
        # *   MinLength: The minimum length of the common parameter.
        # *   MaxLength: The maximum length of the common parameter.
        self.constraints = constraints
        # The description of the common parameter. The description must be 1 to 200 characters in length.
        self.description = description
        # The name of the parameter. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags = tags
        # The data type of the parameter. Valid values: String and StringList.
        self.type = type
        # The value of the common parameter. The value must be 1 to 4096 characters in length.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateParameterShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        constraints: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags_shrink: str = None,
        type: str = None,
        value: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). For more information, see "How to ensure idempotence".
        self.client_token = client_token
        # The constraints of the common parameter. By default, this parameter is null. Valid values:
        # 
        # *   AllowedValues: The value that is allowed for the common parameter. It must be an array string.
        # *   AllowedPattern: The pattern that is allowed for the common parameter. It must be a regular expression.
        # *   MinLength: The minimum length of the common parameter.
        # *   MaxLength: The maximum length of the common parameter.
        self.constraints = constraints
        # The description of the common parameter. The description must be 1 to 200 characters in length.
        self.description = description
        # The name of the parameter. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags_shrink = tags_shrink
        # The data type of the parameter. Valid values: String and StringList.
        self.type = type
        # The value of the common parameter. The value must be 1 to 4096 characters in length.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        parameter_version: int = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The constraints of the common parameter.
        self.constraints = constraints
        # The user who created the common parameter.
        self.created_by = created_by
        # The time when the common parameter was created.
        self.created_date = created_date
        # The description of the common parameter.
        self.description = description
        # The ID of the common parameter.
        self.id = id
        # The name of the common parameter.
        self.name = name
        # The version number of the common parameter.
        self.parameter_version = parameter_version
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the common parameter.
        self.share_type = share_type
        # The tags.
        self.tags = tags
        # The type of the common parameter.
        self.type = type
        # The user who updated the common parameter.
        self.updated_by = updated_by
        # The time when the common parameter was updated.
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class CreateParameterResponseBody(TeaModel):
    def __init__(
        self,
        parameter: CreateParameterResponseBodyParameter = None,
        request_id: str = None,
    ):
        # The information about the common parameter.
        self.parameter = parameter
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = CreateParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateParameterResponseBody = None,
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
            temp_model = CreateParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePatchBaselineRequestTags(TeaModel):
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


class CreatePatchBaselineRequest(TeaModel):
    def __init__(
        self,
        approval_rules: str = None,
        approved_patches: List[str] = None,
        approved_patches_enable_non_security: bool = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        operation_system: str = None,
        region_id: str = None,
        rejected_patches: List[str] = None,
        rejected_patches_action: str = None,
        sources: List[str] = None,
        tags: List[CreatePatchBaselineRequestTags] = None,
    ):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules
        self.approved_patches = approved_patches
        self.approved_patches_enable_non_security = approved_patches_enable_non_security
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The description of the patch baseline.
        self.description = description
        # The name of the patch baseline.
        self.name = name
        # The type of the operating system. Valid values:
        # 
        # *   Windows
        # *   Ubuntu
        # *   CentOS
        # *   Debian
        # *   AliyunLinux
        # *   RedhatEnterpriseLinux
        # *   Anolis
        # *   AlmaLinux
        self.operation_system = operation_system
        # The ID of the region in which you want to create a patch baseline.
        self.region_id = region_id
        self.rejected_patches = rejected_patches
        self.rejected_patches_action = rejected_patches_action
        self.sources = sources
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
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rejected_patches is not None:
            result['RejectedPatches'] = self.rejected_patches
        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RejectedPatches') is not None:
            self.rejected_patches = m.get('RejectedPatches')
        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreatePatchBaselineRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreatePatchBaselineShrinkRequest(TeaModel):
    def __init__(
        self,
        approval_rules: str = None,
        approved_patches_shrink: str = None,
        approved_patches_enable_non_security: bool = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        operation_system: str = None,
        region_id: str = None,
        rejected_patches_shrink: str = None,
        rejected_patches_action: str = None,
        sources_shrink: str = None,
        tags_shrink: str = None,
    ):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules
        self.approved_patches_shrink = approved_patches_shrink
        self.approved_patches_enable_non_security = approved_patches_enable_non_security
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The description of the patch baseline.
        self.description = description
        # The name of the patch baseline.
        self.name = name
        # The type of the operating system. Valid values:
        # 
        # *   Windows
        # *   Ubuntu
        # *   CentOS
        # *   Debian
        # *   AliyunLinux
        # *   RedhatEnterpriseLinux
        # *   Anolis
        # *   AlmaLinux
        self.operation_system = operation_system
        # The ID of the region in which you want to create a patch baseline.
        self.region_id = region_id
        self.rejected_patches_shrink = rejected_patches_shrink
        self.rejected_patches_action = rejected_patches_action
        self.sources_shrink = sources_shrink
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.approved_patches_shrink is not None:
            result['ApprovedPatches'] = self.approved_patches_shrink
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rejected_patches_shrink is not None:
            result['RejectedPatches'] = self.rejected_patches_shrink
        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ApprovedPatches') is not None:
            self.approved_patches_shrink = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RejectedPatches') is not None:
            self.rejected_patches_shrink = m.get('RejectedPatches')
        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class CreatePatchBaselineResponseBodyPatchBaselineTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class CreatePatchBaselineResponseBodyPatchBaseline(TeaModel):
    def __init__(
        self,
        approval_rules: str = None,
        approved_patches: List[str] = None,
        approved_patches_enable_non_security: bool = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        operation_system: str = None,
        rejected_patches: List[str] = None,
        rejected_patches_action: str = None,
        share_type: str = None,
        sources: List[str] = None,
        tags: List[CreatePatchBaselineResponseBodyPatchBaselineTags] = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules
        self.approved_patches = approved_patches
        self.approved_patches_enable_non_security = approved_patches_enable_non_security
        # The creator of the patch baseline.
        self.created_by = created_by
        # The time when the patch baseline was created.
        self.created_date = created_date
        # The description of the patch baseline.
        self.description = description
        # The ID of the patch baseline.
        self.id = id
        # The name of the patch baseline.
        self.name = name
        # The type of the operating system.
        self.operation_system = operation_system
        self.rejected_patches = rejected_patches
        self.rejected_patches_action = rejected_patches_action
        # The share type of the patch baseline.
        self.share_type = share_type
        self.sources = sources
        self.tags = tags
        # The Alibaba Cloud account that last modified the information about the patch baseline.
        self.updated_by = updated_by
        # The time when the information about the patch baseline was last modified.
        self.updated_date = updated_date

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
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.rejected_patches is not None:
            result['RejectedPatches'] = self.rejected_patches
        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RejectedPatches') is not None:
            self.rejected_patches = m.get('RejectedPatches')
        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreatePatchBaselineResponseBodyPatchBaselineTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class CreatePatchBaselineResponseBody(TeaModel):
    def __init__(
        self,
        patch_baseline: CreatePatchBaselineResponseBodyPatchBaseline = None,
        request_id: str = None,
    ):
        # The details of the patch baseline.
        self.patch_baseline = patch_baseline
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.patch_baseline:
            self.patch_baseline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.patch_baseline is not None:
            result['PatchBaseline'] = self.patch_baseline.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PatchBaseline') is not None:
            temp_model = CreatePatchBaselineResponseBodyPatchBaseline()
            self.patch_baseline = temp_model.from_map(m['PatchBaseline'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePatchBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePatchBaselineResponseBody = None,
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
            temp_model = CreatePatchBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecretParameterRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        constraints: str = None,
        description: str = None,
        key_id: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        value: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). For more information, see "How to ensure idempotence".
        self.client_token = client_token
        # The constraints of the encryption parameter. By default, this parameter is null. Valid values:
        # 
        # *   AllowedValues: The value that is allowed for the encryption parameter. It must be an array string.
        # *   AllowedPattern: The pattern that is allowed for the encryption parameter. It must be a regular expression.
        # *   MinLength: The minimum length of the encryption parameter.
        # *   MaxLength: The maximum length of the encryption parameter.
        self.constraints = constraints
        # The description of the encryption parameter. The description must be 1 to 200 characters in length.
        self.description = description
        # The key ID of Key Management Service (KMS) that is used to encrypt the parameter.
        self.key_id = key_id
        # The name of the parameter. The name must be 1 to 180 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags = tags
        # The data type of the parameter. Set the value to Secret.
        self.type = type
        # The value of the encryption parameter. The value must be 1 to 4096 characters in length.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateSecretParameterShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        constraints: str = None,
        description: str = None,
        key_id: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags_shrink: str = None,
        type: str = None,
        value: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can be up to 64 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). For more information, see "How to ensure idempotence".
        self.client_token = client_token
        # The constraints of the encryption parameter. By default, this parameter is null. Valid values:
        # 
        # *   AllowedValues: The value that is allowed for the encryption parameter. It must be an array string.
        # *   AllowedPattern: The pattern that is allowed for the encryption parameter. It must be a regular expression.
        # *   MinLength: The minimum length of the encryption parameter.
        # *   MaxLength: The maximum length of the encryption parameter.
        self.constraints = constraints
        # The description of the encryption parameter. The description must be 1 to 200 characters in length.
        self.description = description
        # The key ID of Key Management Service (KMS) that is used to encrypt the parameter.
        self.key_id = key_id
        # The name of the parameter. The name must be 1 to 180 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags_shrink = tags_shrink
        # The data type of the parameter. Set the value to Secret.
        self.type = type
        # The value of the encryption parameter. The value must be 1 to 4096 characters in length.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.description is not None:
            result['Description'] = self.description
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateSecretParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        key_id: str = None,
        name: str = None,
        parameter_version: int = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The constraints of the encryption parameter.
        self.constraints = constraints
        # The user who created the encryption parameter.
        self.created_by = created_by
        # The time when the encryption parameter was created.
        self.created_date = created_date
        # The description of the encryption parameter.
        self.description = description
        # The ID of the encryption parameter.
        self.id = id
        # The key ID of KMS that is used to encrypt the parameter.
        self.key_id = key_id
        # The name of the encryption parameter.
        self.name = name
        # The version number of the encryption parameter.
        self.parameter_version = parameter_version
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the encryption parameter.
        self.share_type = share_type
        # The tags.
        self.tags = tags
        # The type of the parameter.
        self.type = type
        # The user who updated the encryption parameter.
        self.updated_by = updated_by
        # The time when the encryption parameter was updated.
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class CreateSecretParameterResponseBody(TeaModel):
    def __init__(
        self,
        parameter: CreateSecretParameterResponseBodyParameter = None,
        request_id: str = None,
    ):
        # The information about the encryption parameter.
        self.parameter = parameter
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = CreateSecretParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSecretParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSecretParameterResponseBody = None,
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
            temp_model = CreateSecretParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStateConfigurationRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        configure_mode: str = None,
        description: str = None,
        parameters: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        schedule_expression: str = None,
        schedule_type: str = None,
        tags: Dict[str, Any] = None,
        targets: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        # The description of the desired-state configuration.
        self.client_token = client_token
        # 收集Inventory数据
        self.configure_mode = configure_mode
        # The configuration mode.
        # 
        # ApplyOnce: The configuration is applied only once. After a configuration is updated, the new configuration is applied.
        # 
        # ApplyAndMonitor: The configuration is applied only once. After the configuration is applied, the system only checks whether the configuration is migrated in the future.
        # 
        # ApplyAndAutoCorrect: The configuration is always applied.
        self.description = description
        # The ID of resource group.
        self.parameters = parameters
        # The ID of the template.
        self.region_id = region_id
        # The type of the schedule. Valid value: rate.
        self.resource_group_id = resource_group_id
        # The description.
        self.schedule_expression = schedule_expression
        # The schedule expression.
        self.schedule_type = schedule_type
        # The name of the template. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        self.tags = tags
        # The schedule expression. The interval between two schedules must be a minimum of 30 minutes.
        self.targets = targets
        # The version of the template.
        self.template_name = template_name
        # The required resources.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.targets is not None:
            result['Targets'] = self.targets
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class CreateStateConfigurationShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        configure_mode: str = None,
        description: str = None,
        parameters: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        schedule_expression: str = None,
        schedule_type: str = None,
        tags_shrink: str = None,
        targets: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        # The description of the desired-state configuration.
        self.client_token = client_token
        # 收集Inventory数据
        self.configure_mode = configure_mode
        # The configuration mode.
        # 
        # ApplyOnce: The configuration is applied only once. After a configuration is updated, the new configuration is applied.
        # 
        # ApplyAndMonitor: The configuration is applied only once. After the configuration is applied, the system only checks whether the configuration is migrated in the future.
        # 
        # ApplyAndAutoCorrect: The configuration is always applied.
        self.description = description
        # The ID of resource group.
        self.parameters = parameters
        # The ID of the template.
        self.region_id = region_id
        # The type of the schedule. Valid value: rate.
        self.resource_group_id = resource_group_id
        # The description.
        self.schedule_expression = schedule_expression
        # The schedule expression.
        self.schedule_type = schedule_type
        # The name of the template. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        self.tags_shrink = tags_shrink
        # The schedule expression. The interval between two schedules must be a minimum of 30 minutes.
        self.targets = targets
        # The version of the template.
        self.template_name = template_name
        # The required resources.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.targets is not None:
            result['Targets'] = self.targets
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class CreateStateConfigurationResponseBodyStateConfiguration(TeaModel):
    def __init__(
        self,
        configure_mode: str = None,
        create_time: str = None,
        description: str = None,
        parameters: Dict[str, Any] = None,
        resource_group_id: str = None,
        schedule_expression: str = None,
        schedule_type: str = None,
        state_configuration_id: str = None,
        tags: Dict[str, Any] = None,
        targets: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        # The parameters.
        self.configure_mode = configure_mode
        # The desired-state configuration.
        self.create_time = create_time
        # WB502027
        self.description = description
        # CreateStateConfiguration
        self.parameters = parameters
        self.resource_group_id = resource_group_id
        # The version number. If you do not specify this parameter, the system uses the latest version.
        self.schedule_expression = schedule_expression
        # Creates a desired-state configuration.
        self.schedule_type = schedule_type
        # 收集Inventory数据
        self.state_configuration_id = state_configuration_id
        # The required resources.
        self.tags = tags
        # 1 hour 或 30 minutes
        self.targets = targets
        self.template_id = template_id
        # The name of the template.
        self.template_name = template_name
        # The ID of the request.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.state_configuration_id is not None:
            result['StateConfigurationId'] = self.state_configuration_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.targets is not None:
            result['Targets'] = self.targets
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('StateConfigurationId') is not None:
            self.state_configuration_id = m.get('StateConfigurationId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class CreateStateConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state_configuration: CreateStateConfigurationResponseBodyStateConfiguration = None,
    ):
        # The configuration mode.
        self.request_id = request_id
        # The tag.
        self.state_configuration = state_configuration

    def validate(self):
        if self.state_configuration:
            self.state_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.state_configuration is not None:
            result['StateConfiguration'] = self.state_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StateConfiguration') is not None:
            temp_model = CreateStateConfigurationResponseBodyStateConfiguration()
            self.state_configuration = temp_model.from_map(m['StateConfiguration'])
        return self


class CreateStateConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateStateConfigurationResponseBody = None,
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
            temp_model = CreateStateConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: Dict[str, Any] = None,
        template_name: str = None,
        version_name: str = None,
    ):
        # The content of the template. The content must be in the JSON or YAML format, and its maximum size is 64 KB.
        self.content = content
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tag keys and tag values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags
        # The name of the template. The name can be 1 to 200 characters in length and can contain letters, digits, hyphens (-), and underscores (\_). The name cannot start with ALIYUN, ACS, ALIBABA, or ALICLOUD.
        self.template_name = template_name
        # The name of the version of the template.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags_shrink: str = None,
        template_name: str = None,
        version_name: str = None,
    ):
        # The content of the template. The content must be in the JSON or YAML format, and its maximum size is 64 KB.
        self.content = content
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tag keys and tag values. The number of key-value pairs ranges from 1 to 20.
        self.tags_shrink = tags_shrink
        # The name of the template. The name can be 1 to 200 characters in length and can contain letters, digits, hyphens (-), and underscores (\_). The name cannot start with ALIYUN, ACS, ALIBABA, or ALICLOUD.
        self.template_name = template_name
        # The name of the version of the template.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class CreateTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        has_trigger: bool = None,
        hash: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        template_format: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The creator of the template.
        self.created_by = created_by
        # The time when the template was created.
        self.created_date = created_date
        # The description of the template.
        self.description = description
        # Indicates whether the template was configured with a trigger.
        self.has_trigger = has_trigger
        # The SHA-256 value of the template content.
        self.hash = hash
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the template. The share type of the template that you create is Private.
        self.share_type = share_type
        # The tags of the resources.
        self.tags = tags
        # The format of the template. The system automatically determines whether the format is JSON or YAML.
        self.template_format = template_format
        # The ID of the template.
        self.template_id = template_id
        # The name of the template.
        self.template_name = template_name
        # The version of the template. The name of the version consists of the letter v and a number. The number starts from 1.
        self.template_version = template_version
        # The Alibaba Cloud account that last modified the information about the template.
        self.updated_by = updated_by
        # The time when the template was last updated.
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template: CreateTemplateResponseBodyTemplate = None,
        template_type: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The metadata of the template.
        self.template = template
        # The type of the template.
        self.template_type = template_type

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = CreateTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTemplateResponseBody = None,
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
        name: str = None,
        region_id: str = None,
    ):
        # Specifies whether to forcibly delete the application. Valid values:
        # 
        # *   true
        # *   false
        self.force = force
        # The application name.
        self.name = name
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteApplicationResponseBody(TeaModel):
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
            temp_model = DeleteApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationGroupRequest(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # The name of the application.
        self.application_name = application_name
        # The name of the application group.
        self.name = name
        # The ID of the region. Set the value to cn-hangzhou.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteApplicationGroupResponseBody(TeaModel):
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


class DeleteApplicationGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApplicationGroupResponseBody = None,
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
            temp_model = DeleteApplicationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExecutionsRequest(TeaModel):
    def __init__(
        self,
        execution_ids: str = None,
        region_id: str = None,
    ):
        # The ID of the request.
        self.execution_ids = execution_ids
        # A JSON array that consists of multiple instance IDs. The format of the JSON array is [“xxxxxxxxx”, “yyyyyyyyy”, … “zzzzzzzzz”]. Separate multiple instance IDs with commas (,). A maximum of 100 instance IDs can be specified at a time.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_ids is not None:
            result['ExecutionIds'] = self.execution_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionIds') is not None:
            self.execution_ids = m.get('ExecutionIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteExecutionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Deletes multiple executions.
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


class DeleteExecutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteExecutionsResponseBody = None,
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
            temp_model = DeleteExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteParameterRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        region_id: str = None,
    ):
        # The name of the common parameter. The name can be up to 180 characters in length and can contain only letters, digits, hyphens (-), and underscores (\_). It cannot start with aliyun, acs, alibaba, alicloud, or oos.
        self.name = name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteParameterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteParameterResponseBody = None,
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
            temp_model = DeleteParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePatchBaselineRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        region_id: str = None,
    ):
        # The name of the patch baseline.
        self.name = name
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeletePatchBaselineResponseBody(TeaModel):
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


class DeletePatchBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePatchBaselineResponseBody = None,
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
            temp_model = DeletePatchBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecretParameterRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        region_id: str = None,
    ):
        # The name of the encryption parameter. The name can be up to 180 characters in length and can contain only letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteSecretParameterResponseBody(TeaModel):
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


class DeleteSecretParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSecretParameterResponseBody = None,
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
            temp_model = DeleteSecretParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStateConfigurationsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        state_configuration_ids: str = None,
    ):
        # Deletes desired-state configurations in batches
        self.client_token = client_token
        # The ID of the request.
        self.region_id = region_id
        # ## Debugging
        # 
        # [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=oos\&api=DeleteStateConfigurations\&type=RPC\&version=2019-06-01)
        self.state_configuration_ids = state_configuration_ids

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
        if self.state_configuration_ids is not None:
            result['StateConfigurationIds'] = self.state_configuration_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StateConfigurationIds') is not None:
            self.state_configuration_ids = m.get('StateConfigurationIds')
        return self


class DeleteStateConfigurationsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Deletes desired-state configurations in batches.
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


class DeleteStateConfigurationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteStateConfigurationsResponseBody = None,
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
            temp_model = DeleteStateConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateRequest(TeaModel):
    def __init__(
        self,
        auto_delete_executions: bool = None,
        region_id: str = None,
        template_name: str = None,
    ):
        # You can call this operation to delete a template.
        self.auto_delete_executions = auto_delete_executions
        # Specifies whether to delete the related executions when a template is deleted.
        self.region_id = region_id
        # The ID of the request.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_delete_executions is not None:
            result['AutoDeleteExecutions'] = self.auto_delete_executions
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDeleteExecutions') is not None:
            self.auto_delete_executions = m.get('AutoDeleteExecutions')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # You can call this operation to delete a template.
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


class DeleteTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTemplateResponseBody = None,
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
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplatesRequest(TeaModel):
    def __init__(
        self,
        auto_delete_executions: bool = None,
        region_id: str = None,
        template_names: str = None,
    ):
        # The ID of the request.
        self.auto_delete_executions = auto_delete_executions
        # The name list of templates to be deleted.
        self.region_id = region_id
        # Specifies whether to delete the related executions when a template is deleted.
        self.template_names = template_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_delete_executions is not None:
            result['AutoDeleteExecutions'] = self.auto_delete_executions
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_names is not None:
            result['TemplateNames'] = self.template_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDeleteExecutions') is not None:
            self.auto_delete_executions = m.get('AutoDeleteExecutions')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateNames') is not None:
            self.template_names = m.get('TemplateNames')
        return self


class DeleteTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Deletes multiple templates.
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


class DeleteTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTemplatesResponseBody = None,
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
            temp_model = DeleteTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployApplicationGroupRequest(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        deploy_parameters: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # The name of the application.
        self.application_name = application_name
        # The deployment information about the application group.
        self.deploy_parameters = deploy_parameters
        # The name of the application group.
        self.name = name
        # The ID of the region in which you want to deploy the application group.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.deploy_parameters is not None:
            result['DeployParameters'] = self.deploy_parameters
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('DeployParameters') is not None:
            self.deploy_parameters = m.get('DeployParameters')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeployApplicationGroupResponseBody(TeaModel):
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


class DeployApplicationGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployApplicationGroupResponseBody = None,
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
            temp_model = DeployApplicationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        region_id: str = None,
    ):
        self.accept_language = accept_language
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
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


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

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
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
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


class GenerateExecutionPolicyRequest(TeaModel):
    def __init__(
        self,
        ram_role: str = None,
        region_id: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        # The RAM role.
        self.ram_role = ram_role
        # The ID of the region.
        self.region_id = region_id
        # The name of the template.
        self.template_name = template_name
        # The version of the template. The default value is the latest version of the template.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GenerateExecutionPolicyResponseBody(TeaModel):
    def __init__(
        self,
        missing_policy: str = None,
        policy: str = None,
        request_id: str = None,
    ):
        # The policies that are missing.
        self.missing_policy = missing_policy
        # The RAM policy.
        self.policy = policy
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.missing_policy is not None:
            result['MissingPolicy'] = self.missing_policy
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MissingPolicy') is not None:
            self.missing_policy = m.get('MissingPolicy')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateExecutionPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateExecutionPolicyResponseBody = None,
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
            temp_model = GenerateExecutionPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        region_id: str = None,
    ):
        # The application name.
        self.name = name
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetApplicationResponseBodyApplicationAlarmConfig(TeaModel):
    def __init__(
        self,
        contact_groups: List[str] = None,
        health_check_url: str = None,
        template_ids: List[str] = None,
    ):
        self.contact_groups = contact_groups
        self.health_check_url = health_check_url
        self.template_ids = template_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')
        return self


class GetApplicationResponseBodyApplication(TeaModel):
    def __init__(
        self,
        alarm_config: GetApplicationResponseBodyApplicationAlarmConfig = None,
        application_type: str = None,
        create_date: str = None,
        description: str = None,
        name: str = None,
        resource_group_id: str = None,
        tags: Dict[str, Any] = None,
        update_date: str = None,
    ):
        self.alarm_config = alarm_config
        self.application_type = application_type
        # The time when the application was created.
        self.create_date = create_date
        # The description of the application.
        self.description = description
        # The application name.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags = tags
        # The time when the application was updated.
        self.update_date = update_date

    def validate(self):
        if self.alarm_config:
            self.alarm_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_config is not None:
            result['AlarmConfig'] = self.alarm_config.to_map()
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmConfig') is not None:
            temp_model = GetApplicationResponseBodyApplicationAlarmConfig()
            self.alarm_config = temp_model.from_map(m['AlarmConfig'])
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetApplicationResponseBody(TeaModel):
    def __init__(
        self,
        application: GetApplicationResponseBodyApplication = None,
        request_id: str = None,
    ):
        # The information about the application.
        self.application = application
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = GetApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
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
            temp_model = GetApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApplicationGroupRequest(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # The name of the application.
        self.application_name = application_name
        # The name of the application group.
        self.name = name
        # The ID of the region. Set the value to cn-hangzhou.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetApplicationGroupResponseBodyApplicationGroup(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        cms_group_id: str = None,
        create_date: str = None,
        deploy_outputs: str = None,
        deploy_parameters: str = None,
        deploy_region_id: str = None,
        description: str = None,
        import_tag_key: str = None,
        import_tag_value: str = None,
        name: str = None,
        progress: str = None,
        status: str = None,
        status_reason: str = None,
        update_date: str = None,
    ):
        # The name of the application.
        self.application_name = application_name
        # The ID of the application group in CloudMonitor.
        self.cms_group_id = cms_group_id
        # The time when the application group was created.
        self.create_date = create_date
        # The output of the deployment result.
        self.deploy_outputs = deploy_outputs
        # The configuration information of the application group.
        self.deploy_parameters = deploy_parameters
        # The ID of the region in which you deploy the application group.
        self.deploy_region_id = deploy_region_id
        # The description of the application group.
        self.description = description
        # The tag key.
        self.import_tag_key = import_tag_key
        # The tag value.
        self.import_tag_value = import_tag_value
        # The name of the application group.
        self.name = name
        # The creation progress of the application instance.
        self.progress = progress
        # The state of the application group.
        self.status = status
        # The state information of the application group.
        self.status_reason = status_reason
        # The time when the application group was last modified.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.cms_group_id is not None:
            result['CmsGroupId'] = self.cms_group_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deploy_outputs is not None:
            result['DeployOutputs'] = self.deploy_outputs
        if self.deploy_parameters is not None:
            result['DeployParameters'] = self.deploy_parameters
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.import_tag_key is not None:
            result['ImportTagKey'] = self.import_tag_key
        if self.import_tag_value is not None:
            result['ImportTagValue'] = self.import_tag_value
        if self.name is not None:
            result['Name'] = self.name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('CmsGroupId') is not None:
            self.cms_group_id = m.get('CmsGroupId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeployOutputs') is not None:
            self.deploy_outputs = m.get('DeployOutputs')
        if m.get('DeployParameters') is not None:
            self.deploy_parameters = m.get('DeployParameters')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImportTagKey') is not None:
            self.import_tag_key = m.get('ImportTagKey')
        if m.get('ImportTagValue') is not None:
            self.import_tag_value = m.get('ImportTagValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetApplicationGroupResponseBody(TeaModel):
    def __init__(
        self,
        application_group: GetApplicationGroupResponseBodyApplicationGroup = None,
        request_id: str = None,
    ):
        # The details of the application group.
        self.application_group = application_group
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application_group:
            self.application_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_group is not None:
            result['ApplicationGroup'] = self.application_group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationGroup') is not None:
            temp_model = GetApplicationGroupResponseBodyApplicationGroup()
            self.application_group = temp_model.from_map(m['ApplicationGroup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApplicationGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApplicationGroupResponseBody = None,
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
            temp_model = GetApplicationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExecutionTemplateRequest(TeaModel):
    def __init__(
        self,
        execution_id: str = None,
        region_id: str = None,
    ):
        # The ID of the execution.
        self.execution_id = execution_id
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetExecutionTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        hash: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        template_format: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The creator of the template.
        self.created_by = created_by
        # The time when the template was created.
        self.created_date = created_date
        # The description of the template.
        self.description = description
        # The SHA-256 value of the template content.
        self.hash = hash
        # The share type of the template. The share type of a user-created template is **Private**.
        self.share_type = share_type
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags
        # The format of the template. The system automatically determines whether the format is JSON or YAML.
        self.template_format = template_format
        # The ID of the template.
        self.template_id = template_id
        # The name of the template.
        self.template_name = template_name
        # The version of the template. The name of the version consists of the letter v and a number. The number starts from 1.
        self.template_version = template_version
        # The user who last updated the template.
        self.updated_by = updated_by
        # The time when the template was last updated.
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class GetExecutionTemplateResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
        template: GetExecutionTemplateResponseBodyTemplate = None,
    ):
        # The content of the template.
        self.content = content
        # The ID of the request.
        self.request_id = request_id
        # The metadata of the template.
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = GetExecutionTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class GetExecutionTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExecutionTemplateResponseBody = None,
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
            temp_model = GetExecutionTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInventorySchemaRequest(TeaModel):
    def __init__(
        self,
        aggregator: bool = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        type_name: str = None,
    ):
        # Specifies whether only to return a combination of specified properties.
        # 
        # Valid values:
        # 
        # *   true: only returns a combination of specified properties
        # *   false: returns all properties of the component
        self.aggregator = aggregator
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id
        # The name of the component. Valid values:
        # 
        # *   ACS:InstanceInformation
        # *   ACS:Application
        # *   ACS:File
        # *   ACS:Network
        # *   ACS:WindowsRole
        # *   ACS:Service
        # *   ACS:WindowsUpdate
        # *   ACS:WindowsRegistry
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class GetInventorySchemaResponseBodySchemasAttributes(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        name: str = None,
    ):
        # The data type of the property.
        self.data_type = data_type
        # The name of the property.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetInventorySchemaResponseBodySchemas(TeaModel):
    def __init__(
        self,
        attributes: List[GetInventorySchemaResponseBodySchemasAttributes] = None,
        type_name: str = None,
        version: str = None,
    ):
        # The properties of component.
        self.attributes = attributes
        # The name of the component.
        self.type_name = type_name
        # The version of the component.
        self.version = version

    def validate(self):
        if self.attributes:
            for k in self.attributes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attributes'] = []
        if self.attributes is not None:
            for k in self.attributes:
                result['Attributes'].append(k.to_map() if k else None)
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k in m.get('Attributes'):
                temp_model = GetInventorySchemaResponseBodySchemasAttributes()
                self.attributes.append(temp_model.from_map(k))
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetInventorySchemaResponseBody(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        schemas: List[GetInventorySchemaResponseBodySchemas] = None,
    ):
        # Max results.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The detailed configurations of the component.
        self.schemas = schemas

    def validate(self):
        if self.schemas:
            for k in self.schemas:
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
        result['Schemas'] = []
        if self.schemas is not None:
            for k in self.schemas:
                result['Schemas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.schemas = []
        if m.get('Schemas') is not None:
            for k in m.get('Schemas'):
                temp_model = GetInventorySchemaResponseBodySchemas()
                self.schemas.append(temp_model.from_map(k))
        return self


class GetInventorySchemaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInventorySchemaResponseBody = None,
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
            temp_model = GetInventorySchemaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpsItemRequest(TeaModel):
    def __init__(
        self,
        ops_item_id: str = None,
        region_id: str = None,
    ):
        self.ops_item_id = ops_item_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetOpsItemResponseBodyOpsItem(TeaModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        category: str = None,
        create_by: str = None,
        create_date: str = None,
        dedup_string: str = None,
        description: str = None,
        last_modified_by: str = None,
        ops_item_id: str = None,
        priority: int = None,
        resource_group_id: str = None,
        resources: List[str] = None,
        severity: str = None,
        solutions: List[Dict[str, Any]] = None,
        source: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        title: str = None,
        update_date: str = None,
    ):
        self.attributes = attributes
        self.category = category
        self.create_by = create_by
        self.create_date = create_date
        self.dedup_string = dedup_string
        self.description = description
        self.last_modified_by = last_modified_by
        self.ops_item_id = ops_item_id
        self.priority = priority
        self.resource_group_id = resource_group_id
        self.resources = resources
        self.severity = severity
        self.solutions = solutions
        self.source = source
        self.status = status
        self.tags = tags
        self.title = title
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.category is not None:
            result['Category'] = self.category
        if self.create_by is not None:
            result['CreateBy'] = self.create_by
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.dedup_string is not None:
            result['DedupString'] = self.dedup_string
        if self.description is not None:
            result['Description'] = self.description
        if self.last_modified_by is not None:
            result['LastModifiedBy'] = self.last_modified_by
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.solutions is not None:
            result['Solutions'] = self.solutions
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreateBy') is not None:
            self.create_by = m.get('CreateBy')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DedupString') is not None:
            self.dedup_string = m.get('DedupString')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LastModifiedBy') is not None:
            self.last_modified_by = m.get('LastModifiedBy')
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class GetOpsItemResponseBody(TeaModel):
    def __init__(
        self,
        ops_item: GetOpsItemResponseBodyOpsItem = None,
        request_id: str = None,
    ):
        self.ops_item = ops_item
        self.request_id = request_id

    def validate(self):
        if self.ops_item:
            self.ops_item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ops_item is not None:
            result['OpsItem'] = self.ops_item.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpsItem') is not None:
            temp_model = GetOpsItemResponseBodyOpsItem()
            self.ops_item = temp_model.from_map(m['OpsItem'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOpsItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOpsItemResponseBody = None,
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
            temp_model = GetOpsItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParameterRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameter_version: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The operation that you want to perform. Set the value to GetParameter.
        self.name = name
        # The time when the common parameter was updated.
        self.parameter_version = parameter_version
        # The name of the common parameter.
        self.region_id = region_id
        # The user who created the common parameter.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        parameter_version: int = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
        value: str = None,
    ):
        self.constraints = constraints
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.id = id
        self.name = name
        self.parameter_version = parameter_version
        self.resource_group_id = resource_group_id
        self.share_type = share_type
        # The ID of the request.
        self.tags = tags
        # The region ID of the resource.
        self.type = type
        # The value of the common parameter.
        self.updated_by = updated_by
        # The information of the common parameter.
        self.updated_date = updated_date
        # Queries a common parameter and its value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetParameterResponseBody(TeaModel):
    def __init__(
        self,
        parameter: GetParameterResponseBodyParameter = None,
        request_id: str = None,
    ):
        # The description of the common parameter.
        self.parameter = parameter
        # The user who updated the common parameter.
        self.request_id = request_id

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = GetParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetParameterResponseBody = None,
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
            temp_model = GetParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParametersRequest(TeaModel):
    def __init__(
        self,
        names: str = None,
        region_id: str = None,
    ):
        self.names = names
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.names is not None:
            result['Names'] = self.names
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetParametersResponseBodyParameters(TeaModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        parameter_version: int = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
        value: str = None,
    ):
        self.constraints = constraints
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.id = id
        self.name = name
        self.parameter_version = parameter_version
        self.resource_group_id = resource_group_id
        self.share_type = share_type
        self.tags = tags
        self.type = type
        self.updated_by = updated_by
        self.updated_date = updated_date
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetParametersResponseBody(TeaModel):
    def __init__(
        self,
        invalid_parameters: List[str] = None,
        parameters: List[GetParametersResponseBodyParameters] = None,
        request_id: str = None,
    ):
        self.invalid_parameters = invalid_parameters
        self.parameters = parameters
        self.request_id = request_id

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invalid_parameters is not None:
            result['InvalidParameters'] = self.invalid_parameters
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvalidParameters') is not None:
            self.invalid_parameters = m.get('InvalidParameters')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetParametersResponseBody = None,
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
            temp_model = GetParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetParametersByPathRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        path: str = None,
        recursive: bool = None,
        region_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.path = path
        self.recursive = recursive
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
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetParametersByPathResponseBodyParameters(TeaModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        parameter_version: int = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
        value: str = None,
    ):
        self.constraints = constraints
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.id = id
        self.name = name
        self.parameter_version = parameter_version
        self.share_type = share_type
        self.tags = tags
        self.type = type
        self.updated_by = updated_by
        self.updated_date = updated_date
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetParametersByPathResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        parameters: List[GetParametersByPathResponseBodyParameters] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.parameters = parameters
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.parameters:
            for k in self.parameters:
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
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetParametersByPathResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetParametersByPathResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetParametersByPathResponseBody = None,
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
            temp_model = GetParametersByPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPatchBaselineRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        region_id: str = None,
    ):
        # The name of the patch baseline.
        self.name = name
        # The ID of the region in which the patch baseline whose details you want to query resides.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPatchBaselineResponseBodyPatchBaselineTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetPatchBaselineResponseBodyPatchBaseline(TeaModel):
    def __init__(
        self,
        approval_rules: str = None,
        approved_patches: List[str] = None,
        approved_patches_enable_non_security: bool = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        is_default: bool = None,
        name: str = None,
        operation_system: str = None,
        rejected_patches: List[str] = None,
        rejected_patches_action: str = None,
        share_type: str = None,
        sources: List[str] = None,
        tags: List[GetPatchBaselineResponseBodyPatchBaselineTags] = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules
        self.approved_patches = approved_patches
        self.approved_patches_enable_non_security = approved_patches_enable_non_security
        # The creator of the patch baseline.
        self.created_by = created_by
        # The time when the patch baseline was created.
        self.created_date = created_date
        # The description of the patch baseline.
        self.description = description
        # The ID of the patch baseline.
        self.id = id
        # Indicates whether the patch baseline is set as the default patch baseline.
        self.is_default = is_default
        # The name of the patch baseline.
        self.name = name
        # The type of the operating system.
        self.operation_system = operation_system
        self.rejected_patches = rejected_patches
        self.rejected_patches_action = rejected_patches_action
        # The share type of the patch baseline.
        self.share_type = share_type
        self.sources = sources
        self.tags = tags
        # The user who last modified the patch baseline.
        self.updated_by = updated_by
        # The time when the patch baseline was last modified.
        self.updated_date = updated_date

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
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.rejected_patches is not None:
            result['RejectedPatches'] = self.rejected_patches
        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RejectedPatches') is not None:
            self.rejected_patches = m.get('RejectedPatches')
        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetPatchBaselineResponseBodyPatchBaselineTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class GetPatchBaselineResponseBody(TeaModel):
    def __init__(
        self,
        patch_baseline: GetPatchBaselineResponseBodyPatchBaseline = None,
        request_id: str = None,
    ):
        # The details of the patch baseline.
        self.patch_baseline = patch_baseline
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.patch_baseline:
            self.patch_baseline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.patch_baseline is not None:
            result['PatchBaseline'] = self.patch_baseline.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PatchBaseline') is not None:
            temp_model = GetPatchBaselineResponseBodyPatchBaseline()
            self.patch_baseline = temp_model.from_map(m['PatchBaseline'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPatchBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPatchBaselineResponseBody = None,
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
            temp_model = GetPatchBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretParameterRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        parameter_version: int = None,
        region_id: str = None,
        with_decryption: bool = None,
    ):
        # The name of the parameter. The name must be 1 to 180 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name
        # The version number of the common parameter. Valid values: 1 to 100.
        self.parameter_version = parameter_version
        # The ID of the region.
        self.region_id = region_id
        # Specifies whether to decrypt the parameter value. The decrypted parameter value is returned only if this parameter is set to true. Otherwise, null is returned.
        self.with_decryption = with_decryption

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')
        return self


class GetSecretParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        key_id: str = None,
        name: str = None,
        parameter_version: int = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
        value: str = None,
    ):
        # The constraints of the encryption parameter.
        self.constraints = constraints
        # The user who created the encryption parameter.
        self.created_by = created_by
        # The time when the encryption parameter was created.
        self.created_date = created_date
        # The description of the encryption parameter.
        self.description = description
        # The ID of the encryption parameter.
        self.id = id
        # The ID of the key of Key Management Service (KMS) that is used for encryption.
        self.key_id = key_id
        # The name of the encryption parameter.
        self.name = name
        # The version number of the encryption parameter.
        self.parameter_version = parameter_version
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the encryption parameter.
        self.share_type = share_type
        # The tags of the parameter.
        self.tags = tags
        # The type of the parameter.
        self.type = type
        # The user who updated the encryption parameter.
        self.updated_by = updated_by
        # The time when the encryption parameter was updated.
        self.updated_date = updated_date
        # The value of the encryption parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetSecretParameterResponseBody(TeaModel):
    def __init__(
        self,
        parameter: GetSecretParameterResponseBodyParameter = None,
        request_id: str = None,
    ):
        # The information about the encryption parameter.
        self.parameter = parameter
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = GetSecretParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSecretParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSecretParameterResponseBody = None,
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
            temp_model = GetSecretParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretParametersRequest(TeaModel):
    def __init__(
        self,
        names: str = None,
        region_id: str = None,
        with_decryption: bool = None,
    ):
        # The name of the encryption parameter. Multiple encryption parameters can form a JSON array in the format of \["xxxxxxxxx", "yyyyyyyyy", … "zzzzzzzzz"]. Each JSON array can contain a maximum of 10 encryption parameters. Multiple encryption parameters in the array are separated by commas (,).
        self.names = names
        # The ID of the region.
        self.region_id = region_id
        # Specifies whether to decrypt the parameter value. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.with_decryption = with_decryption

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.names is not None:
            result['Names'] = self.names
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')
        return self


class GetSecretParametersResponseBodyParameters(TeaModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        key_id: str = None,
        name: str = None,
        parameter_version: int = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
        value: str = None,
    ):
        # The constraints of the encryption parameter.
        self.constraints = constraints
        # The user who created the encryption parameter.
        self.created_by = created_by
        # The time when the encryption parameter was created.
        self.created_date = created_date
        # The description of the encryption parameter.
        self.description = description
        # The ID of the encryption parameter.
        self.id = id
        # The ID of the key.
        self.key_id = key_id
        # The name of the encryption parameter.
        self.name = name
        # The version number of the encryption parameter.
        self.parameter_version = parameter_version
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the encryption parameter.
        self.share_type = share_type
        # The tags.
        self.tags = tags
        # The data type of the encryption parameter.
        self.type = type
        # The user who updated the encryption parameter.
        self.updated_by = updated_by
        # The time when the encryption parameter was updated.
        self.updated_date = updated_date
        # The value of the encryption parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetSecretParametersResponseBody(TeaModel):
    def __init__(
        self,
        invalid_parameters: List[str] = None,
        parameters: List[GetSecretParametersResponseBodyParameters] = None,
        request_id: str = None,
    ):
        # Invalid encryption parameter.
        self.invalid_parameters = invalid_parameters
        # The information about the encryption parameter.
        self.parameters = parameters
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invalid_parameters is not None:
            result['InvalidParameters'] = self.invalid_parameters
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvalidParameters') is not None:
            self.invalid_parameters = m.get('InvalidParameters')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetSecretParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSecretParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSecretParametersResponseBody = None,
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
            temp_model = GetSecretParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretParametersByPathRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        path: str = None,
        recursive: bool = None,
        region_id: str = None,
        with_decryption: bool = None,
    ):
        # The number of entries to return on each page. Valid values: 1 to 10. Default value: 10.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The path of the encryption parameter. The path must be 1 to 200 characters in length. For example, if the name of an encryption parameter is /secretParameter/mySecretParameter, the path of the encryption parameter is /secretParameter.
        self.path = path
        # Specifies whether to recursively query encryption parameters from all levels of directories in the specified path. Valid values: true and false. For example, if you want to query the /secretParameter/mySecretParameter and /secretParameter/secretParameter 1/mySecretParameter parameters, the valid values specify the parameters to return.
        # 
        # *   true: Returns both of the /secretParameter/mySecretParameter and /secretParameter/secretParameter1/mySecretParameter parameters.
        # *   false: Returns only the /parameter/myparameter parameter.
        self.recursive = recursive
        # The ID of the region.
        self.region_id = region_id
        # Specifies whether to decrypt the parameter value.
        # 
        # Valid values:
        # 
        # *   true
        # *   false (Default)
        self.with_decryption = with_decryption

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
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')
        return self


class GetSecretParametersByPathResponseBodyParameters(TeaModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        key_id: str = None,
        name: str = None,
        parameter_version: int = None,
        share_type: str = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
        value: str = None,
    ):
        # The constraints of the encryption parameter.
        self.constraints = constraints
        # The user who created the encryption parameter.
        self.created_by = created_by
        # The time when the encryption parameter was updated.
        self.created_date = created_date
        # The description of the encryption parameter.
        self.description = description
        # The ID of the encryption parameter.
        self.id = id
        # The AccessKey ID.
        self.key_id = key_id
        # The name of the encryption parameter.
        self.name = name
        # The version number of the encryption parameter.
        self.parameter_version = parameter_version
        # The share type of the encryption parameter.
        self.share_type = share_type
        # The data type of the encryption parameter.
        self.type = type
        # The user who updated the encryption parameter.
        self.updated_by = updated_by
        # The time when the encryption parameter was updated.
        self.updated_date = updated_date
        # The value of the encryption parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetSecretParametersByPathResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        parameters: List[GetSecretParametersByPathResponseBodyParameters] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The information of the encryption parameter.
        self.parameters = parameters
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.parameters:
            for k in self.parameters:
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
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetSecretParametersByPathResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetSecretParametersByPathResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSecretParametersByPathResponseBody = None,
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
            temp_model = GetSecretParametersByPathResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceSettingsRequest(TeaModel):
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


class GetServiceSettingsResponseBodyServiceSettings(TeaModel):
    def __init__(
        self,
        delivery_oss_bucket_name: str = None,
        delivery_oss_enabled: bool = None,
        delivery_oss_key_prefix: str = None,
        delivery_sls_enabled: bool = None,
        delivery_sls_project_name: str = None,
        rdc_enterprise_id: str = None,
    ):
        self.delivery_oss_bucket_name = delivery_oss_bucket_name
        self.delivery_oss_enabled = delivery_oss_enabled
        self.delivery_oss_key_prefix = delivery_oss_key_prefix
        self.delivery_sls_enabled = delivery_sls_enabled
        self.delivery_sls_project_name = delivery_sls_project_name
        self.rdc_enterprise_id = rdc_enterprise_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_oss_bucket_name is not None:
            result['DeliveryOssBucketName'] = self.delivery_oss_bucket_name
        if self.delivery_oss_enabled is not None:
            result['DeliveryOssEnabled'] = self.delivery_oss_enabled
        if self.delivery_oss_key_prefix is not None:
            result['DeliveryOssKeyPrefix'] = self.delivery_oss_key_prefix
        if self.delivery_sls_enabled is not None:
            result['DeliverySlsEnabled'] = self.delivery_sls_enabled
        if self.delivery_sls_project_name is not None:
            result['DeliverySlsProjectName'] = self.delivery_sls_project_name
        if self.rdc_enterprise_id is not None:
            result['RdcEnterpriseId'] = self.rdc_enterprise_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryOssBucketName') is not None:
            self.delivery_oss_bucket_name = m.get('DeliveryOssBucketName')
        if m.get('DeliveryOssEnabled') is not None:
            self.delivery_oss_enabled = m.get('DeliveryOssEnabled')
        if m.get('DeliveryOssKeyPrefix') is not None:
            self.delivery_oss_key_prefix = m.get('DeliveryOssKeyPrefix')
        if m.get('DeliverySlsEnabled') is not None:
            self.delivery_sls_enabled = m.get('DeliverySlsEnabled')
        if m.get('DeliverySlsProjectName') is not None:
            self.delivery_sls_project_name = m.get('DeliverySlsProjectName')
        if m.get('RdcEnterpriseId') is not None:
            self.rdc_enterprise_id = m.get('RdcEnterpriseId')
        return self


class GetServiceSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_settings: List[GetServiceSettingsResponseBodyServiceSettings] = None,
    ):
        self.request_id = request_id
        self.service_settings = service_settings

    def validate(self):
        if self.service_settings:
            for k in self.service_settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceSettings'] = []
        if self.service_settings is not None:
            for k in self.service_settings:
                result['ServiceSettings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_settings = []
        if m.get('ServiceSettings') is not None:
            for k in m.get('ServiceSettings'):
                temp_model = GetServiceSettingsResponseBodyServiceSettings()
                self.service_settings.append(temp_model.from_map(k))
        return self


class GetServiceSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceSettingsResponseBody = None,
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
            temp_model = GetServiceSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        self.region_id = region_id
        self.template_name = template_name
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class GetTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        has_trigger: bool = None,
        hash: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        template_format: str = None,
        template_id: str = None,
        template_name: str = None,
        template_type: str = None,
        template_version: str = None,
        updated_by: str = None,
        updated_date: str = None,
        version_name: str = None,
    ):
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.has_trigger = has_trigger
        self.hash = hash
        self.resource_group_id = resource_group_id
        self.share_type = share_type
        self.tags = tags
        self.template_format = template_format
        self.template_id = template_id
        self.template_name = template_name
        self.template_type = template_type
        self.template_version = template_version
        self.updated_by = updated_by
        self.updated_date = updated_date
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        content: str = None,
        request_id: str = None,
        template: GetTemplateResponseBodyTemplate = None,
    ):
        self.content = content
        self.request_id = request_id
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = GetTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListActionsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        oosaction_name: str = None,
        region_id: str = None,
    ):
        # The number of entries to return on each page. Valid values: 20 to 100. Default value: 50.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The name of the action. All actions whose names contain the specified action name are returned.
        self.oosaction_name = oosaction_name
        # The ID of the region.
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
        if self.oosaction_name is not None:
            result['OOSActionName'] = self.oosaction_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OOSActionName') is not None:
            self.oosaction_name = m.get('OOSActionName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListActionsResponseBodyActions(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        created_date: str = None,
        description: str = None,
        oosaction_name: str = None,
        popularity: int = None,
        properties: str = None,
        template_version: str = None,
    ):
        # The type of the action.
        # 
        # 1.  Atomic actions
        # 
        #     *   Atomic.API
        #     *   Atomic.Trigger
        #     *   Atomic.Control
        #     *   Atomic.Embedded
        # 
        # 2.  Cloud product actions
        # 
        #     *   Product.ECS
        #     *   Product.RDS
        #     *   Product.VPC
        #     *   Product.FC
        #     *   ...
        self.action_type = action_type
        # The time when the action was created.
        self.created_date = created_date
        # The description of the action.
        self.description = description
        # The name of the action.
        self.oosaction_name = oosaction_name
        # The number of times that the action is used.
        self.popularity = popularity
        # The parameters of the action.
        self.properties = properties
        # The version of the template that corresponds to the action.
        # 
        # >  For atomic actions, this parameter is not returned.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.oosaction_name is not None:
            result['OOSActionName'] = self.oosaction_name
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OOSActionName') is not None:
            self.oosaction_name = m.get('OOSActionName')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class ListActionsResponseBody(TeaModel):
    def __init__(
        self,
        actions: List[ListActionsResponseBodyActions] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The details of the actions.
        self.actions = actions
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = ListActionsResponseBodyActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListActionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListActionsResponseBody = None,
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
            temp_model = ListActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationGroupsRequest(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        deploy_region_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_product: str = None,
        resource_type: str = None,
    ):
        # The name of the application.
        self.application_name = application_name
        # The ID of the region in which the related resources reside.
        self.deploy_region_id = deploy_region_id
        # The number of entries to return on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the region. Set the value to cn-hangzhou.
        self.region_id = region_id
        # The ID of the cloud resource.
        self.resource_id = resource_id
        # The code of the product to which the cloud resource belongs.
        self.resource_product = resource_product
        # The type of the cloud resource.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_product is not None:
            result['ResourceProduct'] = self.resource_product
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceProduct') is not None:
            self.resource_product = m.get('ResourceProduct')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListApplicationGroupsResponseBodyApplicationGroups(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        cms_group_id: str = None,
        create_date: str = None,
        deploy_parameters: str = None,
        deploy_region_id: str = None,
        description: str = None,
        import_tag_key: str = None,
        import_tag_value: str = None,
        name: str = None,
        status: str = None,
        status_reason: str = None,
        update_date: str = None,
    ):
        # The name of the application.
        self.application_name = application_name
        # The ID of the application group in CloudMonitor.
        self.cms_group_id = cms_group_id
        # The time when the application group was created.
        self.create_date = create_date
        # The configuration information of the application group.
        self.deploy_parameters = deploy_parameters
        # The ID of the region in which the related resources reside.
        self.deploy_region_id = deploy_region_id
        # The description of the application group.
        self.description = description
        # The tag key.
        self.import_tag_key = import_tag_key
        # The tag value.
        self.import_tag_value = import_tag_value
        # The name of the application group.
        self.name = name
        # The state of the application group.
        self.status = status
        # The state information of the application group.
        self.status_reason = status_reason
        # The time when the application group was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.cms_group_id is not None:
            result['CmsGroupId'] = self.cms_group_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.deploy_parameters is not None:
            result['DeployParameters'] = self.deploy_parameters
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.import_tag_key is not None:
            result['ImportTagKey'] = self.import_tag_key
        if self.import_tag_value is not None:
            result['ImportTagValue'] = self.import_tag_value
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('CmsGroupId') is not None:
            self.cms_group_id = m.get('CmsGroupId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DeployParameters') is not None:
            self.deploy_parameters = m.get('DeployParameters')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImportTagKey') is not None:
            self.import_tag_key = m.get('ImportTagKey')
        if m.get('ImportTagValue') is not None:
            self.import_tag_value = m.get('ImportTagValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListApplicationGroupsResponseBody(TeaModel):
    def __init__(
        self,
        application_groups: List[ListApplicationGroupsResponseBodyApplicationGroups] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The details of the application group.
        self.application_groups = application_groups
        # The number of entries returned on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application_groups:
            for k in self.application_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationGroups'] = []
        if self.application_groups is not None:
            for k in self.application_groups:
                result['ApplicationGroups'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_groups = []
        if m.get('ApplicationGroups') is not None:
            for k in m.get('ApplicationGroups'):
                temp_model = ListApplicationGroupsResponseBodyApplicationGroups()
                self.application_groups.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListApplicationGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApplicationGroupsResponseBody = None,
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
            temp_model = ListApplicationGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsRequest(TeaModel):
    def __init__(
        self,
        application_type: str = None,
        max_results: int = None,
        name: str = None,
        names: str = None,
        next_token: str = None,
        region_id: str = None,
        tags: Dict[str, Any] = None,
    ):
        # The type of the application.
        self.application_type = application_type
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results
        # The name of the application.
        self.name = name
        # The names of the applications.
        self.names = names
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id
        # The tags.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.names is not None:
            result['Names'] = self.names
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListApplicationsShrinkRequest(TeaModel):
    def __init__(
        self,
        application_type: str = None,
        max_results: int = None,
        name: str = None,
        names: str = None,
        next_token: str = None,
        region_id: str = None,
        tags_shrink: str = None,
    ):
        # The type of the application.
        self.application_type = application_type
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results
        # The name of the application.
        self.name = name
        # The names of the applications.
        self.names = names
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id
        # The tags.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.names is not None:
            result['Names'] = self.names
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class ListApplicationsResponseBodyApplications(TeaModel):
    def __init__(
        self,
        application_type: str = None,
        create_date: str = None,
        description: str = None,
        name: str = None,
        resource_group_id: str = None,
        tags: Dict[str, Any] = None,
        update_date: str = None,
    ):
        # The type of the application.
        self.application_type = application_type
        # The time when the application was created.
        self.create_date = create_date
        # The description of the application.
        self.description = description
        # The name of the application.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # A tag of the resource.
        self.tags = tags
        # The time when the application was updated.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        applications: List[ListApplicationsResponseBodyApplications] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The applications.
        self.applications = applications
        # The number of entries returned per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApplicationsResponseBody = None,
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
            temp_model = ListApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExecutionLogsRequest(TeaModel):
    def __init__(
        self,
        execution_id: str = None,
        log_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        task_execution_id: str = None,
    ):
        # The ID of the execution.
        self.execution_id = execution_id
        # The type of the log.
        self.log_type = log_type
        # The number of entries to return on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the region in which you want to query the logs of the execution.
        self.region_id = region_id
        # The execution ID of the task.
        self.task_execution_id = task_execution_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        return self


class ListExecutionLogsResponseBodyExecutionLogs(TeaModel):
    def __init__(
        self,
        log_type: str = None,
        message: str = None,
        task_execution_id: str = None,
        timestamp: str = None,
    ):
        # The type of the log.
        self.log_type = log_type
        # The details of the task execution.
        self.message = message
        # The execution ID of the task.
        self.task_execution_id = task_execution_id
        # The timestamp when the task was run.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.message is not None:
            result['Message'] = self.message
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class ListExecutionLogsResponseBody(TeaModel):
    def __init__(
        self,
        execution_logs: List[ListExecutionLogsResponseBodyExecutionLogs] = None,
        is_truncated: bool = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The execution logs.
        self.execution_logs = execution_logs
        # Indicates whether the log is truncated.
        self.is_truncated = is_truncated
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.execution_logs:
            for k in self.execution_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExecutionLogs'] = []
        if self.execution_logs is not None:
            for k in self.execution_logs:
                result['ExecutionLogs'].append(k.to_map() if k else None)
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.execution_logs = []
        if m.get('ExecutionLogs') is not None:
            for k in m.get('ExecutionLogs'):
                temp_model = ListExecutionLogsResponseBodyExecutionLogs()
                self.execution_logs.append(temp_model.from_map(k))
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListExecutionLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExecutionLogsResponseBody = None,
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
            temp_model = ListExecutionLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExecutionRiskyTasksRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_name: str = None,
    ):
        # The ID of the region.
        self.region_id = region_id
        # The name of the template.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListExecutionRiskyTasksResponseBodyRiskyTasks(TeaModel):
    def __init__(
        self,
        api: str = None,
        service: str = None,
        task: List[str] = None,
        template: List[str] = None,
    ):
        # The name of the operation that the high-risk task calls.
        self.api = api
        # The cloud service in which the high-risk task runs.
        self.service = service
        # The details of the high-risk task.
        self.task = task
        # The details of templates to which the high-risk task belongs.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['API'] = self.api
        if self.service is not None:
            result['Service'] = self.service
        if self.task is not None:
            result['Task'] = self.task
        if self.template is not None:
            result['Template'] = self.template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('API') is not None:
            self.api = m.get('API')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('Task') is not None:
            self.task = m.get('Task')
        if m.get('Template') is not None:
            self.template = m.get('Template')
        return self


class ListExecutionRiskyTasksResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        risky_tasks: List[ListExecutionRiskyTasksResponseBodyRiskyTasks] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about high-risk tasks.
        self.risky_tasks = risky_tasks

    def validate(self):
        if self.risky_tasks:
            for k in self.risky_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RiskyTasks'] = []
        if self.risky_tasks is not None:
            for k in self.risky_tasks:
                result['RiskyTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.risky_tasks = []
        if m.get('RiskyTasks') is not None:
            for k in m.get('RiskyTasks'):
                temp_model = ListExecutionRiskyTasksResponseBodyRiskyTasks()
                self.risky_tasks.append(temp_model.from_map(k))
        return self


class ListExecutionRiskyTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExecutionRiskyTasksResponseBody = None,
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
            temp_model = ListExecutionRiskyTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExecutionsRequest(TeaModel):
    def __init__(
        self,
        categories: str = None,
        category: str = None,
        depth: str = None,
        description: str = None,
        end_date_after: str = None,
        end_date_before: str = None,
        executed_by: str = None,
        execution_id: str = None,
        include_child_execution: bool = None,
        max_results: int = None,
        mode: str = None,
        next_token: str = None,
        parent_execution_id: str = None,
        ram_role: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_template_name: str = None,
        sort_field: str = None,
        sort_order: str = None,
        start_date_after: str = None,
        start_date_before: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        template_name: str = None,
    ):
        # 执行的模板类型列表。可分为Other、TimerTrigger、EventTrigger、AlarmTrigger。此参数和Categories参数只能同时传入一个，推荐使用Categories。
        self.categories = categories
        # The type of the execution template. Valid values: Other, TimerTrigger, EventTrigger, and AlarmTrigger.
        self.category = category
        # 执行的深度，可分为RootDepth、FirstChildDepth
        # RootDepth只返回主执行，FirstChildDepth只返回第一层的子执行。此参数和IncludeChildExecution参数只能同时传入一个，推荐使用Depth。
        self.depth = depth
        self.description = description
        # The earliest end time. The executions that stop running at or later than the specified time are queried.
        self.end_date_after = end_date_after
        # The latest end time. The executions that stop running at or earlier than the specified time are queried.
        self.end_date_before = end_date_before
        # The executor.
        self.executed_by = executed_by
        # The ID of the execution.
        self.execution_id = execution_id
        # Specifies whether to include child executions. Default value: False.
        self.include_child_execution = include_child_execution
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results
        # The execution mode. Valid values:
        # 
        # *   **Automatic**\
        # *   **Debug**\
        self.mode = mode
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id
        # The RAM role.
        self.ram_role = ram_role
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group to which the instances you want to query belong.
        self.resource_group_id = resource_group_id
        # The ID of the Elastic Compute Service (ECS) resource.
        self.resource_id = resource_id
        # The name of the resource template.
        self.resource_template_name = resource_template_name
        # The field that is used to sort the executions to query. Valid values:
        # 
        # *   **StartDate**: specifies that the executions are sorted based on the time when they are created. This is the default value.
        # *   **EndDate**: specifies that the executions are sorted based on the time when they stop running.
        # *   **Status**: specifies that the executions are sorted based on their states.
        self.sort_field = sort_field
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **Ascending**: ascending order.
        # *   **Descending**: descending order. This is the default value.
        self.sort_order = sort_order
        # The earliest start time. The executions that start to run at or later than the specified time are queried.
        self.start_date_after = start_date_after
        # The latest start time. The executions that start to run at or earlier than the specified point in time are queried.
        self.start_date_before = start_date_before
        # The status of the execution. Valid values: Running, Started, Success, Failed, Waiting, Cancelled, Pending, and Skipped.
        self.status = status
        # The tags for the execution.
        self.tags = tags
        # The name of the template. All templates whose names contain the specified template name are queried.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.category is not None:
            result['Category'] = self.category
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.description is not None:
            result['Description'] = self.description
        if self.end_date_after is not None:
            result['EndDateAfter'] = self.end_date_after
        if self.end_date_before is not None:
            result['EndDateBefore'] = self.end_date_before
        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.include_child_execution is not None:
            result['IncludeChildExecution'] = self.include_child_execution
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_template_name is not None:
            result['ResourceTemplateName'] = self.resource_template_name
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_date_after is not None:
            result['StartDateAfter'] = self.start_date_after
        if self.start_date_before is not None:
            result['StartDateBefore'] = self.start_date_before
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndDateAfter') is not None:
            self.end_date_after = m.get('EndDateAfter')
        if m.get('EndDateBefore') is not None:
            self.end_date_before = m.get('EndDateBefore')
        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('IncludeChildExecution') is not None:
            self.include_child_execution = m.get('IncludeChildExecution')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceTemplateName') is not None:
            self.resource_template_name = m.get('ResourceTemplateName')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartDateAfter') is not None:
            self.start_date_after = m.get('StartDateAfter')
        if m.get('StartDateBefore') is not None:
            self.start_date_before = m.get('StartDateBefore')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListExecutionsShrinkRequest(TeaModel):
    def __init__(
        self,
        categories: str = None,
        category: str = None,
        depth: str = None,
        description: str = None,
        end_date_after: str = None,
        end_date_before: str = None,
        executed_by: str = None,
        execution_id: str = None,
        include_child_execution: bool = None,
        max_results: int = None,
        mode: str = None,
        next_token: str = None,
        parent_execution_id: str = None,
        ram_role: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_template_name: str = None,
        sort_field: str = None,
        sort_order: str = None,
        start_date_after: str = None,
        start_date_before: str = None,
        status: str = None,
        tags_shrink: str = None,
        template_name: str = None,
    ):
        # 执行的模板类型列表。可分为Other、TimerTrigger、EventTrigger、AlarmTrigger。此参数和Categories参数只能同时传入一个，推荐使用Categories。
        self.categories = categories
        # The type of the execution template. Valid values: Other, TimerTrigger, EventTrigger, and AlarmTrigger.
        self.category = category
        # 执行的深度，可分为RootDepth、FirstChildDepth
        # RootDepth只返回主执行，FirstChildDepth只返回第一层的子执行。此参数和IncludeChildExecution参数只能同时传入一个，推荐使用Depth。
        self.depth = depth
        self.description = description
        # The earliest end time. The executions that stop running at or later than the specified time are queried.
        self.end_date_after = end_date_after
        # The latest end time. The executions that stop running at or earlier than the specified time are queried.
        self.end_date_before = end_date_before
        # The executor.
        self.executed_by = executed_by
        # The ID of the execution.
        self.execution_id = execution_id
        # Specifies whether to include child executions. Default value: False.
        self.include_child_execution = include_child_execution
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results
        # The execution mode. Valid values:
        # 
        # *   **Automatic**\
        # *   **Debug**\
        self.mode = mode
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id
        # The RAM role.
        self.ram_role = ram_role
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group to which the instances you want to query belong.
        self.resource_group_id = resource_group_id
        # The ID of the Elastic Compute Service (ECS) resource.
        self.resource_id = resource_id
        # The name of the resource template.
        self.resource_template_name = resource_template_name
        # The field that is used to sort the executions to query. Valid values:
        # 
        # *   **StartDate**: specifies that the executions are sorted based on the time when they are created. This is the default value.
        # *   **EndDate**: specifies that the executions are sorted based on the time when they stop running.
        # *   **Status**: specifies that the executions are sorted based on their states.
        self.sort_field = sort_field
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **Ascending**: ascending order.
        # *   **Descending**: descending order. This is the default value.
        self.sort_order = sort_order
        # The earliest start time. The executions that start to run at or later than the specified time are queried.
        self.start_date_after = start_date_after
        # The latest start time. The executions that start to run at or earlier than the specified point in time are queried.
        self.start_date_before = start_date_before
        # The status of the execution. Valid values: Running, Started, Success, Failed, Waiting, Cancelled, Pending, and Skipped.
        self.status = status
        # The tags for the execution.
        self.tags_shrink = tags_shrink
        # The name of the template. All templates whose names contain the specified template name are queried.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.category is not None:
            result['Category'] = self.category
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.description is not None:
            result['Description'] = self.description
        if self.end_date_after is not None:
            result['EndDateAfter'] = self.end_date_after
        if self.end_date_before is not None:
            result['EndDateBefore'] = self.end_date_before
        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.include_child_execution is not None:
            result['IncludeChildExecution'] = self.include_child_execution
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_template_name is not None:
            result['ResourceTemplateName'] = self.resource_template_name
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_date_after is not None:
            result['StartDateAfter'] = self.start_date_after
        if self.start_date_before is not None:
            result['StartDateBefore'] = self.start_date_before
        if self.status is not None:
            result['Status'] = self.status
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndDateAfter') is not None:
            self.end_date_after = m.get('EndDateAfter')
        if m.get('EndDateBefore') is not None:
            self.end_date_before = m.get('EndDateBefore')
        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('IncludeChildExecution') is not None:
            self.include_child_execution = m.get('IncludeChildExecution')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceTemplateName') is not None:
            self.resource_template_name = m.get('ResourceTemplateName')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartDateAfter') is not None:
            self.start_date_after = m.get('StartDateAfter')
        if m.get('StartDateBefore') is not None:
            self.start_date_before = m.get('StartDateBefore')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListExecutionsResponseBodyExecutionsCurrentTasks(TeaModel):
    def __init__(
        self,
        task_action: str = None,
        task_execution_id: str = None,
        task_name: str = None,
    ):
        # The execution template of the task.
        self.task_action = task_action
        # The ID of the task execution.
        self.task_execution_id = task_execution_id
        # The name of the task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListExecutionsResponseBodyExecutions(TeaModel):
    def __init__(
        self,
        category: str = None,
        counters: Dict[str, Any] = None,
        create_date: str = None,
        current_tasks: List[ListExecutionsResponseBodyExecutionsCurrentTasks] = None,
        description: str = None,
        end_date: str = None,
        executed_by: str = None,
        execution_id: str = None,
        is_parent: bool = None,
        last_successful_trigger_time: str = None,
        last_trigger_outputs: str = None,
        last_trigger_status: str = None,
        last_trigger_status_message: str = None,
        last_trigger_time: str = None,
        mode: str = None,
        outputs: str = None,
        parameters: Dict[str, Any] = None,
        parent_execution_id: str = None,
        ram_role: str = None,
        resource_group_id: str = None,
        resource_status: str = None,
        safety_check: str = None,
        start_date: str = None,
        status: str = None,
        status_message: str = None,
        status_reason: str = None,
        tags: Dict[str, Any] = None,
        targets: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        update_date: str = None,
        waiting_status: str = None,
    ):
        # The type of the execution template. Valid values: Other, TimerTrigger, EventTrigger, and AlarmTrigger.
        self.category = category
        # The number of tasks that are counted by execution status.
        self.counters = counters
        # The time when the execution was created.
        self.create_date = create_date
        # The information about the tasks that are running.
        self.current_tasks = current_tasks
        # The description of the execution.
        self.description = description
        # The time when the execution stops running.
        self.end_date = end_date
        # The account ID of the user who started the execution of the template.
        self.executed_by = executed_by
        # The unique ID of the execution.
        self.execution_id = execution_id
        # Indicates whether the execution contains child executions.
        self.is_parent = is_parent
        # The time when the template was last successfully triggered.
        self.last_successful_trigger_time = last_successful_trigger_time
        self.last_trigger_outputs = last_trigger_outputs
        # The status of the execution after the template was last triggered.
        self.last_trigger_status = last_trigger_status
        self.last_trigger_status_message = last_trigger_status_message
        # The time when the template was last successfully triggered.
        self.last_trigger_time = last_trigger_time
        # The execution mode.
        self.mode = mode
        # The output of the execution.
        self.outputs = outputs
        # The input parameters of the execution.
        self.parameters = parameters
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id
        # The role that started the execution of the template.
        self.ram_role = ram_role
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the resource.
        self.resource_status = resource_status
        # The security check mode. Valid values: Skip, and ConfirmEveryHighRiskAction.
        self.safety_check = safety_check
        # The time when the execution was started.
        self.start_date = start_date
        # The status of the execution. Valid values: Started, Queued, Running, Waiting, Success, Failed, and Cancelled.
        self.status = status
        # The status of the task execution.
        self.status_message = status_message
        # The reason for which the status occurs.
        self.status_reason = status_reason
        # The tags of the execution.
        self.tags = tags
        # The target resource.
        self.targets = targets
        # The ID of the template.
        self.template_id = template_id
        # The name of the template.
        self.template_name = template_name
        # The version number of the template.
        self.template_version = template_version
        # The time when the execution was updated.
        self.update_date = update_date
        # The Waiting state.
        self.waiting_status = waiting_status

    def validate(self):
        if self.current_tasks:
            for k in self.current_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.counters is not None:
            result['Counters'] = self.counters
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        result['CurrentTasks'] = []
        if self.current_tasks is not None:
            for k in self.current_tasks:
                result['CurrentTasks'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.is_parent is not None:
            result['IsParent'] = self.is_parent
        if self.last_successful_trigger_time is not None:
            result['LastSuccessfulTriggerTime'] = self.last_successful_trigger_time
        if self.last_trigger_outputs is not None:
            result['LastTriggerOutputs'] = self.last_trigger_outputs
        if self.last_trigger_status is not None:
            result['LastTriggerStatus'] = self.last_trigger_status
        if self.last_trigger_status_message is not None:
            result['LastTriggerStatusMessage'] = self.last_trigger_status_message
        if self.last_trigger_time is not None:
            result['LastTriggerTime'] = self.last_trigger_time
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.targets is not None:
            result['Targets'] = self.targets
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        if self.waiting_status is not None:
            result['WaitingStatus'] = self.waiting_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Counters') is not None:
            self.counters = m.get('Counters')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        self.current_tasks = []
        if m.get('CurrentTasks') is not None:
            for k in m.get('CurrentTasks'):
                temp_model = ListExecutionsResponseBodyExecutionsCurrentTasks()
                self.current_tasks.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('IsParent') is not None:
            self.is_parent = m.get('IsParent')
        if m.get('LastSuccessfulTriggerTime') is not None:
            self.last_successful_trigger_time = m.get('LastSuccessfulTriggerTime')
        if m.get('LastTriggerOutputs') is not None:
            self.last_trigger_outputs = m.get('LastTriggerOutputs')
        if m.get('LastTriggerStatus') is not None:
            self.last_trigger_status = m.get('LastTriggerStatus')
        if m.get('LastTriggerStatusMessage') is not None:
            self.last_trigger_status_message = m.get('LastTriggerStatusMessage')
        if m.get('LastTriggerTime') is not None:
            self.last_trigger_time = m.get('LastTriggerTime')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        if m.get('WaitingStatus') is not None:
            self.waiting_status = m.get('WaitingStatus')
        return self


class ListExecutionsResponseBody(TeaModel):
    def __init__(
        self,
        executions: List[ListExecutionsResponseBodyExecutions] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The details of the task executions.
        self.executions = executions
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.executions:
            for k in self.executions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Executions'] = []
        if self.executions is not None:
            for k in self.executions:
                result['Executions'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.executions = []
        if m.get('Executions') is not None:
            for k in m.get('Executions'):
                temp_model = ListExecutionsResponseBodyExecutions()
                self.executions.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListExecutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExecutionsResponseBody = None,
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
            temp_model = ListExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancePatchStatesRequest(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The token that is used to retrieve the next page of results.
        self.instance_ids = instance_ids
        # The token that is used to retrieve the next page of results.
        self.max_results = max_results
        # The ID of the Elastic Compute Service (ECS) instance. The value can be a JSON array that consists of up to 100 instance IDs. Separate the instance IDs with commas (,).
        self.next_token = next_token
        # The number of entries to return on each page.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListInstancePatchStatesResponseBodyInstancePatchStates(TeaModel):
    def __init__(
        self,
        baseline_id: str = None,
        failed_count: str = None,
        installed_count: str = None,
        installed_other_count: str = None,
        installed_pending_reboot_count: str = None,
        installed_rejected_count: str = None,
        instance_id: str = None,
        missing_count: str = None,
        operation_end_time: str = None,
        operation_start_time: str = None,
        operation_type: str = None,
        owner_information: str = None,
        patch_group: str = None,
    ):
        # The number of patches that have been installed but require a restart to take effect.
        self.baseline_id = baseline_id
        # The ID of the patch baseline.
        self.failed_count = failed_count
        # Queries patches of an instance.
        self.installed_count = installed_count
        # The ID of the ECS instance.
        self.installed_other_count = installed_other_count
        # The number of patches that are rejected by the user.
        self.installed_pending_reboot_count = installed_pending_reboot_count
        # The patch group.
        self.installed_rejected_count = installed_rejected_count
        # The operation type.
        self.instance_id = instance_id
        # The time when the operation ended.
        self.missing_count = missing_count
        # The information about the user.
        self.operation_end_time = operation_end_time
        # The number of patches that failed to be installed.
        self.operation_start_time = operation_start_time
        # The time when the operation was initiated.
        self.operation_type = operation_type
        # The number of patches that do not meet the baseline.
        self.owner_information = owner_information
        # The number of installed patches.
        self.patch_group = patch_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.installed_count is not None:
            result['InstalledCount'] = self.installed_count
        if self.installed_other_count is not None:
            result['InstalledOtherCount'] = self.installed_other_count
        if self.installed_pending_reboot_count is not None:
            result['InstalledPendingRebootCount'] = self.installed_pending_reboot_count
        if self.installed_rejected_count is not None:
            result['InstalledRejectedCount'] = self.installed_rejected_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.missing_count is not None:
            result['MissingCount'] = self.missing_count
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.owner_information is not None:
            result['OwnerInformation'] = self.owner_information
        if self.patch_group is not None:
            result['PatchGroup'] = self.patch_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('InstalledCount') is not None:
            self.installed_count = m.get('InstalledCount')
        if m.get('InstalledOtherCount') is not None:
            self.installed_other_count = m.get('InstalledOtherCount')
        if m.get('InstalledPendingRebootCount') is not None:
            self.installed_pending_reboot_count = m.get('InstalledPendingRebootCount')
        if m.get('InstalledRejectedCount') is not None:
            self.installed_rejected_count = m.get('InstalledRejectedCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MissingCount') is not None:
            self.missing_count = m.get('MissingCount')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OwnerInformation') is not None:
            self.owner_information = m.get('OwnerInformation')
        if m.get('PatchGroup') is not None:
            self.patch_group = m.get('PatchGroup')
        return self


class ListInstancePatchStatesResponseBody(TeaModel):
    def __init__(
        self,
        instance_patch_states: List[ListInstancePatchStatesResponseBodyInstancePatchStates] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The number of patches that are not installed.
        self.instance_patch_states = instance_patch_states
        # The details of patches of the instance.
        self.max_results = max_results
        # The ID of the request.
        self.next_token = next_token
        # The number of entries returned on each page.
        self.request_id = request_id

    def validate(self):
        if self.instance_patch_states:
            for k in self.instance_patch_states:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstancePatchStates'] = []
        if self.instance_patch_states is not None:
            for k in self.instance_patch_states:
                result['InstancePatchStates'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_patch_states = []
        if m.get('InstancePatchStates') is not None:
            for k in m.get('InstancePatchStates'):
                temp_model = ListInstancePatchStatesResponseBodyInstancePatchStates()
                self.instance_patch_states.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstancePatchStatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancePatchStatesResponseBody = None,
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
            temp_model = ListInstancePatchStatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancePatchesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        patch_statuses: str = None,
        region_id: str = None,
    ):
        # The number of entries to return on each page.
        self.instance_id = instance_id
        # The token that is used to retrieve the next page of results.
        self.max_results = max_results
        # MTRBMDc0NjAtRUJFNy00N0NBLTk3NTctMTJDQzQ
        self.next_token = next_token
        # The token that is used to retrieve the next page of results.
        self.patch_statuses = patch_statuses
        # The ID of the instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.patch_statuses is not None:
            result['PatchStatuses'] = self.patch_statuses
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PatchStatuses') is not None:
            self.patch_statuses = m.get('PatchStatuses')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListInstancePatchesResponseBodyPatches(TeaModel):
    def __init__(
        self,
        classification: str = None,
        installed_time: str = None,
        kbid: str = None,
        severity: str = None,
        status: str = None,
        title: str = None,
    ):
        # Queries the patches of an instance.
        self.classification = classification
        # The name of the patch.
        self.installed_time = installed_time
        # KBId
        self.kbid = kbid
        # The status of the installation.
        self.severity = severity
        # The time when the patch was installed.
        self.status = status
        # The classification of the patch.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classification is not None:
            result['Classification'] = self.classification
        if self.installed_time is not None:
            result['InstalledTime'] = self.installed_time
        if self.kbid is not None:
            result['KBId'] = self.kbid
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classification') is not None:
            self.classification = m.get('Classification')
        if m.get('InstalledTime') is not None:
            self.installed_time = m.get('InstalledTime')
        if m.get('KBId') is not None:
            self.kbid = m.get('KBId')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListInstancePatchesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        patches: List[ListInstancePatchesResponseBodyPatches] = None,
        request_id: str = None,
    ):
        # The information about the patch.
        self.max_results = max_results
        # MTRBMDc0NjAtRUJFNy00N0NBLTk3NTctMTJDQzQ
        self.next_token = next_token
        # The level of the severity.
        self.patches = patches
        # The number of entries returned on each page.
        self.request_id = request_id

    def validate(self):
        if self.patches:
            for k in self.patches:
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
        result['Patches'] = []
        if self.patches is not None:
            for k in self.patches:
                result['Patches'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.patches = []
        if m.get('Patches') is not None:
            for k in m.get('Patches'):
                temp_model = ListInstancePatchesResponseBodyPatches()
                self.patches.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstancePatchesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancePatchesResponseBody = None,
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
            temp_model = ListInstancePatchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInventoryEntriesRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        # The name of the component property. Valid values of N: 1 to 5.
        self.name = name
        # The comparison operator that is used to filter property values. Valid values of N: 1 to 5. Valid values:
        # 
        # *   Equal
        # *   NotEqual
        # *   BeginWith
        # *   LessThan
        # *   GreaterThan
        self.operator = operator
        # The values of properties. Valid values of the first N: 1 to 5. Valid values of the second N: 1 to 20.
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
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListInventoryEntriesRequest(TeaModel):
    def __init__(
        self,
        filter: List[ListInventoryEntriesRequestFilter] = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        type_name: str = None,
    ):
        # The filter rules for the component.
        self.filter = filter
        # The ID of the instance.
        self.instance_id = instance_id
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The ID of the region in which the instance resides.
        self.region_id = region_id
        # The name of the component. Valid values:
        # 
        # *   ACS:InstanceInformation
        # *   ACS:Application
        # *   ACS:File
        # *   ACS:Network
        # *   ACS:WindowsRole
        # *   ACS:Service
        # *   ACS:WindowsRegistry
        # *   ACS:WindowsUpdate
        self.type_name = type_name

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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListInventoryEntriesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class ListInventoryEntriesResponseBody(TeaModel):
    def __init__(
        self,
        capture_time: str = None,
        entries: List[Dict[str, Any]] = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        schema_version: str = None,
        type_name: str = None,
    ):
        # The time when the request was sent.
        self.capture_time = capture_time
        # The configurations of the component.
        self.entries = entries
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The number of entries returned per page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The version number of the component.
        self.schema_version = schema_version
        # The name of the component.
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capture_time is not None:
            result['CaptureTime'] = self.capture_time
        if self.entries is not None:
            result['Entries'] = self.entries
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaptureTime') is not None:
            self.capture_time = m.get('CaptureTime')
        if m.get('Entries') is not None:
            self.entries = m.get('Entries')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class ListInventoryEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInventoryEntriesResponseBody = None,
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
            temp_model = ListInventoryEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOpsItemsRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        self.name = name
        self.operator = operator
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
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListOpsItemsRequest(TeaModel):
    def __init__(
        self,
        filter: List[ListOpsItemsRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_tags: Dict[str, Any] = None,
        tags: Dict[str, Any] = None,
    ):
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.resource_tags = resource_tags
        self.tags = tags

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_tags is not None:
            result['ResourceTags'] = self.resource_tags
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListOpsItemsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceTags') is not None:
            self.resource_tags = m.get('ResourceTags')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListOpsItemsShrinkRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        self.name = name
        self.operator = operator
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
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListOpsItemsShrinkRequest(TeaModel):
    def __init__(
        self,
        filter: List[ListOpsItemsShrinkRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_tags_shrink: str = None,
        tags_shrink: str = None,
    ):
        self.filter = filter
        self.max_results = max_results
        self.next_token = next_token
        self.region_id = region_id
        self.resource_tags_shrink = resource_tags_shrink
        self.tags_shrink = tags_shrink

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_tags_shrink is not None:
            result['ResourceTags'] = self.resource_tags_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListOpsItemsShrinkRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceTags') is not None:
            self.resource_tags_shrink = m.get('ResourceTags')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class ListOpsItemsResponseBodyOpsItems(TeaModel):
    def __init__(
        self,
        category: str = None,
        create_date: str = None,
        ops_item_id: str = None,
        priority: int = None,
        resources: List[str] = None,
        severity: str = None,
        source: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        title: str = None,
        update_date: str = None,
    ):
        self.category = category
        self.create_date = create_date
        self.ops_item_id = ops_item_id
        self.priority = priority
        self.resources = resources
        self.severity = severity
        self.source = source
        self.status = status
        self.tags = tags
        self.title = title
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListOpsItemsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        ops_items: List[ListOpsItemsResponseBodyOpsItems] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.ops_items = ops_items
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.ops_items:
            for k in self.ops_items:
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
        result['OpsItems'] = []
        if self.ops_items is not None:
            for k in self.ops_items:
                result['OpsItems'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.ops_items = []
        if m.get('OpsItems') is not None:
            for k in m.get('OpsItems'):
                temp_model = ListOpsItemsResponseBodyOpsItems()
                self.ops_items.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOpsItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOpsItemsResponseBody = None,
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
            temp_model = ListOpsItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParameterVersionsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        region_id: str = None,
        share_type: str = None,
    ):
        # The share type of the common parameter.
        self.max_results = max_results
        # The pagination token.
        self.name = name
        # The data type of the common parameter.
        self.next_token = next_token
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.region_id = region_id
        # The pagination token.
        self.share_type = share_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        return self


class ListParameterVersionsResponseBodyParameterVersions(TeaModel):
    def __init__(
        self,
        parameter_version: int = None,
        updated_by: str = None,
        updated_date: str = None,
        value: str = None,
    ):
        # The time when the common parameter was updated.
        self.parameter_version = parameter_version
        # Queries versions of a common parameter.
        self.updated_by = updated_by
        # ## Debugging
        # 
        # [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=oos\&api=ListParameterVersions\&type=RPC\&version=2019-06-01)
        self.updated_date = updated_date
        # The user who updated the common parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListParameterVersionsResponseBody(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        parameter_versions: List[ListParameterVersionsResponseBodyParameterVersions] = None,
        request_id: str = None,
        total_count: int = None,
        type: str = None,
    ):
        # The name of the common parameter.
        self.created_by = created_by
        # The total number of entries returned.
        self.created_date = created_date
        # The user who created the common parameter.
        self.description = description
        # The version number of the common parameter.
        self.id = id
        # The time when the common parameter was created.
        self.max_results = max_results
        # The ID of the common parameter.
        self.name = name
        # The description of the common parameter.
        self.next_token = next_token
        # The value of the common parameter.
        self.parameter_versions = parameter_versions
        # The number of entries returned per page.
        self.request_id = request_id
        # The version information of the common parameter.
        self.total_count = total_count
        # The ID of the request.
        self.type = type

    def validate(self):
        if self.parameter_versions:
            for k in self.parameter_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['ParameterVersions'] = []
        if self.parameter_versions is not None:
            for k in self.parameter_versions:
                result['ParameterVersions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.parameter_versions = []
        if m.get('ParameterVersions') is not None:
            for k in m.get('ParameterVersions'):
                temp_model = ListParameterVersionsResponseBodyParameterVersions()
                self.parameter_versions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListParameterVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListParameterVersionsResponseBody = None,
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
            temp_model = ListParameterVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListParametersRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        path: str = None,
        recursive: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        sort_field: str = None,
        sort_order: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
    ):
        self.max_results = max_results
        self.name = name
        self.next_token = next_token
        self.path = path
        self.recursive = recursive
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.share_type = share_type
        self.sort_field = sort_field
        self.sort_order = sort_order
        self.tags = tags
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListParametersShrinkRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        path: str = None,
        recursive: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        sort_field: str = None,
        sort_order: str = None,
        tags_shrink: str = None,
        type: str = None,
    ):
        self.max_results = max_results
        self.name = name
        self.next_token = next_token
        self.path = path
        self.recursive = recursive
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.share_type = share_type
        self.sort_field = sort_field
        self.sort_order = sort_order
        self.tags_shrink = tags_shrink
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListParametersResponseBodyParameters(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        parameter_version: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.created_by = created_by
        self.created_date = created_date
        self.description = description
        self.id = id
        self.name = name
        self.parameter_version = parameter_version
        self.resource_group_id = resource_group_id
        self.share_type = share_type
        self.tags = tags
        self.type = type
        self.updated_by = updated_by
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class ListParametersResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        parameters: List[ListParametersResponseBodyParameters] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.parameters = parameters
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.parameters:
            for k in self.parameters:
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
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = ListParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListParametersResponseBody = None,
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
            temp_model = ListParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPatchBaselinesRequestTags(TeaModel):
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


class ListPatchBaselinesRequest(TeaModel):
    def __init__(
        self,
        approved_patches: List[str] = None,
        approved_patches_enable_non_security: bool = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        operation_system: str = None,
        region_id: str = None,
        share_type: str = None,
        sources: List[str] = None,
        tags: List[ListPatchBaselinesRequestTags] = None,
    ):
        self.approved_patches = approved_patches
        self.approved_patches_enable_non_security = approved_patches_enable_non_security
        # The token that is used to retrieve the next page of results.
        self.max_results = max_results
        # The share type of the patch baseline.
        self.name = name
        # The ID of the request.
        self.next_token = next_token
        # The number of entries to return on each page.
        self.operation_system = operation_system
        # The type of the operating system. Valid values:
        # 
        # *   AliyunLinux
        # *   Windows
        # *   Ubuntu
        # *   Centos
        # *   Debian
        # *   RedhatEnterpriseLinux
        # *   Anolis
        self.region_id = region_id
        # The token that is used to retrieve the next page of results.
        self.share_type = share_type
        self.sources = sources
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
        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListPatchBaselinesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListPatchBaselinesShrinkRequest(TeaModel):
    def __init__(
        self,
        approved_patches_shrink: str = None,
        approved_patches_enable_non_security: bool = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        operation_system: str = None,
        region_id: str = None,
        share_type: str = None,
        sources_shrink: str = None,
        tags_shrink: str = None,
    ):
        self.approved_patches_shrink = approved_patches_shrink
        self.approved_patches_enable_non_security = approved_patches_enable_non_security
        # The token that is used to retrieve the next page of results.
        self.max_results = max_results
        # The share type of the patch baseline.
        self.name = name
        # The ID of the request.
        self.next_token = next_token
        # The number of entries to return on each page.
        self.operation_system = operation_system
        # The type of the operating system. Valid values:
        # 
        # *   AliyunLinux
        # *   Windows
        # *   Ubuntu
        # *   Centos
        # *   Debian
        # *   RedhatEnterpriseLinux
        # *   Anolis
        self.region_id = region_id
        # The token that is used to retrieve the next page of results.
        self.share_type = share_type
        self.sources_shrink = sources_shrink
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approved_patches_shrink is not None:
            result['ApprovedPatches'] = self.approved_patches_shrink
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovedPatches') is not None:
            self.approved_patches_shrink = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class ListPatchBaselinesResponseBodyPatchBaselinesTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListPatchBaselinesResponseBodyPatchBaselines(TeaModel):
    def __init__(
        self,
        approved_patches: List[str] = None,
        approved_patches_enable_non_security: bool = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        is_default: bool = None,
        name: str = None,
        operation_system: str = None,
        share_type: str = None,
        sources: List[str] = None,
        tags: List[ListPatchBaselinesResponseBodyPatchBaselinesTags] = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        self.approved_patches = approved_patches
        self.approved_patches_enable_non_security = approved_patches_enable_non_security
        # The name of the patch baseline.
        self.created_by = created_by
        # The ID of the patch baseline.
        self.created_date = created_date
        # The user who last modified the patch baseline.
        self.description = description
        # Queries the details of patch baselines.
        self.id = id
        # The time when the patch baseline was last modified.
        self.is_default = is_default
        # The share type of the patch baseline.
        self.name = name
        # The description of the patch baseline.
        self.operation_system = operation_system
        # Queries the details of patch baselines.
        self.share_type = share_type
        self.sources = sources
        self.tags = tags
        # The time when the patch baseline was created.
        self.updated_by = updated_by
        # The creator of the patch baseline.
        self.updated_date = updated_date

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
        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListPatchBaselinesResponseBodyPatchBaselinesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class ListPatchBaselinesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        patch_baselines: List[ListPatchBaselinesResponseBodyPatchBaselines] = None,
        request_id: str = None,
    ):
        # The type of the operating system.
        self.max_results = max_results
        # gAAAAABfTgv5ewUWmNdJ3g7JVLvX70sPH90GZOVGC
        self.next_token = next_token
        # Indicates whether the patch baseline is set as the default patch baseline.
        self.patch_baselines = patch_baselines
        # The details of the patch baselines.
        self.request_id = request_id

    def validate(self):
        if self.patch_baselines:
            for k in self.patch_baselines:
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
        result['PatchBaselines'] = []
        if self.patch_baselines is not None:
            for k in self.patch_baselines:
                result['PatchBaselines'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.patch_baselines = []
        if m.get('PatchBaselines') is not None:
            for k in m.get('PatchBaselines'):
                temp_model = ListPatchBaselinesResponseBodyPatchBaselines()
                self.patch_baselines.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPatchBaselinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPatchBaselinesResponseBody = None,
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
            temp_model = ListPatchBaselinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceExecutionStatusRequest(TeaModel):
    def __init__(
        self,
        execution_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The ID of the execution.
        self.execution_id = execution_id
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListResourceExecutionStatusResponseBodyResourceExecutionStatus(TeaModel):
    def __init__(
        self,
        execution_id: str = None,
        execution_time: str = None,
        outputs: str = None,
        resource_id: str = None,
        status: str = None,
    ):
        # The ID of the execution.
        self.execution_id = execution_id
        # The time when the execution started running.
        self.execution_time = execution_time
        # The output of the template.
        self.outputs = outputs
        # The ID of the resource.
        self.resource_id = resource_id
        # The status of the execution.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListResourceExecutionStatusResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resource_execution_status: List[ListResourceExecutionStatusResponseBodyResourceExecutionStatus] = None,
    ):
        # The number of entries returned on each page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The execution information of the resource.
        self.resource_execution_status = resource_execution_status

    def validate(self):
        if self.resource_execution_status:
            for k in self.resource_execution_status:
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
        result['ResourceExecutionStatus'] = []
        if self.resource_execution_status is not None:
            for k in self.resource_execution_status:
                result['ResourceExecutionStatus'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_execution_status = []
        if m.get('ResourceExecutionStatus') is not None:
            for k in m.get('ResourceExecutionStatus'):
                temp_model = ListResourceExecutionStatusResponseBodyResourceExecutionStatus()
                self.resource_execution_status.append(temp_model.from_map(k))
        return self


class ListResourceExecutionStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceExecutionStatusResponseBody = None,
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
            temp_model = ListResourceExecutionStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecretParameterVersionsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        region_id: str = None,
        share_type: str = None,
        with_decryption: bool = None,
    ):
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results
        # The name of the encryption parameter.
        self.name = name
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id
        # The share type of the encryption parameter.
        self.share_type = share_type
        # Specifies whether to decrypt the parameter value. The decrypted parameter value is returned only if this parameter is set to true. Otherwise, null is returned.
        self.with_decryption = with_decryption

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')
        return self


class ListSecretParameterVersionsResponseBodyParameterVersions(TeaModel):
    def __init__(
        self,
        parameter_version: int = None,
        updated_by: str = None,
        updated_date: str = None,
        value: str = None,
    ):
        # The version number of the encryption parameter.
        self.parameter_version = parameter_version
        # The user who updated the encryption parameter.
        self.updated_by = updated_by
        # The time when the encryption parameter was updated.
        self.updated_date = updated_date
        # The value of the encryption parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListSecretParameterVersionsResponseBody(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        parameter_versions: List[ListSecretParameterVersionsResponseBodyParameterVersions] = None,
        request_id: str = None,
        total_count: int = None,
        type: str = None,
    ):
        # The user who created the encryption parameter.
        self.created_by = created_by
        # The time when the encryption parameter was created.
        self.created_date = created_date
        # The description of the encryption parameter.
        self.description = description
        # The ID of the encryption parameter.
        self.id = id
        # The number of entries returned per page.
        self.max_results = max_results
        # The name of the encryption parameter.
        self.name = name
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The information about the version of the encryption parameter.
        self.parameter_versions = parameter_versions
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The type of the encryption parameter.
        self.type = type

    def validate(self):
        if self.parameter_versions:
            for k in self.parameter_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['ParameterVersions'] = []
        if self.parameter_versions is not None:
            for k in self.parameter_versions:
                result['ParameterVersions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.parameter_versions = []
        if m.get('ParameterVersions') is not None:
            for k in m.get('ParameterVersions'):
                temp_model = ListSecretParameterVersionsResponseBodyParameterVersions()
                self.parameter_versions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListSecretParameterVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSecretParameterVersionsResponseBody = None,
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
            temp_model = ListSecretParameterVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecretParametersRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        path: str = None,
        recursive: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        sort_field: str = None,
        sort_order: str = None,
        tags: Dict[str, Any] = None,
    ):
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results
        # The name of the parameter. **You can enter a keyword to query parameter names in fuzzy match mode.
        self.name = name
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The path of the parameter. For example, if the name of a parameter is /path/path1/Myparameter, the path of the parameter is /path/path1/.
        self.path = path
        # Specifies whether to query parameters from all levels of directories in the specified path. Default value: false.
        self.recursive = recursive
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The field used to sort the query results. Valid values:
        # 
        # *   Name
        # *   CreatedDate
        self.sort_field = sort_field
        # The order in which the entries are sorted. Valid values:
        # 
        # *   Ascending
        # *   Descending (Default)
        self.sort_order = sort_order
        # The tags of the parameter.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListSecretParametersShrinkRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        path: str = None,
        recursive: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        sort_field: str = None,
        sort_order: str = None,
        tags_shrink: str = None,
    ):
        # The number of entries to return on each page. Valid values: 10 to 100. Default value: 50.
        self.max_results = max_results
        # The name of the parameter. **You can enter a keyword to query parameter names in fuzzy match mode.
        self.name = name
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The path of the parameter. For example, if the name of a parameter is /path/path1/Myparameter, the path of the parameter is /path/path1/.
        self.path = path
        # Specifies whether to query parameters from all levels of directories in the specified path. Default value: false.
        self.recursive = recursive
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The field used to sort the query results. Valid values:
        # 
        # *   Name
        # *   CreatedDate
        self.sort_field = sort_field
        # The order in which the entries are sorted. Valid values:
        # 
        # *   Ascending
        # *   Descending (Default)
        self.sort_order = sort_order
        # The tags of the parameter.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.path is not None:
            result['Path'] = self.path
        if self.recursive is not None:
            result['Recursive'] = self.recursive
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Recursive') is not None:
            self.recursive = m.get('Recursive')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class ListSecretParametersResponseBodyParameters(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        key_id: str = None,
        name: str = None,
        parameter_version: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The user who created the parameter.
        self.created_by = created_by
        # The time when the parameter was created.
        self.created_date = created_date
        # The description of the parameter.
        self.description = description
        # The ID of the parameter.
        self.id = id
        # The ID of the KMS customer master key (CMK) that is used for encryption.
        self.key_id = key_id
        # The name of the parameter.
        self.name = name
        # The version number of the parameter.
        self.parameter_version = parameter_version
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the parameter.
        self.share_type = share_type
        # The tags of the parameter.
        self.tags = tags
        # The type of the parameter.
        self.type = type
        # The user who updated the parameter.
        self.updated_by = updated_by
        # The time when the parameter was updated.
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class ListSecretParametersResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        parameters: List[ListSecretParametersResponseBodyParameters] = None,
        request_id: str = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The information about the parameters.
        self.parameters = parameters
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.parameters:
            for k in self.parameters:
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
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = ListSecretParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSecretParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSecretParametersResponseBody = None,
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
            temp_model = ListSecretParametersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStateConfigurationsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        state_configuration_ids: str = None,
        tags: Dict[str, Any] = None,
        template_name: str = None,
        template_version: str = None,
    ):
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The token of the next page.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of each desired-state configuration.
        self.state_configuration_ids = state_configuration_ids
        # The tag.
        self.tags = tags
        # The name of the template. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        self.template_name = template_name
        # The version number. If you do not specify this parameter, the system uses the latest version.
        self.template_version = template_version

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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state_configuration_ids is not None:
            result['StateConfigurationIds'] = self.state_configuration_ids
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StateConfigurationIds') is not None:
            self.state_configuration_ids = m.get('StateConfigurationIds')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class ListStateConfigurationsShrinkRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        state_configuration_ids: str = None,
        tags_shrink: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The token of the next page.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of each desired-state configuration.
        self.state_configuration_ids = state_configuration_ids
        # The tag.
        self.tags_shrink = tags_shrink
        # The name of the template. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        self.template_name = template_name
        # The version number. If you do not specify this parameter, the system uses the latest version.
        self.template_version = template_version

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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state_configuration_ids is not None:
            result['StateConfigurationIds'] = self.state_configuration_ids
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StateConfigurationIds') is not None:
            self.state_configuration_ids = m.get('StateConfigurationIds')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class ListStateConfigurationsResponseBodyStateConfigurations(TeaModel):
    def __init__(
        self,
        configure_mode: str = None,
        create_time: str = None,
        description: str = None,
        parameters: str = None,
        resource_group_id: str = None,
        schedule_expression: str = None,
        schedule_type: str = None,
        state_configuration_id: str = None,
        tags: Dict[str, Any] = None,
        targets: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        update_time: str = None,
    ):
        # The configuration mode.
        self.configure_mode = configure_mode
        # The creation time.
        self.create_time = create_time
        # The description.
        self.description = description
        # The parameters.
        self.parameters = parameters
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The schedule expression.
        self.schedule_expression = schedule_expression
        # The schedule type.
        self.schedule_type = schedule_type
        # The ID of the desired-state configuration.
        self.state_configuration_id = state_configuration_id
        # The tag of the auxiliary media asset.
        self.tags = tags
        # The target EMR resource.
        self.targets = targets
        # The ID of the cluster template.
        self.template_id = template_id
        # The name of the template.
        self.template_name = template_name
        # The version of the template.
        self.template_version = template_version
        # The time when the configuration is updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.state_configuration_id is not None:
            result['StateConfigurationId'] = self.state_configuration_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.targets is not None:
            result['Targets'] = self.targets
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('StateConfigurationId') is not None:
            self.state_configuration_id = m.get('StateConfigurationId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListStateConfigurationsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        state_configurations: List[ListStateConfigurationsResponseBodyStateConfigurations] = None,
    ):
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The desired-state configurations.
        self.state_configurations = state_configurations

    def validate(self):
        if self.state_configurations:
            for k in self.state_configurations:
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
        result['StateConfigurations'] = []
        if self.state_configurations is not None:
            for k in self.state_configurations:
                result['StateConfigurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.state_configurations = []
        if m.get('StateConfigurations') is not None:
            for k in m.get('StateConfigurations'):
                temp_model = ListStateConfigurationsResponseBodyStateConfigurations()
                self.state_configurations.append(temp_model.from_map(k))
        return self


class ListStateConfigurationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStateConfigurationsResponseBody = None,
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
            temp_model = ListStateConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        # The maximum number of entries to return on each page. Valid value: 10 to 100. Default value: 50.
        self.max_results = max_results
        # The token that is used to retrieve the next page.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id
        # The type of the resource to which the tag is added.
        self.resource_type = resource_type

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
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        keys: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The tag keys.
        self.keys = keys
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
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
        next_token: str = None,
        region_id: str = None,
        resource_ids: Dict[str, Any] = None,
        resource_type: str = None,
        tags: Dict[str, Any] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id
        # The IDs of resources. The number of resource IDs ranges from 1 to 50.
        self.resource_ids = resource_ids
        # The type of the resource. Valid values: template execution
        self.resource_type = resource_type
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListTagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_ids_shrink: str = None,
        resource_type: str = None,
        tags_shrink: str = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id
        # The IDs of resources. The number of resource IDs ranges from 1 to 50.
        self.resource_ids_shrink = resource_ids_shrink
        # The type of the resource. Valid values: template execution
        self.resource_type = resource_type
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type
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


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. If the return value of the NextToken parameter is empty, the next page does not exist.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The set of resources and the tags that are added to the resources.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
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


class ListTagValuesRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        # The tag key to query.
        self.key = key
        # The maximum number of results on each page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id
        # The type of the tagged resource.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        values: List[str] = None,
    ):
        # The maximum number of results on each page.
        self.max_results = max_results
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The tag values returned.
        self.values = values

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Values') is not None:
            self.values = m.get('Values')
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


class ListTaskExecutionsRequest(TeaModel):
    def __init__(
        self,
        end_date_after: str = None,
        end_date_before: str = None,
        execution_id: str = None,
        include_child_task_execution: bool = None,
        max_results: int = None,
        next_token: str = None,
        parent_task_execution_id: str = None,
        region_id: str = None,
        sort_field: str = None,
        sort_order: str = None,
        start_date_after: str = None,
        start_date_before: str = None,
        status: str = None,
        task_action: str = None,
        task_execution_id: str = None,
        task_name: str = None,
    ):
        # The execution ID of the task.
        self.end_date_after = end_date_after
        # Specifies to query task executions that stop running at or later than the specified time.
        self.end_date_before = end_date_before
        # The status of the execution. Valid values: Running, Started, Success, Failed, Waiting, Cancelled, Pending, and Skipped.
        self.execution_id = execution_id
        # The number of entries to return on each page. Valid values: 20 to 100. Default value: 50.
        self.include_child_task_execution = include_child_task_execution
        # The token that is used to retrieve the next page of results.
        self.max_results = max_results
        # Sorts the task executions to query. Valid values:
        # 
        # *   **StartDate**: specifies that the task executions are sorted based on the time when they are created. This is the default value.
        # *   **EndDate**: specifies that the task executions are sorted based on the time when the time when they stop running.
        # *   **Status**: specifies that the task executions are sorted based on their statuses.
        self.next_token = next_token
        # Specifies whether to show the child nodes in the loop task. Default value: False.
        self.parent_task_execution_id = parent_task_execution_id
        # The ID of the execution.
        self.region_id = region_id
        # The order in which you want to sort the task executions to query. Valid values:
        # 
        # *   **Ascending**: ascending order.
        # *   **Descending**: descending order. This is the default value.
        self.sort_field = sort_field
        # The token that is used to retrieve the next page of results.
        self.sort_order = sort_order
        # Specifies to query task executions that stop running at or before the specified time.
        self.start_date_after = start_date_after
        # Specifies to query task executions that start to run at or later than the specified time.
        self.start_date_before = start_date_before
        # Specifies to query task executions that start to run at or before the specified time.
        self.status = status
        # The execution ID of the parent node. In a loop task, set this parameter to the execution ID of the parent node.
        self.task_action = task_action
        # The name of the task.
        self.task_execution_id = task_execution_id
        # The action of the task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date_after is not None:
            result['EndDateAfter'] = self.end_date_after
        if self.end_date_before is not None:
            result['EndDateBefore'] = self.end_date_before
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.include_child_task_execution is not None:
            result['IncludeChildTaskExecution'] = self.include_child_task_execution
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.parent_task_execution_id is not None:
            result['ParentTaskExecutionId'] = self.parent_task_execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.start_date_after is not None:
            result['StartDateAfter'] = self.start_date_after
        if self.start_date_before is not None:
            result['StartDateBefore'] = self.start_date_before
        if self.status is not None:
            result['Status'] = self.status
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDateAfter') is not None:
            self.end_date_after = m.get('EndDateAfter')
        if m.get('EndDateBefore') is not None:
            self.end_date_before = m.get('EndDateBefore')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('IncludeChildTaskExecution') is not None:
            self.include_child_task_execution = m.get('IncludeChildTaskExecution')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ParentTaskExecutionId') is not None:
            self.parent_task_execution_id = m.get('ParentTaskExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('StartDateAfter') is not None:
            self.start_date_after = m.get('StartDateAfter')
        if m.get('StartDateBefore') is not None:
            self.start_date_before = m.get('StartDateBefore')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListTaskExecutionsResponseBodyTaskExecutions(TeaModel):
    def __init__(
        self,
        child_execution_id: str = None,
        create_date: str = None,
        end_date: str = None,
        execution_id: str = None,
        extra_data: Dict[str, Any] = None,
        loop: Dict[str, Any] = None,
        loop_batch_number: int = None,
        loop_item: str = None,
        outputs: str = None,
        parent_task_execution_id: str = None,
        properties: str = None,
        start_date: str = None,
        status: str = None,
        status_message: str = None,
        task_action: str = None,
        task_execution_id: str = None,
        task_name: str = None,
        template_id: str = None,
        update_date: str = None,
    ):
        # The output of the execution.
        self.child_execution_id = child_execution_id
        # The ID of the execution.
        self.create_date = create_date
        # The execution ID of the parent node.
        self.end_date = end_date
        # The action of the task.
        self.execution_id = execution_id
        # The Input parameters of the task execution.
        self.extra_data = extra_data
        # The ID of the template.
        self.loop = loop
        # The status information of the task execution.
        self.loop_batch_number = loop_batch_number
        # The time when the execution was created.
        self.loop_item = loop_item
        # The status of the task.
        self.outputs = outputs
        # The name of the task.
        self.parent_task_execution_id = parent_task_execution_id
        # Queries task executions. Multiple methods are supported to filter task executions.
        self.properties = properties
        # The elements in the loop task.
        self.start_date = start_date
        # The time when the task execution stopped running.
        self.status = status
        # The additional information.
        self.status_message = status_message
        # The execution ID of the task.
        self.task_action = task_action
        # The time when the execution was last updated.
        self.task_execution_id = task_execution_id
        # The time when the execution started.
        self.task_name = task_name
        # The number of times for which the loop task is run.
        self.template_id = template_id
        # The configuration and statistics information of the loop task. This parameter is returned only for the parent node of the loop task.
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_execution_id is not None:
            result['ChildExecutionId'] = self.child_execution_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data
        if self.loop is not None:
            result['Loop'] = self.loop
        if self.loop_batch_number is not None:
            result['LoopBatchNumber'] = self.loop_batch_number
        if self.loop_item is not None:
            result['LoopItem'] = self.loop_item
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parent_task_execution_id is not None:
            result['ParentTaskExecutionId'] = self.parent_task_execution_id
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChildExecutionId') is not None:
            self.child_execution_id = m.get('ChildExecutionId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')
        if m.get('Loop') is not None:
            self.loop = m.get('Loop')
        if m.get('LoopBatchNumber') is not None:
            self.loop_batch_number = m.get('LoopBatchNumber')
        if m.get('LoopItem') is not None:
            self.loop_item = m.get('LoopItem')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('ParentTaskExecutionId') is not None:
            self.parent_task_execution_id = m.get('ParentTaskExecutionId')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class ListTaskExecutionsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        task_executions: List[ListTaskExecutionsResponseBodyTaskExecutions] = None,
    ):
        # The details of the task executions.
        self.max_results = max_results
        # The ID of the request.
        self.next_token = next_token
        # The number of entries returned on each page.
        self.request_id = request_id
        # The execution ID of the child node.
        self.task_executions = task_executions

    def validate(self):
        if self.task_executions:
            for k in self.task_executions:
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
        result['TaskExecutions'] = []
        if self.task_executions is not None:
            for k in self.task_executions:
                result['TaskExecutions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_executions = []
        if m.get('TaskExecutions') is not None:
            for k in m.get('TaskExecutions'):
                temp_model = ListTaskExecutionsResponseBodyTaskExecutions()
                self.task_executions.append(temp_model.from_map(k))
        return self


class ListTaskExecutionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTaskExecutionsResponseBody = None,
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
            temp_model = ListTaskExecutionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplateVersionsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        share_type: str = None,
        template_name: str = None,
    ):
        # The maximum number of results on each page. Valid values: 10 to 100
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id
        # The type of the template. Valid values: Private and Public.
        self.share_type = share_type
        # The name of the template.
        self.template_name = template_name

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
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListTemplateVersionsResponseBodyTemplateVersions(TeaModel):
    def __init__(
        self,
        description: str = None,
        template_format: str = None,
        template_version: str = None,
        updated_by: str = None,
        updated_date: str = None,
        version_name: str = None,
    ):
        # The description of the version.
        self.description = description
        # The format of the template content. Valid values: YAML and JSON.
        self.template_format = template_format
        # The number of the version.
        self.template_version = template_version
        # The user who last updated the version.
        self.updated_by = updated_by
        # The time when the version was last updated.
        self.updated_date = updated_date
        # The name of the version.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class ListTemplateVersionsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        template_versions: List[ListTemplateVersionsResponseBodyTemplateVersions] = None,
    ):
        # The maximum number of results on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The versions of the template.
        self.template_versions = template_versions

    def validate(self):
        if self.template_versions:
            for k in self.template_versions:
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
        result['TemplateVersions'] = []
        if self.template_versions is not None:
            for k in self.template_versions:
                result['TemplateVersions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.template_versions = []
        if m.get('TemplateVersions') is not None:
            for k in m.get('TemplateVersions'):
                temp_model = ListTemplateVersionsResponseBodyTemplateVersions()
                self.template_versions.append(temp_model.from_map(k))
        return self


class ListTemplateVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTemplateVersionsResponseBody = None,
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
            temp_model = ListTemplateVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        created_by: str = None,
        created_date_after: str = None,
        created_date_before: str = None,
        has_trigger: bool = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        sort_field: str = None,
        sort_order: str = None,
        tags: Dict[str, Any] = None,
        template_format: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The type of the template. Valid values include TimerTrigger, EventTrigger, AlarmTrigger, and Other.
        self.category = category
        # The creator of the template.
        # 
        # *   To query the template provided by Alibaba Cloud, set this parameter to **ACS**.
        # *   To query the template created by a user, set this parameter to the **ID** of the template or the **name of the user** who creates the template.
        self.created_by = created_by
        # Specifies to query the template that is created at or later than the specified time.
        # 
        # The value must be in the YYYY-MM-DDThh:mm:ssZ format.
        self.created_date_after = created_date_after
        # Specifies to query the template that is created at or before the specified time.
        # 
        # The value must be in the YYYY-MM-DDThh:mm::ssZ format.
        self.created_date_before = created_date_before
        # Specifies whether to query the template that is configured with a trigger.
        self.has_trigger = has_trigger
        # The number of entries to return on each page. Valid values: 20 to 100. Default value: 50.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the region in which you want to query templates.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the template. Valid values:
        # 
        # *   **Public**\
        # *   **Private**\
        self.share_type = share_type
        # The field that is used to sort the templates to be returned. Valid values:
        # 
        # *   **TotalExecutionCounts**: The system sorts the returned templates based on the total number of execution times of the template. This is the default value.
        # *   **Popularity**: The system sorts the returned templates based on the popularity of the template.
        # *   **TemplateName**: The system sorts the returned templates based on the name of the template.
        # *   **CreatedDate**: The system sorts the returned templates based on the creation time of the template.
        self.sort_field = sort_field
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **Ascending**: ascending order.
        # *   **Descending**: descending order. This is the default value.
        self.sort_order = sort_order
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags
        # The format of the template. Valid values:
        # 
        # *   **JSON**\
        # *   **YAML**\
        self.template_format = template_format
        # The name of the template. All templates whose names contain the specified template name are to be returned.
        self.template_name = template_name
        # The type of the template.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date_after is not None:
            result['CreatedDateAfter'] = self.created_date_after
        if self.created_date_before is not None:
            result['CreatedDateBefore'] = self.created_date_before
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDateAfter') is not None:
            self.created_date_after = m.get('CreatedDateAfter')
        if m.get('CreatedDateBefore') is not None:
            self.created_date_before = m.get('CreatedDateBefore')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListTemplatesShrinkRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        created_by: str = None,
        created_date_after: str = None,
        created_date_before: str = None,
        has_trigger: bool = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        sort_field: str = None,
        sort_order: str = None,
        tags_shrink: str = None,
        template_format: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The type of the template. Valid values include TimerTrigger, EventTrigger, AlarmTrigger, and Other.
        self.category = category
        # The creator of the template.
        # 
        # *   To query the template provided by Alibaba Cloud, set this parameter to **ACS**.
        # *   To query the template created by a user, set this parameter to the **ID** of the template or the **name of the user** who creates the template.
        self.created_by = created_by
        # Specifies to query the template that is created at or later than the specified time.
        # 
        # The value must be in the YYYY-MM-DDThh:mm:ssZ format.
        self.created_date_after = created_date_after
        # Specifies to query the template that is created at or before the specified time.
        # 
        # The value must be in the YYYY-MM-DDThh:mm::ssZ format.
        self.created_date_before = created_date_before
        # Specifies whether to query the template that is configured with a trigger.
        self.has_trigger = has_trigger
        # The number of entries to return on each page. Valid values: 20 to 100. Default value: 50.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the region in which you want to query templates.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the template. Valid values:
        # 
        # *   **Public**\
        # *   **Private**\
        self.share_type = share_type
        # The field that is used to sort the templates to be returned. Valid values:
        # 
        # *   **TotalExecutionCounts**: The system sorts the returned templates based on the total number of execution times of the template. This is the default value.
        # *   **Popularity**: The system sorts the returned templates based on the popularity of the template.
        # *   **TemplateName**: The system sorts the returned templates based on the name of the template.
        # *   **CreatedDate**: The system sorts the returned templates based on the creation time of the template.
        self.sort_field = sort_field
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **Ascending**: ascending order.
        # *   **Descending**: descending order. This is the default value.
        self.sort_order = sort_order
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags_shrink = tags_shrink
        # The format of the template. Valid values:
        # 
        # *   **JSON**\
        # *   **YAML**\
        self.template_format = template_format
        # The name of the template. All templates whose names contain the specified template name are to be returned.
        self.template_name = template_name
        # The type of the template.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date_after is not None:
            result['CreatedDateAfter'] = self.created_date_after
        if self.created_date_before is not None:
            result['CreatedDateBefore'] = self.created_date_before
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sort_field is not None:
            result['SortField'] = self.sort_field
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDateAfter') is not None:
            self.created_date_after = m.get('CreatedDateAfter')
        if m.get('CreatedDateBefore') is not None:
            self.created_date_before = m.get('CreatedDateBefore')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('SortField') is not None:
            self.sort_field = m.get('SortField')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        category: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        has_trigger: bool = None,
        hash: str = None,
        popularity: int = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        template_format: str = None,
        template_id: str = None,
        template_name: str = None,
        template_type: str = None,
        template_version: str = None,
        total_execution_count: int = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The type of the template.
        self.category = category
        # The user who created the template.
        self.created_by = created_by
        # The time when the template was created.
        self.created_date = created_date
        # The description of the template.
        self.description = description
        # Indicates whether the template is configured with a trigger.
        self.has_trigger = has_trigger
        # The SHA-256 value of the template content.
        self.hash = hash
        # The popularity of the public template. Valid values: **1-10**. A greater value indicates higher popularity. If the **ShareType** parameter is set to **Private**, the value of this parameter is `-1`.
        # 
        # **Notes** This parameter is valid only if the value of the **ShareType** parameter is set to **Public**.
        self.popularity = popularity
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the template. The share type of the template that you create is **Private**. Valid values:
        # 
        # *   **Public**\
        # *   **Private**\
        self.share_type = share_type
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags
        # The format of the template. The system automatically determines whether the format is JSON or YAML.
        self.template_format = template_format
        # The ID of the template.
        self.template_id = template_id
        # The name of the template.
        self.template_name = template_name
        # The type of the template.
        self.template_type = template_type
        # The version of the template. The name of the version consists of the letter v and a number. The number starts from 1.
        self.template_version = template_version
        # The number of times for which the private template is executed. If the **ShareType** parameter is set to **Public**, the value of this parameter is `-1`.
        # **Notes** This parameter is valid only if the **ShareType** parameter is set to **Private**.
        self.total_execution_count = total_execution_count
        # The user who last updated the template.
        self.updated_by = updated_by
        # The time when the template was last updated.
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.popularity is not None:
            result['Popularity'] = self.popularity
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.total_execution_count is not None:
            result['TotalExecutionCount'] = self.total_execution_count
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('Popularity') is not None:
            self.popularity = m.get('Popularity')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TotalExecutionCount') is not None:
            self.total_execution_count = m.get('TotalExecutionCount')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        templates: List[ListTemplatesResponseBodyTemplates] = None,
    ):
        # The number of entries returned on each page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The metadata of the template.
        self.templates = templates

    def validate(self):
        if self.templates:
            for k in self.templates:
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
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTemplatesResponseBody = None,
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
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NotifyExecutionRequest(TeaModel):
    def __init__(
        self,
        execution_id: str = None,
        execution_status: str = None,
        loop_item: str = None,
        notify_note: str = None,
        notify_type: str = None,
        parameters: str = None,
        region_id: str = None,
        task_execution_id: str = None,
        task_execution_ids: str = None,
        task_name: str = None,
    ):
        # The ID of the execution.
        self.execution_id = execution_id
        # The state of the terminated execution. This parameter is valid if you set the NotifyType parameter to CompleteExecution.
        self.execution_status = execution_status
        # The items of the child node in the loop task.
        self.loop_item = loop_item
        # The description for the notification.
        self.notify_note = notify_note
        # The type of the notification. Valid values:
        # 
        # *   **ExecuteTask**: starts to run a specific task. This value is used if you perform debugging in the Debug mode. If you set this parameter to ExecuteTask, you also need to set the Parameters parameter.
        # *   **CancelTask**: cancels a current task. This value is used if you perform debugging in the Debug mode.
        # *   **CompleteExecution**: manually terminates an execution if you perform debugging in the Debug mode. You can specify the state of the terminated execution by using the **ExecutionStatus** parameter.
        # *   **Approve**: approves an execution. For example, you are aware of the risks of an operation task and agree to approve the execution.
        # *   **Reject**: rejects an execution. For example, you want to reject the execution of a high-risk operation task.
        # *   **RetryTask**: retries a failed task whose execution mode is Suspend upon Failure.
        # *   **SkipTask**: skips a failed task whose execution mode is Suspend upon Failure.
        self.notify_type = notify_type
        # The parameters of the subsequent task. This parameter is valid if you set the NotifyType parameter to ExecuteTask.
        self.parameters = parameters
        # The ID of the region in which the execution resides.
        self.region_id = region_id
        # The execution ID of the task.
        self.task_execution_id = task_execution_id
        # The execution IDs of the tasks.
        self.task_execution_ids = task_execution_ids
        # The name of the subsequent task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.execution_status is not None:
            result['ExecutionStatus'] = self.execution_status
        if self.loop_item is not None:
            result['LoopItem'] = self.loop_item
        if self.notify_note is not None:
            result['NotifyNote'] = self.notify_note
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_execution_ids is not None:
            result['TaskExecutionIds'] = self.task_execution_ids
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('ExecutionStatus') is not None:
            self.execution_status = m.get('ExecutionStatus')
        if m.get('LoopItem') is not None:
            self.loop_item = m.get('LoopItem')
        if m.get('NotifyNote') is not None:
            self.notify_note = m.get('NotifyNote')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskExecutionIds') is not None:
            self.task_execution_ids = m.get('TaskExecutionIds')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class NotifyExecutionResponseBody(TeaModel):
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


class NotifyExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: NotifyExecutionResponseBody = None,
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
            temp_model = NotifyExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterDefaultPatchBaselineRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        region_id: str = None,
    ):
        # The name of the patch baseline.
        self.name = name
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RegisterDefaultPatchBaselineResponseBodyPatchBaseline(TeaModel):
    def __init__(
        self,
        approval_rules: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        operation_system: str = None,
        share_type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules
        # The user who created the patch baseline.
        self.created_by = created_by
        # The time when the patch baseline was created.
        self.created_date = created_date
        # The description of the patch baseline.
        self.description = description
        # The ID of the patch baseline.
        self.id = id
        # The name of the patch baseline.
        self.name = name
        # The type of the operating system.
        self.operation_system = operation_system
        # The share type of the patch baseline.
        self.share_type = share_type
        # The user who last updated the patch baseline.
        self.updated_by = updated_by
        # The time when the patch baseline was last updated.
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class RegisterDefaultPatchBaselineResponseBody(TeaModel):
    def __init__(
        self,
        patch_baseline: RegisterDefaultPatchBaselineResponseBodyPatchBaseline = None,
        request_id: str = None,
    ):
        # The details of the patch baseline.
        self.patch_baseline = patch_baseline
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.patch_baseline:
            self.patch_baseline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.patch_baseline is not None:
            result['PatchBaseline'] = self.patch_baseline.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PatchBaseline') is not None:
            temp_model = RegisterDefaultPatchBaselineResponseBodyPatchBaseline()
            self.patch_baseline = temp_model.from_map(m['PatchBaseline'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterDefaultPatchBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterDefaultPatchBaselineResponseBody = None,
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
            temp_model = RegisterDefaultPatchBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchInventoryRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        # The name of the component property. Valid values of N: 1 to 5. Different components have different property names. You can call the [GetInventorySchema](https://api.aliyun.com/#/?product=oos\&version=2019-06-01\&api=GetInventorySchema) operation to query the property names of different components. For example, the ACS:InstanceInformation component has the InstanceId property. Therefore, you can set this parameter to ACS:InstanceInformation.InstanceId.
        self.name = name
        # The comparison operator that is used to filter property values. Valid values of N: 1 to 5. Valid values:
        # 
        # *   Equal
        # *   NotEqual
        # *   BeginWith
        # *   LessThan
        # *   GreaterThan
        self.operator = operator
        # The property values to query.
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
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchInventoryRequest(TeaModel):
    def __init__(
        self,
        aggregator: List[str] = None,
        filter: List[SearchInventoryRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The information about aggregators. You can use one or more aggregators to query the aggregate information of an instance. Valid values:
        # 
        # *   ACS:Application.Name
        # *   ACS:Application.Version
        self.aggregator = aggregator
        # The filter rules for the component.
        self.filter = filter
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 50.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the region.
        self.region_id = region_id

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
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = SearchInventoryRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchInventoryResponseBody(TeaModel):
    def __init__(
        self,
        entities: List[Dict[str, Any]] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.entities = entities
        # The number of entries returned per page.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entities is not None:
            result['Entities'] = self.entities
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entities') is not None:
            self.entities = m.get('Entities')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchInventoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchInventoryResponseBody = None,
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
            temp_model = SearchInventoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetServiceSettingsRequest(TeaModel):
    def __init__(
        self,
        delivery_oss_bucket_name: str = None,
        delivery_oss_enabled: bool = None,
        delivery_oss_key_prefix: str = None,
        delivery_sls_enabled: bool = None,
        delivery_sls_project_name: str = None,
        rdc_enterprise_id: str = None,
        region_id: str = None,
    ):
        self.delivery_oss_bucket_name = delivery_oss_bucket_name
        self.delivery_oss_enabled = delivery_oss_enabled
        self.delivery_oss_key_prefix = delivery_oss_key_prefix
        self.delivery_sls_enabled = delivery_sls_enabled
        self.delivery_sls_project_name = delivery_sls_project_name
        self.rdc_enterprise_id = rdc_enterprise_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_oss_bucket_name is not None:
            result['DeliveryOssBucketName'] = self.delivery_oss_bucket_name
        if self.delivery_oss_enabled is not None:
            result['DeliveryOssEnabled'] = self.delivery_oss_enabled
        if self.delivery_oss_key_prefix is not None:
            result['DeliveryOssKeyPrefix'] = self.delivery_oss_key_prefix
        if self.delivery_sls_enabled is not None:
            result['DeliverySlsEnabled'] = self.delivery_sls_enabled
        if self.delivery_sls_project_name is not None:
            result['DeliverySlsProjectName'] = self.delivery_sls_project_name
        if self.rdc_enterprise_id is not None:
            result['RdcEnterpriseId'] = self.rdc_enterprise_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryOssBucketName') is not None:
            self.delivery_oss_bucket_name = m.get('DeliveryOssBucketName')
        if m.get('DeliveryOssEnabled') is not None:
            self.delivery_oss_enabled = m.get('DeliveryOssEnabled')
        if m.get('DeliveryOssKeyPrefix') is not None:
            self.delivery_oss_key_prefix = m.get('DeliveryOssKeyPrefix')
        if m.get('DeliverySlsEnabled') is not None:
            self.delivery_sls_enabled = m.get('DeliverySlsEnabled')
        if m.get('DeliverySlsProjectName') is not None:
            self.delivery_sls_project_name = m.get('DeliverySlsProjectName')
        if m.get('RdcEnterpriseId') is not None:
            self.rdc_enterprise_id = m.get('RdcEnterpriseId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SetServiceSettingsResponseBodyServiceSettings(TeaModel):
    def __init__(
        self,
        delivery_oss_bucket_name: str = None,
        delivery_oss_enabled: bool = None,
        delivery_oss_key_prefix: str = None,
        delivery_sls_enabled: bool = None,
        delivery_sls_project_name: str = None,
        rdc_enterprise_id: str = None,
    ):
        self.delivery_oss_bucket_name = delivery_oss_bucket_name
        self.delivery_oss_enabled = delivery_oss_enabled
        self.delivery_oss_key_prefix = delivery_oss_key_prefix
        self.delivery_sls_enabled = delivery_sls_enabled
        self.delivery_sls_project_name = delivery_sls_project_name
        self.rdc_enterprise_id = rdc_enterprise_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_oss_bucket_name is not None:
            result['DeliveryOssBucketName'] = self.delivery_oss_bucket_name
        if self.delivery_oss_enabled is not None:
            result['DeliveryOssEnabled'] = self.delivery_oss_enabled
        if self.delivery_oss_key_prefix is not None:
            result['DeliveryOssKeyPrefix'] = self.delivery_oss_key_prefix
        if self.delivery_sls_enabled is not None:
            result['DeliverySlsEnabled'] = self.delivery_sls_enabled
        if self.delivery_sls_project_name is not None:
            result['DeliverySlsProjectName'] = self.delivery_sls_project_name
        if self.rdc_enterprise_id is not None:
            result['RdcEnterpriseId'] = self.rdc_enterprise_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryOssBucketName') is not None:
            self.delivery_oss_bucket_name = m.get('DeliveryOssBucketName')
        if m.get('DeliveryOssEnabled') is not None:
            self.delivery_oss_enabled = m.get('DeliveryOssEnabled')
        if m.get('DeliveryOssKeyPrefix') is not None:
            self.delivery_oss_key_prefix = m.get('DeliveryOssKeyPrefix')
        if m.get('DeliverySlsEnabled') is not None:
            self.delivery_sls_enabled = m.get('DeliverySlsEnabled')
        if m.get('DeliverySlsProjectName') is not None:
            self.delivery_sls_project_name = m.get('DeliverySlsProjectName')
        if m.get('RdcEnterpriseId') is not None:
            self.rdc_enterprise_id = m.get('RdcEnterpriseId')
        return self


class SetServiceSettingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_settings: List[SetServiceSettingsResponseBodyServiceSettings] = None,
    ):
        self.request_id = request_id
        self.service_settings = service_settings

    def validate(self):
        if self.service_settings:
            for k in self.service_settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceSettings'] = []
        if self.service_settings is not None:
            for k in self.service_settings:
                result['ServiceSettings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_settings = []
        if m.get('ServiceSettings') is not None:
            for k in m.get('ServiceSettings'):
                temp_model = SetServiceSettingsResponseBodyServiceSettings()
                self.service_settings.append(temp_model.from_map(k))
        return self


class SetServiceSettingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetServiceSettingsResponseBody = None,
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
            temp_model = SetServiceSettingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartExecutionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        loop_mode: str = None,
        mode: str = None,
        parameters: str = None,
        parent_execution_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        safety_check: str = None,
        tags: Dict[str, Any] = None,
        template_content: str = None,
        template_name: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        # The access token.
        self.client_token = client_token
        # The description of the execution.
        self.description = description
        # The loop mode. Valid values:
        # 
        # *   Automatic: does not suspend the execution of the template. This is the default value.
        # *   FirstBatchPause: suspends the execution of the template after the first batch is complete.
        # *   EveryBatchPause: suspends the execution of the template after each batch is complete.
        self.loop_mode = loop_mode
        # The execution mode. Valid values:
        # 
        # *   Automatic: automatically starts the execution of the template. This is the default value.
        # *   FailurePause: suspends the execution of the template upon a failure.
        # *   Debug: manually starts the execution of the template.
        self.mode = mode
        # The JSON string that consists of a set of parameters. Default value: {}.
        self.parameters = parameters
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id
        # The ID of the region in which the execution resides.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The security check mode. Valid values:
        # 
        # *   Skip: specifies that you are aware of the risks. The system performs all actions in the execution without manual confirmation, regardless of the risk level. This parameter is valid only if the `Mode` parameter is set to Automatic.
        # *   ConfirmEveryHighRiskAction: requires you to confirm each high-risk action. This is the default value. You can call the **NotifyExecution** operation to confirm or cancel an action.
        self.safety_check = safety_check
        # The tags for the execution.
        self.tags = tags
        # The content of the template in the JSON or YAML format. This parameter is the same as the Content parameter that you can specify when you call the CreateTemplate operation. You can use this parameter to specify the tasks that you want to run. This way, you do not need to create a template before you start an execution. If you select an existing template, you do not need to specify this parameter.
        self.template_content = template_content
        # The name of the template. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        self.template_name = template_name
        # The Object Storage Service (OSS) URL of the object that stores the content of the Operation Orchestration Service (OOS) template. The access control list (ACL) of the object must be public-read. You can use this parameter to specify the tasks that you want to run. This way, you do not need to create a template before you start an execution. If you select an existing template, you do not need to specify this parameter.
        self.template_url = template_url
        # The version number of the template. If you do not specify this parameter, the system uses the latest version.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.loop_mode is not None:
            result['LoopMode'] = self.loop_mode
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LoopMode') is not None:
            self.loop_mode = m.get('LoopMode')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class StartExecutionShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        loop_mode: str = None,
        mode: str = None,
        parameters: str = None,
        parent_execution_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        safety_check: str = None,
        tags_shrink: str = None,
        template_content: str = None,
        template_name: str = None,
        template_url: str = None,
        template_version: str = None,
    ):
        # The access token.
        self.client_token = client_token
        # The description of the execution.
        self.description = description
        # The loop mode. Valid values:
        # 
        # *   Automatic: does not suspend the execution of the template. This is the default value.
        # *   FirstBatchPause: suspends the execution of the template after the first batch is complete.
        # *   EveryBatchPause: suspends the execution of the template after each batch is complete.
        self.loop_mode = loop_mode
        # The execution mode. Valid values:
        # 
        # *   Automatic: automatically starts the execution of the template. This is the default value.
        # *   FailurePause: suspends the execution of the template upon a failure.
        # *   Debug: manually starts the execution of the template.
        self.mode = mode
        # The JSON string that consists of a set of parameters. Default value: {}.
        self.parameters = parameters
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id
        # The ID of the region in which the execution resides.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The security check mode. Valid values:
        # 
        # *   Skip: specifies that you are aware of the risks. The system performs all actions in the execution without manual confirmation, regardless of the risk level. This parameter is valid only if the `Mode` parameter is set to Automatic.
        # *   ConfirmEveryHighRiskAction: requires you to confirm each high-risk action. This is the default value. You can call the **NotifyExecution** operation to confirm or cancel an action.
        self.safety_check = safety_check
        # The tags for the execution.
        self.tags_shrink = tags_shrink
        # The content of the template in the JSON or YAML format. This parameter is the same as the Content parameter that you can specify when you call the CreateTemplate operation. You can use this parameter to specify the tasks that you want to run. This way, you do not need to create a template before you start an execution. If you select an existing template, you do not need to specify this parameter.
        self.template_content = template_content
        # The name of the template. The name must be 1 to 200 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_).
        self.template_name = template_name
        # The Object Storage Service (OSS) URL of the object that stores the content of the Operation Orchestration Service (OOS) template. The access control list (ACL) of the object must be public-read. You can use this parameter to specify the tasks that you want to run. This way, you do not need to create a template before you start an execution. If you select an existing template, you do not need to specify this parameter.
        self.template_url = template_url
        # The version number of the template. If you do not specify this parameter, the system uses the latest version.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.loop_mode is not None:
            result['LoopMode'] = self.loop_mode
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LoopMode') is not None:
            self.loop_mode = m.get('LoopMode')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class StartExecutionResponseBodyExecutionCurrentTasks(TeaModel):
    def __init__(
        self,
        task_action: str = None,
        task_execution_id: str = None,
        task_name: str = None,
    ):
        # The action of the task.
        self.task_action = task_action
        # The execution ID of the task.
        self.task_execution_id = task_execution_id
        # The name of the task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_action is not None:
            result['TaskAction'] = self.task_action
        if self.task_execution_id is not None:
            result['TaskExecutionId'] = self.task_execution_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskAction') is not None:
            self.task_action = m.get('TaskAction')
        if m.get('TaskExecutionId') is not None:
            self.task_execution_id = m.get('TaskExecutionId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class StartExecutionResponseBodyExecution(TeaModel):
    def __init__(
        self,
        counters: Dict[str, Any] = None,
        create_date: str = None,
        current_tasks: List[StartExecutionResponseBodyExecutionCurrentTasks] = None,
        description: str = None,
        end_date: str = None,
        executed_by: str = None,
        execution_id: str = None,
        is_parent: bool = None,
        loop_mode: str = None,
        mode: str = None,
        outputs: str = None,
        parameters: str = None,
        parent_execution_id: str = None,
        ram_role: str = None,
        resource_group_id: str = None,
        safety_check: str = None,
        start_date: str = None,
        status: str = None,
        status_message: str = None,
        tags: Dict[str, Any] = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        update_date: str = None,
    ):
        # The number of executions.
        self.counters = counters
        # The time when the execution was created.
        self.create_date = create_date
        # The information about in-progress tasks.
        self.current_tasks = current_tasks
        # The description of the execution.
        self.description = description
        # The time when the execution stopped.
        self.end_date = end_date
        # The account ID of the user who started the execution of the template.
        self.executed_by = executed_by
        # The GUID of the execution.
        self.execution_id = execution_id
        # Indicates whether the execution is a parent execution.
        self.is_parent = is_parent
        # The loop mode.
        self.loop_mode = loop_mode
        # The execution mode.
        self.mode = mode
        # The output of the execution.
        self.outputs = outputs
        # The input parameters of the execution.
        self.parameters = parameters
        # The ID of the parent execution.
        self.parent_execution_id = parent_execution_id
        # The role that started the execution of the template.
        self.ram_role = ram_role
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The security check mode.
        self.safety_check = safety_check
        # The time when the execution was started.
        self.start_date = start_date
        # The status of the execution.
        self.status = status
        # The status information of the execution.
        self.status_message = status_message
        # The tags of the execution.
        self.tags = tags
        # The ID of the template.
        self.template_id = template_id
        # The name of the template.
        self.template_name = template_name
        # The version number of the template.
        self.template_version = template_version
        # The time when the execution was last updated.
        self.update_date = update_date

    def validate(self):
        if self.current_tasks:
            for k in self.current_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.counters is not None:
            result['Counters'] = self.counters
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        result['CurrentTasks'] = []
        if self.current_tasks is not None:
            for k in self.current_tasks:
                result['CurrentTasks'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.executed_by is not None:
            result['ExecutedBy'] = self.executed_by
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.is_parent is not None:
            result['IsParent'] = self.is_parent
        if self.loop_mode is not None:
            result['LoopMode'] = self.loop_mode
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.parent_execution_id is not None:
            result['ParentExecutionId'] = self.parent_execution_id
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.safety_check is not None:
            result['SafetyCheck'] = self.safety_check
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Counters') is not None:
            self.counters = m.get('Counters')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        self.current_tasks = []
        if m.get('CurrentTasks') is not None:
            for k in m.get('CurrentTasks'):
                temp_model = StartExecutionResponseBodyExecutionCurrentTasks()
                self.current_tasks.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ExecutedBy') is not None:
            self.executed_by = m.get('ExecutedBy')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('IsParent') is not None:
            self.is_parent = m.get('IsParent')
        if m.get('LoopMode') is not None:
            self.loop_mode = m.get('LoopMode')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ParentExecutionId') is not None:
            self.parent_execution_id = m.get('ParentExecutionId')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SafetyCheck') is not None:
            self.safety_check = m.get('SafetyCheck')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class StartExecutionResponseBody(TeaModel):
    def __init__(
        self,
        execution: StartExecutionResponseBodyExecution = None,
        request_id: str = None,
    ):
        # The details of the execution.
        self.execution = execution
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.execution:
            self.execution.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution is not None:
            result['Execution'] = self.execution.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Execution') is not None:
            temp_model = StartExecutionResponseBodyExecution()
            self.execution = temp_model.from_map(m['Execution'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartExecutionResponseBody = None,
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
            temp_model = StartExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids: Dict[str, Any] = None,
        resource_type: str = None,
        tags: Dict[str, Any] = None,
    ):
        # The ID of the request.
        self.region_id = region_id
        # The operation that you want to perform. Set the value to TagResources.
        self.resource_ids = resource_ids
        # The IDs of resources. The number of resource IDs ranges from 1 to 50.
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class TagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids_shrink: str = None,
        resource_type: str = None,
        tags_shrink: str = None,
    ):
        # The ID of the request.
        self.region_id = region_id
        # The operation that you want to perform. Set the value to TagResources.
        self.resource_ids_shrink = resource_ids_shrink
        # The IDs of resources. The number of resource IDs ranges from 1 to 50.
        self.resource_type = resource_type
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class TagResourcesResponseBody(TeaModel):
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


class TriggerExecutionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        content: str = None,
        execution_id: str = None,
        region_id: str = None,
        type: str = None,
    ):
        self.client_token = client_token
        # The client token that is used to ensure the idempotence of the request.
        self.content = content
        # The ID of the request.
        self.execution_id = execution_id
        # The message body to be sent to the trigger task.
        self.region_id = region_id
        # The operation that you want to perform. Set the value to TriggerExecution.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.content is not None:
            result['Content'] = self.content
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class TriggerExecutionResponseBody(TeaModel):
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


class TriggerExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TriggerExecutionResponseBody = None,
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
            temp_model = TriggerExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_ids: Dict[str, Any] = None,
        resource_type: str = None,
        tag_keys: Dict[str, Any] = None,
    ):
        self.all = all
        # Specifies whether to delete all tags. This parameter takes effect only when the TagKeys parameter is not specified. Valid values: true and false. Default value: false. The TagKeys parameter is required when this parameter is set to false.
        self.region_id = region_id
        # You can call this operation to delete tags that are attached to one or more resources.
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class UntagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_ids_shrink: str = None,
        resource_type: str = None,
        tag_keys_shrink: str = None,
    ):
        self.all = all
        # Specifies whether to delete all tags. This parameter takes effect only when the TagKeys parameter is not specified. Valid values: true and false. Default value: false. The TagKeys parameter is required when this parameter is set to false.
        self.region_id = region_id
        # You can call this operation to delete tags that are attached to one or more resources.
        self.resource_ids_shrink = resource_ids_shrink
        self.resource_type = resource_type
        self.tag_keys_shrink = tag_keys_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_keys_shrink is not None:
            result['TagKeys'] = self.tag_keys_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKeys') is not None:
            self.tag_keys_shrink = m.get('TagKeys')
        return self


class UntagResourcesResponseBody(TeaModel):
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


class UpdateApplicationRequestAlarmConfig(TeaModel):
    def __init__(
        self,
        contact_groups: List[str] = None,
        health_check_url: str = None,
        template_ids: List[str] = None,
    ):
        self.contact_groups = contact_groups
        self.health_check_url = health_check_url
        self.template_ids = template_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')
        return self


class UpdateApplicationRequest(TeaModel):
    def __init__(
        self,
        alarm_config: UpdateApplicationRequestAlarmConfig = None,
        delete_alarm_rules_before_update: bool = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        tags: Dict[str, Any] = None,
    ):
        self.alarm_config = alarm_config
        self.delete_alarm_rules_before_update = delete_alarm_rules_before_update
        # The description to be updated for the application.
        self.description = description
        # The application name.
        self.name = name
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id
        # The tags.
        self.tags = tags

    def validate(self):
        if self.alarm_config:
            self.alarm_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_config is not None:
            result['AlarmConfig'] = self.alarm_config.to_map()
        if self.delete_alarm_rules_before_update is not None:
            result['DeleteAlarmRulesBeforeUpdate'] = self.delete_alarm_rules_before_update
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmConfig') is not None:
            temp_model = UpdateApplicationRequestAlarmConfig()
            self.alarm_config = temp_model.from_map(m['AlarmConfig'])
        if m.get('DeleteAlarmRulesBeforeUpdate') is not None:
            self.delete_alarm_rules_before_update = m.get('DeleteAlarmRulesBeforeUpdate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class UpdateApplicationShrinkRequest(TeaModel):
    def __init__(
        self,
        alarm_config_shrink: str = None,
        delete_alarm_rules_before_update: bool = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        tags_shrink: str = None,
    ):
        self.alarm_config_shrink = alarm_config_shrink
        self.delete_alarm_rules_before_update = delete_alarm_rules_before_update
        # The description to be updated for the application.
        self.description = description
        # The application name.
        self.name = name
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id
        # The tags.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_config_shrink is not None:
            result['AlarmConfig'] = self.alarm_config_shrink
        if self.delete_alarm_rules_before_update is not None:
            result['DeleteAlarmRulesBeforeUpdate'] = self.delete_alarm_rules_before_update
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmConfig') is not None:
            self.alarm_config_shrink = m.get('AlarmConfig')
        if m.get('DeleteAlarmRulesBeforeUpdate') is not None:
            self.delete_alarm_rules_before_update = m.get('DeleteAlarmRulesBeforeUpdate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class UpdateApplicationResponseBodyApplication(TeaModel):
    def __init__(
        self,
        created_date: str = None,
        description: str = None,
        name: str = None,
        resource_group_id: str = None,
        tags: Dict[str, Any] = None,
        updated_date: str = None,
    ):
        # The time when the application was created.
        self.created_date = created_date
        # The description of the application.
        self.description = description
        # The application name.
        self.name = name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags = tags
        # The time when the application was updated.
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdateApplicationResponseBody(TeaModel):
    def __init__(
        self,
        application: UpdateApplicationResponseBodyApplication = None,
        request_id: str = None,
    ):
        # The information about the application.
        self.application = application
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['Application'] = self.application.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Application') is not None:
            temp_model = UpdateApplicationResponseBodyApplication()
            self.application = temp_model.from_map(m['Application'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateApplicationResponseBody = None,
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
            temp_model = UpdateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationGroupRequest(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        name: str = None,
        new_name: str = None,
        region_id: str = None,
    ):
        # The application name.
        self.application_name = application_name
        # The name of the application group.
        self.name = name
        # The new name of the application group.
        self.new_name = new_name
        # The region ID. Set the value to cn-hangzhou.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.name is not None:
            result['Name'] = self.name
        if self.new_name is not None:
            result['NewName'] = self.new_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewName') is not None:
            self.new_name = m.get('NewName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateApplicationGroupResponseBodyApplicationGroup(TeaModel):
    def __init__(
        self,
        application_name: str = None,
        created_date: str = None,
        deploy_region_id: str = None,
        description: str = None,
        import_tag_key: str = None,
        import_tag_value: str = None,
        name: str = None,
        updated_date: str = None,
    ):
        # The application name.
        self.application_name = application_name
        # The time when the application group was created.
        self.created_date = created_date
        # The ID of the region in which the related resources reside.
        self.deploy_region_id = deploy_region_id
        # The description of the application group.
        self.description = description
        # The key of the tag.
        self.import_tag_key = import_tag_key
        # The value of the tag.
        self.import_tag_value = import_tag_value
        # The name of the application group.
        self.name = name
        # The time when the application group was updated.
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.import_tag_key is not None:
            result['ImportTagKey'] = self.import_tag_key
        if self.import_tag_value is not None:
            result['ImportTagValue'] = self.import_tag_value
        if self.name is not None:
            result['Name'] = self.name
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImportTagKey') is not None:
            self.import_tag_key = m.get('ImportTagKey')
        if m.get('ImportTagValue') is not None:
            self.import_tag_value = m.get('ImportTagValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdateApplicationGroupResponseBody(TeaModel):
    def __init__(
        self,
        application_group: UpdateApplicationGroupResponseBodyApplicationGroup = None,
        request_id: str = None,
    ):
        # The information about the application group.
        self.application_group = application_group
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.application_group:
            self.application_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_group is not None:
            result['ApplicationGroup'] = self.application_group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationGroup') is not None:
            temp_model = UpdateApplicationGroupResponseBodyApplicationGroup()
            self.application_group = temp_model.from_map(m['ApplicationGroup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateApplicationGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateApplicationGroupResponseBody = None,
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
            temp_model = UpdateApplicationGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExecutionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        execution_id: str = None,
        parameters: str = None,
        region_id: str = None,
    ):
        # The description of the execution.
        self.client_token = client_token
        # 执行的描述。
        self.description = description
        # The ID of the execution.
        self.execution_id = execution_id
        # A JSON string consisting of a collection of parameters. Default value: {}.
        self.parameters = parameters
        # The ID of the region.
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
        if self.description is not None:
            result['Description'] = self.description
        if self.execution_id is not None:
            result['ExecutionId'] = self.execution_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExecutionId') is not None:
            self.execution_id = m.get('ExecutionId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateExecutionResponseBody(TeaModel):
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


class UpdateExecutionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExecutionResponseBody = None,
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
            temp_model = UpdateExecutionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOpsItemRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        client_token: str = None,
        dedup_string: str = None,
        description: str = None,
        ops_item_id: str = None,
        priority: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resources: str = None,
        severity: str = None,
        solutions: str = None,
        source: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        title: str = None,
    ):
        self.category = category
        self.client_token = client_token
        self.dedup_string = dedup_string
        self.description = description
        self.ops_item_id = ops_item_id
        self.priority = priority
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resources = resources
        self.severity = severity
        self.solutions = solutions
        self.source = source
        self.status = status
        self.tags = tags
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedup_string is not None:
            result['DedupString'] = self.dedup_string
        if self.description is not None:
            result['Description'] = self.description
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.solutions is not None:
            result['Solutions'] = self.solutions
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedupString') is not None:
            self.dedup_string = m.get('DedupString')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateOpsItemShrinkRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        client_token: str = None,
        dedup_string: str = None,
        description: str = None,
        ops_item_id: str = None,
        priority: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resources: str = None,
        severity: str = None,
        solutions: str = None,
        source: str = None,
        status: str = None,
        tags_shrink: str = None,
        title: str = None,
    ):
        self.category = category
        self.client_token = client_token
        self.dedup_string = dedup_string
        self.description = description
        self.ops_item_id = ops_item_id
        self.priority = priority
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.resources = resources
        self.severity = severity
        self.solutions = solutions
        self.source = source
        self.status = status
        self.tags_shrink = tags_shrink
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedup_string is not None:
            result['DedupString'] = self.dedup_string
        if self.description is not None:
            result['Description'] = self.description
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.solutions is not None:
            result['Solutions'] = self.solutions
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedupString') is not None:
            self.dedup_string = m.get('DedupString')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateOpsItemResponseBodyOpsItem(TeaModel):
    def __init__(
        self,
        attributes: str = None,
        category: str = None,
        create_date: str = None,
        created_by: str = None,
        description: str = None,
        last_modified_by: str = None,
        ops_item_id: str = None,
        priority: int = None,
        resource_group_id: str = None,
        resources: List[str] = None,
        severity: str = None,
        solutions: List[str] = None,
        source: str = None,
        status: str = None,
        tags: Dict[str, Any] = None,
        title: str = None,
        update_date: str = None,
    ):
        self.attributes = attributes
        self.category = category
        self.create_date = create_date
        self.created_by = created_by
        self.description = description
        self.last_modified_by = last_modified_by
        self.ops_item_id = ops_item_id
        self.priority = priority
        self.resource_group_id = resource_group_id
        self.resources = resources
        self.severity = severity
        self.solutions = solutions
        self.source = source
        self.status = status
        self.tags = tags
        self.title = title
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.category is not None:
            result['Category'] = self.category
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.description is not None:
            result['Description'] = self.description
        if self.last_modified_by is not None:
            result['LastModifiedBy'] = self.last_modified_by
        if self.ops_item_id is not None:
            result['OpsItemId'] = self.ops_item_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.solutions is not None:
            result['Solutions'] = self.solutions
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LastModifiedBy') is not None:
            self.last_modified_by = m.get('LastModifiedBy')
        if m.get('OpsItemId') is not None:
            self.ops_item_id = m.get('OpsItemId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class UpdateOpsItemResponseBody(TeaModel):
    def __init__(
        self,
        ops_item: UpdateOpsItemResponseBodyOpsItem = None,
        request_id: str = None,
    ):
        self.ops_item = ops_item
        self.request_id = request_id

    def validate(self):
        if self.ops_item:
            self.ops_item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ops_item is not None:
            result['OpsItem'] = self.ops_item.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpsItem') is not None:
            temp_model = UpdateOpsItemResponseBodyOpsItem()
            self.ops_item = temp_model.from_map(m['OpsItem'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateOpsItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateOpsItemResponseBody = None,
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
            temp_model = UpdateOpsItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateParameterRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: str = None,
        value: str = None,
    ):
        # The ID of the common parameter.
        self.description = description
        # The data type of the common parameter.
        self.name = name
        # The version number of the common parameter.
        self.region_id = region_id
        # The operation that you want to perform. Set the value to UpdateParameter.
        self.resource_group_id = resource_group_id
        # The name of the common parameter.
        self.tags = tags
        # The value of the common parameter. The value must be 1 to 4096 characters in length.
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
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        parameter_version: int = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: str = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The ID of the request.
        self.constraints = constraints
        self.created_by = created_by
        self.created_date = created_date
        # The description of the common parameter. The description must be 1 to 200 characters in length.
        self.description = description
        self.id = id
        self.name = name
        self.parameter_version = parameter_version
        # Updates a common parameter.
        self.resource_group_id = resource_group_id
        self.share_type = share_type
        # The information of the common parameter.
        self.tags = tags
        # The user who updated the common parameter.
        self.type = type
        # The region ID of the resource.
        self.updated_by = updated_by
        # The description of the common parameter.
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdateParameterResponseBody(TeaModel):
    def __init__(
        self,
        parameter: UpdateParameterResponseBodyParameter = None,
        request_id: str = None,
    ):
        # The user who created the common parameter.
        self.parameter = parameter
        # The time when the common parameter was updated.
        self.request_id = request_id

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = UpdateParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateParameterResponseBody = None,
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
            temp_model = UpdateParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePatchBaselineRequestTags(TeaModel):
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


class UpdatePatchBaselineRequest(TeaModel):
    def __init__(
        self,
        approval_rules: str = None,
        approved_patches: List[str] = None,
        approved_patches_enable_non_security: bool = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        rejected_patches: List[str] = None,
        rejected_patches_action: str = None,
        sources: List[str] = None,
        tags: List[UpdatePatchBaselineRequestTags] = None,
    ):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules
        self.approved_patches = approved_patches
        self.approved_patches_enable_non_security = approved_patches_enable_non_security
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The description of the patch baseline.
        self.description = description
        # The name of the patch baseline.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        self.rejected_patches = rejected_patches
        self.rejected_patches_action = rejected_patches_action
        self.sources = sources
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
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rejected_patches is not None:
            result['RejectedPatches'] = self.rejected_patches
        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RejectedPatches') is not None:
            self.rejected_patches = m.get('RejectedPatches')
        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = UpdatePatchBaselineRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class UpdatePatchBaselineShrinkRequest(TeaModel):
    def __init__(
        self,
        approval_rules: str = None,
        approved_patches_shrink: str = None,
        approved_patches_enable_non_security: bool = None,
        client_token: str = None,
        description: str = None,
        name: str = None,
        region_id: str = None,
        rejected_patches_shrink: str = None,
        rejected_patches_action: str = None,
        sources_shrink: str = None,
        tags_shrink: str = None,
    ):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules
        self.approved_patches_shrink = approved_patches_shrink
        self.approved_patches_enable_non_security = approved_patches_enable_non_security
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The description of the patch baseline.
        self.description = description
        # The name of the patch baseline.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        self.rejected_patches_shrink = rejected_patches_shrink
        self.rejected_patches_action = rejected_patches_action
        self.sources_shrink = sources_shrink
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.approved_patches_shrink is not None:
            result['ApprovedPatches'] = self.approved_patches_shrink
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rejected_patches_shrink is not None:
            result['RejectedPatches'] = self.rejected_patches_shrink
        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action
        if self.sources_shrink is not None:
            result['Sources'] = self.sources_shrink
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ApprovedPatches') is not None:
            self.approved_patches_shrink = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RejectedPatches') is not None:
            self.rejected_patches_shrink = m.get('RejectedPatches')
        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')
        if m.get('Sources') is not None:
            self.sources_shrink = m.get('Sources')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        return self


class UpdatePatchBaselineResponseBodyPatchBaselineTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class UpdatePatchBaselineResponseBodyPatchBaseline(TeaModel):
    def __init__(
        self,
        approval_rules: str = None,
        approved_patches: List[str] = None,
        approved_patches_enable_non_security: bool = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        operation_system: str = None,
        rejected_patches: List[str] = None,
        rejected_patches_action: str = None,
        share_type: str = None,
        sources: List[str] = None,
        tags: List[UpdatePatchBaselineResponseBodyPatchBaselineTags] = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The rules of scanning and installing patches for the specified operating system.
        self.approval_rules = approval_rules
        self.approved_patches = approved_patches
        self.approved_patches_enable_non_security = approved_patches_enable_non_security
        # The creator of the patch baseline.
        self.created_by = created_by
        # The time when the patch baseline was created.
        self.created_date = created_date
        # The description of the patch baseline.
        self.description = description
        # The ID of the patch baseline.
        self.id = id
        # The name of the patch baseline.
        self.name = name
        # The operating system.
        self.operation_system = operation_system
        self.rejected_patches = rejected_patches
        self.rejected_patches_action = rejected_patches_action
        # The share type of the patch baseline.
        self.share_type = share_type
        self.sources = sources
        self.tags = tags
        # The user who updated the patch baseline.
        self.updated_by = updated_by
        # The time when the patch baseline was updated.
        self.updated_date = updated_date

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
        if self.approval_rules is not None:
            result['ApprovalRules'] = self.approval_rules
        if self.approved_patches is not None:
            result['ApprovedPatches'] = self.approved_patches
        if self.approved_patches_enable_non_security is not None:
            result['ApprovedPatchesEnableNonSecurity'] = self.approved_patches_enable_non_security
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_system is not None:
            result['OperationSystem'] = self.operation_system
        if self.rejected_patches is not None:
            result['RejectedPatches'] = self.rejected_patches
        if self.rejected_patches_action is not None:
            result['RejectedPatchesAction'] = self.rejected_patches_action
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.sources is not None:
            result['Sources'] = self.sources
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApprovalRules') is not None:
            self.approval_rules = m.get('ApprovalRules')
        if m.get('ApprovedPatches') is not None:
            self.approved_patches = m.get('ApprovedPatches')
        if m.get('ApprovedPatchesEnableNonSecurity') is not None:
            self.approved_patches_enable_non_security = m.get('ApprovedPatchesEnableNonSecurity')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationSystem') is not None:
            self.operation_system = m.get('OperationSystem')
        if m.get('RejectedPatches') is not None:
            self.rejected_patches = m.get('RejectedPatches')
        if m.get('RejectedPatchesAction') is not None:
            self.rejected_patches_action = m.get('RejectedPatchesAction')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = UpdatePatchBaselineResponseBodyPatchBaselineTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdatePatchBaselineResponseBody(TeaModel):
    def __init__(
        self,
        patch_baseline: UpdatePatchBaselineResponseBodyPatchBaseline = None,
        request_id: str = None,
    ):
        # The details of the patch baseline.
        self.patch_baseline = patch_baseline
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.patch_baseline:
            self.patch_baseline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.patch_baseline is not None:
            result['PatchBaseline'] = self.patch_baseline.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PatchBaseline') is not None:
            temp_model = UpdatePatchBaselineResponseBodyPatchBaseline()
            self.patch_baseline = temp_model.from_map(m['PatchBaseline'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePatchBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePatchBaselineResponseBody = None,
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
            temp_model = UpdatePatchBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecretParameterRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: Dict[str, Any] = None,
        value: str = None,
    ):
        # The description of the parameter. The description must be 1 to 200 characters in length.
        self.description = description
        # The name of the parameter. The name must be 1 to 180 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags of the parameter.
        self.tags = tags
        # The value of the parameter. The value must be 1 to 4096 characters in length.
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
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateSecretParameterShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags_shrink: str = None,
        value: str = None,
    ):
        # The description of the parameter. The description must be 1 to 200 characters in length.
        self.description = description
        # The name of the parameter. The name must be 1 to 180 characters in length, and can contain letters, digits, hyphens (-), and underscores (\_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags of the parameter.
        self.tags_shrink = tags_shrink
        # The value of the parameter. The value must be 1 to 4096 characters in length.
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
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateSecretParameterResponseBodyParameter(TeaModel):
    def __init__(
        self,
        constraints: str = None,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        id: str = None,
        key_id: str = None,
        name: str = None,
        parameter_version: int = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: str = None,
        type: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The constraints of the parameter.
        self.constraints = constraints
        # The user who created the parameter.
        self.created_by = created_by
        # The time when the parameter was created.
        self.created_date = created_date
        # The description of the parameter.
        self.description = description
        # The ID of the parameter.
        self.id = id
        # The ID of customer master key (CMK) of Key Management Service (KMS) that is used for encryption.
        self.key_id = key_id
        # The name of the parameter.
        self.name = name
        # The version number of the parameter.
        self.parameter_version = parameter_version
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the parameter.
        self.share_type = share_type
        # The tags of the parameter.
        self.tags = tags
        # The type of the parameter.
        self.type = type
        # The user who updated the parameter.
        self.updated_by = updated_by
        # The time when the parameter was updated.
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraints is not None:
            result['Constraints'] = self.constraints
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.key_id is not None:
            result['KeyId'] = self.key_id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.type is not None:
            result['Type'] = self.type
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdateSecretParameterResponseBody(TeaModel):
    def __init__(
        self,
        parameter: UpdateSecretParameterResponseBodyParameter = None,
        request_id: str = None,
    ):
        # The information about the parameter.
        self.parameter = parameter
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.parameter:
            self.parameter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter is not None:
            result['Parameter'] = self.parameter.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameter') is not None:
            temp_model = UpdateSecretParameterResponseBodyParameter()
            self.parameter = temp_model.from_map(m['Parameter'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSecretParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSecretParameterResponseBody = None,
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
            temp_model = UpdateSecretParameterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStateConfigurationRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        configure_mode: str = None,
        description: str = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        resource_group_id: str = None,
        schedule_expression: str = None,
        schedule_type: str = None,
        state_configuration_id: str = None,
        tags: Dict[str, Any] = None,
        targets: str = None,
    ):
        # The schedule type.
        self.client_token = client_token
        # The description of the desired-state configuration.
        self.configure_mode = configure_mode
        # The schedule expression.
        self.description = description
        # The ID of the region.
        self.parameters = parameters
        # The configuration mode.
        self.region_id = region_id
        # The parameters.
        self.resource_group_id = resource_group_id
        # The name of the template.
        self.schedule_expression = schedule_expression
        # The ID of the resource group.
        self.schedule_type = schedule_type
        # The ID of the desired-state configuration.
        self.state_configuration_id = state_configuration_id
        # The tag.
        self.tags = tags
        # The required resources.
        self.targets = targets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.state_configuration_id is not None:
            result['StateConfigurationId'] = self.state_configuration_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('StateConfigurationId') is not None:
            self.state_configuration_id = m.get('StateConfigurationId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class UpdateStateConfigurationShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        configure_mode: str = None,
        description: str = None,
        parameters_shrink: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        schedule_expression: str = None,
        schedule_type: str = None,
        state_configuration_id: str = None,
        tags_shrink: str = None,
        targets: str = None,
    ):
        # The schedule type.
        self.client_token = client_token
        # The description of the desired-state configuration.
        self.configure_mode = configure_mode
        # The schedule expression.
        self.description = description
        # The ID of the region.
        self.parameters_shrink = parameters_shrink
        # The configuration mode.
        self.region_id = region_id
        # The parameters.
        self.resource_group_id = resource_group_id
        # The name of the template.
        self.schedule_expression = schedule_expression
        # The ID of the resource group.
        self.schedule_type = schedule_type
        # The ID of the desired-state configuration.
        self.state_configuration_id = state_configuration_id
        # The tag.
        self.tags_shrink = tags_shrink
        # The required resources.
        self.targets = targets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.state_configuration_id is not None:
            result['StateConfigurationId'] = self.state_configuration_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('StateConfigurationId') is not None:
            self.state_configuration_id = m.get('StateConfigurationId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class UpdateStateConfigurationResponseBodyStateConfiguration(TeaModel):
    def __init__(
        self,
        configure_mode: str = None,
        create_time: str = None,
        description: str = None,
        parameters: str = None,
        resource_group_id: str = None,
        schedule_expression: str = None,
        schedule_type: str = None,
        state_configuration_id: str = None,
        tags: Dict[str, Any] = None,
        targets: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        update_time: str = None,
    ):
        # The configuration mode. ApplyOnce: The configuration is applied only once. After a configuration is updated, the new configuration is applied. ApplyAndMonitor: The configuration is applied only once. After the configuration is applied, the system only checks whether the configuration is migrated in the future. ApplyAndAutoCorrect: The configuration is always applied.
        self.configure_mode = configure_mode
        # The parameters.
        self.create_time = create_time
        # Updates a desired-state configuration.
        self.description = description
        # The ID of the request.
        self.parameters = parameters
        self.resource_group_id = resource_group_id
        # The configuration list.
        self.schedule_expression = schedule_expression
        # The update time.
        self.schedule_type = schedule_type
        # The schedule expression.
        self.state_configuration_id = state_configuration_id
        # The ID of the resource group.
        self.tags = tags
        # The required resources.
        self.targets = targets
        self.template_id = template_id
        # The ID of the desired-state configuration.
        self.template_name = template_name
        # The ID of the template.
        self.template_version = template_version
        # The version of the template.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.state_configuration_id is not None:
            result['StateConfigurationId'] = self.state_configuration_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.targets is not None:
            result['Targets'] = self.targets
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('StateConfigurationId') is not None:
            self.state_configuration_id = m.get('StateConfigurationId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class UpdateStateConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state_configuration: List[UpdateStateConfigurationResponseBodyStateConfiguration] = None,
    ):
        # The idempotency token.
        self.request_id = request_id
        # The description.
        self.state_configuration = state_configuration

    def validate(self):
        if self.state_configuration:
            for k in self.state_configuration:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StateConfiguration'] = []
        if self.state_configuration is not None:
            for k in self.state_configuration:
                result['StateConfiguration'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.state_configuration = []
        if m.get('StateConfiguration') is not None:
            for k in m.get('StateConfiguration'):
                temp_model = UpdateStateConfigurationResponseBodyStateConfiguration()
                self.state_configuration.append(temp_model.from_map(k))
        return self


class UpdateStateConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateStateConfigurationResponseBody = None,
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
            temp_model = UpdateStateConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: Dict[str, Any] = None,
        template_name: str = None,
        version_name: str = None,
    ):
        # The content of the template. The content must be in the JSON or YAML format, and its maximum size is 64 KB.
        self.content = content
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags
        # The name of the template. The name can be up to 200 characters in length and can contain letters, digits, hyphens (-), and underscores (\_). The name cannot start with ALIYUN, ACS, ALIBABA, or ALICLOUD.
        self.template_name = template_name
        # The name of the template version.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdateTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags_shrink: str = None,
        template_name: str = None,
        version_name: str = None,
    ):
        # The content of the template. The content must be in the JSON or YAML format, and its maximum size is 64 KB.
        self.content = content
        # The ID of the region.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags_shrink = tags_shrink
        # The name of the template. The name can be up to 200 characters in length and can contain letters, digits, hyphens (-), and underscores (\_). The name cannot start with ALIYUN, ACS, ALIBABA, or ALICLOUD.
        self.template_name = template_name
        # The name of the template version.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class UpdateTemplateResponseBodyTemplate(TeaModel):
    def __init__(
        self,
        created_by: str = None,
        created_date: str = None,
        description: str = None,
        has_trigger: bool = None,
        hash: str = None,
        resource_group_id: str = None,
        share_type: str = None,
        tags: Dict[str, Any] = None,
        template_format: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
        updated_by: str = None,
        updated_date: str = None,
    ):
        # The user who created the template.
        self.created_by = created_by
        # The time when the template was created.
        self.created_date = created_date
        # The description of the template.
        self.description = description
        # Indicates whether the template is configured with a trigger.
        self.has_trigger = has_trigger
        # The SHA-256 value of the template content.
        self.hash = hash
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The share type of the template. The share type of a user-created template is **Private**.
        self.share_type = share_type
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        self.tags = tags
        # The format of the template. The system automatically determines whether the format is JSON or YAML.
        self.template_format = template_format
        # The ID of the template.
        self.template_id = template_id
        # The name of the template.
        self.template_name = template_name
        # The version of the template. The name of the version consists of the letter v and a number. The number starts from 1.
        self.template_version = template_version
        # The user who last modified the information about the template.
        self.updated_by = updated_by
        # The time when the information about the template was last modified.
        self.updated_date = updated_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_by is not None:
            result['CreatedBy'] = self.created_by
        if self.created_date is not None:
            result['CreatedDate'] = self.created_date
        if self.description is not None:
            result['Description'] = self.description
        if self.has_trigger is not None:
            result['HasTrigger'] = self.has_trigger
        if self.hash is not None:
            result['Hash'] = self.hash
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_format is not None:
            result['TemplateFormat'] = self.template_format
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by
        if self.updated_date is not None:
            result['UpdatedDate'] = self.updated_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')
        if m.get('CreatedDate') is not None:
            self.created_date = m.get('CreatedDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasTrigger') is not None:
            self.has_trigger = m.get('HasTrigger')
        if m.get('Hash') is not None:
            self.hash = m.get('Hash')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateFormat') is not None:
            self.template_format = m.get('TemplateFormat')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')
        if m.get('UpdatedDate') is not None:
            self.updated_date = m.get('UpdatedDate')
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template: UpdateTemplateResponseBodyTemplate = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The metadata of the template.
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = UpdateTemplateResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTemplateResponseBody = None,
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
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateTemplateContentRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        region_id: str = None,
        template_url: str = None,
    ):
        # The content of the template.
        self.content = content
        # The ID of the region.
        self.region_id = region_id
        # The URL that is used to store the content of the Operation Orchestration Service (OOS) template in the Alibaba Cloud Object Storage Service (OSS). Only the public-read URL is supported. You can use this parameter to specify the tasks that you want to run. This way, you do not need to create a template before you start an execution. If you select an existing template, you do not need to specify this parameter.
        self.template_url = template_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.template_url is not None:
            result['TemplateURL'] = self.template_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TemplateURL') is not None:
            self.template_url = m.get('TemplateURL')
        return self


class ValidateTemplateContentResponseBodyTasks(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        outputs: str = None,
        properties: str = None,
        type: str = None,
    ):
        # The description of the task.
        self.description = description
        # The name of the task.
        self.name = name
        # The outputs of the task.
        self.outputs = outputs
        # The properties of the task.
        self.properties = properties
        # The type of the task.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ValidateTemplateContentResponseBody(TeaModel):
    def __init__(
        self,
        outputs: str = None,
        parameters: str = None,
        ram_role: str = None,
        request_id: str = None,
        tasks: List[ValidateTemplateContentResponseBodyTasks] = None,
    ):
        # The outputs of the template.
        self.outputs = outputs
        # The parameters of the template.
        self.parameters = parameters
        # The RAM role.
        self.ram_role = ram_role
        # The ID of the request.
        self.request_id = request_id
        # The task defined in the template.
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.ram_role is not None:
            result['RamRole'] = self.ram_role
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ValidateTemplateContentResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class ValidateTemplateContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateTemplateContentResponseBody = None,
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
            temp_model = ValidateTemplateContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


