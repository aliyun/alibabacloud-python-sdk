# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class CreateCloudGtmAddressRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address: str = None,
        attribute_info: str = None,
        available_mode: str = None,
        client_token: str = None,
        enable_status: str = None,
        health_judgement: str = None,
        health_tasks: List[main_models.CreateCloudGtmAddressRequestHealthTasks] = None,
        manual_available_status: str = None,
        name: str = None,
        remark: str = None,
        type: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh-CN: Chinese.
        # 
        # - en-US (default): English.
        self.accept_language = accept_language
        # The IP address or domain name.
        # 
        # This parameter is required.
        self.address = address
        # The attribution information of the address.
        self.attribute_info = attribute_info
        # The switchover mode for the address when a health check is abnormal. Valid values:
        # 
        # - auto: The system automatically manages the address status based on health check results. If an address is unhealthy, DNS resolution for it stops. If the address becomes healthy, DNS resolution resumes.
        # 
        # - manual: You manually manage the address status. If you set an address to abnormal, DNS resolution for it stops. It does not resume even if the address becomes healthy. If you set an address to normal, DNS resolution for it resumes. If a healthy address becomes unhealthy, the system sends an alert but does not stop DNS resolution.
        # 
        # This parameter is required.
        self.available_mode = available_mode
        # The client token that is used to ensure the idempotence of the request. Make sure that the token is unique for each request. The token can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The status of the address. Valid values:
        # 
        # - enable: The address is enabled.
        # 
        # - disable: The address is disabled.
        # 
        # This parameter is required.
        self.enable_status = enable_status
        # The condition for determining the health of the address. This parameter is required if you specify HealthTasks. Valid values:
        # 
        # - any_ok: At least one health check is successful.
        # 
        # - p30_ok: At least 30% of health checks are successful.
        # 
        # - p50_ok: At least 50% of health checks are successful.
        # 
        # - p70_ok: At least 70% of health checks are successful.
        # 
        # - all_ok: All health checks are successful.
        # 
        # This parameter is required.
        self.health_judgement = health_judgement
        # The health check tasks for the address.
        self.health_tasks = health_tasks
        # The availability status of the address when the health check-based switchover mode is set to **manual**. Valid values:
        # 
        # - available: The address is available. In this state, DNS resolution for the address is normal. If a health check is abnormal, the system only sends an alert and does not stop DNS resolution.
        # 
        # - unavailable: The address is unavailable. In this state, DNS resolution for the address is stopped. DNS resolution is not resumed even if a health check is normal.
        self.manual_available_status = manual_available_status
        # The name of the address.
        # 
        # This parameter is required.
        self.name = name
        # The remarks about the address.
        self.remark = remark
        # The type of the address. Valid values:
        # 
        # - IPv4
        # 
        # - IPv6
        # 
        # - domain
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.health_tasks:
            for v1 in self.health_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.address is not None:
            result['Address'] = self.address

        if self.attribute_info is not None:
            result['AttributeInfo'] = self.attribute_info

        if self.available_mode is not None:
            result['AvailableMode'] = self.available_mode

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.health_judgement is not None:
            result['HealthJudgement'] = self.health_judgement

        result['HealthTasks'] = []
        if self.health_tasks is not None:
            for k1 in self.health_tasks:
                result['HealthTasks'].append(k1.to_map() if k1 else None)

        if self.manual_available_status is not None:
            result['ManualAvailableStatus'] = self.manual_available_status

        if self.name is not None:
            result['Name'] = self.name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AttributeInfo') is not None:
            self.attribute_info = m.get('AttributeInfo')

        if m.get('AvailableMode') is not None:
            self.available_mode = m.get('AvailableMode')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('HealthJudgement') is not None:
            self.health_judgement = m.get('HealthJudgement')

        self.health_tasks = []
        if m.get('HealthTasks') is not None:
            for k1 in m.get('HealthTasks'):
                temp_model = main_models.CreateCloudGtmAddressRequestHealthTasks()
                self.health_tasks.append(temp_model.from_map(k1))

        if m.get('ManualAvailableStatus') is not None:
            self.manual_available_status = m.get('ManualAvailableStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateCloudGtmAddressRequestHealthTasks(DaraModel):
    def __init__(
        self,
        port: int = None,
        template_id: str = None,
    ):
        # The service port of the destination address for the health check. This parameter is not supported for health checks that use the ping protocol.
        self.port = port
        # The ID of the health check template.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

