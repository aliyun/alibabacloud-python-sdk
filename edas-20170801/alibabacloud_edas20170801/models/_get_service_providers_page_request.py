# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServiceProvidersPageRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        group: str = None,
        ip: str = None,
        namespace: str = None,
        origin: str = None,
        page: int = None,
        region: str = None,
        registry_type: str = None,
        service_id: str = None,
        service_name: str = None,
        service_type: str = None,
        service_version: str = None,
        size: int = None,
        source: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The group to which the service belongs.
        self.group = group
        # The IP address of the service provider. Fuzzy searches are supported.
        self.ip = ip
        # The ID of the namespace.
        self.namespace = namespace
        # The source of data. Valid values:
        # 
        # *   agent: Use this value if you use the service query feature of the latest version to pass the query result.
        # *   registry: Use this value if you use the service query feature of the earlier version to pass the query result.
        self.origin = origin
        # The number of the page to return. Pages start from Page 0.
        self.page = page
        # The ID of the region.
        self.region = region
        # The type of the service registry. This parameter is deprecated. You can ignore it.
        self.registry_type = registry_type
        # The ID of the service. This parameter is deprecated. You can ignore it.
        self.service_id = service_id
        # The name of the service.
        self.service_name = service_name
        # The type of the service. Valid values:
        # 
        # *   dubbo: Dubbo service
        # *   springCloud: Spring Cloud service
        # *   hsf: High-speed Service Framework (HSF) service
        self.service_type = service_type
        # The version of the service.
        self.service_version = service_version
        # The number of entries to return on each page.
        self.size = size
        # The source of the service. Set the value to edas.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.group is not None:
            result['group'] = self.group

        if self.ip is not None:
            result['ip'] = self.ip

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.origin is not None:
            result['origin'] = self.origin

        if self.page is not None:
            result['page'] = self.page

        if self.region is not None:
            result['region'] = self.region

        if self.registry_type is not None:
            result['registryType'] = self.registry_type

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.service_type is not None:
            result['serviceType'] = self.service_type

        if self.service_version is not None:
            result['serviceVersion'] = self.service_version

        if self.size is not None:
            result['size'] = self.size

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('ip') is not None:
            self.ip = m.get('ip')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('origin') is not None:
            self.origin = m.get('origin')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('registryType') is not None:
            self.registry_type = m.get('registryType')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')

        if m.get('serviceVersion') is not None:
            self.service_version = m.get('serviceVersion')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

