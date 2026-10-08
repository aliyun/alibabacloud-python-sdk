# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class ListConsumedServicesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        consumed_services_list: main_models.ListConsumedServicesResponseBodyConsumedServicesList = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        self.consumed_services_list = consumed_services_list
        # The returned message.
        self.message = message
        # The unique request ID.
        self.request_id = request_id

    def validate(self):
        if self.consumed_services_list:
            self.consumed_services_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.consumed_services_list is not None:
            result['ConsumedServicesList'] = self.consumed_services_list.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ConsumedServicesList') is not None:
            temp_model = main_models.ListConsumedServicesResponseBodyConsumedServicesList()
            self.consumed_services_list = temp_model.from_map(m.get('ConsumedServicesList'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListConsumedServicesResponseBodyConsumedServicesList(DaraModel):
    def __init__(
        self,
        list_consumed_services: List[main_models.ListConsumedServicesResponseBodyConsumedServicesListListConsumedServices] = None,
    ):
        self.list_consumed_services = list_consumed_services

    def validate(self):
        if self.list_consumed_services:
            for v1 in self.list_consumed_services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ListConsumedServices'] = []
        if self.list_consumed_services is not None:
            for k1 in self.list_consumed_services:
                result['ListConsumedServices'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list_consumed_services = []
        if m.get('ListConsumedServices') is not None:
            for k1 in m.get('ListConsumedServices'):
                temp_model = main_models.ListConsumedServicesResponseBodyConsumedServicesListListConsumedServices()
                self.list_consumed_services.append(temp_model.from_map(k1))

        return self

class ListConsumedServicesResponseBodyConsumedServicesListListConsumedServices(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        docker_application: bool = None,
        group_2ip: str = None,
        groups: main_models.ListConsumedServicesResponseBodyConsumedServicesListListConsumedServicesGroups = None,
        ips: main_models.ListConsumedServicesResponseBodyConsumedServicesListListConsumedServicesIps = None,
        name: str = None,
        type: str = None,
        version: str = None,
    ):
        self.app_id = app_id
        self.docker_application = docker_application
        self.group_2ip = group_2ip
        self.groups = groups
        self.ips = ips
        self.name = name
        self.type = type
        self.version = version

    def validate(self):
        if self.groups:
            self.groups.validate()
        if self.ips:
            self.ips.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.docker_application is not None:
            result['DockerApplication'] = self.docker_application

        if self.group_2ip is not None:
            result['Group2Ip'] = self.group_2ip

        if self.groups is not None:
            result['Groups'] = self.groups.to_map()

        if self.ips is not None:
            result['Ips'] = self.ips.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DockerApplication') is not None:
            self.docker_application = m.get('DockerApplication')

        if m.get('Group2Ip') is not None:
            self.group_2ip = m.get('Group2Ip')

        if m.get('Groups') is not None:
            temp_model = main_models.ListConsumedServicesResponseBodyConsumedServicesListListConsumedServicesGroups()
            self.groups = temp_model.from_map(m.get('Groups'))

        if m.get('Ips') is not None:
            temp_model = main_models.ListConsumedServicesResponseBodyConsumedServicesListListConsumedServicesIps()
            self.ips = temp_model.from_map(m.get('Ips'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListConsumedServicesResponseBodyConsumedServicesListListConsumedServicesIps(DaraModel):
    def __init__(
        self,
        ip: List[str] = None,
    ):
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')

        return self

class ListConsumedServicesResponseBodyConsumedServicesListListConsumedServicesGroups(DaraModel):
    def __init__(
        self,
        group: List[str] = None,
    ):
        self.group = group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['group'] = self.group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')

        return self

