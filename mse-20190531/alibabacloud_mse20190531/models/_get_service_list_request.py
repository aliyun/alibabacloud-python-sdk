# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServiceListRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_id: str = None,
        ip: str = None,
        region: str = None,
        service_name: str = None,
        service_type: str = None,
    ):
        # The language of the response.
        self.accept_language = accept_language
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The IP address.
        self.ip = ip
        # The ID of the region.
        self.region = region
        # The name of the service.
        self.service_name = service_name
        # The type of the framework.
        self.service_type = service_type

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

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.region is not None:
            result['Region'] = self.region

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        return self

