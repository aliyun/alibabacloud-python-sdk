# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateAlertActionRequest(DaraModel):
    def __init__(
        self,
        alert_action_id: str = None,
        alert_action_name: str = None,
        eb_param: main_models.CreateAlertActionRequestEbParam = None,
        ess_param: main_models.CreateAlertActionRequestEssParam = None,
        fc_3param: main_models.CreateAlertActionRequestFc3Param = None,
        fc_param: main_models.CreateAlertActionRequestFcParam = None,
        mns_param: main_models.CreateAlertActionRequestMnsParam = None,
        pager_duty_param: main_models.CreateAlertActionRequestPagerDutyParam = None,
        sls_param: main_models.CreateAlertActionRequestSlsParam = None,
        type: str = None,
        webhook_param: main_models.CreateAlertActionRequestWebhookParam = None,
    ):
        self.alert_action_id = alert_action_id
        # This parameter is required.
        self.alert_action_name = alert_action_name
        self.eb_param = eb_param
        self.ess_param = ess_param
        self.fc_3param = fc_3param
        self.fc_param = fc_param
        self.mns_param = mns_param
        self.pager_duty_param = pager_duty_param
        self.sls_param = sls_param
        # This parameter is required.
        self.type = type
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
            temp_model = main_models.CreateAlertActionRequestEbParam()
            self.eb_param = temp_model.from_map(m.get('ebParam'))

        if m.get('essParam') is not None:
            temp_model = main_models.CreateAlertActionRequestEssParam()
            self.ess_param = temp_model.from_map(m.get('essParam'))

        if m.get('fc3Param') is not None:
            temp_model = main_models.CreateAlertActionRequestFc3Param()
            self.fc_3param = temp_model.from_map(m.get('fc3Param'))

        if m.get('fcParam') is not None:
            temp_model = main_models.CreateAlertActionRequestFcParam()
            self.fc_param = temp_model.from_map(m.get('fcParam'))

        if m.get('mnsParam') is not None:
            temp_model = main_models.CreateAlertActionRequestMnsParam()
            self.mns_param = temp_model.from_map(m.get('mnsParam'))

        if m.get('pagerDutyParam') is not None:
            temp_model = main_models.CreateAlertActionRequestPagerDutyParam()
            self.pager_duty_param = temp_model.from_map(m.get('pagerDutyParam'))

        if m.get('slsParam') is not None:
            temp_model = main_models.CreateAlertActionRequestSlsParam()
            self.sls_param = temp_model.from_map(m.get('slsParam'))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('webhookParam') is not None:
            temp_model = main_models.CreateAlertActionRequestWebhookParam()
            self.webhook_param = temp_model.from_map(m.get('webhookParam'))

        return self

class CreateAlertActionRequestWebhookParam(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        headers: Dict[str, str] = None,
        method: str = None,
        url: str = None,
    ):
        self.content_type = content_type
        self.headers = headers
        self.method = method
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

class CreateAlertActionRequestSlsParam(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        region_id: str = None,
    ):
        self.logstore = logstore
        self.project = project
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

class CreateAlertActionRequestPagerDutyParam(DaraModel):
    def __init__(
        self,
        key: str = None,
        url: str = None,
    ):
        self.key = key
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

class CreateAlertActionRequestMnsParam(DaraModel):
    def __init__(
        self,
        mns_type: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.mns_type = mns_type
        self.name = name
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

class CreateAlertActionRequestFcParam(DaraModel):
    def __init__(
        self,
        function: str = None,
        region_id: str = None,
        service: str = None,
    ):
        self.function = function
        self.region_id = region_id
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

class CreateAlertActionRequestFc3Param(DaraModel):
    def __init__(
        self,
        function: str = None,
        qualifier: str = None,
        region_id: str = None,
    ):
        self.function = function
        self.qualifier = qualifier
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

class CreateAlertActionRequestEssParam(DaraModel):
    def __init__(
        self,
        ess_group_id: str = None,
        ess_rule_id: str = None,
        region_id: str = None,
    ):
        self.ess_group_id = ess_group_id
        self.ess_rule_id = ess_rule_id
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

class CreateAlertActionRequestEbParam(DaraModel):
    def __init__(
        self,
        eb_source: str = None,
        event_bus_name: str = None,
        region_id: str = None,
        subject: str = None,
    ):
        self.eb_source = eb_source
        self.event_bus_name = event_bus_name
        self.region_id = region_id
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

