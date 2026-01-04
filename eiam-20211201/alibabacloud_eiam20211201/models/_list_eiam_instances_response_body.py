# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListEiamInstancesResponseBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListEiamInstancesResponseBodyInstances] = None,
        request_id: str = None,
    ):
        # The instance list.
        self.instances = instances
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListEiamInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListEiamInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        description: str = None,
        developer_apiprivate_domain: str = None,
        developer_apipublic_domain: str = None,
        instance_id: str = None,
        instance_status: str = None,
        instance_version: str = None,
        open_apiprivate_domain: str = None,
        open_apipublic_domain: str = None,
        ssodomain: str = None,
        start_time: int = None,
    ):
        # The instance description.
        self.description = description
        # The private domain name of the instance Developer API.
        self.developer_apiprivate_domain = developer_apiprivate_domain
        # The public domain of the instance Developer API.
        self.developer_apipublic_domain = developer_apipublic_domain
        # The instance ID.
        self.instance_id = instance_id
        # The instance status.
        self.instance_status = instance_status
        # The instance version.
        # 
        # Valid values:
        # 
        # *   EIAM 2.0
        # *   EIAM 1.0
        self.instance_version = instance_version
        # The private domain of the instance OpenAPI.
        self.open_apiprivate_domain = open_apiprivate_domain
        # The public domain of the instance OpenAPI.
        self.open_apipublic_domain = open_apipublic_domain
        # The single sign-on (SSO) domain  of the instance.
        self.ssodomain = ssodomain
        # The time when the instance was created.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.developer_apiprivate_domain is not None:
            result['DeveloperAPIPrivateDomain'] = self.developer_apiprivate_domain

        if self.developer_apipublic_domain is not None:
            result['DeveloperAPIPublicDomain'] = self.developer_apipublic_domain

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_version is not None:
            result['InstanceVersion'] = self.instance_version

        if self.open_apiprivate_domain is not None:
            result['OpenAPIPrivateDomain'] = self.open_apiprivate_domain

        if self.open_apipublic_domain is not None:
            result['OpenAPIPublicDomain'] = self.open_apipublic_domain

        if self.ssodomain is not None:
            result['SSODomain'] = self.ssodomain

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DeveloperAPIPrivateDomain') is not None:
            self.developer_apiprivate_domain = m.get('DeveloperAPIPrivateDomain')

        if m.get('DeveloperAPIPublicDomain') is not None:
            self.developer_apipublic_domain = m.get('DeveloperAPIPublicDomain')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceVersion') is not None:
            self.instance_version = m.get('InstanceVersion')

        if m.get('OpenAPIPrivateDomain') is not None:
            self.open_apiprivate_domain = m.get('OpenAPIPrivateDomain')

        if m.get('OpenAPIPublicDomain') is not None:
            self.open_apipublic_domain = m.get('OpenAPIPublicDomain')

        if m.get('SSODomain') is not None:
            self.ssodomain = m.get('SSODomain')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

