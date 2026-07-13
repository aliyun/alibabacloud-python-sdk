# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentteams20260605 import models as main_models
from darabonba.model import DaraModel

class GetServiceEndpointResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetServiceEndpointResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetServiceEndpointResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetServiceEndpointResponseBodyData(DaraModel):
    def __init__(
        self,
        cert_identifier: str = None,
        component: str = None,
        create_time: str = None,
        domain: str = None,
        domain_type: str = None,
        endpoint_id: str = None,
        endpoint_name: str = None,
        instance_id: str = None,
        network_type: str = None,
        region_id: str = None,
        status: str = None,
        update_time: str = None,
    ):
        self.cert_identifier = cert_identifier
        self.component = component
        self.create_time = create_time
        self.domain = domain
        self.domain_type = domain_type
        self.endpoint_id = endpoint_id
        self.endpoint_name = endpoint_name
        self.instance_id = instance_id
        self.network_type = network_type
        self.region_id = region_id
        self.status = status
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.component is not None:
            result['Component'] = self.component

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('Component') is not None:
            self.component = m.get('Component')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

