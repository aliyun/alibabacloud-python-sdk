# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AbolishFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class AbolishFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AbolishFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AbolishFlowResponseBody = None,
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
            temp_model = AbolishFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        flow_version: int = None,
    ):
        self.flow_id = flow_id
        self.flow_version = flow_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        return self


class CloneFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloneFlowResponseBody = None,
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
            temp_model = CloneFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFlowRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        definition: str = None,
    ):
        self.name = name
        self.description = description
        self.definition = definition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.definition is not None:
            result['Definition'] = self.definition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        return self


class CreateFlowResponseBody(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        request_id: str = None,
    ):
        self.flow_id = flow_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFlowResponseBody = None,
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
            temp_model = CreateFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        flow_ids: str = None,
    ):
        self.flow_id = flow_id
        self.flow_ids = flow_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_ids is not None:
            result['FlowIds'] = self.flow_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowIds') is not None:
            self.flow_ids = m.get('FlowIds')
        return self


class DeleteFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFlowResponseBody = None,
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
            temp_model = DeleteFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class DeployFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeployFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeployFlowResponseBody = None,
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
            temp_model = DeployFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountSummaryResponseBody(TeaModel):
    def __init__(
        self,
        instance_count: int = None,
        online_instance_count: int = None,
        request_id: str = None,
        invocation_count: int = None,
        daily_invocation_error_count: int = None,
    ):
        self.instance_count = instance_count
        self.online_instance_count = online_instance_count
        self.request_id = request_id
        self.invocation_count = invocation_count
        self.daily_invocation_error_count = daily_invocation_error_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.online_instance_count is not None:
            result['OnlineInstanceCount'] = self.online_instance_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invocation_count is not None:
            result['InvocationCount'] = self.invocation_count
        if self.daily_invocation_error_count is not None:
            result['DailyInvocationErrorCount'] = self.daily_invocation_error_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('OnlineInstanceCount') is not None:
            self.online_instance_count = m.get('OnlineInstanceCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InvocationCount') is not None:
            self.invocation_count = m.get('InvocationCount')
        if m.get('DailyInvocationErrorCount') is not None:
            self.daily_invocation_error_count = m.get('DailyInvocationErrorCount')
        return self


class DescribeAccountSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAccountSummaryResponseBody = None,
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
            temp_model = DescribeAccountSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConnectorAttributeRequest(TeaModel):
    def __init__(
        self,
        connector_name: str = None,
        lang: str = None,
        step_info: str = None,
    ):
        self.connector_name = connector_name
        self.lang = lang
        self.step_info = step_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.connector_name is not None:
            result['ConnectorName'] = self.connector_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.step_info is not None:
            result['StepInfo'] = self.step_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectorName') is not None:
            self.connector_name = m.get('ConnectorName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('StepInfo') is not None:
            self.step_info = m.get('StepInfo')
        return self


class DescribeConnectorAttributeResponseBodyCapabilitiesActions(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        type: str = None,
        visibility: str = None,
        description: str = None,
        document_url: str = None,
        name: str = None,
        system: bool = None,
        default_action_name: str = None,
    ):
        self.display_name = display_name
        self.type = type
        self.visibility = visibility
        self.description = description
        self.document_url = document_url
        self.name = name
        self.system = system
        self.default_action_name = default_action_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.type is not None:
            result['Type'] = self.type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.description is not None:
            result['Description'] = self.description
        if self.document_url is not None:
            result['DocumentUrl'] = self.document_url
        if self.name is not None:
            result['Name'] = self.name
        if self.system is not None:
            result['System'] = self.system
        if self.default_action_name is not None:
            result['DefaultActionName'] = self.default_action_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocumentUrl') is not None:
            self.document_url = m.get('DocumentUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('System') is not None:
            self.system = m.get('System')
        if m.get('DefaultActionName') is not None:
            self.default_action_name = m.get('DefaultActionName')
        return self


class DescribeConnectorAttributeResponseBodyCapabilitiesTriggers(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        type: str = None,
        visibility: str = None,
        description: str = None,
        document_url: str = None,
        name: str = None,
        system: bool = None,
    ):
        self.display_name = display_name
        self.type = type
        self.visibility = visibility
        self.description = description
        self.document_url = document_url
        self.name = name
        self.system = system

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.type is not None:
            result['Type'] = self.type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.description is not None:
            result['Description'] = self.description
        if self.document_url is not None:
            result['DocumentUrl'] = self.document_url
        if self.name is not None:
            result['Name'] = self.name
        if self.system is not None:
            result['System'] = self.system
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocumentUrl') is not None:
            self.document_url = m.get('DocumentUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('System') is not None:
            self.system = m.get('System')
        return self


class DescribeConnectorAttributeResponseBodyCapabilities(TeaModel):
    def __init__(
        self,
        actions: List[DescribeConnectorAttributeResponseBodyCapabilitiesActions] = None,
        triggers: List[DescribeConnectorAttributeResponseBodyCapabilitiesTriggers] = None,
    ):
        self.actions = actions
        self.triggers = triggers

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        result['Triggers'] = []
        if self.triggers is not None:
            for k in self.triggers:
                result['Triggers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = DescribeConnectorAttributeResponseBodyCapabilitiesActions()
                self.actions.append(temp_model.from_map(k))
        self.triggers = []
        if m.get('Triggers') is not None:
            for k in m.get('Triggers'):
                temp_model = DescribeConnectorAttributeResponseBodyCapabilitiesTriggers()
                self.triggers.append(temp_model.from_map(k))
        return self


class DescribeConnectorAttributeResponseBodyIcon(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeConnectorAttributeResponseBodyStepResult(TeaModel):
    def __init__(
        self,
        has_next: bool = None,
    ):
        self.has_next = has_next

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        return self


class DescribeConnectorAttributeResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        category: str = None,
        request_id: str = None,
        capabilities: DescribeConnectorAttributeResponseBodyCapabilities = None,
        full_name: str = None,
        display_name: str = None,
        region_id: str = None,
        icon: DescribeConnectorAttributeResponseBodyIcon = None,
        brand_color: str = None,
        step_result: DescribeConnectorAttributeResponseBodyStepResult = None,
        name: str = None,
        connector_id: str = None,
    ):
        self.description = description
        self.category = category
        self.request_id = request_id
        self.capabilities = capabilities
        self.full_name = full_name
        self.display_name = display_name
        self.region_id = region_id
        self.icon = icon
        self.brand_color = brand_color
        self.step_result = step_result
        self.name = name
        self.connector_id = connector_id

    def validate(self):
        if self.capabilities:
            self.capabilities.validate()
        if self.icon:
            self.icon.validate()
        if self.step_result:
            self.step_result.validate()

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.category is not None:
            result['Category'] = self.category
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities.to_map()
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.icon is not None:
            result['Icon'] = self.icon.to_map()
        if self.brand_color is not None:
            result['BrandColor'] = self.brand_color
        if self.step_result is not None:
            result['StepResult'] = self.step_result.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Capabilities') is not None:
            temp_model = DescribeConnectorAttributeResponseBodyCapabilities()
            self.capabilities = temp_model.from_map(m['Capabilities'])
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Icon') is not None:
            temp_model = DescribeConnectorAttributeResponseBodyIcon()
            self.icon = temp_model.from_map(m['Icon'])
        if m.get('BrandColor') is not None:
            self.brand_color = m.get('BrandColor')
        if m.get('StepResult') is not None:
            temp_model = DescribeConnectorAttributeResponseBodyStepResult()
            self.step_result = temp_model.from_map(m['StepResult'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        return self


class DescribeConnectorAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConnectorAttributeResponseBody = None,
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
            temp_model = DescribeConnectorAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConnectorCapabilityRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
        lang: str = None,
        preset: str = None,
    ):
        self.type = type
        self.lang = lang
        self.preset = preset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.preset is not None:
            result['Preset'] = self.preset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Preset') is not None:
            self.preset = m.get('Preset')
        return self


class DescribeConnectorCapabilityResponseBodyConnections(TeaModel):
    def __init__(
        self,
        definition: str = None,
        connection_name: str = None,
        content: str = None,
    ):
        self.definition = definition
        self.connection_name = connection_name
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeConnectorCapabilityResponseBodyConnectorIcon(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeConnectorCapabilityResponseBodyConnectorConnectionParameters(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeConnectorCapabilityResponseBodyConnector(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        default_policy: List[str] = None,
        full_name: str = None,
        icon: DescribeConnectorCapabilityResponseBodyConnectorIcon = None,
        connector_id: str = None,
        region_id: str = None,
        ram_map: str = None,
        description: str = None,
        brand_color: str = None,
        category: str = None,
        connection_parameters: DescribeConnectorCapabilityResponseBodyConnectorConnectionParameters = None,
        name: str = None,
    ):
        self.display_name = display_name
        self.default_policy = default_policy
        self.full_name = full_name
        self.icon = icon
        self.connector_id = connector_id
        self.region_id = region_id
        self.ram_map = ram_map
        self.description = description
        self.brand_color = brand_color
        self.category = category
        self.connection_parameters = connection_parameters
        self.name = name

    def validate(self):
        if self.icon:
            self.icon.validate()
        if self.connection_parameters:
            self.connection_parameters.validate()

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.default_policy is not None:
            result['DefaultPolicy'] = self.default_policy
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.icon is not None:
            result['Icon'] = self.icon.to_map()
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.ram_map is not None:
            result['RamMap'] = self.ram_map
        if self.description is not None:
            result['Description'] = self.description
        if self.brand_color is not None:
            result['BrandColor'] = self.brand_color
        if self.category is not None:
            result['Category'] = self.category
        if self.connection_parameters is not None:
            result['ConnectionParameters'] = self.connection_parameters.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('DefaultPolicy') is not None:
            self.default_policy = m.get('DefaultPolicy')
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('Icon') is not None:
            temp_model = DescribeConnectorCapabilityResponseBodyConnectorIcon()
            self.icon = temp_model.from_map(m['Icon'])
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RamMap') is not None:
            self.ram_map = m.get('RamMap')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('BrandColor') is not None:
            self.brand_color = m.get('BrandColor')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ConnectionParameters') is not None:
            temp_model = DescribeConnectorCapabilityResponseBodyConnectorConnectionParameters()
            self.connection_parameters = temp_model.from_map(m['ConnectionParameters'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeConnectorCapabilityResponseBodyParametersSubParameters(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        type: str = None,
        required: bool = None,
        name: str = None,
    ):
        self.display_name = display_name
        self.type = type
        self.required = required
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.type is not None:
            result['Type'] = self.type
        if self.required is not None:
            result['Required'] = self.required
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeConnectorCapabilityResponseBodyParameters(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        type: str = None,
        place_holder: str = None,
        read_only: bool = None,
        example: str = None,
        default_value: str = None,
        sub_type: str = None,
        enum_display_name: List[str] = None,
        required: bool = None,
        description: str = None,
        position: str = None,
        enum: List[str] = None,
        sub_parameters: List[DescribeConnectorCapabilityResponseBodyParametersSubParameters] = None,
        name: str = None,
    ):
        self.display_name = display_name
        self.type = type
        self.place_holder = place_holder
        self.read_only = read_only
        self.example = example
        self.default_value = default_value
        self.sub_type = sub_type
        self.enum_display_name = enum_display_name
        self.required = required
        self.description = description
        self.position = position
        self.enum = enum
        self.sub_parameters = sub_parameters
        self.name = name

    def validate(self):
        if self.sub_parameters:
            for k in self.sub_parameters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.type is not None:
            result['Type'] = self.type
        if self.place_holder is not None:
            result['PlaceHolder'] = self.place_holder
        if self.read_only is not None:
            result['ReadOnly'] = self.read_only
        if self.example is not None:
            result['Example'] = self.example
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        if self.enum_display_name is not None:
            result['EnumDisplayName'] = self.enum_display_name
        if self.required is not None:
            result['Required'] = self.required
        if self.description is not None:
            result['Description'] = self.description
        if self.position is not None:
            result['Position'] = self.position
        if self.enum is not None:
            result['Enum'] = self.enum
        result['SubParameters'] = []
        if self.sub_parameters is not None:
            for k in self.sub_parameters:
                result['SubParameters'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('PlaceHolder') is not None:
            self.place_holder = m.get('PlaceHolder')
        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')
        if m.get('Example') is not None:
            self.example = m.get('Example')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        if m.get('EnumDisplayName') is not None:
            self.enum_display_name = m.get('EnumDisplayName')
        if m.get('Required') is not None:
            self.required = m.get('Required')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('Enum') is not None:
            self.enum = m.get('Enum')
        self.sub_parameters = []
        if m.get('SubParameters') is not None:
            for k in m.get('SubParameters'):
                temp_model = DescribeConnectorCapabilityResponseBodyParametersSubParameters()
                self.sub_parameters.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeConnectorCapabilityResponseBodyResponses(TeaModel):
    def __init__(
        self,
        type: str = None,
        display_name: str = None,
        description: str = None,
        expression: str = None,
        example: str = None,
        name: str = None,
    ):
        self.type = type
        self.display_name = display_name
        self.description = description
        self.expression = expression
        self.example = example
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.description is not None:
            result['Description'] = self.description
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.example is not None:
            result['Example'] = self.example
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Example') is not None:
            self.example = m.get('Example')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeConnectorCapabilityResponseBody(TeaModel):
    def __init__(
        self,
        connections: List[DescribeConnectorCapabilityResponseBodyConnections] = None,
        connector: DescribeConnectorCapabilityResponseBodyConnector = None,
        type: str = None,
        parameters: List[DescribeConnectorCapabilityResponseBodyParameters] = None,
        request_id: str = None,
        display_name: str = None,
        document_url: str = None,
        visibility: str = None,
        default_inputs: str = None,
        system: bool = None,
        name: str = None,
        responses: List[DescribeConnectorCapabilityResponseBodyResponses] = None,
    ):
        self.connections = connections
        self.connector = connector
        self.type = type
        self.parameters = parameters
        self.request_id = request_id
        self.display_name = display_name
        self.document_url = document_url
        self.visibility = visibility
        self.default_inputs = default_inputs
        self.system = system
        self.name = name
        self.responses = responses

    def validate(self):
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()
        if self.connector:
            self.connector.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()
        if self.responses:
            for k in self.responses:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        if self.connector is not None:
            result['Connector'] = self.connector.to_map()
        if self.type is not None:
            result['Type'] = self.type
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.document_url is not None:
            result['DocumentUrl'] = self.document_url
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.default_inputs is not None:
            result['DefaultInputs'] = self.default_inputs
        if self.system is not None:
            result['System'] = self.system
        if self.name is not None:
            result['Name'] = self.name
        result['Responses'] = []
        if self.responses is not None:
            for k in self.responses:
                result['Responses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k in m.get('Connections'):
                temp_model = DescribeConnectorCapabilityResponseBodyConnections()
                self.connections.append(temp_model.from_map(k))
        if m.get('Connector') is not None:
            temp_model = DescribeConnectorCapabilityResponseBodyConnector()
            self.connector = temp_model.from_map(m['Connector'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = DescribeConnectorCapabilityResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('DocumentUrl') is not None:
            self.document_url = m.get('DocumentUrl')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('DefaultInputs') is not None:
            self.default_inputs = m.get('DefaultInputs')
        if m.get('System') is not None:
            self.system = m.get('System')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.responses = []
        if m.get('Responses') is not None:
            for k in m.get('Responses'):
                temp_model = DescribeConnectorCapabilityResponseBodyResponses()
                self.responses.append(temp_model.from_map(k))
        return self


class DescribeConnectorCapabilityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeConnectorCapabilityResponseBody = None,
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
            temp_model = DescribeConnectorCapabilityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        flow_version: int = None,
    ):
        self.flow_id = flow_id
        self.flow_version = flow_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        return self


class DescribeFlowResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        flow_id: str = None,
        description: str = None,
        request_id: str = None,
        version: int = None,
        created_at: str = None,
        definition: str = None,
        edit_mode: str = None,
        region_id: str = None,
        updated_at: str = None,
        source: str = None,
        name: str = None,
    ):
        self.status = status
        self.flow_id = flow_id
        self.description = description
        self.request_id = request_id
        self.version = version
        self.created_at = created_at
        self.definition = definition
        self.edit_mode = edit_mode
        self.region_id = region_id
        self.updated_at = updated_at
        self.source = source
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.edit_mode is not None:
            result['EditMode'] = self.edit_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.source is not None:
            result['Source'] = self.source
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('EditMode') is not None:
            self.edit_mode = m.get('EditMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFlowResponseBody = None,
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
            temp_model = DescribeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowMetricRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class DescribeFlowMetricResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        invocation_count: int = None,
        invocation_error_count: int = None,
        error_rate: float = None,
        cost_average: int = None,
    ):
        self.request_id = request_id
        self.invocation_count = invocation_count
        self.invocation_error_count = invocation_error_count
        self.error_rate = error_rate
        self.cost_average = cost_average

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invocation_count is not None:
            result['InvocationCount'] = self.invocation_count
        if self.invocation_error_count is not None:
            result['InvocationErrorCount'] = self.invocation_error_count
        if self.error_rate is not None:
            result['ErrorRate'] = self.error_rate
        if self.cost_average is not None:
            result['CostAverage'] = self.cost_average
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InvocationCount') is not None:
            self.invocation_count = m.get('InvocationCount')
        if m.get('InvocationErrorCount') is not None:
            self.invocation_error_count = m.get('InvocationErrorCount')
        if m.get('ErrorRate') is not None:
            self.error_rate = m.get('ErrorRate')
        if m.get('CostAverage') is not None:
            self.cost_average = m.get('CostAverage')
        return self


class DescribeFlowMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFlowMetricResponseBody = None,
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
            temp_model = DescribeFlowMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFlowTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: str = None,
    ):
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeFlowTemplateResponseBody(TeaModel):
    def __init__(
        self,
        locale: str = None,
        connector: str = None,
        summary_en: str = None,
        description: str = None,
        request_id: str = None,
        created_at: str = None,
        definition: str = None,
        overview: str = None,
        updated_at: str = None,
        name: str = None,
        summary: str = None,
        tag: str = None,
        template_id: str = None,
    ):
        self.locale = locale
        self.connector = connector
        self.summary_en = summary_en
        self.description = description
        self.request_id = request_id
        self.created_at = created_at
        self.definition = definition
        self.overview = overview
        self.updated_at = updated_at
        self.name = name
        self.summary = summary
        self.tag = tag
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.connector is not None:
            result['Connector'] = self.connector
        if self.summary_en is not None:
            result['SummaryEn'] = self.summary_en
        if self.description is not None:
            result['Description'] = self.description
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.overview is not None:
            result['Overview'] = self.overview
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Connector') is not None:
            self.connector = m.get('Connector')
        if m.get('SummaryEn') is not None:
            self.summary_en = m.get('SummaryEn')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Overview') is not None:
            self.overview = m.get('Overview')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DescribeFlowTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFlowTemplateResponseBody = None,
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
            temp_model = DescribeFlowTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInvocationLogRequest(TeaModel):
    def __init__(
        self,
        invocation_id: str = None,
        pages: str = None,
    ):
        self.invocation_id = invocation_id
        self.pages = pages

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id
        if self.pages is not None:
            result['Pages'] = self.pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        return self


class DescribeInvocationLogResponseBodyActionsError(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
    ):
        self.error_code = error_code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DescribeInvocationLogResponseBodyActionsOutputsResult(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        content_size: str = None,
        url: str = None,
    ):
        self.content_type = content_type
        self.content_size = content_size
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.content_size is not None:
            result['ContentSize'] = self.content_size
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ContentSize') is not None:
            self.content_size = m.get('ContentSize')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeInvocationLogResponseBodyActionsInputsResult(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        content_size: str = None,
        url: str = None,
    ):
        self.content_type = content_type
        self.content_size = content_size
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.content_size is not None:
            result['ContentSize'] = self.content_size
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ContentSize') is not None:
            self.content_size = m.get('ContentSize')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeInvocationLogResponseBodyActions(TeaModel):
    def __init__(
        self,
        loop_count: int = None,
        end_time: int = None,
        status: str = None,
        start_time: int = None,
        invocation_id: str = None,
        return_code: str = None,
        error: DescribeInvocationLogResponseBodyActionsError = None,
        outputs_result: DescribeInvocationLogResponseBodyActionsOutputsResult = None,
        name: str = None,
        inputs_result: DescribeInvocationLogResponseBodyActionsInputsResult = None,
    ):
        self.loop_count = loop_count
        self.end_time = end_time
        self.status = status
        self.start_time = start_time
        self.invocation_id = invocation_id
        self.return_code = return_code
        self.error = error
        self.outputs_result = outputs_result
        self.name = name
        self.inputs_result = inputs_result

    def validate(self):
        if self.error:
            self.error.validate()
        if self.outputs_result:
            self.outputs_result.validate()
        if self.inputs_result:
            self.inputs_result.validate()

    def to_map(self):
        result = dict()
        if self.loop_count is not None:
            result['LoopCount'] = self.loop_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id
        if self.return_code is not None:
            result['ReturnCode'] = self.return_code
        if self.error is not None:
            result['Error'] = self.error.to_map()
        if self.outputs_result is not None:
            result['OutputsResult'] = self.outputs_result.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.inputs_result is not None:
            result['InputsResult'] = self.inputs_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoopCount') is not None:
            self.loop_count = m.get('LoopCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')
        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')
        if m.get('Error') is not None:
            temp_model = DescribeInvocationLogResponseBodyActionsError()
            self.error = temp_model.from_map(m['Error'])
        if m.get('OutputsResult') is not None:
            temp_model = DescribeInvocationLogResponseBodyActionsOutputsResult()
            self.outputs_result = temp_model.from_map(m['OutputsResult'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('InputsResult') is not None:
            temp_model = DescribeInvocationLogResponseBodyActionsInputsResult()
            self.inputs_result = temp_model.from_map(m['InputsResult'])
        return self


class DescribeInvocationLogResponseBodyWorkflow(TeaModel):
    def __init__(
        self,
        definition: str = None,
        version: str = None,
        flow_id: str = None,
    ):
        self.definition = definition
        self.version = version
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.version is not None:
            result['Version'] = self.version
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class DescribeInvocationLogResponseBodyInvocationError(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
    ):
        self.error_code = error_code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DescribeInvocationLogResponseBodyTriggerError(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
    ):
        self.error_code = error_code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DescribeInvocationLogResponseBodyTriggerOutputsResult(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        content_size: str = None,
        url: str = None,
    ):
        self.content_type = content_type
        self.content_size = content_size
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.content_size is not None:
            result['ContentSize'] = self.content_size
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ContentSize') is not None:
            self.content_size = m.get('ContentSize')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeInvocationLogResponseBodyTriggerInputsResult(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        content_size: str = None,
        url: str = None,
    ):
        self.content_type = content_type
        self.content_size = content_size
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.content_size is not None:
            result['ContentSize'] = self.content_size
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ContentSize') is not None:
            self.content_size = m.get('ContentSize')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeInvocationLogResponseBodyTrigger(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        status: str = None,
        start_time: int = None,
        invocation_id: str = None,
        return_code: str = None,
        error: DescribeInvocationLogResponseBodyTriggerError = None,
        outputs_result: DescribeInvocationLogResponseBodyTriggerOutputsResult = None,
        name: str = None,
        inputs_result: DescribeInvocationLogResponseBodyTriggerInputsResult = None,
    ):
        self.end_time = end_time
        self.status = status
        self.start_time = start_time
        self.invocation_id = invocation_id
        self.return_code = return_code
        self.error = error
        self.outputs_result = outputs_result
        self.name = name
        self.inputs_result = inputs_result

    def validate(self):
        if self.error:
            self.error.validate()
        if self.outputs_result:
            self.outputs_result.validate()
        if self.inputs_result:
            self.inputs_result.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id
        if self.return_code is not None:
            result['ReturnCode'] = self.return_code
        if self.error is not None:
            result['Error'] = self.error.to_map()
        if self.outputs_result is not None:
            result['OutputsResult'] = self.outputs_result.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.inputs_result is not None:
            result['InputsResult'] = self.inputs_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')
        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')
        if m.get('Error') is not None:
            temp_model = DescribeInvocationLogResponseBodyTriggerError()
            self.error = temp_model.from_map(m['Error'])
        if m.get('OutputsResult') is not None:
            temp_model = DescribeInvocationLogResponseBodyTriggerOutputsResult()
            self.outputs_result = temp_model.from_map(m['OutputsResult'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('InputsResult') is not None:
            temp_model = DescribeInvocationLogResponseBodyTriggerInputsResult()
            self.inputs_result = temp_model.from_map(m['InputsResult'])
        return self


class DescribeInvocationLogResponseBodyResponseResult(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        content_size: str = None,
        url: str = None,
    ):
        self.content_type = content_type
        self.content_size = content_size
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.content_size is not None:
            result['ContentSize'] = self.content_size
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ContentSize') is not None:
            self.content_size = m.get('ContentSize')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeInvocationLogResponseBodyOutputsResult(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        content_size: str = None,
        url: str = None,
    ):
        self.content_type = content_type
        self.content_size = content_size
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.content_size is not None:
            result['ContentSize'] = self.content_size
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ContentSize') is not None:
            self.content_size = m.get('ContentSize')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeInvocationLogResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        parameters: Dict[str, Any] = None,
        return_code: str = None,
        end_time: int = None,
        request_id: str = None,
        actions: List[DescribeInvocationLogResponseBodyActions] = None,
        timeout_time: int = None,
        start_time: int = None,
        workflow: DescribeInvocationLogResponseBodyWorkflow = None,
        invocation_error: DescribeInvocationLogResponseBodyInvocationError = None,
        trigger: DescribeInvocationLogResponseBodyTrigger = None,
        response_result: DescribeInvocationLogResponseBodyResponseResult = None,
        invocation_id: str = None,
        outputs_result: DescribeInvocationLogResponseBodyOutputsResult = None,
    ):
        self.status = status
        self.parameters = parameters
        self.return_code = return_code
        self.end_time = end_time
        self.request_id = request_id
        self.actions = actions
        self.timeout_time = timeout_time
        self.start_time = start_time
        self.workflow = workflow
        self.invocation_error = invocation_error
        self.trigger = trigger
        self.response_result = response_result
        self.invocation_id = invocation_id
        self.outputs_result = outputs_result

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.workflow:
            self.workflow.validate()
        if self.invocation_error:
            self.invocation_error.validate()
        if self.trigger:
            self.trigger.validate()
        if self.response_result:
            self.response_result.validate()
        if self.outputs_result:
            self.outputs_result.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.return_code is not None:
            result['ReturnCode'] = self.return_code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.timeout_time is not None:
            result['TimeoutTime'] = self.timeout_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.workflow is not None:
            result['Workflow'] = self.workflow.to_map()
        if self.invocation_error is not None:
            result['InvocationError'] = self.invocation_error.to_map()
        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()
        if self.response_result is not None:
            result['ResponseResult'] = self.response_result.to_map()
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id
        if self.outputs_result is not None:
            result['OutputsResult'] = self.outputs_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = DescribeInvocationLogResponseBodyActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('TimeoutTime') is not None:
            self.timeout_time = m.get('TimeoutTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Workflow') is not None:
            temp_model = DescribeInvocationLogResponseBodyWorkflow()
            self.workflow = temp_model.from_map(m['Workflow'])
        if m.get('InvocationError') is not None:
            temp_model = DescribeInvocationLogResponseBodyInvocationError()
            self.invocation_error = temp_model.from_map(m['InvocationError'])
        if m.get('Trigger') is not None:
            temp_model = DescribeInvocationLogResponseBodyTrigger()
            self.trigger = temp_model.from_map(m['Trigger'])
        if m.get('ResponseResult') is not None:
            temp_model = DescribeInvocationLogResponseBodyResponseResult()
            self.response_result = temp_model.from_map(m['ResponseResult'])
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')
        if m.get('OutputsResult') is not None:
            temp_model = DescribeInvocationLogResponseBodyOutputsResult()
            self.outputs_result = temp_model.from_map(m['OutputsResult'])
        return self


class DescribeInvocationLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInvocationLogResponseBody = None,
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
            temp_model = DescribeInvocationLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMetricDetailRequest(TeaModel):
    def __init__(
        self,
        metric_name: str = None,
        period: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.metric_name = metric_name
        self.period = period
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.period is not None:
            result['Period'] = self.period
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class DescribeMetricDetailResponseBodyDatapoints(TeaModel):
    def __init__(
        self,
        value: str = None,
        timestamp: int = None,
    ):
        self.value = value
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeMetricDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        datapoints: List[DescribeMetricDetailResponseBodyDatapoints] = None,
    ):
        self.request_id = request_id
        self.datapoints = datapoints

    def validate(self):
        if self.datapoints:
            for k in self.datapoints:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Datapoints'] = []
        if self.datapoints is not None:
            for k in self.datapoints:
                result['Datapoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.datapoints = []
        if m.get('Datapoints') is not None:
            for k in m.get('Datapoints'):
                temp_model = DescribeMetricDetailResponseBodyDatapoints()
                self.datapoints.append(temp_model.from_map(k))
        return self


class DescribeMetricDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMetricDetailResponseBody = None,
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
            temp_model = DescribeMetricDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class DisableFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableFlowResponseBody = None,
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
            temp_model = DisableFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class EnableFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableFlowResponseBody = None,
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
            temp_model = EnableFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        parameters: str = None,
        data: str = None,
        client_token: str = None,
        definition: str = None,
    ):
        self.flow_id = flow_id
        self.parameters = parameters
        self.data = data
        self.client_token = client_token
        self.definition = definition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.data is not None:
            result['Data'] = self.data
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.definition is not None:
            result['Definition'] = self.definition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        return self


class InvokeFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        invocation_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.invocation_id = invocation_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InvokeFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InvokeFlowResponseBody = None,
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
            temp_model = InvokeFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectorsRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        lang: str = None,
    ):
        self.category = category
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ListConnectorsResponseBodyConnectorsIcon(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListConnectorsResponseBodyConnectorsConnectionParameters(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListConnectorsResponseBodyConnectors(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        capabilities: List[str] = None,
        parent_connector: str = None,
        full_name: str = None,
        icon: ListConnectorsResponseBodyConnectorsIcon = None,
        connector_id: str = None,
        region_id: str = None,
        description: str = None,
        brand_color: str = None,
        category: str = None,
        connection_parameters: ListConnectorsResponseBodyConnectorsConnectionParameters = None,
        name: str = None,
    ):
        self.display_name = display_name
        self.capabilities = capabilities
        self.parent_connector = parent_connector
        self.full_name = full_name
        self.icon = icon
        self.connector_id = connector_id
        self.region_id = region_id
        self.description = description
        self.brand_color = brand_color
        self.category = category
        self.connection_parameters = connection_parameters
        self.name = name

    def validate(self):
        if self.icon:
            self.icon.validate()
        if self.connection_parameters:
            self.connection_parameters.validate()

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities
        if self.parent_connector is not None:
            result['ParentConnector'] = self.parent_connector
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.icon is not None:
            result['Icon'] = self.icon.to_map()
        if self.connector_id is not None:
            result['ConnectorId'] = self.connector_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.description is not None:
            result['Description'] = self.description
        if self.brand_color is not None:
            result['BrandColor'] = self.brand_color
        if self.category is not None:
            result['Category'] = self.category
        if self.connection_parameters is not None:
            result['ConnectionParameters'] = self.connection_parameters.to_map()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Capabilities') is not None:
            self.capabilities = m.get('Capabilities')
        if m.get('ParentConnector') is not None:
            self.parent_connector = m.get('ParentConnector')
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('Icon') is not None:
            temp_model = ListConnectorsResponseBodyConnectorsIcon()
            self.icon = temp_model.from_map(m['Icon'])
        if m.get('ConnectorId') is not None:
            self.connector_id = m.get('ConnectorId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('BrandColor') is not None:
            self.brand_color = m.get('BrandColor')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ConnectionParameters') is not None:
            temp_model = ListConnectorsResponseBodyConnectorsConnectionParameters()
            self.connection_parameters = temp_model.from_map(m['ConnectionParameters'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListConnectorsResponseBody(TeaModel):
    def __init__(
        self,
        connectors: List[ListConnectorsResponseBodyConnectors] = None,
        request_id: str = None,
    ):
        self.connectors = connectors
        self.request_id = request_id

    def validate(self):
        if self.connectors:
            for k in self.connectors:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Connectors'] = []
        if self.connectors is not None:
            for k in self.connectors:
                result['Connectors'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connectors = []
        if m.get('Connectors') is not None:
            for k in m.get('Connectors'):
                temp_model = ListConnectorsResponseBodyConnectors()
                self.connectors.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListConnectorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConnectorsResponseBody = None,
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
            temp_model = ListConnectorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectorTriggersRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        lang: str = None,
    ):
        self.category = category
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ListConnectorTriggersResponseBodyTriggersConnectorIcon(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListConnectorTriggersResponseBodyTriggersConnector(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        description: str = None,
        full_name: str = None,
        brand_color: str = None,
        icon: ListConnectorTriggersResponseBodyTriggersConnectorIcon = None,
        category: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.display_name = display_name
        self.description = description
        self.full_name = full_name
        self.brand_color = brand_color
        self.icon = icon
        self.category = category
        self.name = name
        self.region_id = region_id

    def validate(self):
        if self.icon:
            self.icon.validate()

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.description is not None:
            result['Description'] = self.description
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.brand_color is not None:
            result['BrandColor'] = self.brand_color
        if self.icon is not None:
            result['Icon'] = self.icon.to_map()
        if self.category is not None:
            result['Category'] = self.category
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('BrandColor') is not None:
            self.brand_color = m.get('BrandColor')
        if m.get('Icon') is not None:
            temp_model = ListConnectorTriggersResponseBodyTriggersConnectorIcon()
            self.icon = temp_model.from_map(m['Icon'])
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListConnectorTriggersResponseBodyTriggers(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        type: str = None,
        visibility: str = None,
        description: str = None,
        document_url: str = None,
        connector: ListConnectorTriggersResponseBodyTriggersConnector = None,
        name: str = None,
        system: bool = None,
    ):
        self.display_name = display_name
        self.type = type
        self.visibility = visibility
        self.description = description
        self.document_url = document_url
        self.connector = connector
        self.name = name
        self.system = system

    def validate(self):
        if self.connector:
            self.connector.validate()

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.type is not None:
            result['Type'] = self.type
        if self.visibility is not None:
            result['Visibility'] = self.visibility
        if self.description is not None:
            result['Description'] = self.description
        if self.document_url is not None:
            result['DocumentUrl'] = self.document_url
        if self.connector is not None:
            result['Connector'] = self.connector.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.system is not None:
            result['System'] = self.system
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DocumentUrl') is not None:
            self.document_url = m.get('DocumentUrl')
        if m.get('Connector') is not None:
            temp_model = ListConnectorTriggersResponseBodyTriggersConnector()
            self.connector = temp_model.from_map(m['Connector'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('System') is not None:
            self.system = m.get('System')
        return self


class ListConnectorTriggersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        triggers: List[ListConnectorTriggersResponseBodyTriggers] = None,
    ):
        self.request_id = request_id
        self.triggers = triggers

    def validate(self):
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Triggers'] = []
        if self.triggers is not None:
            for k in self.triggers:
                result['Triggers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.triggers = []
        if m.get('Triggers') is not None:
            for k in m.get('Triggers'):
                temp_model = ListConnectorTriggersResponseBodyTriggers()
                self.triggers.append(temp_model.from_map(k))
        return self


class ListConnectorTriggersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConnectorTriggersResponseBody = None,
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
            temp_model = ListConnectorTriggersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        name: str = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListFlowResponseBodyFlows(TeaModel):
    def __init__(
        self,
        status: str = None,
        prod_version: int = None,
        description: str = None,
        created_at: str = None,
        current_version: int = None,
        edit_mode: str = None,
        updated_at: str = None,
        source: str = None,
        name: str = None,
        flow_id: str = None,
    ):
        self.status = status
        self.prod_version = prod_version
        self.description = description
        self.created_at = created_at
        self.current_version = current_version
        self.edit_mode = edit_mode
        self.updated_at = updated_at
        self.source = source
        self.name = name
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.prod_version is not None:
            result['ProdVersion'] = self.prod_version
        if self.description is not None:
            result['Description'] = self.description
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.edit_mode is not None:
            result['EditMode'] = self.edit_mode
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.source is not None:
            result['Source'] = self.source
        if self.name is not None:
            result['Name'] = self.name
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ProdVersion') is not None:
            self.prod_version = m.get('ProdVersion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('EditMode') is not None:
            self.edit_mode = m.get('EditMode')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class ListFlowResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        total_page: int = None,
        request_id: str = None,
        flows: List[ListFlowResponseBodyFlows] = None,
    ):
        self.total_count = total_count
        self.total_page = total_page
        self.request_id = request_id
        self.flows = flows

    def validate(self):
        if self.flows:
            for k in self.flows:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Flows'] = []
        if self.flows is not None:
            for k in self.flows:
                result['Flows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.flows = []
        if m.get('Flows') is not None:
            for k in m.get('Flows'):
                temp_model = ListFlowResponseBodyFlows()
                self.flows.append(temp_model.from_map(k))
        return self


class ListFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFlowResponseBody = None,
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
            temp_model = ListFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowConnectionsRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class ListFlowConnectionsResponseBodyConnectionsActions(TeaModel):
    def __init__(
        self,
        type: str = None,
        action_name: str = None,
    ):
        self.type = type
        self.action_name = action_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.action_name is not None:
            result['ActionName'] = self.action_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ActionName') is not None:
            self.action_name = m.get('ActionName')
        return self


class ListFlowConnectionsResponseBodyConnectionsConnectorIcon(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListFlowConnectionsResponseBodyConnectionsConnectorConnectionParameters(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFlowConnectionsResponseBodyConnectionsConnector(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        brand_color: str = None,
        icon: ListFlowConnectionsResponseBodyConnectionsConnectorIcon = None,
        name: str = None,
        connection_parameters: ListFlowConnectionsResponseBodyConnectionsConnectorConnectionParameters = None,
    ):
        self.display_name = display_name
        self.brand_color = brand_color
        self.icon = icon
        self.name = name
        self.connection_parameters = connection_parameters

    def validate(self):
        if self.icon:
            self.icon.validate()
        if self.connection_parameters:
            self.connection_parameters.validate()

    def to_map(self):
        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.brand_color is not None:
            result['BrandColor'] = self.brand_color
        if self.icon is not None:
            result['Icon'] = self.icon.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.connection_parameters is not None:
            result['ConnectionParameters'] = self.connection_parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('BrandColor') is not None:
            self.brand_color = m.get('BrandColor')
        if m.get('Icon') is not None:
            temp_model = ListFlowConnectionsResponseBodyConnectionsConnectorIcon()
            self.icon = temp_model.from_map(m['Icon'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ConnectionParameters') is not None:
            temp_model = ListFlowConnectionsResponseBodyConnectionsConnectorConnectionParameters()
            self.connection_parameters = temp_model.from_map(m['ConnectionParameters'])
        return self


class ListFlowConnectionsResponseBodyConnections(TeaModel):
    def __init__(
        self,
        definition: str = None,
        actions: List[ListFlowConnectionsResponseBodyConnectionsActions] = None,
        connection_name: str = None,
        connector: ListFlowConnectionsResponseBodyConnectionsConnector = None,
        content: str = None,
    ):
        self.definition = definition
        self.actions = actions
        self.connection_name = connection_name
        self.connector = connector
        self.content = content

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.connector:
            self.connector.validate()

    def to_map(self):
        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        result['Actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['Actions'].append(k.to_map() if k else None)
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.connector is not None:
            result['Connector'] = self.connector.to_map()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        self.actions = []
        if m.get('Actions') is not None:
            for k in m.get('Actions'):
                temp_model = ListFlowConnectionsResponseBodyConnectionsActions()
                self.actions.append(temp_model.from_map(k))
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('Connector') is not None:
            temp_model = ListFlowConnectionsResponseBodyConnectionsConnector()
            self.connector = temp_model.from_map(m['Connector'])
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ListFlowConnectionsResponseBody(TeaModel):
    def __init__(
        self,
        connections: List[ListFlowConnectionsResponseBodyConnections] = None,
        request_id: str = None,
    ):
        self.connections = connections
        self.request_id = request_id

    def validate(self):
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k in m.get('Connections'):
                temp_model = ListFlowConnectionsResponseBodyConnections()
                self.connections.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowConnectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFlowConnectionsResponseBody = None,
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
            temp_model = ListFlowConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowTemplateRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        name: str = None,
        tag: str = None,
        lang: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.name = name
        self.tag = tag
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ListFlowTemplateResponseBodyFlowTemplates(TeaModel):
    def __init__(
        self,
        summary: str = None,
        locale: str = None,
        summary_en: str = None,
        created_at: str = None,
        overview: str = None,
        connector: str = None,
        tag: str = None,
        creator: str = None,
        description: str = None,
        version: int = None,
        updated_at: str = None,
        name: str = None,
        template_id: str = None,
    ):
        self.summary = summary
        self.locale = locale
        self.summary_en = summary_en
        self.created_at = created_at
        self.overview = overview
        self.connector = connector
        self.tag = tag
        self.creator = creator
        self.description = description
        self.version = version
        self.updated_at = updated_at
        self.name = name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.summary_en is not None:
            result['SummaryEn'] = self.summary_en
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.overview is not None:
            result['Overview'] = self.overview
        if self.connector is not None:
            result['Connector'] = self.connector
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.description is not None:
            result['Description'] = self.description
        if self.version is not None:
            result['Version'] = self.version
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('SummaryEn') is not None:
            self.summary_en = m.get('SummaryEn')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Overview') is not None:
            self.overview = m.get('Overview')
        if m.get('Connector') is not None:
            self.connector = m.get('Connector')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ListFlowTemplateResponseBody(TeaModel):
    def __init__(
        self,
        total_page: int = None,
        request_id: str = None,
        flow_templates: List[ListFlowTemplateResponseBodyFlowTemplates] = None,
    ):
        self.total_page = total_page
        self.request_id = request_id
        self.flow_templates = flow_templates

    def validate(self):
        if self.flow_templates:
            for k in self.flow_templates:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['FlowTemplates'] = []
        if self.flow_templates is not None:
            for k in self.flow_templates:
                result['FlowTemplates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.flow_templates = []
        if m.get('FlowTemplates') is not None:
            for k in m.get('FlowTemplates'):
                temp_model = ListFlowTemplateResponseBodyFlowTemplates()
                self.flow_templates.append(temp_model.from_map(k))
        return self


class ListFlowTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFlowTemplateResponseBody = None,
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
            temp_model = ListFlowTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowTriggersRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class ListFlowTriggersResponseBodyTriggers(TeaModel):
    def __init__(
        self,
        trigger_name: str = None,
        endpoint: str = None,
        actions_count: int = None,
        trigger_action_name: str = None,
        trigger_description: str = None,
        trigger_action_description: str = None,
        trigger_type: str = None,
    ):
        self.trigger_name = trigger_name
        self.endpoint = endpoint
        self.actions_count = actions_count
        self.trigger_action_name = trigger_action_name
        self.trigger_description = trigger_description
        self.trigger_action_description = trigger_action_description
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.trigger_name is not None:
            result['TriggerName'] = self.trigger_name
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.actions_count is not None:
            result['ActionsCount'] = self.actions_count
        if self.trigger_action_name is not None:
            result['TriggerActionName'] = self.trigger_action_name
        if self.trigger_description is not None:
            result['TriggerDescription'] = self.trigger_description
        if self.trigger_action_description is not None:
            result['TriggerActionDescription'] = self.trigger_action_description
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ActionsCount') is not None:
            self.actions_count = m.get('ActionsCount')
        if m.get('TriggerActionName') is not None:
            self.trigger_action_name = m.get('TriggerActionName')
        if m.get('TriggerDescription') is not None:
            self.trigger_description = m.get('TriggerDescription')
        if m.get('TriggerActionDescription') is not None:
            self.trigger_action_description = m.get('TriggerActionDescription')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        return self


class ListFlowTriggersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        triggers: List[ListFlowTriggersResponseBodyTriggers] = None,
    ):
        self.request_id = request_id
        self.triggers = triggers

    def validate(self):
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Triggers'] = []
        if self.triggers is not None:
            for k in self.triggers:
                result['Triggers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.triggers = []
        if m.get('Triggers') is not None:
            for k in m.get('Triggers'):
                temp_model = ListFlowTriggersResponseBodyTriggers()
                self.triggers.append(temp_model.from_map(k))
        return self


class ListFlowTriggersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFlowTriggersResponseBody = None,
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
            temp_model = ListFlowTriggersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFlowVersionRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.flow_id = flow_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListFlowVersionResponseBodyVersions(TeaModel):
    def __init__(
        self,
        version: int = None,
        state: int = None,
        version_id: str = None,
        created_at: str = None,
        updated_at: str = None,
        flow_id: str = None,
    ):
        self.version = version
        self.state = state
        self.version_id = version_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.state is not None:
            result['State'] = self.state
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class ListFlowVersionResponseBody(TeaModel):
    def __init__(
        self,
        versions: List[ListFlowVersionResponseBodyVersions] = None,
        total_page: int = None,
        request_id: str = None,
    ):
        self.versions = versions
        self.total_page = total_page
        self.request_id = request_id

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ListFlowVersionResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFlowVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFlowVersionResponseBody = None,
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
            temp_model = ListFlowVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInvocationLogsRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
        flow_version: str = None,
        start_time: str = None,
        end_time: str = None,
        tags: str = None,
    ):
        # 工作流 ID
        self.flow_id = flow_id
        # 页码
        self.page_number = page_number
        # 每页返回数量
        self.page_size = page_size
        # 执行状态
        self.status = status
        # 工作流版本
        self.flow_version = flow_version
        # 执行开始时间
        self.start_time = start_time
        # 结束执行时间
        self.end_time = end_time
        # 标签
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.flow_version is not None:
            result['FlowVersion'] = self.flow_version
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FlowVersion') is not None:
            self.flow_version = m.get('FlowVersion')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListInvocationLogsResponseBodyLogsInvocationError(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        message: str = None,
    ):
        self.error_code = error_code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListInvocationLogsResponseBodyLogsWorkflow(TeaModel):
    def __init__(
        self,
        definition: str = None,
        version: str = None,
        flow_id: str = None,
    ):
        # 工作流定义
        self.definition = definition
        # 工作流版本
        self.version = version
        # 工作流 ID
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.version is not None:
            result['Version'] = self.version
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class ListInvocationLogsResponseBodyLogsTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 标签名
        self.key = key
        # 标签值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
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


class ListInvocationLogsResponseBodyLogs(TeaModel):
    def __init__(
        self,
        status: str = None,
        end_time: str = None,
        start_time: str = None,
        invocation_id: str = None,
        return_code: str = None,
        invocation_error: ListInvocationLogsResponseBodyLogsInvocationError = None,
        workflow: ListInvocationLogsResponseBodyLogsWorkflow = None,
        tags: List[ListInvocationLogsResponseBodyLogsTags] = None,
    ):
        # 执行状态
        self.status = status
        # 执行完成时间
        self.end_time = end_time
        # 开始执行时间
        self.start_time = start_time
        # 执行唯一标识符
        self.invocation_id = invocation_id
        # 返回码
        self.return_code = return_code
        # 错误信息
        self.invocation_error = invocation_error
        # 工作流详情
        self.workflow = workflow
        # 本次执行的标签
        self.tags = tags

    def validate(self):
        if self.invocation_error:
            self.invocation_error.validate()
        if self.workflow:
            self.workflow.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id
        if self.return_code is not None:
            result['ReturnCode'] = self.return_code
        if self.invocation_error is not None:
            result['InvocationError'] = self.invocation_error.to_map()
        if self.workflow is not None:
            result['Workflow'] = self.workflow.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')
        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')
        if m.get('InvocationError') is not None:
            temp_model = ListInvocationLogsResponseBodyLogsInvocationError()
            self.invocation_error = temp_model.from_map(m['InvocationError'])
        if m.get('Workflow') is not None:
            temp_model = ListInvocationLogsResponseBodyLogsWorkflow()
            self.workflow = temp_model.from_map(m['Workflow'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListInvocationLogsResponseBodyLogsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListInvocationLogsResponseBody(TeaModel):
    def __init__(
        self,
        total_page: int = None,
        request_id: str = None,
        logs: List[ListInvocationLogsResponseBodyLogs] = None,
        total_count: int = None,
    ):
        # 总页数
        self.total_page = total_page
        # 请求 ID
        self.request_id = request_id
        # 日志列表
        self.logs = logs
        # 总数
        self.total_count = total_count

    def validate(self):
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = ListInvocationLogsResponseBodyLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInvocationLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInvocationLogsResponseBody = None,
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
            temp_model = ListInvocationLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResponseBodyTags(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        name: str = None,
        id: int = None,
        count: int = None,
    ):
        self.created_at = created_at
        self.name = name
        self.id = id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class ListTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tags: List[ListTagResponseBodyTags] = None,
    ):
        self.request_id = request_id
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResponseBody = None,
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
            temp_model = ListTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
        name: str = None,
        description: str = None,
        definition: str = None,
        flow_role: str = None,
    ):
        self.flow_id = flow_id
        self.name = name
        self.description = description
        self.definition = definition
        self.flow_role = flow_role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        if self.name is not None:
            result['Name'] = self.name
        if self.description is not None:
            result['Description'] = self.description
        if self.definition is not None:
            result['Definition'] = self.definition
        if self.flow_role is not None:
            result['FlowRole'] = self.flow_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        if m.get('FlowRole') is not None:
            self.flow_role = m.get('FlowRole')
        return self


class ModifyFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyFlowResponseBody = None,
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
            temp_model = ModifyFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollBackFlowRequest(TeaModel):
    def __init__(
        self,
        flow_id: str = None,
    ):
        self.flow_id = flow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class RollBackFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RollBackFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RollBackFlowResponseBody = None,
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
            temp_model = RollBackFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConnectionRequest(TeaModel):
    def __init__(
        self,
        connector: str = None,
        connection_name: str = None,
        connection_content: str = None,
        action_type: str = None,
        connection_type: str = None,
    ):
        self.connector = connector
        self.connection_name = connection_name
        self.connection_content = connection_content
        self.action_type = action_type
        self.connection_type = connection_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.connector is not None:
            result['Connector'] = self.connector
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.connection_content is not None:
            result['ConnectionContent'] = self.connection_content
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Connector') is not None:
            self.connector = m.get('Connector')
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('ConnectionContent') is not None:
            self.connection_content = m.get('ConnectionContent')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')
        return self


class UpdateConnectionResponseBody(TeaModel):
    def __init__(
        self,
        connection_name: str = None,
        connection_id: str = None,
        request_id: str = None,
        content: str = None,
        definition: str = None,
    ):
        self.connection_name = connection_name
        self.connection_id = connection_id
        self.request_id = request_id
        self.content = content
        self.definition = definition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content
        if self.definition is not None:
            result['Definition'] = self.definition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')
        return self


class UpdateConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateConnectionResponseBody = None,
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
            temp_model = UpdateConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


