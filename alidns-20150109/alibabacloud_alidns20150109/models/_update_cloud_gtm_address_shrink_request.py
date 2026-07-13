# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudGtmAddressShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address: str = None,
        address_id: str = None,
        attribute_info: str = None,
        client_token: str = None,
        health_judgement: str = None,
        health_tasks_shrink: str = None,
        name: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - zh-CN: Chinese
        # 
        # - en-US (default): English
        self.accept_language = accept_language
        # The updated IP address or domain name.
        self.address = address
        # The unique ID of the address.
        # 
        # This parameter is required.
        self.address_id = address_id
        # The attribution information of the address.
        self.attribute_info = attribute_info
        # A client token that is used to ensure the idempotence of the request. You can specify a custom value for this parameter, but you must make sure that the value is unique among different requests. The value can contain a maximum of 64 ASCII characters.
        self.client_token = client_token
        # The updated condition for determining the health status of the address:
        # 
        # - any_ok: At least one probe is normal for all health check templates.
        # 
        # - p30_ok: At least 30% of the probes are normal for all health check templates.
        # 
        # - p50_ok: At least 50% of the probes are normal for all health check templates.
        # 
        # - p70_ok: At least 70% of the probes are normal for all health check templates.
        # 
        # - all_ok: All probes are normal for all health check templates.
        self.health_judgement = health_judgement
        # The list of health check tasks.
        self.health_tasks_shrink = health_tasks_shrink
        # The updated name of the address.
        self.name = name

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

        if self.address_id is not None:
            result['AddressId'] = self.address_id

        if self.attribute_info is not None:
            result['AttributeInfo'] = self.attribute_info

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.health_judgement is not None:
            result['HealthJudgement'] = self.health_judgement

        if self.health_tasks_shrink is not None:
            result['HealthTasks'] = self.health_tasks_shrink

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')

        if m.get('AttributeInfo') is not None:
            self.attribute_info = m.get('AttributeInfo')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('HealthJudgement') is not None:
            self.health_judgement = m.get('HealthJudgement')

        if m.get('HealthTasks') is not None:
            self.health_tasks_shrink = m.get('HealthTasks')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

