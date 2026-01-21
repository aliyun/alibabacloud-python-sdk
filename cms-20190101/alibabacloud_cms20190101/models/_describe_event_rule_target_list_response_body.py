# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeEventRuleTargetListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        contact_parameters: main_models.DescribeEventRuleTargetListResponseBodyContactParameters = None,
        fc_parameters: main_models.DescribeEventRuleTargetListResponseBodyFcParameters = None,
        message: str = None,
        mns_parameters: main_models.DescribeEventRuleTargetListResponseBodyMnsParameters = None,
        open_api_parameters: main_models.DescribeEventRuleTargetListResponseBodyOpenApiParameters = None,
        request_id: str = None,
        sls_parameters: main_models.DescribeEventRuleTargetListResponseBodySlsParameters = None,
        webhook_parameters: main_models.DescribeEventRuleTargetListResponseBodyWebhookParameters = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the call was successful.
        self.code = code
        # The information about the recipients if alert notifications are sent to the alert contacts of an alert contact group.
        self.contact_parameters = contact_parameters
        # The information about the recipients in Function Compute.
        self.fc_parameters = fc_parameters
        # The error message.
        self.message = message
        # The notifications of Simple Message Queue (formerly MNS) (SMQ).
        self.mns_parameters = mns_parameters
        # The information about the recipients in OpenAPI Explorer.
        self.open_api_parameters = open_api_parameters
        # The ID of the request.
        self.request_id = request_id
        # The information about the recipients in Log Service.
        self.sls_parameters = sls_parameters
        # The information about the recipients if alert notifications are sent by sending a request to a callback URL.
        self.webhook_parameters = webhook_parameters

    def validate(self):
        if self.contact_parameters:
            self.contact_parameters.validate()
        if self.fc_parameters:
            self.fc_parameters.validate()
        if self.mns_parameters:
            self.mns_parameters.validate()
        if self.open_api_parameters:
            self.open_api_parameters.validate()
        if self.sls_parameters:
            self.sls_parameters.validate()
        if self.webhook_parameters:
            self.webhook_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.contact_parameters is not None:
            result['ContactParameters'] = self.contact_parameters.to_map()

        if self.fc_parameters is not None:
            result['FcParameters'] = self.fc_parameters.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.mns_parameters is not None:
            result['MnsParameters'] = self.mns_parameters.to_map()

        if self.open_api_parameters is not None:
            result['OpenApiParameters'] = self.open_api_parameters.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sls_parameters is not None:
            result['SlsParameters'] = self.sls_parameters.to_map()

        if self.webhook_parameters is not None:
            result['WebhookParameters'] = self.webhook_parameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ContactParameters') is not None:
            temp_model = main_models.DescribeEventRuleTargetListResponseBodyContactParameters()
            self.contact_parameters = temp_model.from_map(m.get('ContactParameters'))

        if m.get('FcParameters') is not None:
            temp_model = main_models.DescribeEventRuleTargetListResponseBodyFcParameters()
            self.fc_parameters = temp_model.from_map(m.get('FcParameters'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MnsParameters') is not None:
            temp_model = main_models.DescribeEventRuleTargetListResponseBodyMnsParameters()
            self.mns_parameters = temp_model.from_map(m.get('MnsParameters'))

        if m.get('OpenApiParameters') is not None:
            temp_model = main_models.DescribeEventRuleTargetListResponseBodyOpenApiParameters()
            self.open_api_parameters = temp_model.from_map(m.get('OpenApiParameters'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlsParameters') is not None:
            temp_model = main_models.DescribeEventRuleTargetListResponseBodySlsParameters()
            self.sls_parameters = temp_model.from_map(m.get('SlsParameters'))

        if m.get('WebhookParameters') is not None:
            temp_model = main_models.DescribeEventRuleTargetListResponseBodyWebhookParameters()
            self.webhook_parameters = temp_model.from_map(m.get('WebhookParameters'))

        return self

class DescribeEventRuleTargetListResponseBodyWebhookParameters(DaraModel):
    def __init__(
        self,
        webhook_parameter: List[main_models.DescribeEventRuleTargetListResponseBodyWebhookParametersWebhookParameter] = None,
    ):
        self.webhook_parameter = webhook_parameter

    def validate(self):
        if self.webhook_parameter:
            for v1 in self.webhook_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WebhookParameter'] = []
        if self.webhook_parameter is not None:
            for k1 in self.webhook_parameter:
                result['WebhookParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.webhook_parameter = []
        if m.get('WebhookParameter') is not None:
            for k1 in m.get('WebhookParameter'):
                temp_model = main_models.DescribeEventRuleTargetListResponseBodyWebhookParametersWebhookParameter()
                self.webhook_parameter.append(temp_model.from_map(k1))

        return self

class DescribeEventRuleTargetListResponseBodyWebhookParametersWebhookParameter(DaraModel):
    def __init__(
        self,
        id: str = None,
        method: str = None,
        protocol: str = None,
        url: str = None,
    ):
        # The ID of the recipient.
        self.id = id
        # The HTTP request method. Valid values: GET and POST.
        self.method = method
        # The protocol type.
        self.protocol = protocol
        # The callback URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.method is not None:
            result['Method'] = self.method

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class DescribeEventRuleTargetListResponseBodySlsParameters(DaraModel):
    def __init__(
        self,
        sls_parameter: List[main_models.DescribeEventRuleTargetListResponseBodySlsParametersSlsParameter] = None,
    ):
        self.sls_parameter = sls_parameter

    def validate(self):
        if self.sls_parameter:
            for v1 in self.sls_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SlsParameter'] = []
        if self.sls_parameter is not None:
            for k1 in self.sls_parameter:
                result['SlsParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sls_parameter = []
        if m.get('SlsParameter') is not None:
            for k1 in m.get('SlsParameter'):
                temp_model = main_models.DescribeEventRuleTargetListResponseBodySlsParametersSlsParameter()
                self.sls_parameter.append(temp_model.from_map(k1))

        return self

class DescribeEventRuleTargetListResponseBodySlsParametersSlsParameter(DaraModel):
    def __init__(
        self,
        arn: str = None,
        id: str = None,
        log_store: str = None,
        project: str = None,
        region: str = None,
    ):
        # The ARN of the Log Service Logstore. 
        # 
        # Format: `arn:acs:${Service}:${Region}:${Account}:${ResourceType}/${ResourceId}`. Fields: 
        # 
        # - Service: the code of an Alibaba Cloud service
        # - Region: the region ID
        # - Account: the ID of an Alibaba Cloud account
        # - ResourceType: the resource type
        # - ResourceId: the resource ID
        self.arn = arn
        # The ID of the recipient.
        self.id = id
        # The name of the Logstore.
        self.log_store = log_store
        # The name of the project.
        self.project = project
        # The ID of the region where the Log Service project resides.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.id is not None:
            result['Id'] = self.id

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.project is not None:
            result['Project'] = self.project

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class DescribeEventRuleTargetListResponseBodyOpenApiParameters(DaraModel):
    def __init__(
        self,
        open_api_parameters: List[main_models.DescribeEventRuleTargetListResponseBodyOpenApiParametersOpenApiParameters] = None,
    ):
        self.open_api_parameters = open_api_parameters

    def validate(self):
        if self.open_api_parameters:
            for v1 in self.open_api_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OpenApiParameters'] = []
        if self.open_api_parameters is not None:
            for k1 in self.open_api_parameters:
                result['OpenApiParameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.open_api_parameters = []
        if m.get('OpenApiParameters') is not None:
            for k1 in m.get('OpenApiParameters'):
                temp_model = main_models.DescribeEventRuleTargetListResponseBodyOpenApiParametersOpenApiParameters()
                self.open_api_parameters.append(temp_model.from_map(k1))

        return self

class DescribeEventRuleTargetListResponseBodyOpenApiParametersOpenApiParameters(DaraModel):
    def __init__(
        self,
        action: str = None,
        arn: str = None,
        id: str = None,
        product: str = None,
        region: str = None,
        role: str = None,
        version: str = None,
    ):
        # The name of the API operation.
        self.action = action
        # The ARN of the API operation. 
        # 
        # Format: `arn:acs:${Service}:${Region}:${Account}:${ResourceType}/${ResourceId}`. Fields: 
        # 
        # - Service: the code of an Alibaba Cloud service
        # - Region: the region ID
        # - Account: the ID of an Alibaba Cloud account
        # - ResourceType: the resource type
        # - ResourceId: the resource ID The ARN of the Log Service Logstore. 
        # 
        # Format: `arn:acs:${Service}:${Region}:${Account}:${ResourceType}/${ResourceId}`. Fields:
        # - Service: the code of an Alibaba Cloud service
        # - Region: the region ID
        # - Account: the ID of an Alibaba Cloud account
        # - ResourceType: the resource type
        # - ResourceId: the resource ID
        self.arn = arn
        # The ID of the recipient.
        self.id = id
        # The ID of the cloud service to which the API operation belongs.
        self.product = product
        # The region where the resource resides.
        self.region = region
        # The name of the role.
        self.role = role
        # The version of the API.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.arn is not None:
            result['Arn'] = self.arn

        if self.id is not None:
            result['Id'] = self.id

        if self.product is not None:
            result['Product'] = self.product

        if self.region is not None:
            result['Region'] = self.region

        if self.role is not None:
            result['Role'] = self.role

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeEventRuleTargetListResponseBodyMnsParameters(DaraModel):
    def __init__(
        self,
        mns_parameter: List[main_models.DescribeEventRuleTargetListResponseBodyMnsParametersMnsParameter] = None,
    ):
        self.mns_parameter = mns_parameter

    def validate(self):
        if self.mns_parameter:
            for v1 in self.mns_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MnsParameter'] = []
        if self.mns_parameter is not None:
            for k1 in self.mns_parameter:
                result['MnsParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mns_parameter = []
        if m.get('MnsParameter') is not None:
            for k1 in m.get('MnsParameter'):
                temp_model = main_models.DescribeEventRuleTargetListResponseBodyMnsParametersMnsParameter()
                self.mns_parameter.append(temp_model.from_map(k1))

        return self

class DescribeEventRuleTargetListResponseBodyMnsParametersMnsParameter(DaraModel):
    def __init__(
        self,
        arn: str = None,
        id: str = None,
        queue: str = None,
        region: str = None,
        topic: str = None,
    ):
        # The ARN of the MNS queue. 
        # 
        # Format: `arn:acs:${Service}:${Region}:${Account}:${ResourceType}/${ResourceId}`. Fields: 
        # 
        # - Service: the code of an Alibaba Cloud service
        # - Region: the region ID
        # - Account: the ID of an Alibaba Cloud account
        # - ResourceType: the resource type
        # - ResourceId: the resource ID
        self.arn = arn
        # The ID of the recipient.
        self.id = id
        # The name of the SMQ queue.
        self.queue = queue
        # The region for SMQ.
        self.region = region
        # The SMQ topic.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.id is not None:
            result['Id'] = self.id

        if self.queue is not None:
            result['Queue'] = self.queue

        if self.region is not None:
            result['Region'] = self.region

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Queue') is not None:
            self.queue = m.get('Queue')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class DescribeEventRuleTargetListResponseBodyFcParameters(DaraModel):
    def __init__(
        self,
        fcparameter: List[main_models.DescribeEventRuleTargetListResponseBodyFcParametersFCParameter] = None,
    ):
        self.fcparameter = fcparameter

    def validate(self):
        if self.fcparameter:
            for v1 in self.fcparameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FCParameter'] = []
        if self.fcparameter is not None:
            for k1 in self.fcparameter:
                result['FCParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fcparameter = []
        if m.get('FCParameter') is not None:
            for k1 in m.get('FCParameter'):
                temp_model = main_models.DescribeEventRuleTargetListResponseBodyFcParametersFCParameter()
                self.fcparameter.append(temp_model.from_map(k1))

        return self

class DescribeEventRuleTargetListResponseBodyFcParametersFCParameter(DaraModel):
    def __init__(
        self,
        arn: str = None,
        function_name: str = None,
        id: str = None,
        region: str = None,
        service_name: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the function. 
        # 
        # Format: `arn:acs:${Service}:${Region}:${Account}:${ResourceType}/${ResourceId}`. Fields: 
        # 
        # - Service: the code of an Alibaba Cloud service
        # - Region: the region ID
        # - Account: the ID of an Alibaba Cloud account
        # - ResourceType: the resource type
        # - ResourceId: the resource ID
        self.arn = arn
        # The name of the function.
        self.function_name = function_name
        # The ID of the recipient.
        self.id = id
        # The region where Function Compute is deployed.
        self.region = region
        # The name of the Function Compute service.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.id is not None:
            result['Id'] = self.id

        if self.region is not None:
            result['Region'] = self.region

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

class DescribeEventRuleTargetListResponseBodyContactParameters(DaraModel):
    def __init__(
        self,
        contact_parameter: List[main_models.DescribeEventRuleTargetListResponseBodyContactParametersContactParameter] = None,
    ):
        self.contact_parameter = contact_parameter

    def validate(self):
        if self.contact_parameter:
            for v1 in self.contact_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContactParameter'] = []
        if self.contact_parameter is not None:
            for k1 in self.contact_parameter:
                result['ContactParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_parameter = []
        if m.get('ContactParameter') is not None:
            for k1 in m.get('ContactParameter'):
                temp_model = main_models.DescribeEventRuleTargetListResponseBodyContactParametersContactParameter()
                self.contact_parameter.append(temp_model.from_map(k1))

        return self

class DescribeEventRuleTargetListResponseBodyContactParametersContactParameter(DaraModel):
    def __init__(
        self,
        contact_group_name: str = None,
        id: str = None,
        level: str = None,
    ):
        # The name of the alert group.
        self.contact_group_name = contact_group_name
        # The ID of the recipient.
        self.id = id
        # The alert notification methods. Valid values:
        # 
        # 4: Alert notifications are sent by using DingTalk chatbots and emails.
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name

        if self.id is not None:
            result['Id'] = self.id

        if self.level is not None:
            result['Level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        return self

