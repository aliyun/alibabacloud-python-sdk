# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudGtmAddressShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address: str = None,
        attribute_info: str = None,
        available_mode: str = None,
        client_token: str = None,
        enable_status: str = None,
        health_judgement: str = None,
        health_tasks_shrink: str = None,
        manual_available_status: str = None,
        name: str = None,
        remark: str = None,
        type: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US (default): English
        self.accept_language = accept_language
        # IP address or domain name.
        # 
        # This parameter is required.
        self.address = address
        # Address ownership information.
        self.attribute_info = attribute_info
        # The failover mode that is used when address exceptions are identified. Valid values:
        # 
        # *   auto: the automatic mode. The system determines whether to return an address based on the health check results. If the address fails health checks, the system does not return the address. If the address passes health checks, the system returns the address.
        # *   manual: the manual mode. If an address is in the unavailable state, the address is not returned for DNS requests even if the address passes health checks. If an address is in the available state, the address is returned for DNS requests even if an alert is triggered when the address fails health checks.
        # 
        # This parameter is required.
        self.available_mode = available_mode
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Indicates the current enabled status of the address:
        # - enable: Enabled status 
        # - disable: Disabled status
        # 
        # This parameter is required.
        self.enable_status = enable_status
        # The condition for determining the health status of the address. This parameter is required when HealthTasks is specified. Valid values:
        # 
        # *   any_ok: The health check results of at least one health check template are normal.
        # *   p30_ok: The health check results of at least 30% of health check templates are normal.
        # *   p50_ok: The health check results of at least 50% of health check templates are normal.
        # *   p70_ok: The health check results of at least 70% of health check templates are normal.
        # *   all_ok: The health check results of all health check templates are normal.
        # 
        # This parameter is required.
        self.health_judgement = health_judgement
        # The health check tasks associated with the address.
        self.health_tasks_shrink = health_tasks_shrink
        # The availability state of the address. This parameter is required when AvailableMode is set to **manual**. Valid values:
        # 
        # *   available: The address is normal. In this state, the address is returned for DNS requests even if an alert is triggered when the address fails health checks.
        # *   unavailable: The address is abnormal. In this state, the address is not returned for DNS requests even if the address passes health checks.
        self.manual_available_status = manual_available_status
        # Address name.
        # 
        # This parameter is required.
        self.name = name
        # Remarks.
        self.remark = remark
        # Address type:
        # - IPv4
        # - IPv6
        # - domain
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

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

        if self.health_tasks_shrink is not None:
            result['HealthTasks'] = self.health_tasks_shrink

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

        if m.get('HealthTasks') is not None:
            self.health_tasks_shrink = m.get('HealthTasks')

        if m.get('ManualAvailableStatus') is not None:
            self.manual_available_status = m.get('ManualAvailableStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

