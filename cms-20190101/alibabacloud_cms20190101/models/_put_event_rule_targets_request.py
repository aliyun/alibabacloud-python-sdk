# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class PutEventRuleTargetsRequest(DaraModel):
    def __init__(
        self,
        contact_parameters: List[main_models.PutEventRuleTargetsRequestContactParameters] = None,
        fc_parameters: List[main_models.PutEventRuleTargetsRequestFcParameters] = None,
        mns_parameters: List[main_models.PutEventRuleTargetsRequestMnsParameters] = None,
        open_api_parameters: List[main_models.PutEventRuleTargetsRequestOpenApiParameters] = None,
        region_id: str = None,
        rule_name: str = None,
        sls_parameters: List[main_models.PutEventRuleTargetsRequestSlsParameters] = None,
        webhook_parameters: List[main_models.PutEventRuleTargetsRequestWebhookParameters] = None,
    ):
        # The information about the alert contact groups that receive alert notifications.
        self.contact_parameters = contact_parameters
        # The information about the recipients in Function Compute.
        self.fc_parameters = fc_parameters
        # The notifications of Simple Message Queue (formerly MNS) (SMQ).
        self.mns_parameters = mns_parameters
        # The parameters of API callback notification.
        self.open_api_parameters = open_api_parameters
        self.region_id = region_id
        # The name of the alert rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The information about the recipients in Simple Log Service.
        self.sls_parameters = sls_parameters
        # The information about the callback URLs that are used to receive alert notifications.
        self.webhook_parameters = webhook_parameters

    def validate(self):
        if self.contact_parameters:
            for v1 in self.contact_parameters:
                 if v1:
                    v1.validate()
        if self.fc_parameters:
            for v1 in self.fc_parameters:
                 if v1:
                    v1.validate()
        if self.mns_parameters:
            for v1 in self.mns_parameters:
                 if v1:
                    v1.validate()
        if self.open_api_parameters:
            for v1 in self.open_api_parameters:
                 if v1:
                    v1.validate()
        if self.sls_parameters:
            for v1 in self.sls_parameters:
                 if v1:
                    v1.validate()
        if self.webhook_parameters:
            for v1 in self.webhook_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContactParameters'] = []
        if self.contact_parameters is not None:
            for k1 in self.contact_parameters:
                result['ContactParameters'].append(k1.to_map() if k1 else None)

        result['FcParameters'] = []
        if self.fc_parameters is not None:
            for k1 in self.fc_parameters:
                result['FcParameters'].append(k1.to_map() if k1 else None)

        result['MnsParameters'] = []
        if self.mns_parameters is not None:
            for k1 in self.mns_parameters:
                result['MnsParameters'].append(k1.to_map() if k1 else None)

        result['OpenApiParameters'] = []
        if self.open_api_parameters is not None:
            for k1 in self.open_api_parameters:
                result['OpenApiParameters'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        result['SlsParameters'] = []
        if self.sls_parameters is not None:
            for k1 in self.sls_parameters:
                result['SlsParameters'].append(k1.to_map() if k1 else None)

        result['WebhookParameters'] = []
        if self.webhook_parameters is not None:
            for k1 in self.webhook_parameters:
                result['WebhookParameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_parameters = []
        if m.get('ContactParameters') is not None:
            for k1 in m.get('ContactParameters'):
                temp_model = main_models.PutEventRuleTargetsRequestContactParameters()
                self.contact_parameters.append(temp_model.from_map(k1))

        self.fc_parameters = []
        if m.get('FcParameters') is not None:
            for k1 in m.get('FcParameters'):
                temp_model = main_models.PutEventRuleTargetsRequestFcParameters()
                self.fc_parameters.append(temp_model.from_map(k1))

        self.mns_parameters = []
        if m.get('MnsParameters') is not None:
            for k1 in m.get('MnsParameters'):
                temp_model = main_models.PutEventRuleTargetsRequestMnsParameters()
                self.mns_parameters.append(temp_model.from_map(k1))

        self.open_api_parameters = []
        if m.get('OpenApiParameters') is not None:
            for k1 in m.get('OpenApiParameters'):
                temp_model = main_models.PutEventRuleTargetsRequestOpenApiParameters()
                self.open_api_parameters.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        self.sls_parameters = []
        if m.get('SlsParameters') is not None:
            for k1 in m.get('SlsParameters'):
                temp_model = main_models.PutEventRuleTargetsRequestSlsParameters()
                self.sls_parameters.append(temp_model.from_map(k1))

        self.webhook_parameters = []
        if m.get('WebhookParameters') is not None:
            for k1 in m.get('WebhookParameters'):
                temp_model = main_models.PutEventRuleTargetsRequestWebhookParameters()
                self.webhook_parameters.append(temp_model.from_map(k1))

        return self

class PutEventRuleTargetsRequestWebhookParameters(DaraModel):
    def __init__(
        self,
        id: str = None,
        method: str = None,
        protocol: str = None,
        url: str = None,
    ):
        # The ID of the recipient that receives alert notifications. Valid values of N: 1 to 5.
        self.id = id
        # The HTTP request method. Valid values of N: 1 to 5.
        # 
        # Valid values: GET and POST.
        self.method = method
        # The name of the protocol. Valid values of N: 1 to 5. Valid values:
        # 
        # *   http
        # *   telnet
        # *   ping
        self.protocol = protocol
        # The callback URL. Valid values of N: 1 to 5.
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

class PutEventRuleTargetsRequestSlsParameters(DaraModel):
    def __init__(
        self,
        id: str = None,
        log_store: str = None,
        project: str = None,
        region: str = None,
    ):
        # The ID of the recipient that receives alert notifications. Valid values of N: 1 to 5.
        self.id = id
        # The name of the Simple Log Service Logstore. Valid values of N: 1 to 5.
        self.log_store = log_store
        # The name of the Simple Log Service project. Valid values of N: 1 to 5.
        self.project = project
        # The region where Simple Log Service is deployed. Valid values of N: 1 to 5.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

class PutEventRuleTargetsRequestOpenApiParameters(DaraModel):
    def __init__(
        self,
        action: str = None,
        arn: str = None,
        id: str = None,
        json_params: str = None,
        product: str = None,
        region: str = None,
        role: str = None,
        version: str = None,
    ):
        # The API name.
        self.action = action
        # The Alibaba Cloud Resource Name (ARN) of the resource. Valid values of N: 1 to 5. Format: `arn:acs:${Service}:${Region}:${Account}:${ResourceType}/${ResourceId}`. Fields:
        # 
        # *   Service: the code of a cloud service
        # *   Region: the region ID
        # *   Account: the ID of an Alibaba Cloud account
        # *   ResourceType: the resource type
        # *   ResourceId: the resource ID
        self.arn = arn
        # The ID of the recipient that receives alert notifications sent by an API callback.
        self.id = id
        # The parameters of the alert callback. Specify the parameters in the JSON format.
        self.json_params = json_params
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

        if self.json_params is not None:
            result['JsonParams'] = self.json_params

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

        if m.get('JsonParams') is not None:
            self.json_params = m.get('JsonParams')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class PutEventRuleTargetsRequestMnsParameters(DaraModel):
    def __init__(
        self,
        id: str = None,
        queue: str = None,
        region: str = None,
        topic: str = None,
    ):
        # The ID of the recipient that receives alert notifications. Valid values of N: 1 to 5.
        self.id = id
        # The name of the SMQ queue. Valid values of N: 1 to 5.
        self.queue = queue
        # The region for SMQ. Valid values of N: 1 to 5.
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
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Queue') is not None:
            self.queue = m.get('Queue')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class PutEventRuleTargetsRequestFcParameters(DaraModel):
    def __init__(
        self,
        function_name: str = None,
        id: str = None,
        region: str = None,
        service_name: str = None,
    ):
        # The name of the function. Valid values of N: 1 to 5.
        self.function_name = function_name
        # The ID of the recipient that receives alert notifications. Valid values of N: 1 to 5.
        self.id = id
        # The region where Function Compute is deployed. Valid values of N: 1 to 5.
        self.region = region
        # The name of the Function Compute service. Valid values of N: 1 to 5.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

class PutEventRuleTargetsRequestContactParameters(DaraModel):
    def __init__(
        self,
        contact_group_name: str = None,
        id: str = None,
        level: str = None,
    ):
        # The name of the alert contact group. Valid values of N: 1 to 5.
        self.contact_group_name = contact_group_name
        # The ID of the recipient that receives alert notifications. Valid values of N: 1 to 5.
        self.id = id
        # The alert notification methods. Valid values of N: 1 to 5. Valid values:
        # 
        # 4: Alert notifications are sent by using DingTalk and emails.
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

