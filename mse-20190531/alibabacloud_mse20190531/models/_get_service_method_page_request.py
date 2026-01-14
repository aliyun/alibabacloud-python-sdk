# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServiceMethodPageRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        app_name: str = None,
        ip: str = None,
        method_controller: str = None,
        name: str = None,
        namespace: str = None,
        page_number: int = None,
        page_size: int = None,
        path: str = None,
        region: str = None,
        service_group: str = None,
        service_name: str = None,
        service_type: str = None,
        service_version: str = None,
    ):
        self.accept_language = accept_language
        self.app_id = app_id
        self.app_name = app_name
        self.ip = ip
        self.method_controller = method_controller
        self.name = name
        self.namespace = namespace
        self.page_number = page_number
        self.page_size = page_size
        self.path = path
        self.region = region
        self.service_group = service_group
        self.service_name = service_name
        self.service_type = service_type
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.method_controller is not None:
            result['MethodController'] = self.method_controller

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path is not None:
            result['Path'] = self.path

        if self.region is not None:
            result['Region'] = self.region

        if self.service_group is not None:
            result['ServiceGroup'] = self.service_group

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('MethodController') is not None:
            self.method_controller = m.get('MethodController')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ServiceGroup') is not None:
            self.service_group = m.get('ServiceGroup')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        return self

