# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class UpdateCloudGtmAddressRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        address: str = None,
        address_id: str = None,
        attribute_info: str = None,
        client_token: str = None,
        health_judgement: str = None,
        health_tasks: List[main_models.UpdateCloudGtmAddressRequestHealthTasks] = None,
        name: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US (default): English
        self.accept_language = accept_language
        # The IP address or domain name.
        self.address = address
        # The ID of the address. This ID uniquely identifies the address.
        # 
        # This parameter is required.
        self.address_id = address_id
        # Address Attribution information.
        self.attribute_info = attribute_info
        # The client token that is used to ensure the idempotence of the request. You can specify a custom value for this parameter, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The new condition for determining the health state of the address. Valid values:
        # 
        # *   any_ok: The health check results of at least one health check template are normal.
        # *   p30_ok: The health check results of at least 30% of health check templates are normal.
        # *   p50_ok: The health check results of at least 50% of health check templates are normal.
        # *   p70_ok: The health check results of at least 70% of health check templates are normal.
        # *   all_ok: The health check results of all health check templates are normal.
        self.health_judgement = health_judgement
        # The health check tasks.
        self.health_tasks = health_tasks
        # The name of the address.
        self.name = name

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

        if self.address_id is not None:
            result['AddressId'] = self.address_id

        if self.attribute_info is not None:
            result['AttributeInfo'] = self.attribute_info

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.health_judgement is not None:
            result['HealthJudgement'] = self.health_judgement

        result['HealthTasks'] = []
        if self.health_tasks is not None:
            for k1 in self.health_tasks:
                result['HealthTasks'].append(k1.to_map() if k1 else None)

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

        self.health_tasks = []
        if m.get('HealthTasks') is not None:
            for k1 in m.get('HealthTasks'):
                temp_model = main_models.UpdateCloudGtmAddressRequestHealthTasks()
                self.health_tasks.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class UpdateCloudGtmAddressRequestHealthTasks(DaraModel):
    def __init__(
        self,
        port: int = None,
        template_id: str = None,
    ):
        # The service port of the address on which health check tasks are performed. If the ping protocol is used for health checks, the configuration of the service port is not supported.
        # 
        # *   If you leave this parameter empty, the existing service port is deleted.
        # *   If you specify this parameter, the existing service port is updated based on the value of this parameter.
        self.port = port
        # The ID of the health check template that is associated with the address. This parameter is required if you specify a service port of the address for health check tasks.
        # 
        # *   If you leave this parameter empty, the associated health check template is disassociated from the address.
        # *   If you specify this parameter, the associated health check template is updated based on the value of this parameter.
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

