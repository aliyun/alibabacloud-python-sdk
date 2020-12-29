# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AddGrafanaRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        cluster_id: str = None,
        integration: str = None,
    ):
        self.region_id = region_id
        self.cluster_id = cluster_id
        self.integration = integration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.integration is not None:
            result['Integration'] = self.integration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Integration') is not None:
            self.integration = m.get('Integration')
        return self


class AddGrafanaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class AddGrafanaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddGrafanaResponseBody = None,
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
            temp_model = AddGrafanaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddIntegrationRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        cluster_id: str = None,
        integration: str = None,
    ):
        self.region_id = region_id
        self.cluster_id = cluster_id
        self.integration = integration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.integration is not None:
            result['Integration'] = self.integration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Integration') is not None:
            self.integration = m.get('Integration')
        return self


class AddIntegrationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class AddIntegrationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddIntegrationResponseBody = None,
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
            temp_model = AddIntegrationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyScenarioRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        scenario: str = None,
        name: str = None,
        app_id: str = None,
        sign: str = None,
        config: Dict[str, Any] = None,
        sn_transfer: bool = None,
        sn_stat: bool = None,
        sn_dump: bool = None,
        sn_force: bool = None,
        update_option: bool = None,
    ):
        self.region_id = region_id
        self.scenario = scenario
        self.name = name
        self.app_id = app_id
        self.sign = sign
        self.config = config
        self.sn_transfer = sn_transfer
        self.sn_stat = sn_stat
        self.sn_dump = sn_dump
        self.sn_force = sn_force
        self.update_option = update_option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.name is not None:
            result['Name'] = self.name
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.config is not None:
            result['Config'] = self.config
        if self.sn_transfer is not None:
            result['SnTransfer'] = self.sn_transfer
        if self.sn_stat is not None:
            result['SnStat'] = self.sn_stat
        if self.sn_dump is not None:
            result['SnDump'] = self.sn_dump
        if self.sn_force is not None:
            result['SnForce'] = self.sn_force
        if self.update_option is not None:
            result['UpdateOption'] = self.update_option
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('SnTransfer') is not None:
            self.sn_transfer = m.get('SnTransfer')
        if m.get('SnStat') is not None:
            self.sn_stat = m.get('SnStat')
        if m.get('SnDump') is not None:
            self.sn_dump = m.get('SnDump')
        if m.get('SnForce') is not None:
            self.sn_force = m.get('SnForce')
        if m.get('UpdateOption') is not None:
            self.update_option = m.get('UpdateOption')
        return self


class ApplyScenarioShrinkRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        scenario: str = None,
        name: str = None,
        app_id: str = None,
        sign: str = None,
        config_shrink: str = None,
        sn_transfer: bool = None,
        sn_stat: bool = None,
        sn_dump: bool = None,
        sn_force: bool = None,
        update_option: bool = None,
    ):
        self.region_id = region_id
        self.scenario = scenario
        self.name = name
        self.app_id = app_id
        self.sign = sign
        self.config_shrink = config_shrink
        self.sn_transfer = sn_transfer
        self.sn_stat = sn_stat
        self.sn_dump = sn_dump
        self.sn_force = sn_force
        self.update_option = update_option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.name is not None:
            result['Name'] = self.name
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink
        if self.sn_transfer is not None:
            result['SnTransfer'] = self.sn_transfer
        if self.sn_stat is not None:
            result['SnStat'] = self.sn_stat
        if self.sn_dump is not None:
            result['SnDump'] = self.sn_dump
        if self.sn_force is not None:
            result['SnForce'] = self.sn_force
        if self.update_option is not None:
            result['UpdateOption'] = self.update_option
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')
        if m.get('SnTransfer') is not None:
            self.sn_transfer = m.get('SnTransfer')
        if m.get('SnStat') is not None:
            self.sn_stat = m.get('SnStat')
        if m.get('SnDump') is not None:
            self.sn_dump = m.get('SnDump')
        if m.get('SnForce') is not None:
            self.sn_force = m.get('SnForce')
        if m.get('UpdateOption') is not None:
            self.update_option = m.get('UpdateOption')
        return self


class ApplyScenarioResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ApplyScenarioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApplyScenarioResponseBody = None,
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
            temp_model = ApplyScenarioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDataConsistencyRequest(TeaModel):
    def __init__(
        self,
        current_timestamp: int = None,
        region_id: str = None,
        proxy_user_id: str = None,
        pid: str = None,
        app_type: str = None,
    ):
        self.current_timestamp = current_timestamp
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id
        self.pid = pid
        self.app_type = app_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_timestamp is not None:
            result['CurrentTimestamp'] = self.current_timestamp
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentTimestamp') is not None:
            self.current_timestamp = m.get('CurrentTimestamp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class CheckDataConsistencyResponseBody(TeaModel):
    def __init__(
        self,
        is_data_consistency: bool = None,
        request_id: str = None,
    ):
        self.is_data_consistency = is_data_consistency
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_data_consistency is not None:
            result['IsDataConsistency'] = self.is_data_consistency
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDataConsistency') is not None:
            self.is_data_consistency = m.get('IsDataConsistency')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDataConsistencyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckDataConsistencyResponseBody = None,
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
            temp_model = CheckDataConsistencyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceLinkedRoleForDeletingRequest(TeaModel):
    def __init__(
        self,
        role_arn: str = None,
        service_name: str = None,
        spiregion_id: str = None,
        deletion_task_id: str = None,
        region_id: str = None,
    ):
        self.role_arn = role_arn
        self.service_name = service_name
        self.spiregion_id = spiregion_id
        self.deletion_task_id = deletion_task_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.spiregion_id is not None:
            result['SPIRegionId'] = self.spiregion_id
        if self.deletion_task_id is not None:
            result['DeletionTaskId'] = self.deletion_task_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('SPIRegionId') is not None:
            self.spiregion_id = m.get('SPIRegionId')
        if m.get('DeletionTaskId') is not None:
            self.deletion_task_id = m.get('DeletionTaskId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages(TeaModel):
    def __init__(
        self,
        region: str = None,
        resources: List[str] = None,
    ):
        self.region = region
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class CheckServiceLinkedRoleForDeletingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        deletable: bool = None,
        role_usages: List[CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages] = None,
    ):
        self.request_id = request_id
        self.deletable = deletable
        self.role_usages = role_usages

    def validate(self):
        if self.role_usages:
            for k in self.role_usages:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        result['RoleUsages'] = []
        if self.role_usages is not None:
            for k in self.role_usages:
                result['RoleUsages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        self.role_usages = []
        if m.get('RoleUsages') is not None:
            for k in m.get('RoleUsages'):
                temp_model = CheckServiceLinkedRoleForDeletingResponseBodyRoleUsages()
                self.role_usages.append(temp_model.from_map(k))
        return self


class CheckServiceLinkedRoleForDeletingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckServiceLinkedRoleForDeletingResponseBody = None,
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
            temp_model = CheckServiceLinkedRoleForDeletingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigAppRequest(TeaModel):
    def __init__(
        self,
        app_ids: str = None,
        enable: str = None,
        region_id: str = None,
    ):
        self.app_ids = app_ids
        self.enable = enable
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ConfigAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfigAppResponseBody = None,
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
            temp_model = ConfigAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlertContactRequest(TeaModel):
    def __init__(
        self,
        contact_name: str = None,
        phone_num: str = None,
        email: str = None,
        ding_robot_webhook_url: str = None,
        system_noc: bool = None,
        region_id: str = None,
        proxy_user_id: str = None,
    ):
        self.contact_name = contact_name
        self.phone_num = phone_num
        self.email = email
        self.ding_robot_webhook_url = ding_robot_webhook_url
        self.system_noc = system_noc
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.email is not None:
            result['Email'] = self.email
        if self.ding_robot_webhook_url is not None:
            result['DingRobotWebhookUrl'] = self.ding_robot_webhook_url
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('DingRobotWebhookUrl') is not None:
            self.ding_robot_webhook_url = m.get('DingRobotWebhookUrl')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        return self


class CreateAlertContactResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        contact_id: str = None,
    ):
        self.request_id = request_id
        self.contact_id = contact_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        return self


class CreateAlertContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAlertContactResponseBody = None,
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
            temp_model = CreateAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlertContactGroupRequest(TeaModel):
    def __init__(
        self,
        contact_group_name: str = None,
        contact_ids: str = None,
        region_id: str = None,
        proxy_user_id: str = None,
    ):
        self.contact_group_name = contact_group_name
        self.contact_ids = contact_ids
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        return self


class CreateAlertContactGroupResponseBody(TeaModel):
    def __init__(
        self,
        contact_group_id: str = None,
        request_id: str = None,
    ):
        self.contact_group_id = contact_group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAlertContactGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAlertContactGroupResponseBody = None,
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
            temp_model = CreateAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRetcodeAppRequest(TeaModel):
    def __init__(
        self,
        retcode_app_name: str = None,
        retcode_app_type: str = None,
        region_id: str = None,
    ):
        self.retcode_app_name = retcode_app_name
        self.retcode_app_type = retcode_app_type
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.retcode_app_name is not None:
            result['RetcodeAppName'] = self.retcode_app_name
        if self.retcode_app_type is not None:
            result['RetcodeAppType'] = self.retcode_app_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetcodeAppName') is not None:
            self.retcode_app_name = m.get('RetcodeAppName')
        if m.get('RetcodeAppType') is not None:
            self.retcode_app_type = m.get('RetcodeAppType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateRetcodeAppResponseBodyRetcodeAppDataBean(TeaModel):
    def __init__(
        self,
        pid: str = None,
        app_id: int = None,
    ):
        self.pid = pid
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class CreateRetcodeAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        retcode_app_data_bean: CreateRetcodeAppResponseBodyRetcodeAppDataBean = None,
    ):
        self.request_id = request_id
        self.retcode_app_data_bean = retcode_app_data_bean

    def validate(self):
        if self.retcode_app_data_bean:
            self.retcode_app_data_bean.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retcode_app_data_bean is not None:
            result['RetcodeAppDataBean'] = self.retcode_app_data_bean.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RetcodeAppDataBean') is not None:
            temp_model = CreateRetcodeAppResponseBodyRetcodeAppDataBean()
            self.retcode_app_data_bean = temp_model.from_map(m['RetcodeAppDataBean'])
        return self


class CreateRetcodeAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRetcodeAppResponseBody = None,
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
            temp_model = CreateRetcodeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWehookRequest(TeaModel):
    def __init__(
        self,
        contact_name: str = None,
        method: str = None,
        url: str = None,
        http_params: str = None,
        http_headers: str = None,
        region_id: str = None,
        proxy_user_id: str = None,
        body: str = None,
    ):
        self.contact_name = contact_name
        self.method = method
        self.url = url
        self.http_params = http_params
        self.http_headers = http_headers
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.method is not None:
            result['Method'] = self.method
        if self.url is not None:
            result['Url'] = self.url
        if self.http_params is not None:
            result['HttpParams'] = self.http_params
        if self.http_headers is not None:
            result['HttpHeaders'] = self.http_headers
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.body is not None:
            result['Body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('HttpParams') is not None:
            self.http_params = m.get('HttpParams')
        if m.get('HttpHeaders') is not None:
            self.http_headers = m.get('HttpHeaders')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        return self


class CreateWehookResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        contact_id: str = None,
    ):
        self.request_id = request_id
        self.contact_id = contact_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        return self


class CreateWehookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateWehookResponseBody = None,
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
            temp_model = CreateWehookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertContactRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        proxy_user_id: str = None,
        contact_id: int = None,
    ):
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id
        self.contact_id = contact_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        return self


class DeleteAlertContactResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlertContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAlertContactResponseBody = None,
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
            temp_model = DeleteAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertContactGroupRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        proxy_user_id: str = None,
        contact_group_id: int = None,
    ):
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id
        self.contact_group_id = contact_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        return self


class DeleteAlertContactGroupResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlertContactGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAlertContactGroupResponseBody = None,
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
            temp_model = DeleteAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertRulesRequest(TeaModel):
    def __init__(
        self,
        alert_ids: str = None,
        proxy_user_id: str = None,
        region_id: str = None,
    ):
        self.alert_ids = alert_ids
        self.proxy_user_id = proxy_user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alert_ids is not None:
            result['AlertIds'] = self.alert_ids
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertIds') is not None:
            self.alert_ids = m.get('AlertIds')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAlertRulesResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAlertRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAlertRulesResponseBody = None,
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
            temp_model = DeleteAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRetcodeAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        region_id: str = None,
    ):
        self.app_id = app_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteRetcodeAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DeleteRetcodeAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRetcodeAppResponseBody = None,
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
            temp_model = DeleteRetcodeAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScenarioRequest(TeaModel):
    def __init__(
        self,
        scenario_id: int = None,
        region_id: str = None,
    ):
        self.scenario_id = scenario_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteScenarioResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DeleteScenarioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteScenarioResponseBody = None,
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
            temp_model = DeleteScenarioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTraceAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        region_id: str = None,
        type: str = None,
        pid: str = None,
    ):
        self.app_id = app_id
        self.region_id = region_id
        self.type = type
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        if self.pid is not None:
            result['Pid'] = self.pid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        return self


class DeleteTraceAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DeleteTraceAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteTraceAppResponseBody = None,
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
            temp_model = DeleteTraceAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDispatchRuleRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        region_id: str = None,
        proxy_user_id: str = None,
    ):
        self.id = id
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        operator: str = None,
    ):
        self.key = key
        self.value = value
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        if self.operator is not None:
            result['Operator'] = self.operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups(TeaModel):
    def __init__(
        self,
        label_match_expressions: List[DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions] = None,
    ):
        self.label_match_expressions = label_match_expressions

    def validate(self):
        if self.label_match_expressions:
            for k in self.label_match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['LabelMatchExpressions'] = []
        if self.label_match_expressions is not None:
            for k in self.label_match_expressions:
                result['LabelMatchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_match_expressions = []
        if m.get('LabelMatchExpressions') is not None:
            for k in m.get('LabelMatchExpressions'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroupsLabelMatchExpressions()
                self.label_match_expressions.append(temp_model.from_map(k))
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid(TeaModel):
    def __init__(
        self,
        label_match_expression_groups: List[DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups] = None,
    ):
        self.label_match_expression_groups = label_match_expression_groups

    def validate(self):
        if self.label_match_expression_groups:
            for k in self.label_match_expression_groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['LabelMatchExpressionGroups'] = []
        if self.label_match_expression_groups is not None:
            for k in self.label_match_expression_groups:
                result['LabelMatchExpressionGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_match_expression_groups = []
        if m.get('LabelMatchExpressionGroups') is not None:
            for k in m.get('LabelMatchExpressionGroups'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGridLabelMatchExpressionGroups()
                self.label_match_expression_groups.append(temp_model.from_map(k))
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleGroupRules(TeaModel):
    def __init__(
        self,
        grouping_fields: List[str] = None,
        group_id: int = None,
        group_interval: int = None,
        group_wait_time: int = None,
    ):
        self.grouping_fields = grouping_fields
        self.group_id = group_id
        self.group_interval = group_interval
        self.group_wait_time = group_wait_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.grouping_fields is not None:
            result['GroupingFields'] = self.grouping_fields
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_interval is not None:
            result['GroupInterval'] = self.group_interval
        if self.group_wait_time is not None:
            result['GroupWaitTime'] = self.group_wait_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupingFields') is not None:
            self.grouping_fields = m.get('GroupingFields')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupInterval') is not None:
            self.group_interval = m.get('GroupInterval')
        if m.get('GroupWaitTime') is not None:
            self.group_wait_time = m.get('GroupWaitTime')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects(TeaModel):
    def __init__(
        self,
        notify_object_id: str = None,
        notify_type: str = None,
        name: str = None,
    ):
        self.notify_object_id = notify_object_id
        self.notify_type = notify_type
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.notify_object_id is not None:
            result['NotifyObjectId'] = self.notify_object_id
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotifyObjectId') is not None:
            self.notify_object_id = m.get('NotifyObjectId')
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules(TeaModel):
    def __init__(
        self,
        notify_objects: List[DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects] = None,
        notify_channels: List[str] = None,
    ):
        self.notify_objects = notify_objects
        self.notify_channels = notify_channels

    def validate(self):
        if self.notify_objects:
            for k in self.notify_objects:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['NotifyObjects'] = []
        if self.notify_objects is not None:
            for k in self.notify_objects:
                result['NotifyObjects'].append(k.to_map() if k else None)
        if self.notify_channels is not None:
            result['NotifyChannels'] = self.notify_channels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.notify_objects = []
        if m.get('NotifyObjects') is not None:
            for k in m.get('NotifyObjects'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleNotifyRulesNotifyObjects()
                self.notify_objects.append(temp_model.from_map(k))
        if m.get('NotifyChannels') is not None:
            self.notify_channels = m.get('NotifyChannels')
        return self


class DescribeDispatchRuleResponseBodyDispatchRule(TeaModel):
    def __init__(
        self,
        state: str = None,
        label_match_expression_grid: DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid = None,
        name: str = None,
        group_rules: List[DescribeDispatchRuleResponseBodyDispatchRuleGroupRules] = None,
        rule_id: int = None,
        notify_rules: List[DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules] = None,
    ):
        self.state = state
        self.label_match_expression_grid = label_match_expression_grid
        self.name = name
        self.group_rules = group_rules
        self.rule_id = rule_id
        self.notify_rules = notify_rules

    def validate(self):
        if self.label_match_expression_grid:
            self.label_match_expression_grid.validate()
        if self.group_rules:
            for k in self.group_rules:
                if k:
                    k.validate()
        if self.notify_rules:
            for k in self.notify_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.state is not None:
            result['State'] = self.state
        if self.label_match_expression_grid is not None:
            result['LabelMatchExpressionGrid'] = self.label_match_expression_grid.to_map()
        if self.name is not None:
            result['Name'] = self.name
        result['GroupRules'] = []
        if self.group_rules is not None:
            for k in self.group_rules:
                result['GroupRules'].append(k.to_map() if k else None)
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        result['NotifyRules'] = []
        if self.notify_rules is not None:
            for k in self.notify_rules:
                result['NotifyRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('LabelMatchExpressionGrid') is not None:
            temp_model = DescribeDispatchRuleResponseBodyDispatchRuleLabelMatchExpressionGrid()
            self.label_match_expression_grid = temp_model.from_map(m['LabelMatchExpressionGrid'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.group_rules = []
        if m.get('GroupRules') is not None:
            for k in m.get('GroupRules'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleGroupRules()
                self.group_rules.append(temp_model.from_map(k))
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        self.notify_rules = []
        if m.get('NotifyRules') is not None:
            for k in m.get('NotifyRules'):
                temp_model = DescribeDispatchRuleResponseBodyDispatchRuleNotifyRules()
                self.notify_rules.append(temp_model.from_map(k))
        return self


class DescribeDispatchRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dispatch_rule: DescribeDispatchRuleResponseBodyDispatchRule = None,
    ):
        self.request_id = request_id
        self.dispatch_rule = dispatch_rule

    def validate(self):
        if self.dispatch_rule:
            self.dispatch_rule.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dispatch_rule is not None:
            result['DispatchRule'] = self.dispatch_rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DispatchRule') is not None:
            temp_model = DescribeDispatchRuleResponseBodyDispatchRule()
            self.dispatch_rule = temp_model.from_map(m['DispatchRule'])
        return self


class DescribeDispatchRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDispatchRuleResponseBody = None,
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
            temp_model = DescribeDispatchRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTraceLicenseKeyRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeTraceLicenseKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        license_key: str = None,
    ):
        self.request_id = request_id
        self.license_key = license_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.license_key is not None:
            result['LicenseKey'] = self.license_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')
        return self


class DescribeTraceLicenseKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTraceLicenseKeyResponseBody = None,
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
            temp_model = DescribeTraceLicenseKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTraceLocationRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeTraceLocationResponseBodyRegionConfigs(TeaModel):
    def __init__(
        self,
        region_no: str = None,
        url: str = None,
    ):
        self.region_no = region_no
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeTraceLocationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        region_configs: List[DescribeTraceLocationResponseBodyRegionConfigs] = None,
    ):
        self.request_id = request_id
        self.region_configs = region_configs

    def validate(self):
        if self.region_configs:
            for k in self.region_configs:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RegionConfigs'] = []
        if self.region_configs is not None:
            for k in self.region_configs:
                result['RegionConfigs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.region_configs = []
        if m.get('RegionConfigs') is not None:
            for k in m.get('RegionConfigs'):
                temp_model = DescribeTraceLocationResponseBodyRegionConfigs()
                self.region_configs.append(temp_model.from_map(k))
        return self


class DescribeTraceLocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTraceLocationResponseBody = None,
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
            temp_model = DescribeTraceLocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportPrometheusRulesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        cluster_id: str = None,
        name_space: str = None,
        name: str = None,
    ):
        self.region_id = region_id
        self.cluster_id = cluster_id
        self.name_space = name_space
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ExportPrometheusRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ExportPrometheusRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportPrometheusRulesResponseBody = None,
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
            temp_model = ExportPrometheusRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentDownloadUrlRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAgentDownloadUrlResponseBody(TeaModel):
    def __init__(
        self,
        arms_agent_download_url: str = None,
        request_id: str = None,
    ):
        self.arms_agent_download_url = arms_agent_download_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.arms_agent_download_url is not None:
            result['ArmsAgentDownloadUrl'] = self.arms_agent_download_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArmsAgentDownloadUrl') is not None:
            self.arms_agent_download_url = m.get('ArmsAgentDownloadUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAgentDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAgentDownloadUrlResponseBody = None,
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
            temp_model = GetAgentDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppApiByPageRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        start_time: int = None,
        end_time: int = None,
        current_page: int = None,
        page_size: int = None,
        interval_mills: int = None,
        pid: str = None,
    ):
        self.region_id = region_id
        self.start_time = start_time
        self.end_time = end_time
        self.current_page = current_page
        self.page_size = page_size
        self.interval_mills = interval_mills
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.interval_mills is not None:
            result['IntervalMills'] = self.interval_mills
        if self.pid is not None:
            result['PId'] = self.pid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('IntervalMills') is not None:
            self.interval_mills = m.get('IntervalMills')
        if m.get('PId') is not None:
            self.pid = m.get('PId')
        return self


class GetAppApiByPageResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[Dict[str, Any]] = None,
        page_size: int = None,
        total: str = None,
        page: int = None,
    ):
        self.items = items
        self.page_size = page_size
        self.total = total
        self.page = page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.items is not None:
            result['Items'] = self.items
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class GetAppApiByPageResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: GetAppApiByPageResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAppApiByPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAppApiByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAppApiByPageResponseBody = None,
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
            temp_model = GetAppApiByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConsistencySnapshotRequest(TeaModel):
    def __init__(
        self,
        current_timestamp: int = None,
        region_id: str = None,
        proxy_user_id: str = None,
        pid: str = None,
        app_type: str = None,
    ):
        self.current_timestamp = current_timestamp
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id
        self.pid = pid
        self.app_type = app_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.current_timestamp is not None:
            result['CurrentTimestamp'] = self.current_timestamp
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentTimestamp') is not None:
            self.current_timestamp = m.get('CurrentTimestamp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class GetConsistencySnapshotResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        consistency_result_json_str: str = None,
    ):
        self.request_id = request_id
        self.consistency_result_json_str = consistency_result_json_str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.consistency_result_json_str is not None:
            result['ConsistencyResultJsonStr'] = self.consistency_result_json_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConsistencyResultJsonStr') is not None:
            self.consistency_result_json_str = m.get('ConsistencyResultJsonStr')
        return self


class GetConsistencySnapshotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConsistencySnapshotResponseBody = None,
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
            temp_model = GetConsistencySnapshotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIntegrationTokenRequest(TeaModel):
    def __init__(
        self,
        product_type: str = None,
        region_id: str = None,
        proxy_user_id: str = None,
    ):
        self.product_type = product_type
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        return self


class GetIntegrationTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        token: str = None,
    ):
        self.request_id = request_id
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetIntegrationTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetIntegrationTokenResponseBody = None,
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
            temp_model = GetIntegrationTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMultipleTraceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        trace_ids: List[str] = None,
    ):
        self.region_id = region_id
        self.trace_ids = trace_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.trace_ids is not None:
            result['TraceIDs'] = self.trace_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TraceIDs') is not None:
            self.trace_ids = m.get('TraceIDs')
        return self


class GetMultipleTraceResponseBodyMultiCallChainInfosSpansTagEntryList(TeaModel):
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


class GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventListTagEntryList(TeaModel):
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


class GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventList(TeaModel):
    def __init__(
        self,
        tag_entry_list: List[GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventListTagEntryList] = None,
        timestamp: int = None,
    ):
        self.tag_entry_list = tag_entry_list
        self.timestamp = timestamp

    def validate(self):
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventListTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetMultipleTraceResponseBodyMultiCallChainInfosSpans(TeaModel):
    def __init__(
        self,
        operation_name: str = None,
        result_code: str = None,
        timestamp: int = None,
        rpc_type: int = None,
        tag_entry_list: List[GetMultipleTraceResponseBodyMultiCallChainInfosSpansTagEntryList] = None,
        log_event_list: List[GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventList] = None,
        have_stack: bool = None,
        service_ip: str = None,
        duration: int = None,
        rpc_id: str = None,
        service_name: str = None,
        trace_id: str = None,
    ):
        self.operation_name = operation_name
        self.result_code = result_code
        self.timestamp = timestamp
        self.rpc_type = rpc_type
        self.tag_entry_list = tag_entry_list
        self.log_event_list = log_event_list
        self.have_stack = have_stack
        self.service_ip = service_ip
        self.duration = duration
        self.rpc_id = rpc_id
        self.service_name = service_name
        self.trace_id = trace_id

    def validate(self):
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()
        if self.log_event_list:
            for k in self.log_event_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.rpc_type is not None:
            result['RpcType'] = self.rpc_type
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        result['LogEventList'] = []
        if self.log_event_list is not None:
            for k in self.log_event_list:
                result['LogEventList'].append(k.to_map() if k else None)
        if self.have_stack is not None:
            result['HaveStack'] = self.have_stack
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('RpcType') is not None:
            self.rpc_type = m.get('RpcType')
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpansTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        self.log_event_list = []
        if m.get('LogEventList') is not None:
            for k in m.get('LogEventList'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpansLogEventList()
                self.log_event_list.append(temp_model.from_map(k))
        if m.get('HaveStack') is not None:
            self.have_stack = m.get('HaveStack')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetMultipleTraceResponseBodyMultiCallChainInfos(TeaModel):
    def __init__(
        self,
        spans: List[GetMultipleTraceResponseBodyMultiCallChainInfosSpans] = None,
        trace_id: str = None,
    ):
        self.spans = spans
        self.trace_id = trace_id

    def validate(self):
        if self.spans:
            for k in self.spans:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Spans'] = []
        if self.spans is not None:
            for k in self.spans:
                result['Spans'].append(k.to_map() if k else None)
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.spans = []
        if m.get('Spans') is not None:
            for k in m.get('Spans'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfosSpans()
                self.spans.append(temp_model.from_map(k))
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetMultipleTraceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        multi_call_chain_infos: List[GetMultipleTraceResponseBodyMultiCallChainInfos] = None,
    ):
        self.request_id = request_id
        self.multi_call_chain_infos = multi_call_chain_infos

    def validate(self):
        if self.multi_call_chain_infos:
            for k in self.multi_call_chain_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['MultiCallChainInfos'] = []
        if self.multi_call_chain_infos is not None:
            for k in self.multi_call_chain_infos:
                result['MultiCallChainInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.multi_call_chain_infos = []
        if m.get('MultiCallChainInfos') is not None:
            for k in m.get('MultiCallChainInfos'):
                temp_model = GetMultipleTraceResponseBodyMultiCallChainInfos()
                self.multi_call_chain_infos.append(temp_model.from_map(k))
        return self


class GetMultipleTraceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMultipleTraceResponseBody = None,
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
            temp_model = GetMultipleTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPrometheusApiTokenRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetPrometheusApiTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        token: str = None,
    ):
        self.request_id = request_id
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetPrometheusApiTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPrometheusApiTokenResponseBody = None,
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
            temp_model = GetPrometheusApiTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRetcodeShareUrlRequest(TeaModel):
    def __init__(
        self,
        pid: str = None,
    ):
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        return self


class GetRetcodeShareUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        url: str = None,
    ):
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetRetcodeShareUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRetcodeShareUrlResponseBody = None,
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
            temp_model = GetRetcodeShareUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStackRequest(TeaModel):
    def __init__(
        self,
        trace_id: str = None,
        region_id: str = None,
        rpc_id: str = None,
        pid: str = None,
    ):
        self.trace_id = trace_id
        self.region_id = region_id
        self.rpc_id = rpc_id
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rpc_id is not None:
            result['RpcID'] = self.rpc_id
        if self.pid is not None:
            result['Pid'] = self.pid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RpcID') is not None:
            self.rpc_id = m.get('RpcID')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        return self


class GetStackResponseBodyStackInfoExtInfo(TeaModel):
    def __init__(
        self,
        type: str = None,
        info: str = None,
    ):
        self.type = type
        self.info = info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.info is not None:
            result['Info'] = self.info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Info') is not None:
            self.info = m.get('Info')
        return self


class GetStackResponseBodyStackInfo(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        exception: str = None,
        api: str = None,
        line: str = None,
        duration: int = None,
        rpc_id: str = None,
        service_name: str = None,
        ext_info: GetStackResponseBodyStackInfoExtInfo = None,
    ):
        self.start_time = start_time
        self.exception = exception
        self.api = api
        self.line = line
        self.duration = duration
        self.rpc_id = rpc_id
        self.service_name = service_name
        self.ext_info = ext_info

    def validate(self):
        if self.ext_info:
            self.ext_info.validate()

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.exception is not None:
            result['Exception'] = self.exception
        if self.api is not None:
            result['Api'] = self.api
        if self.line is not None:
            result['Line'] = self.line
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Exception') is not None:
            self.exception = m.get('Exception')
        if m.get('Api') is not None:
            self.api = m.get('Api')
        if m.get('Line') is not None:
            self.line = m.get('Line')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ExtInfo') is not None:
            temp_model = GetStackResponseBodyStackInfoExtInfo()
            self.ext_info = temp_model.from_map(m['ExtInfo'])
        return self


class GetStackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stack_info: List[GetStackResponseBodyStackInfo] = None,
    ):
        self.request_id = request_id
        self.stack_info = stack_info

    def validate(self):
        if self.stack_info:
            for k in self.stack_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StackInfo'] = []
        if self.stack_info is not None:
            for k in self.stack_info:
                result['StackInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stack_info = []
        if m.get('StackInfo') is not None:
            for k in m.get('StackInfo'):
                temp_model = GetStackResponseBodyStackInfo()
                self.stack_info.append(temp_model.from_map(k))
        return self


class GetStackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetStackResponseBody = None,
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
            temp_model = GetStackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTraceRequest(TeaModel):
    def __init__(
        self,
        trace_id: str = None,
        region_id: str = None,
    ):
        self.trace_id = trace_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetTraceResponseBodySpansTagEntryList(TeaModel):
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


class GetTraceResponseBodySpansLogEventListTagEntryList(TeaModel):
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


class GetTraceResponseBodySpansLogEventList(TeaModel):
    def __init__(
        self,
        tag_entry_list: List[GetTraceResponseBodySpansLogEventListTagEntryList] = None,
        timestamp: int = None,
    ):
        self.tag_entry_list = tag_entry_list
        self.timestamp = timestamp

    def validate(self):
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetTraceResponseBodySpansLogEventListTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetTraceResponseBodySpans(TeaModel):
    def __init__(
        self,
        operation_name: str = None,
        result_code: str = None,
        timestamp: int = None,
        rpc_type: int = None,
        tag_entry_list: List[GetTraceResponseBodySpansTagEntryList] = None,
        log_event_list: List[GetTraceResponseBodySpansLogEventList] = None,
        have_stack: bool = None,
        service_ip: str = None,
        duration: int = None,
        rpc_id: str = None,
        service_name: str = None,
        trace_id: str = None,
    ):
        self.operation_name = operation_name
        self.result_code = result_code
        self.timestamp = timestamp
        self.rpc_type = rpc_type
        self.tag_entry_list = tag_entry_list
        self.log_event_list = log_event_list
        self.have_stack = have_stack
        self.service_ip = service_ip
        self.duration = duration
        self.rpc_id = rpc_id
        self.service_name = service_name
        self.trace_id = trace_id

    def validate(self):
        if self.tag_entry_list:
            for k in self.tag_entry_list:
                if k:
                    k.validate()
        if self.log_event_list:
            for k in self.log_event_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.rpc_type is not None:
            result['RpcType'] = self.rpc_type
        result['TagEntryList'] = []
        if self.tag_entry_list is not None:
            for k in self.tag_entry_list:
                result['TagEntryList'].append(k.to_map() if k else None)
        result['LogEventList'] = []
        if self.log_event_list is not None:
            for k in self.log_event_list:
                result['LogEventList'].append(k.to_map() if k else None)
        if self.have_stack is not None:
            result['HaveStack'] = self.have_stack
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.rpc_id is not None:
            result['RpcId'] = self.rpc_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('RpcType') is not None:
            self.rpc_type = m.get('RpcType')
        self.tag_entry_list = []
        if m.get('TagEntryList') is not None:
            for k in m.get('TagEntryList'):
                temp_model = GetTraceResponseBodySpansTagEntryList()
                self.tag_entry_list.append(temp_model.from_map(k))
        self.log_event_list = []
        if m.get('LogEventList') is not None:
            for k in m.get('LogEventList'):
                temp_model = GetTraceResponseBodySpansLogEventList()
                self.log_event_list.append(temp_model.from_map(k))
        if m.get('HaveStack') is not None:
            self.have_stack = m.get('HaveStack')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('RpcId') is not None:
            self.rpc_id = m.get('RpcId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class GetTraceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        spans: List[GetTraceResponseBodySpans] = None,
    ):
        self.request_id = request_id
        self.spans = spans

    def validate(self):
        if self.spans:
            for k in self.spans:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Spans'] = []
        if self.spans is not None:
            for k in self.spans:
                result['Spans'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.spans = []
        if m.get('Spans') is not None:
            for k in m.get('Spans'):
                temp_model = GetTraceResponseBodySpans()
                self.spans.append(temp_model.from_map(k))
        return self


class GetTraceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTraceResponseBody = None,
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
            temp_model = GetTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTraceAppRequest(TeaModel):
    def __init__(
        self,
        pid: str = None,
        region_id: str = None,
    ):
        self.pid = pid
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetTraceAppResponseBodyTraceApp(TeaModel):
    def __init__(
        self,
        type: str = None,
        app_name: str = None,
        update_time: int = None,
        labels: List[str] = None,
        show: bool = None,
        create_time: int = None,
        pid: str = None,
        app_id: int = None,
        user_id: str = None,
        region_id: str = None,
    ):
        self.type = type
        self.app_name = app_name
        self.update_time = update_time
        self.labels = labels
        self.show = show
        self.create_time = create_time
        self.pid = pid
        self.app_id = app_id
        self.user_id = user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.show is not None:
            result['Show'] = self.show
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetTraceAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trace_app: GetTraceAppResponseBodyTraceApp = None,
    ):
        self.request_id = request_id
        self.trace_app = trace_app

    def validate(self):
        if self.trace_app:
            self.trace_app.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_app is not None:
            result['TraceApp'] = self.trace_app.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceApp') is not None:
            temp_model = GetTraceAppResponseBodyTraceApp()
            self.trace_app = temp_model.from_map(m['TraceApp'])
        return self


class GetTraceAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTraceAppResponseBody = None,
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
            temp_model = GetTraceAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportAppAlertRulesRequest(TeaModel):
    def __init__(
        self,
        template_alert_id: str = None,
        pids: str = None,
        region_id: str = None,
        contact_group_ids: str = None,
        is_auto_start: bool = None,
        templage_alert_config: str = None,
        proxy_user_id: str = None,
    ):
        self.template_alert_id = template_alert_id
        self.pids = pids
        self.region_id = region_id
        self.contact_group_ids = contact_group_ids
        self.is_auto_start = is_auto_start
        self.templage_alert_config = templage_alert_config
        self.proxy_user_id = proxy_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_alert_id is not None:
            result['TemplateAlertId'] = self.template_alert_id
        if self.pids is not None:
            result['Pids'] = self.pids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.is_auto_start is not None:
            result['IsAutoStart'] = self.is_auto_start
        if self.templage_alert_config is not None:
            result['TemplageAlertConfig'] = self.templage_alert_config
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateAlertId') is not None:
            self.template_alert_id = m.get('TemplateAlertId')
        if m.get('Pids') is not None:
            self.pids = m.get('Pids')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('IsAutoStart') is not None:
            self.is_auto_start = m.get('IsAutoStart')
        if m.get('TemplageAlertConfig') is not None:
            self.templage_alert_config = m.get('TemplageAlertConfig')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        return self


class ImportAppAlertRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ImportAppAlertRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportAppAlertRulesResponseBody = None,
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
            temp_model = ImportAppAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportCustomAlertRulesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        contact_group_ids: str = None,
        is_auto_start: bool = None,
        template_alert_config: str = None,
        proxy_user_id: str = None,
        templage_alert_config: str = None,
    ):
        self.region_id = region_id
        self.contact_group_ids = contact_group_ids
        self.is_auto_start = is_auto_start
        self.template_alert_config = template_alert_config
        self.proxy_user_id = proxy_user_id
        self.templage_alert_config = templage_alert_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.is_auto_start is not None:
            result['IsAutoStart'] = self.is_auto_start
        if self.template_alert_config is not None:
            result['TemplateAlertConfig'] = self.template_alert_config
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.templage_alert_config is not None:
            result['TemplageAlertConfig'] = self.templage_alert_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('IsAutoStart') is not None:
            self.is_auto_start = m.get('IsAutoStart')
        if m.get('TemplateAlertConfig') is not None:
            self.template_alert_config = m.get('TemplateAlertConfig')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('TemplageAlertConfig') is not None:
            self.templage_alert_config = m.get('TemplageAlertConfig')
        return self


class ImportCustomAlertRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ImportCustomAlertRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportCustomAlertRulesResponseBody = None,
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
            temp_model = ImportCustomAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportPrometheusRulesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        cluster_id: str = None,
        name_space: str = None,
        name: str = None,
        content: str = None,
    ):
        self.region_id = region_id
        self.cluster_id = cluster_id
        self.name_space = name_space
        self.name = name
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.name_space is not None:
            result['NameSpace'] = self.name_space
        if self.name is not None:
            result['Name'] = self.name
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NameSpace') is not None:
            self.name_space = m.get('NameSpace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ImportPrometheusRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ImportPrometheusRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportPrometheusRulesResponseBody = None,
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
            temp_model = ImportPrometheusRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterFromGrafanaRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListClusterFromGrafanaResponseBodyPromClusterList(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        create_time: int = None,
        user_id: str = None,
        options: str = None,
        is_controller_installed: bool = None,
        agent_status: str = None,
        extra: str = None,
        controller_id: str = None,
        region_id: str = None,
        install_time: int = None,
        plugins_json_array: str = None,
        cluster_type: str = None,
        cluster_name: str = None,
        state_json: str = None,
        last_heart_beat_time: int = None,
        node_num: int = None,
        id: int = None,
        cluster_id: str = None,
    ):
        self.update_time = update_time
        self.create_time = create_time
        self.user_id = user_id
        self.options = options
        self.is_controller_installed = is_controller_installed
        self.agent_status = agent_status
        self.extra = extra
        self.controller_id = controller_id
        self.region_id = region_id
        self.install_time = install_time
        self.plugins_json_array = plugins_json_array
        self.cluster_type = cluster_type
        self.cluster_name = cluster_name
        self.state_json = state_json
        self.last_heart_beat_time = last_heart_beat_time
        self.node_num = node_num
        self.id = id
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.options is not None:
            result['Options'] = self.options
        if self.is_controller_installed is not None:
            result['IsControllerInstalled'] = self.is_controller_installed
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.controller_id is not None:
            result['ControllerId'] = self.controller_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.install_time is not None:
            result['InstallTime'] = self.install_time
        if self.plugins_json_array is not None:
            result['PluginsJsonArray'] = self.plugins_json_array
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.state_json is not None:
            result['StateJson'] = self.state_json
        if self.last_heart_beat_time is not None:
            result['LastHeartBeatTime'] = self.last_heart_beat_time
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.id is not None:
            result['Id'] = self.id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('IsControllerInstalled') is not None:
            self.is_controller_installed = m.get('IsControllerInstalled')
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('ControllerId') is not None:
            self.controller_id = m.get('ControllerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')
        if m.get('PluginsJsonArray') is not None:
            self.plugins_json_array = m.get('PluginsJsonArray')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('StateJson') is not None:
            self.state_json = m.get('StateJson')
        if m.get('LastHeartBeatTime') is not None:
            self.last_heart_beat_time = m.get('LastHeartBeatTime')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListClusterFromGrafanaResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prom_cluster_list: List[ListClusterFromGrafanaResponseBodyPromClusterList] = None,
    ):
        self.request_id = request_id
        self.prom_cluster_list = prom_cluster_list

    def validate(self):
        if self.prom_cluster_list:
            for k in self.prom_cluster_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PromClusterList'] = []
        if self.prom_cluster_list is not None:
            for k in self.prom_cluster_list:
                result['PromClusterList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.prom_cluster_list = []
        if m.get('PromClusterList') is not None:
            for k in m.get('PromClusterList'):
                temp_model = ListClusterFromGrafanaResponseBodyPromClusterList()
                self.prom_cluster_list.append(temp_model.from_map(k))
        return self


class ListClusterFromGrafanaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListClusterFromGrafanaResponseBody = None,
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
            temp_model = ListClusterFromGrafanaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDashboardsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        cluster_id: str = None,
        cluster_type: str = None,
        title: str = None,
    ):
        self.region_id = region_id
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListDashboardsResponseBodyDashboardVos(TeaModel):
    def __init__(
        self,
        type: str = None,
        time: str = None,
        exporter: str = None,
        is_arms_exporter: bool = None,
        url: str = None,
        tags: List[str] = None,
        title: str = None,
        id: str = None,
        uid: str = None,
    ):
        self.type = type
        self.time = time
        self.exporter = exporter
        self.is_arms_exporter = is_arms_exporter
        self.url = url
        self.tags = tags
        self.title = title
        self.id = id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.time is not None:
            result['Time'] = self.time
        if self.exporter is not None:
            result['Exporter'] = self.exporter
        if self.is_arms_exporter is not None:
            result['IsArmsExporter'] = self.is_arms_exporter
        if self.url is not None:
            result['Url'] = self.url
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.id is not None:
            result['Id'] = self.id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Exporter') is not None:
            self.exporter = m.get('Exporter')
        if m.get('IsArmsExporter') is not None:
            self.is_arms_exporter = m.get('IsArmsExporter')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class ListDashboardsResponseBody(TeaModel):
    def __init__(
        self,
        dashboard_vos: List[ListDashboardsResponseBodyDashboardVos] = None,
        request_id: str = None,
    ):
        self.dashboard_vos = dashboard_vos
        self.request_id = request_id

    def validate(self):
        if self.dashboard_vos:
            for k in self.dashboard_vos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DashboardVos'] = []
        if self.dashboard_vos is not None:
            for k in self.dashboard_vos:
                result['DashboardVos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dashboard_vos = []
        if m.get('DashboardVos') is not None:
            for k in m.get('DashboardVos'):
                temp_model = ListDashboardsResponseBodyDashboardVos()
                self.dashboard_vos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDashboardsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDashboardsResponseBody = None,
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
            temp_model = ListDashboardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPromClustersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListPromClustersResponseBodyPromClusterList(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        create_time: int = None,
        user_id: str = None,
        options: str = None,
        is_controller_installed: bool = None,
        agent_status: str = None,
        extra: str = None,
        controller_id: str = None,
        region_id: str = None,
        install_time: int = None,
        plugins_json_array: str = None,
        cluster_type: str = None,
        cluster_name: str = None,
        state_json: str = None,
        last_heart_beat_time: int = None,
        node_num: int = None,
        id: int = None,
        cluster_id: str = None,
    ):
        self.update_time = update_time
        self.create_time = create_time
        self.user_id = user_id
        self.options = options
        self.is_controller_installed = is_controller_installed
        self.agent_status = agent_status
        self.extra = extra
        self.controller_id = controller_id
        self.region_id = region_id
        self.install_time = install_time
        self.plugins_json_array = plugins_json_array
        self.cluster_type = cluster_type
        self.cluster_name = cluster_name
        self.state_json = state_json
        self.last_heart_beat_time = last_heart_beat_time
        self.node_num = node_num
        self.id = id
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.options is not None:
            result['Options'] = self.options
        if self.is_controller_installed is not None:
            result['IsControllerInstalled'] = self.is_controller_installed
        if self.agent_status is not None:
            result['AgentStatus'] = self.agent_status
        if self.extra is not None:
            result['Extra'] = self.extra
        if self.controller_id is not None:
            result['ControllerId'] = self.controller_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.install_time is not None:
            result['InstallTime'] = self.install_time
        if self.plugins_json_array is not None:
            result['PluginsJsonArray'] = self.plugins_json_array
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.state_json is not None:
            result['StateJson'] = self.state_json
        if self.last_heart_beat_time is not None:
            result['LastHeartBeatTime'] = self.last_heart_beat_time
        if self.node_num is not None:
            result['NodeNum'] = self.node_num
        if self.id is not None:
            result['Id'] = self.id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Options') is not None:
            self.options = m.get('Options')
        if m.get('IsControllerInstalled') is not None:
            self.is_controller_installed = m.get('IsControllerInstalled')
        if m.get('AgentStatus') is not None:
            self.agent_status = m.get('AgentStatus')
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')
        if m.get('ControllerId') is not None:
            self.controller_id = m.get('ControllerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')
        if m.get('PluginsJsonArray') is not None:
            self.plugins_json_array = m.get('PluginsJsonArray')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('StateJson') is not None:
            self.state_json = m.get('StateJson')
        if m.get('LastHeartBeatTime') is not None:
            self.last_heart_beat_time = m.get('LastHeartBeatTime')
        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ListPromClustersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        prom_cluster_list: List[ListPromClustersResponseBodyPromClusterList] = None,
    ):
        self.request_id = request_id
        self.prom_cluster_list = prom_cluster_list

    def validate(self):
        if self.prom_cluster_list:
            for k in self.prom_cluster_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['PromClusterList'] = []
        if self.prom_cluster_list is not None:
            for k in self.prom_cluster_list:
                result['PromClusterList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.prom_cluster_list = []
        if m.get('PromClusterList') is not None:
            for k in m.get('PromClusterList'):
                temp_model = ListPromClustersResponseBodyPromClusterList()
                self.prom_cluster_list.append(temp_model.from_map(k))
        return self


class ListPromClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListPromClustersResponseBody = None,
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
            temp_model = ListPromClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRetcodeAppsRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        region_id: str = None,
    ):
        self.security_token = security_token
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRetcodeAppsResponseBodyRetcodeApps(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_id: int = None,
        pid: str = None,
    ):
        self.app_name = app_name
        self.app_id = app_id
        self.pid = pid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.pid is not None:
            result['Pid'] = self.pid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        return self


class ListRetcodeAppsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        retcode_apps: List[ListRetcodeAppsResponseBodyRetcodeApps] = None,
    ):
        self.request_id = request_id
        self.retcode_apps = retcode_apps

    def validate(self):
        if self.retcode_apps:
            for k in self.retcode_apps:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RetcodeApps'] = []
        if self.retcode_apps is not None:
            for k in self.retcode_apps:
                result['RetcodeApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.retcode_apps = []
        if m.get('RetcodeApps') is not None:
            for k in m.get('RetcodeApps'):
                temp_model = ListRetcodeAppsResponseBodyRetcodeApps()
                self.retcode_apps.append(temp_model.from_map(k))
        return self


class ListRetcodeAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRetcodeAppsResponseBody = None,
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
            temp_model = ListRetcodeAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScenarioRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        scenario: str = None,
        name: str = None,
        app_id: str = None,
        sign: str = None,
    ):
        self.region_id = region_id
        self.scenario = scenario
        self.name = name
        self.app_id = app_id
        self.sign = sign

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scenario is not None:
            result['Scenario'] = self.scenario
        if self.name is not None:
            result['Name'] = self.name
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.sign is not None:
            result['Sign'] = self.sign
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        return self


class ListScenarioResponseBodyArmsScenarios(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        app_id: str = None,
        sign: str = None,
        create_time: str = None,
        user_id: str = None,
        extensions: str = None,
        name: str = None,
        id: int = None,
        region_id: str = None,
    ):
        self.update_time = update_time
        self.app_id = app_id
        self.sign = sign
        self.create_time = create_time
        self.user_id = user_id
        self.extensions = extensions
        self.name = name
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListScenarioResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        arms_scenarios: List[ListScenarioResponseBodyArmsScenarios] = None,
    ):
        self.request_id = request_id
        self.arms_scenarios = arms_scenarios

    def validate(self):
        if self.arms_scenarios:
            for k in self.arms_scenarios:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ArmsScenarios'] = []
        if self.arms_scenarios is not None:
            for k in self.arms_scenarios:
                result['ArmsScenarios'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.arms_scenarios = []
        if m.get('ArmsScenarios') is not None:
            for k in m.get('ArmsScenarios'):
                temp_model = ListScenarioResponseBodyArmsScenarios()
                self.arms_scenarios.append(temp_model.from_map(k))
        return self


class ListScenarioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListScenarioResponseBody = None,
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
            temp_model = ListScenarioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTraceAppsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListTraceAppsResponseBodyTraceApps(TeaModel):
    def __init__(
        self,
        type: str = None,
        app_name: str = None,
        update_time: int = None,
        labels: List[str] = None,
        show: bool = None,
        create_time: int = None,
        pid: str = None,
        app_id: int = None,
        user_id: str = None,
        region_id: str = None,
    ):
        self.type = type
        self.app_name = app_name
        self.update_time = update_time
        self.labels = labels
        self.show = show
        self.create_time = create_time
        self.pid = pid
        self.app_id = app_id
        self.user_id = user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.show is not None:
            result['Show'] = self.show
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListTraceAppsResponseBody(TeaModel):
    def __init__(
        self,
        trace_apps: List[ListTraceAppsResponseBodyTraceApps] = None,
        message: str = None,
        request_id: str = None,
        code: int = None,
        success: bool = None,
    ):
        self.trace_apps = trace_apps
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        if self.trace_apps:
            for k in self.trace_apps:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TraceApps'] = []
        if self.trace_apps is not None:
            for k in self.trace_apps:
                result['TraceApps'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trace_apps = []
        if m.get('TraceApps') is not None:
            for k in m.get('TraceApps'):
                temp_model = ListTraceAppsResponseBodyTraceApps()
                self.trace_apps.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListTraceAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTraceAppsResponseBody = None,
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
            temp_model = ListTraceAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenArmsServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        type: str = None,
    ):
        self.owner_id = owner_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class OpenArmsServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class OpenArmsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenArmsServiceResponseBody = None,
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
            temp_model = OpenArmsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDatasetRequestDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryDatasetRequestRequiredDims(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryDatasetRequestOptionalDims(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryDatasetRequest(TeaModel):
    def __init__(
        self,
        dataset_id: int = None,
        interval_in_sec: int = None,
        date_str: str = None,
        min_time: int = None,
        max_time: int = None,
        is_drill_down: bool = None,
        order_by_key: str = None,
        limit: int = None,
        reduce_tail: bool = None,
        hungry_mode: bool = None,
        proxy_user_id: str = None,
        measures: List[str] = None,
        dimensions: List[QueryDatasetRequestDimensions] = None,
        required_dims: List[QueryDatasetRequestRequiredDims] = None,
        optional_dims: List[QueryDatasetRequestOptionalDims] = None,
    ):
        self.dataset_id = dataset_id
        self.interval_in_sec = interval_in_sec
        self.date_str = date_str
        self.min_time = min_time
        self.max_time = max_time
        self.is_drill_down = is_drill_down
        self.order_by_key = order_by_key
        self.limit = limit
        self.reduce_tail = reduce_tail
        self.hungry_mode = hungry_mode
        self.proxy_user_id = proxy_user_id
        self.measures = measures
        self.dimensions = dimensions
        self.required_dims = required_dims
        self.optional_dims = optional_dims

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()
        if self.required_dims:
            for k in self.required_dims:
                if k:
                    k.validate()
        if self.optional_dims:
            for k in self.optional_dims:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec
        if self.date_str is not None:
            result['DateStr'] = self.date_str
        if self.min_time is not None:
            result['MinTime'] = self.min_time
        if self.max_time is not None:
            result['MaxTime'] = self.max_time
        if self.is_drill_down is not None:
            result['IsDrillDown'] = self.is_drill_down
        if self.order_by_key is not None:
            result['OrderByKey'] = self.order_by_key
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.reduce_tail is not None:
            result['ReduceTail'] = self.reduce_tail
        if self.hungry_mode is not None:
            result['HungryMode'] = self.hungry_mode
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.measures is not None:
            result['Measures'] = self.measures
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        result['RequiredDims'] = []
        if self.required_dims is not None:
            for k in self.required_dims:
                result['RequiredDims'].append(k.to_map() if k else None)
        result['OptionalDims'] = []
        if self.optional_dims is not None:
            for k in self.optional_dims:
                result['OptionalDims'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')
        if m.get('DateStr') is not None:
            self.date_str = m.get('DateStr')
        if m.get('MinTime') is not None:
            self.min_time = m.get('MinTime')
        if m.get('MaxTime') is not None:
            self.max_time = m.get('MaxTime')
        if m.get('IsDrillDown') is not None:
            self.is_drill_down = m.get('IsDrillDown')
        if m.get('OrderByKey') is not None:
            self.order_by_key = m.get('OrderByKey')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('ReduceTail') is not None:
            self.reduce_tail = m.get('ReduceTail')
        if m.get('HungryMode') is not None:
            self.hungry_mode = m.get('HungryMode')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = QueryDatasetRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        self.required_dims = []
        if m.get('RequiredDims') is not None:
            for k in m.get('RequiredDims'):
                temp_model = QueryDatasetRequestRequiredDims()
                self.required_dims.append(temp_model.from_map(k))
        self.optional_dims = []
        if m.get('OptionalDims') is not None:
            for k in m.get('OptionalDims'):
                temp_model = QueryDatasetRequestOptionalDims()
                self.optional_dims.append(temp_model.from_map(k))
        return self


class QueryDatasetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class QueryDatasetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDatasetResponseBody = None,
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
            temp_model = QueryDatasetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMetricRequestFilters(TeaModel):
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


class QueryMetricRequest(TeaModel):
    def __init__(
        self,
        interval_in_sec: int = None,
        start_time: int = None,
        end_time: int = None,
        order_by: str = None,
        limit: int = None,
        metric: str = None,
        order: str = None,
        proxy_user_id: str = None,
        consistency_data_key: str = None,
        consistency_query_strategy: str = None,
        filters: List[QueryMetricRequestFilters] = None,
        dimensions: List[str] = None,
        measures: List[str] = None,
    ):
        self.interval_in_sec = interval_in_sec
        self.start_time = start_time
        self.end_time = end_time
        self.order_by = order_by
        self.limit = limit
        self.metric = metric
        self.order = order
        self.proxy_user_id = proxy_user_id
        self.consistency_data_key = consistency_data_key
        self.consistency_query_strategy = consistency_query_strategy
        self.filters = filters
        self.dimensions = dimensions
        self.measures = measures

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.order is not None:
            result['Order'] = self.order
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.consistency_data_key is not None:
            result['ConsistencyDataKey'] = self.consistency_data_key
        if self.consistency_query_strategy is not None:
            result['ConsistencyQueryStrategy'] = self.consistency_query_strategy
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.measures is not None:
            result['Measures'] = self.measures
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ConsistencyDataKey') is not None:
            self.consistency_data_key = m.get('ConsistencyDataKey')
        if m.get('ConsistencyQueryStrategy') is not None:
            self.consistency_query_strategy = m.get('ConsistencyQueryStrategy')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = QueryMetricRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        return self


class QueryMetricResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class QueryMetricResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMetricResponseBody = None,
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
            temp_model = QueryMetricResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMetricByPageRequestFilters(TeaModel):
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


class QueryMetricByPageRequest(TeaModel):
    def __init__(
        self,
        interval_in_sec: int = None,
        start_time: int = None,
        end_time: int = None,
        order_by: str = None,
        metric: str = None,
        order: str = None,
        proxy_user_id: str = None,
        consistency_data_key: str = None,
        consistency_query_strategy: str = None,
        current_page: int = None,
        page_size: int = None,
        filters: List[QueryMetricByPageRequestFilters] = None,
        dimensions: List[str] = None,
        measures: List[str] = None,
    ):
        self.interval_in_sec = interval_in_sec
        self.start_time = start_time
        self.end_time = end_time
        self.order_by = order_by
        self.metric = metric
        self.order = order
        self.proxy_user_id = proxy_user_id
        self.consistency_data_key = consistency_data_key
        self.consistency_query_strategy = consistency_query_strategy
        self.current_page = current_page
        self.page_size = page_size
        self.filters = filters
        self.dimensions = dimensions
        self.measures = measures

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.metric is not None:
            result['Metric'] = self.metric
        if self.order is not None:
            result['Order'] = self.order
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.consistency_data_key is not None:
            result['ConsistencyDataKey'] = self.consistency_data_key
        if self.consistency_query_strategy is not None:
            result['ConsistencyQueryStrategy'] = self.consistency_query_strategy
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.measures is not None:
            result['Measures'] = self.measures
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ConsistencyDataKey') is not None:
            self.consistency_data_key = m.get('ConsistencyDataKey')
        if m.get('ConsistencyQueryStrategy') is not None:
            self.consistency_query_strategy = m.get('ConsistencyQueryStrategy')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = QueryMetricByPageRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('Measures') is not None:
            self.measures = m.get('Measures')
        return self


class QueryMetricByPageResponseBodyData(TeaModel):
    def __init__(
        self,
        items: List[Dict[str, Any]] = None,
        page_size: int = None,
        total: int = None,
        page: int = None,
    ):
        self.items = items
        self.page_size = page_size
        self.total = total
        self.page = page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.items is not None:
            result['Items'] = self.items
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryMetricByPageResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: QueryMetricByPageResponseBodyData = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryMetricByPageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMetricByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMetricByPageResponseBody = None,
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
            temp_model = QueryMetricByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveTraceAppConfigRequestSettings(TeaModel):
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


class SaveTraceAppConfigRequest(TeaModel):
    def __init__(
        self,
        pid: str = None,
        settings: List[SaveTraceAppConfigRequestSettings] = None,
    ):
        self.pid = pid
        self.settings = settings

    def validate(self):
        if self.settings:
            for k in self.settings:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        result['Settings'] = []
        if self.settings is not None:
            for k in self.settings:
                result['Settings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        self.settings = []
        if m.get('Settings') is not None:
            for k in m.get('Settings'):
                temp_model = SaveTraceAppConfigRequestSettings()
                self.settings.append(temp_model.from_map(k))
        return self


class SaveTraceAppConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class SaveTraceAppConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveTraceAppConfigResponseBody = None,
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
            temp_model = SaveTraceAppConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertContactRequest(TeaModel):
    def __init__(
        self,
        contact_name: str = None,
        phone: str = None,
        email: str = None,
        current_page: str = None,
        page_size: str = None,
        region_id: str = None,
        proxy_user_id: str = None,
        contact_ids: str = None,
    ):
        self.contact_name = contact_name
        self.phone = phone
        self.email = email
        self.current_page = current_page
        self.page_size = page_size
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id
        self.contact_ids = contact_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.email is not None:
            result['Email'] = self.email
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        return self


class SearchAlertContactResponseBodyPageBeanContacts(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        ding_robot: str = None,
        webhook: str = None,
        email: str = None,
        contact_id: int = None,
        create_time: int = None,
        user_id: str = None,
        contact_name: str = None,
        system_noc: bool = None,
        phone: str = None,
    ):
        self.update_time = update_time
        self.ding_robot = ding_robot
        self.webhook = webhook
        self.email = email
        self.contact_id = contact_id
        self.create_time = create_time
        self.user_id = user_id
        self.contact_name = contact_name
        self.system_noc = system_noc
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.ding_robot is not None:
            result['DingRobot'] = self.ding_robot
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        if self.email is not None:
            result['Email'] = self.email
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('DingRobot') is not None:
            self.ding_robot = m.get('DingRobot')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class SearchAlertContactResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        contacts: List[SearchAlertContactResponseBodyPageBeanContacts] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.contacts = contacts
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = SearchAlertContactResponseBodyPageBeanContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAlertContactResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchAlertContactResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchAlertContactResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchAlertContactResponseBody = None,
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
            temp_model = SearchAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertContactGroupRequest(TeaModel):
    def __init__(
        self,
        contact_group_name: str = None,
        region_id: str = None,
        proxy_user_id: str = None,
        contact_name: str = None,
        contact_id: int = None,
        contact_group_ids: str = None,
        is_detail: bool = None,
    ):
        self.contact_group_name = contact_group_name
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id
        self.contact_name = contact_name
        self.contact_id = contact_id
        self.contact_group_ids = contact_group_ids
        self.is_detail = is_detail

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.is_detail is not None:
            result['IsDetail'] = self.is_detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('IsDetail') is not None:
            self.is_detail = m.get('IsDetail')
        return self


class SearchAlertContactGroupResponseBodyContactGroupsContacts(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        ding_robot: str = None,
        email: str = None,
        contact_id: int = None,
        create_time: int = None,
        user_id: str = None,
        contact_name: str = None,
        system_noc: bool = None,
        phone: str = None,
    ):
        self.update_time = update_time
        self.ding_robot = ding_robot
        self.email = email
        self.contact_id = contact_id
        self.create_time = create_time
        self.user_id = user_id
        self.contact_name = contact_name
        self.system_noc = system_noc
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.ding_robot is not None:
            result['DingRobot'] = self.ding_robot
        if self.email is not None:
            result['Email'] = self.email
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('DingRobot') is not None:
            self.ding_robot = m.get('DingRobot')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class SearchAlertContactGroupResponseBodyContactGroups(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        contact_group_name: str = None,
        contacts: List[SearchAlertContactGroupResponseBodyContactGroupsContacts] = None,
        contact_group_id: int = None,
        create_time: int = None,
        user_id: str = None,
    ):
        self.update_time = update_time
        self.contact_group_name = contact_group_name
        self.contacts = contacts
        self.contact_group_id = contact_group_id
        self.create_time = create_time
        self.user_id = user_id

    def validate(self):
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = SearchAlertContactGroupResponseBodyContactGroupsContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class SearchAlertContactGroupResponseBody(TeaModel):
    def __init__(
        self,
        contact_groups: List[SearchAlertContactGroupResponseBodyContactGroups] = None,
        request_id: str = None,
    ):
        self.contact_groups = contact_groups
        self.request_id = request_id

    def validate(self):
        if self.contact_groups:
            for k in self.contact_groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ContactGroups'] = []
        if self.contact_groups is not None:
            for k in self.contact_groups:
                result['ContactGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_groups = []
        if m.get('ContactGroups') is not None:
            for k in m.get('ContactGroups'):
                temp_model = SearchAlertContactGroupResponseBodyContactGroups()
                self.contact_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertContactGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchAlertContactGroupResponseBody = None,
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
            temp_model = SearchAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertHistoriesRequest(TeaModel):
    def __init__(
        self,
        proxy_user_id: str = None,
        alert_id: int = None,
        alert_type: int = None,
        current_page: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.proxy_user_id = proxy_user_id
        self.alert_id = alert_id
        self.alert_type = alert_type
        self.current_page = current_page
        self.page_size = page_size
        self.region_id = region_id
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class SearchAlertHistoriesResponseBodyPageBeanAlarmHistories(TeaModel):
    def __init__(
        self,
        alarm_time: int = None,
        strategy_id: str = None,
        alarm_response_code: int = None,
        emails: str = None,
        user_id: str = None,
        alarm_sources: str = None,
        alarm_content: str = None,
        phones: str = None,
        alarm_type: int = None,
        target: str = None,
        id: int = None,
    ):
        self.alarm_time = alarm_time
        self.strategy_id = strategy_id
        self.alarm_response_code = alarm_response_code
        self.emails = emails
        self.user_id = user_id
        self.alarm_sources = alarm_sources
        self.alarm_content = alarm_content
        self.phones = phones
        self.alarm_type = alarm_type
        self.target = target
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.alarm_response_code is not None:
            result['AlarmResponseCode'] = self.alarm_response_code
        if self.emails is not None:
            result['Emails'] = self.emails
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.alarm_sources is not None:
            result['AlarmSources'] = self.alarm_sources
        if self.alarm_content is not None:
            result['AlarmContent'] = self.alarm_content
        if self.phones is not None:
            result['Phones'] = self.phones
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.target is not None:
            result['Target'] = self.target
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('AlarmResponseCode') is not None:
            self.alarm_response_code = m.get('AlarmResponseCode')
        if m.get('Emails') is not None:
            self.emails = m.get('Emails')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('AlarmSources') is not None:
            self.alarm_sources = m.get('AlarmSources')
        if m.get('AlarmContent') is not None:
            self.alarm_content = m.get('AlarmContent')
        if m.get('Phones') is not None:
            self.phones = m.get('Phones')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class SearchAlertHistoriesResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        alarm_histories: List[SearchAlertHistoriesResponseBodyPageBeanAlarmHistories] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.alarm_histories = alarm_histories
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.alarm_histories:
            for k in self.alarm_histories:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AlarmHistories'] = []
        if self.alarm_histories is not None:
            for k in self.alarm_histories:
                result['AlarmHistories'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_histories = []
        if m.get('AlarmHistories') is not None:
            for k in m.get('AlarmHistories'):
                temp_model = SearchAlertHistoriesResponseBodyPageBeanAlarmHistories()
                self.alarm_histories.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAlertHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchAlertHistoriesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchAlertHistoriesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchAlertHistoriesResponseBody = None,
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
            temp_model = SearchAlertHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAlertRulesRequest(TeaModel):
    def __init__(
        self,
        proxy_user_id: str = None,
        title: str = None,
        type: str = None,
        current_page: int = None,
        page_size: int = None,
        region_id: str = None,
        pid: str = None,
        app_type: str = None,
    ):
        self.proxy_user_id = proxy_user_id
        self.title = title
        self.type = type
        self.current_page = current_page
        self.page_size = page_size
        self.region_id = region_id
        self.pid = pid
        self.app_type = app_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext(TeaModel):
    def __init__(
        self,
        alarm_content_sub_title: str = None,
        alarm_content_template: str = None,
        sub_title: str = None,
        content: str = None,
    ):
        self.alarm_content_sub_title = alarm_content_sub_title
        self.alarm_content_template = alarm_content_template
        self.sub_title = sub_title
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alarm_content_sub_title is not None:
            result['AlarmContentSubTitle'] = self.alarm_content_sub_title
        if self.alarm_content_template is not None:
            result['AlarmContentTemplate'] = self.alarm_content_template
        if self.sub_title is not None:
            result['SubTitle'] = self.sub_title
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmContentSubTitle') is not None:
            self.alarm_content_sub_title = m.get('AlarmContentSubTitle')
        if m.get('AlarmContentTemplate') is not None:
            self.alarm_content_template = m.get('AlarmContentTemplate')
        if m.get('SubTitle') is not None:
            self.sub_title = m.get('SubTitle')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesNotice(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        notice_end_time: int = None,
        start_time: int = None,
        notice_start_time: int = None,
    ):
        self.end_time = end_time
        self.notice_end_time = notice_end_time
        self.start_time = start_time
        self.notice_start_time = notice_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.notice_end_time is not None:
            result['NoticeEndTime'] = self.notice_end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.notice_start_time is not None:
            result['NoticeStartTime'] = self.notice_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NoticeEndTime') is not None:
            self.notice_end_time = m.get('NoticeEndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('NoticeStartTime') is not None:
            self.notice_start_time = m.get('NoticeStartTime')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules(TeaModel):
    def __init__(
        self,
        measure: str = None,
        value: float = None,
        aggregates: str = None,
        nvalue: int = None,
        operator: str = None,
        alias: str = None,
    ):
        self.measure = measure
        self.value = value
        self.aggregates = aggregates
        self.nvalue = nvalue
        self.operator = operator
        self.alias = alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.measure is not None:
            result['Measure'] = self.measure
        if self.value is not None:
            result['Value'] = self.value
        if self.aggregates is not None:
            result['Aggregates'] = self.aggregates
        if self.nvalue is not None:
            result['NValue'] = self.nvalue
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.alias is not None:
            result['Alias'] = self.alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Measure') is not None:
            self.measure = m.get('Measure')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Aggregates') is not None:
            self.aggregates = m.get('Aggregates')
        if m.get('NValue') is not None:
            self.nvalue = m.get('NValue')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule(TeaModel):
    def __init__(
        self,
        operator: str = None,
        rules: List[SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules] = None,
    ):
        self.operator = operator
        self.rules = rules

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.operator is not None:
            result['Operator'] = self.operator
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRuleRules()
                self.rules.append(temp_model.from_map(k))
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions(TeaModel):
    def __init__(
        self,
        key: str = None,
        type: str = None,
        value: str = None,
    ):
        self.key = key
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam(TeaModel):
    def __init__(
        self,
        type: str = None,
        app_group_id: str = None,
        app_id: str = None,
        pid: str = None,
        dimensions: List[SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions] = None,
    ):
        self.type = type
        self.app_group_id = app_group_id
        self.app_id = app_id
        self.pid = pid
        self.dimensions = dimensions

    def validate(self):
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.app_group_id is not None:
            result['AppGroupId'] = self.app_group_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.pid is not None:
            result['Pid'] = self.pid
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AppGroupId') is not None:
            self.app_group_id = m.get('AppGroupId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParamDimensions()
                self.dimensions.append(temp_model.from_map(k))
        return self


class SearchAlertRulesResponseBodyPageBeanAlertRules(TeaModel):
    def __init__(
        self,
        status: str = None,
        alarm_context: SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext = None,
        update_time: int = None,
        contact_group_id_list: str = None,
        notice: SearchAlertRulesResponseBodyPageBeanAlertRulesNotice = None,
        create_time: int = None,
        alert_title: str = None,
        user_id: str = None,
        alert_version: int = None,
        alert_rule: SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule = None,
        metric_param: SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam = None,
        alert_type: int = None,
        contact_group_ids: str = None,
        config: str = None,
        region_id: str = None,
        alert_level: str = None,
        alert_way: List[str] = None,
        task_status: str = None,
        title: str = None,
        task_id: int = None,
        id: int = None,
        alert_ways: List[str] = None,
    ):
        self.status = status
        self.alarm_context = alarm_context
        self.update_time = update_time
        self.contact_group_id_list = contact_group_id_list
        self.notice = notice
        self.create_time = create_time
        self.alert_title = alert_title
        self.user_id = user_id
        self.alert_version = alert_version
        self.alert_rule = alert_rule
        self.metric_param = metric_param
        self.alert_type = alert_type
        self.contact_group_ids = contact_group_ids
        self.config = config
        self.region_id = region_id
        self.alert_level = alert_level
        self.alert_way = alert_way
        self.task_status = task_status
        self.title = title
        self.task_id = task_id
        self.id = id
        self.alert_ways = alert_ways

    def validate(self):
        if self.alarm_context:
            self.alarm_context.validate()
        if self.notice:
            self.notice.validate()
        if self.alert_rule:
            self.alert_rule.validate()
        if self.metric_param:
            self.metric_param.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.alarm_context is not None:
            result['AlarmContext'] = self.alarm_context.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.contact_group_id_list is not None:
            result['ContactGroupIdList'] = self.contact_group_id_list
        if self.notice is not None:
            result['Notice'] = self.notice.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.alert_title is not None:
            result['AlertTitle'] = self.alert_title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.alert_version is not None:
            result['AlertVersion'] = self.alert_version
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule.to_map()
        if self.metric_param is not None:
            result['MetricParam'] = self.metric_param.to_map()
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.config is not None:
            result['Config'] = self.config
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level
        if self.alert_way is not None:
            result['AlertWay'] = self.alert_way
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.title is not None:
            result['Title'] = self.title
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.id is not None:
            result['Id'] = self.id
        if self.alert_ways is not None:
            result['AlertWays'] = self.alert_ways
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AlarmContext') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesAlarmContext()
            self.alarm_context = temp_model.from_map(m['AlarmContext'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ContactGroupIdList') is not None:
            self.contact_group_id_list = m.get('ContactGroupIdList')
        if m.get('Notice') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesNotice()
            self.notice = temp_model.from_map(m['Notice'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AlertTitle') is not None:
            self.alert_title = m.get('AlertTitle')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('AlertVersion') is not None:
            self.alert_version = m.get('AlertVersion')
        if m.get('AlertRule') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesAlertRule()
            self.alert_rule = temp_model.from_map(m['AlertRule'])
        if m.get('MetricParam') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBeanAlertRulesMetricParam()
            self.metric_param = temp_model.from_map(m['MetricParam'])
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')
        if m.get('AlertWay') is not None:
            self.alert_way = m.get('AlertWay')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('AlertWays') is not None:
            self.alert_ways = m.get('AlertWays')
        return self


class SearchAlertRulesResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        alert_rules: List[SearchAlertRulesResponseBodyPageBeanAlertRules] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.alert_rules = alert_rules
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.alert_rules:
            for k in self.alert_rules:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AlertRules'] = []
        if self.alert_rules is not None:
            for k in self.alert_rules:
                result['AlertRules'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_rules = []
        if m.get('AlertRules') is not None:
            for k in m.get('AlertRules'):
                temp_model = SearchAlertRulesResponseBodyPageBeanAlertRules()
                self.alert_rules.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchAlertRulesResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchAlertRulesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchAlertRulesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchAlertRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchAlertRulesResponseBody = None,
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
            temp_model = SearchAlertRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchEventsRequest(TeaModel):
    def __init__(
        self,
        proxy_user_id: str = None,
        alert_id: int = None,
        pid: str = None,
        current_page: int = None,
        page_size: int = None,
        region_id: str = None,
        app_type: str = None,
        alert_type: int = None,
        is_trigger: int = None,
        start_time: int = None,
        end_time: int = None,
    ):
        self.proxy_user_id = proxy_user_id
        self.alert_id = alert_id
        self.pid = pid
        self.current_page = current_page
        self.page_size = page_size
        self.region_id = region_id
        self.app_type = app_type
        self.alert_type = alert_type
        self.is_trigger = is_trigger
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.is_trigger is not None:
            result['IsTrigger'] = self.is_trigger
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('IsTrigger') is not None:
            self.is_trigger = m.get('IsTrigger')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class SearchEventsResponseBodyPageBeanEvent(TeaModel):
    def __init__(
        self,
        event_time: int = None,
        links: List[str] = None,
        event_level: str = None,
        alert_rule: str = None,
        message: str = None,
        alert_type: int = None,
        alert_name: str = None,
        id: int = None,
        alert_id: int = None,
    ):
        self.event_time = event_time
        self.links = links
        self.event_level = event_level
        self.alert_rule = alert_rule
        self.message = message
        self.alert_type = alert_type
        self.alert_name = alert_name
        self.id = id
        self.alert_id = alert_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.links is not None:
            result['Links'] = self.links
        if self.event_level is not None:
            result['EventLevel'] = self.event_level
        if self.alert_rule is not None:
            result['AlertRule'] = self.alert_rule
        if self.message is not None:
            result['Message'] = self.message
        if self.alert_type is not None:
            result['AlertType'] = self.alert_type
        if self.alert_name is not None:
            result['AlertName'] = self.alert_name
        if self.id is not None:
            result['Id'] = self.id
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('Links') is not None:
            self.links = m.get('Links')
        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')
        if m.get('AlertRule') is not None:
            self.alert_rule = m.get('AlertRule')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('AlertType') is not None:
            self.alert_type = m.get('AlertType')
        if m.get('AlertName') is not None:
            self.alert_name = m.get('AlertName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        return self


class SearchEventsResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        event: List[SearchEventsResponseBodyPageBeanEvent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.event = event
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.event:
            for k in self.event:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Event'] = []
        if self.event is not None:
            for k in self.event:
                result['Event'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event = []
        if m.get('Event') is not None:
            for k in m.get('Event'):
                temp_model = SearchEventsResponseBodyPageBeanEvent()
                self.event.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SearchEventsResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchEventsResponseBodyPageBean = None,
        request_id: str = None,
        is_trigger: int = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id
        self.is_trigger = is_trigger

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_trigger is not None:
            result['IsTrigger'] = self.is_trigger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchEventsResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsTrigger') is not None:
            self.is_trigger = m.get('IsTrigger')
        return self


class SearchEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchEventsResponseBody = None,
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
            temp_model = SearchEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchRetcodeAppByPageRequest(TeaModel):
    def __init__(
        self,
        retcode_app_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.retcode_app_name = retcode_app_name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.retcode_app_name is not None:
            result['RetcodeAppName'] = self.retcode_app_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetcodeAppName') is not None:
            self.retcode_app_name = m.get('RetcodeAppName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps(TeaModel):
    def __init__(
        self,
        type: str = None,
        app_name: str = None,
        update_time: int = None,
        create_time: int = None,
        app_id: int = None,
        pid: str = None,
        user_id: str = None,
        region_id: str = None,
    ):
        self.type = type
        self.app_name = app_name
        self.update_time = update_time
        self.create_time = create_time
        self.app_id = app_id
        self.pid = pid
        self.user_id = user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchRetcodeAppByPageResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        retcode_apps: List[SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.retcode_apps = retcode_apps

    def validate(self):
        if self.retcode_apps:
            for k in self.retcode_apps:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['RetcodeApps'] = []
        if self.retcode_apps is not None:
            for k in self.retcode_apps:
                result['RetcodeApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.retcode_apps = []
        if m.get('RetcodeApps') is not None:
            for k in m.get('RetcodeApps'):
                temp_model = SearchRetcodeAppByPageResponseBodyPageBeanRetcodeApps()
                self.retcode_apps.append(temp_model.from_map(k))
        return self


class SearchRetcodeAppByPageResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchRetcodeAppByPageResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchRetcodeAppByPageResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchRetcodeAppByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchRetcodeAppByPageResponseBody = None,
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
            temp_model = SearchRetcodeAppByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTraceAppByNameRequest(TeaModel):
    def __init__(
        self,
        trace_app_name: str = None,
        region_id: str = None,
    ):
        self.trace_app_name = trace_app_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.trace_app_name is not None:
            result['TraceAppName'] = self.trace_app_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TraceAppName') is not None:
            self.trace_app_name = m.get('TraceAppName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchTraceAppByNameResponseBodyTraceApps(TeaModel):
    def __init__(
        self,
        type: str = None,
        app_name: str = None,
        update_time: int = None,
        labels: List[str] = None,
        show: bool = None,
        create_time: int = None,
        pid: str = None,
        app_id: int = None,
        user_id: str = None,
        region_id: str = None,
    ):
        self.type = type
        self.app_name = app_name
        self.update_time = update_time
        self.labels = labels
        self.show = show
        self.create_time = create_time
        self.pid = pid
        self.app_id = app_id
        self.user_id = user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.show is not None:
            result['Show'] = self.show
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchTraceAppByNameResponseBody(TeaModel):
    def __init__(
        self,
        trace_apps: List[SearchTraceAppByNameResponseBodyTraceApps] = None,
        request_id: str = None,
    ):
        self.trace_apps = trace_apps
        self.request_id = request_id

    def validate(self):
        if self.trace_apps:
            for k in self.trace_apps:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TraceApps'] = []
        if self.trace_apps is not None:
            for k in self.trace_apps:
                result['TraceApps'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trace_apps = []
        if m.get('TraceApps') is not None:
            for k in m.get('TraceApps'):
                temp_model = SearchTraceAppByNameResponseBodyTraceApps()
                self.trace_apps.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchTraceAppByNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchTraceAppByNameResponseBody = None,
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
            temp_model = SearchTraceAppByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTraceAppByPageRequest(TeaModel):
    def __init__(
        self,
        trace_app_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.trace_app_name = trace_app_name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.trace_app_name is not None:
            result['TraceAppName'] = self.trace_app_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TraceAppName') is not None:
            self.trace_app_name = m.get('TraceAppName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchTraceAppByPageResponseBodyPageBeanTraceApps(TeaModel):
    def __init__(
        self,
        type: str = None,
        app_name: str = None,
        update_time: int = None,
        labels: List[str] = None,
        show: bool = None,
        create_time: int = None,
        pid: str = None,
        app_id: int = None,
        user_id: str = None,
        region_id: str = None,
    ):
        self.type = type
        self.app_name = app_name
        self.update_time = update_time
        self.labels = labels
        self.show = show
        self.create_time = create_time
        self.pid = pid
        self.app_id = app_id
        self.user_id = user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.show is not None:
            result['Show'] = self.show
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchTraceAppByPageResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        trace_apps: List[SearchTraceAppByPageResponseBodyPageBeanTraceApps] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.trace_apps = trace_apps

    def validate(self):
        if self.trace_apps:
            for k in self.trace_apps:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['TraceApps'] = []
        if self.trace_apps is not None:
            for k in self.trace_apps:
                result['TraceApps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.trace_apps = []
        if m.get('TraceApps') is not None:
            for k in m.get('TraceApps'):
                temp_model = SearchTraceAppByPageResponseBodyPageBeanTraceApps()
                self.trace_apps.append(temp_model.from_map(k))
        return self


class SearchTraceAppByPageResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchTraceAppByPageResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchTraceAppByPageResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchTraceAppByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchTraceAppByPageResponseBody = None,
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
            temp_model = SearchTraceAppByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTracesRequestTag(TeaModel):
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


class SearchTracesRequestExclusionFilters(TeaModel):
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


class SearchTracesRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        region_id: str = None,
        service_name: str = None,
        operation_name: str = None,
        min_duration: int = None,
        reverse: bool = None,
        service_ip: str = None,
        tag: List[SearchTracesRequestTag] = None,
        exclusion_filters: List[SearchTracesRequestExclusionFilters] = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.region_id = region_id
        self.service_name = service_name
        self.operation_name = operation_name
        self.min_duration = min_duration
        self.reverse = reverse
        self.service_ip = service_ip
        self.tag = tag
        self.exclusion_filters = exclusion_filters

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.exclusion_filters:
            for k in self.exclusion_filters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        result['ExclusionFilters'] = []
        if self.exclusion_filters is not None:
            for k in self.exclusion_filters:
                result['ExclusionFilters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = SearchTracesRequestTag()
                self.tag.append(temp_model.from_map(k))
        self.exclusion_filters = []
        if m.get('ExclusionFilters') is not None:
            for k in m.get('ExclusionFilters'):
                temp_model = SearchTracesRequestExclusionFilters()
                self.exclusion_filters.append(temp_model.from_map(k))
        return self


class SearchTracesResponseBodyTraceInfos(TeaModel):
    def __init__(
        self,
        operation_name: str = None,
        service_ip: str = None,
        duration: int = None,
        timestamp: int = None,
        service_name: str = None,
        trace_id: str = None,
    ):
        self.operation_name = operation_name
        self.service_ip = service_ip
        self.duration = duration
        self.timestamp = timestamp
        self.service_name = service_name
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class SearchTracesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trace_infos: List[SearchTracesResponseBodyTraceInfos] = None,
    ):
        self.request_id = request_id
        self.trace_infos = trace_infos

    def validate(self):
        if self.trace_infos:
            for k in self.trace_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TraceInfos'] = []
        if self.trace_infos is not None:
            for k in self.trace_infos:
                result['TraceInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.trace_infos = []
        if m.get('TraceInfos') is not None:
            for k in m.get('TraceInfos'):
                temp_model = SearchTracesResponseBodyTraceInfos()
                self.trace_infos.append(temp_model.from_map(k))
        return self


class SearchTracesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchTracesResponseBody = None,
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
            temp_model = SearchTracesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchTracesByPageRequestExclusionFilters(TeaModel):
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


class SearchTracesByPageRequest(TeaModel):
    def __init__(
        self,
        start_time: int = None,
        end_time: int = None,
        region_id: str = None,
        service_name: str = None,
        operation_name: str = None,
        min_duration: int = None,
        reverse: bool = None,
        service_ip: str = None,
        page_number: int = None,
        page_size: int = None,
        exclusion_filters: List[SearchTracesByPageRequestExclusionFilters] = None,
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.region_id = region_id
        self.service_name = service_name
        self.operation_name = operation_name
        self.min_duration = min_duration
        self.reverse = reverse
        self.service_ip = service_ip
        self.page_number = page_number
        self.page_size = page_size
        self.exclusion_filters = exclusion_filters

    def validate(self):
        if self.exclusion_filters:
            for k in self.exclusion_filters:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.min_duration is not None:
            result['MinDuration'] = self.min_duration
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['ExclusionFilters'] = []
        if self.exclusion_filters is not None:
            for k in self.exclusion_filters:
                result['ExclusionFilters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('MinDuration') is not None:
            self.min_duration = m.get('MinDuration')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.exclusion_filters = []
        if m.get('ExclusionFilters') is not None:
            for k in m.get('ExclusionFilters'):
                temp_model = SearchTracesByPageRequestExclusionFilters()
                self.exclusion_filters.append(temp_model.from_map(k))
        return self


class SearchTracesByPageResponseBodyPageBeanTraceInfos(TeaModel):
    def __init__(
        self,
        operation_name: str = None,
        service_ip: str = None,
        duration: int = None,
        timestamp: int = None,
        service_name: str = None,
        trace_id: str = None,
    ):
        self.operation_name = operation_name
        self.service_ip = service_ip
        self.duration = duration
        self.timestamp = timestamp
        self.service_name = service_name
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.service_ip is not None:
            result['ServiceIp'] = self.service_ip
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.trace_id is not None:
            result['TraceID'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('ServiceIp') is not None:
            self.service_ip = m.get('ServiceIp')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('TraceID') is not None:
            self.trace_id = m.get('TraceID')
        return self


class SearchTracesByPageResponseBodyPageBean(TeaModel):
    def __init__(
        self,
        trace_infos: List[SearchTracesByPageResponseBodyPageBeanTraceInfos] = None,
        page_number: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.trace_infos = trace_infos
        self.page_number = page_number
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.trace_infos:
            for k in self.trace_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TraceInfos'] = []
        if self.trace_infos is not None:
            for k in self.trace_infos:
                result['TraceInfos'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trace_infos = []
        if m.get('TraceInfos') is not None:
            for k in m.get('TraceInfos'):
                temp_model = SearchTracesByPageResponseBodyPageBeanTraceInfos()
                self.trace_infos.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class SearchTracesByPageResponseBody(TeaModel):
    def __init__(
        self,
        page_bean: SearchTracesByPageResponseBodyPageBean = None,
        request_id: str = None,
    ):
        self.page_bean = page_bean
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = SearchTracesByPageResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m['PageBean'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SearchTracesByPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SearchTracesByPageResponseBody = None,
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
            temp_model = SearchTracesByPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCustomIncidentsRequest(TeaModel):
    def __init__(
        self,
        incidents: str = None,
        region_id: str = None,
        proxy_user_id: str = None,
        product_type: str = None,
    ):
        self.incidents = incidents
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.incidents is not None:
            result['Incidents'] = self.incidents
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Incidents') is not None:
            self.incidents = m.get('Incidents')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class SendCustomIncidentsResponseBody(TeaModel):
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


class SendCustomIncidentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendCustomIncidentsResponseBody = None,
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
            temp_model = SendCustomIncidentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMseIncidentRequest(TeaModel):
    def __init__(
        self,
        incidents: str = None,
        region_id: str = None,
        proxy_user_id: str = None,
    ):
        self.incidents = incidents
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.incidents is not None:
            result['Incidents'] = self.incidents
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Incidents') is not None:
            self.incidents = m.get('Incidents')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        return self


class SendMseIncidentResponseBody(TeaModel):
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


class SendMseIncidentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendMseIncidentResponseBody = None,
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
            temp_model = SendMseIncidentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRetcodeShareStatusRequest(TeaModel):
    def __init__(
        self,
        pid: str = None,
        status: bool = None,
    ):
        self.pid = pid
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class SetRetcodeShareStatusResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetRetcodeShareStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetRetcodeShareStatusResponseBody = None,
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
            temp_model = SetRetcodeShareStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAlertRequest(TeaModel):
    def __init__(
        self,
        alert_id: str = None,
        proxy_user_id: str = None,
        region_id: str = None,
    ):
        self.alert_id = alert_id
        self.proxy_user_id = proxy_user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartAlertResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartAlertResponseBody = None,
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
            temp_model = StartAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAlertRequest(TeaModel):
    def __init__(
        self,
        alert_id: str = None,
        proxy_user_id: str = None,
        region_id: str = None,
    ):
        self.alert_id = alert_id
        self.proxy_user_id = proxy_user_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopAlertResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopAlertResponseBody = None,
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
            temp_model = StopAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlertContactRequest(TeaModel):
    def __init__(
        self,
        contact_name: str = None,
        phone_num: str = None,
        email: str = None,
        ding_robot_webhook_url: str = None,
        system_noc: bool = None,
        region_id: str = None,
        proxy_user_id: str = None,
        contact_id: int = None,
    ):
        self.contact_name = contact_name
        self.phone_num = phone_num
        self.email = email
        self.ding_robot_webhook_url = ding_robot_webhook_url
        self.system_noc = system_noc
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id
        self.contact_id = contact_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        if self.email is not None:
            result['Email'] = self.email
        if self.ding_robot_webhook_url is not None:
            result['DingRobotWebhookUrl'] = self.ding_robot_webhook_url
        if self.system_noc is not None:
            result['SystemNoc'] = self.system_noc
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('DingRobotWebhookUrl') is not None:
            self.ding_robot_webhook_url = m.get('DingRobotWebhookUrl')
        if m.get('SystemNoc') is not None:
            self.system_noc = m.get('SystemNoc')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        return self


class UpdateAlertContactResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAlertContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAlertContactResponseBody = None,
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
            temp_model = UpdateAlertContactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlertContactGroupRequest(TeaModel):
    def __init__(
        self,
        contact_group_name: str = None,
        contact_ids: str = None,
        region_id: str = None,
        proxy_user_id: str = None,
        contact_group_id: int = None,
    ):
        self.contact_group_name = contact_group_name
        self.contact_ids = contact_ids
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id
        self.contact_group_id = contact_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.contact_group_name is not None:
            result['ContactGroupName'] = self.contact_group_name
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.contact_group_id is not None:
            result['ContactGroupId'] = self.contact_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactGroupName') is not None:
            self.contact_group_name = m.get('ContactGroupName')
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ContactGroupId') is not None:
            self.contact_group_id = m.get('ContactGroupId')
        return self


class UpdateAlertContactGroupResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAlertContactGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAlertContactGroupResponseBody = None,
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
            temp_model = UpdateAlertContactGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlertRuleRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        contact_group_ids: str = None,
        is_auto_start: bool = None,
        templage_alert_config: str = None,
        proxy_user_id: str = None,
        alert_id: int = None,
    ):
        self.region_id = region_id
        self.contact_group_ids = contact_group_ids
        self.is_auto_start = is_auto_start
        self.templage_alert_config = templage_alert_config
        self.proxy_user_id = proxy_user_id
        self.alert_id = alert_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.contact_group_ids is not None:
            result['ContactGroupIds'] = self.contact_group_ids
        if self.is_auto_start is not None:
            result['IsAutoStart'] = self.is_auto_start
        if self.templage_alert_config is not None:
            result['TemplageAlertConfig'] = self.templage_alert_config
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ContactGroupIds') is not None:
            self.contact_group_ids = m.get('ContactGroupIds')
        if m.get('IsAutoStart') is not None:
            self.is_auto_start = m.get('IsAutoStart')
        if m.get('TemplageAlertConfig') is not None:
            self.templage_alert_config = m.get('TemplageAlertConfig')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        return self


class UpdateAlertRuleResponseBody(TeaModel):
    def __init__(
        self,
        alert_id: int = None,
        request_id: str = None,
        data: str = None,
    ):
        self.alert_id = alert_id
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.alert_id is not None:
            result['AlertId'] = self.alert_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertId') is not None:
            self.alert_id = m.get('AlertId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class UpdateAlertRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAlertRuleResponseBody = None,
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
            temp_model = UpdateAlertRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWebhookRequest(TeaModel):
    def __init__(
        self,
        contact_name: str = None,
        method: str = None,
        url: str = None,
        http_params: str = None,
        http_headers: str = None,
        region_id: str = None,
        proxy_user_id: str = None,
        contact_id: int = None,
        body: str = None,
    ):
        self.contact_name = contact_name
        self.method = method
        self.url = url
        self.http_params = http_params
        self.http_headers = http_headers
        self.region_id = region_id
        self.proxy_user_id = proxy_user_id
        self.contact_id = contact_id
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.method is not None:
            result['Method'] = self.method
        if self.url is not None:
            result['Url'] = self.url
        if self.http_params is not None:
            result['HttpParams'] = self.http_params
        if self.http_headers is not None:
            result['HttpHeaders'] = self.http_headers
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.proxy_user_id is not None:
            result['ProxyUserId'] = self.proxy_user_id
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.body is not None:
            result['Body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Method') is not None:
            self.method = m.get('Method')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('HttpParams') is not None:
            self.http_params = m.get('HttpParams')
        if m.get('HttpHeaders') is not None:
            self.http_headers = m.get('HttpHeaders')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProxyUserId') is not None:
            self.proxy_user_id = m.get('ProxyUserId')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        return self


class UpdateWebhookResponseBody(TeaModel):
    def __init__(
        self,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWebhookResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateWebhookResponseBody = None,
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
            temp_model = UpdateWebhookResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


