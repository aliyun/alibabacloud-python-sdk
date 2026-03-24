# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListAlertActionsResponseBody(DaraModel):
    def __init__(
        self,
        alert_actions: List[main_models.ListAlertActionsResponseBodyAlertActions] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The list of alert action integration configurations.
        self.alert_actions = alert_actions
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.alert_actions:
            for v1 in self.alert_actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['alertActions'] = []
        if self.alert_actions is not None:
            for k1 in self.alert_actions:
                result['alertActions'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_actions = []
        if m.get('alertActions') is not None:
            for k1 in m.get('alertActions'):
                temp_model = main_models.ListAlertActionsResponseBodyAlertActions()
                self.alert_actions.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAlertActionsResponseBodyAlertActions(DaraModel):
    def __init__(
        self,
        alert_action_id: str = None,
        alert_action_name: str = None,
        eb_param: main_models.ListAlertActionsResponseBodyAlertActionsEbParam = None,
        ess_param: main_models.ListAlertActionsResponseBodyAlertActionsEssParam = None,
        fc_3param: main_models.ListAlertActionsResponseBodyAlertActionsFc3Param = None,
        fc_param: main_models.ListAlertActionsResponseBodyAlertActionsFcParam = None,
        mns_param: main_models.ListAlertActionsResponseBodyAlertActionsMnsParam = None,
        pager_duty_param: main_models.ListAlertActionsResponseBodyAlertActionsPagerDutyParam = None,
        sls_param: main_models.ListAlertActionsResponseBodyAlertActionsSlsParam = None,
        type: str = None,
        webhook_param: main_models.ListAlertActionsResponseBodyAlertActionsWebhookParam = None,
    ):
        # The unique ID of the alert action integration.
        self.alert_action_id = alert_action_id
        # The name of the alert action integration.
        self.alert_action_name = alert_action_name
        # Specifies the event bus.
        self.eb_param = eb_param
        # The parameters of Auto Scaling.
        self.ess_param = ess_param
        # The parameters of Function Compute 3.0.
        self.fc_3param = fc_3param
        # The parameters of Function Compute.
        self.fc_param = fc_param
        # The parameters of Simple Message Queue (formerly MNS).
        self.mns_param = mns_param
        # The PagerDuty parameters.
        self.pager_duty_param = pager_duty_param
        # The parameters of Simple Log Service.
        self.sls_param = sls_param
        # The type of the alert action integration.
        self.type = type
        # The webhook parameters.
        self.webhook_param = webhook_param

    def validate(self):
        if self.eb_param:
            self.eb_param.validate()
        if self.ess_param:
            self.ess_param.validate()
        if self.fc_3param:
            self.fc_3param.validate()
        if self.fc_param:
            self.fc_param.validate()
        if self.mns_param:
            self.mns_param.validate()
        if self.pager_duty_param:
            self.pager_duty_param.validate()
        if self.sls_param:
            self.sls_param.validate()
        if self.webhook_param:
            self.webhook_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_action_id is not None:
            result['alertActionId'] = self.alert_action_id

        if self.alert_action_name is not None:
            result['alertActionName'] = self.alert_action_name

        if self.eb_param is not None:
            result['ebParam'] = self.eb_param.to_map()

        if self.ess_param is not None:
            result['essParam'] = self.ess_param.to_map()

        if self.fc_3param is not None:
            result['fc3Param'] = self.fc_3param.to_map()

        if self.fc_param is not None:
            result['fcParam'] = self.fc_param.to_map()

        if self.mns_param is not None:
            result['mnsParam'] = self.mns_param.to_map()

        if self.pager_duty_param is not None:
            result['pagerDutyParam'] = self.pager_duty_param.to_map()

        if self.sls_param is not None:
            result['slsParam'] = self.sls_param.to_map()

        if self.type is not None:
            result['type'] = self.type

        if self.webhook_param is not None:
            result['webhookParam'] = self.webhook_param.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertActionId') is not None:
            self.alert_action_id = m.get('alertActionId')

        if m.get('alertActionName') is not None:
            self.alert_action_name = m.get('alertActionName')

        if m.get('ebParam') is not None:
            temp_model = main_models.ListAlertActionsResponseBodyAlertActionsEbParam()
            self.eb_param = temp_model.from_map(m.get('ebParam'))

        if m.get('essParam') is not None:
            temp_model = main_models.ListAlertActionsResponseBodyAlertActionsEssParam()
            self.ess_param = temp_model.from_map(m.get('essParam'))

        if m.get('fc3Param') is not None:
            temp_model = main_models.ListAlertActionsResponseBodyAlertActionsFc3Param()
            self.fc_3param = temp_model.from_map(m.get('fc3Param'))

        if m.get('fcParam') is not None:
            temp_model = main_models.ListAlertActionsResponseBodyAlertActionsFcParam()
            self.fc_param = temp_model.from_map(m.get('fcParam'))

        if m.get('mnsParam') is not None:
            temp_model = main_models.ListAlertActionsResponseBodyAlertActionsMnsParam()
            self.mns_param = temp_model.from_map(m.get('mnsParam'))

        if m.get('pagerDutyParam') is not None:
            temp_model = main_models.ListAlertActionsResponseBodyAlertActionsPagerDutyParam()
            self.pager_duty_param = temp_model.from_map(m.get('pagerDutyParam'))

        if m.get('slsParam') is not None:
            temp_model = main_models.ListAlertActionsResponseBodyAlertActionsSlsParam()
            self.sls_param = temp_model.from_map(m.get('slsParam'))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('webhookParam') is not None:
            temp_model = main_models.ListAlertActionsResponseBodyAlertActionsWebhookParam()
            self.webhook_param = temp_model.from_map(m.get('webhookParam'))

        return self

class ListAlertActionsResponseBodyAlertActionsWebhookParam(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        headers: Dict[str, str] = None,
        method: str = None,
        url: str = None,
    ):
        # The data format. This parameter is valid only when the request method is POST.
        self.content_type = content_type
        # The request headers.
        self.headers = headers
        # The request method of the webhook.
        self.method = method
        # The callback URL for alerts.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.headers is not None:
            result['headers'] = self.headers

        if self.method is not None:
            result['method'] = self.method

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListAlertActionsResponseBodyAlertActionsSlsParam(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        region_id: str = None,
    ):
        # The name of the Simple Log Service Logstore.
        self.logstore = logstore
        # The name of the Simple Log Service project.
        self.project = project
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.project is not None:
            result['project'] = self.project

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class ListAlertActionsResponseBodyAlertActionsPagerDutyParam(DaraModel):
    def __init__(
        self,
        key: str = None,
        url: str = None,
    ):
        # The integration key of PagerDuty.
        self.key = key
        # The integration webhook of PagerDuty. Versions 1 and 2 are supported.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListAlertActionsResponseBodyAlertActionsMnsParam(DaraModel):
    def __init__(
        self,
        mns_type: str = None,
        name: str = None,
        region_id: str = None,
    ):
        # The resource type of Simple Message Queue (formerly MNS).
        self.mns_type = mns_type
        # The name of the resource.
        # 
        # - If the resource type is \\`queue\\`, this parameter specifies the queue name.
        # 
        # - If the resource type is \\`topic\\`, this parameter specifies the topic name.
        self.name = name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mns_type is not None:
            result['mnsType'] = self.mns_type

        if self.name is not None:
            result['name'] = self.name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mnsType') is not None:
            self.mns_type = m.get('mnsType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class ListAlertActionsResponseBodyAlertActionsFcParam(DaraModel):
    def __init__(
        self,
        function: str = None,
        region_id: str = None,
        service: str = None,
    ):
        # The function name of the Function Compute service.
        self.function = function
        # The region ID.
        self.region_id = region_id
        # The service name of Function Compute.
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['function'] = self.function

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.service is not None:
            result['service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('function') is not None:
            self.function = m.get('function')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('service') is not None:
            self.service = m.get('service')

        return self

class ListAlertActionsResponseBodyAlertActionsFc3Param(DaraModel):
    def __init__(
        self,
        function: str = None,
        qualifier: str = None,
        region_id: str = None,
    ):
        # The function name of the Function Compute service.
        self.function = function
        # The version or alias of the function.
        self.qualifier = qualifier
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['function'] = self.function

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('function') is not None:
            self.function = m.get('function')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class ListAlertActionsResponseBodyAlertActionsEssParam(DaraModel):
    def __init__(
        self,
        ess_group_id: str = None,
        ess_rule_id: str = None,
        region_id: str = None,
    ):
        # The ID of the Auto Scaling group.
        self.ess_group_id = ess_group_id
        # The ID of the scaling rule.
        self.ess_rule_id = ess_rule_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ess_group_id is not None:
            result['essGroupId'] = self.ess_group_id

        if self.ess_rule_id is not None:
            result['essRuleId'] = self.ess_rule_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('essGroupId') is not None:
            self.ess_group_id = m.get('essGroupId')

        if m.get('essRuleId') is not None:
            self.ess_rule_id = m.get('essRuleId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class ListAlertActionsResponseBodyAlertActionsEbParam(DaraModel):
    def __init__(
        self,
        eb_source: str = None,
        event_bus_name: str = None,
        region_id: str = None,
        subject: str = None,
    ):
        # The event provider.
        self.eb_source = eb_source
        # The name of the event bus.
        self.event_bus_name = event_bus_name
        # The region ID.
        self.region_id = region_id
        # The subject.
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eb_source is not None:
            result['ebSource'] = self.eb_source

        if self.event_bus_name is not None:
            result['eventBusName'] = self.event_bus_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.subject is not None:
            result['subject'] = self.subject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ebSource') is not None:
            self.eb_source = m.get('ebSource')

        if m.get('eventBusName') is not None:
            self.event_bus_name = m.get('eventBusName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('subject') is not None:
            self.subject = m.get('subject')

        return self

