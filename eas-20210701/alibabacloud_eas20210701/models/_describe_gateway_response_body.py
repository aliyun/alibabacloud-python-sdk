# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class DescribeGatewayResponseBody(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        create_time: str = None,
        external_cluster_id: str = None,
        gateway_id: str = None,
        gateway_name: str = None,
        instance_type: str = None,
        internet_domain: str = None,
        internet_enabled: bool = None,
        internet_status: str = None,
        intranet_domain: str = None,
        intranet_enabled: bool = None,
        is_default: bool = None,
        labels: List[main_models.DescribeGatewayResponseBodyLabels] = None,
        replicas: int = None,
        request_id: str = None,
        sslredirection_enabled: bool = None,
        status: str = None,
        update_time: str = None,
    ):
        self.charge_type = charge_type
        # The time when the private gateway was created. The time is displayed in UTC.
        self.create_time = create_time
        # The ID of the self-managed cluster.
        self.external_cluster_id = external_cluster_id
        # The ID of the private gateway.
        self.gateway_id = gateway_id
        # The alias of the private gateway.
        self.gateway_name = gateway_name
        # The instance type used by the private gateway.
        # 
        # Valid values:
        # 
        # *   8c16g
        # *   4c8g
        # *   2c4g
        # *   16c32g
        self.instance_type = instance_type
        # The public endpoint.
        self.internet_domain = internet_domain
        # Indicates whether Internet access is enabled.
        self.internet_enabled = internet_enabled
        # Indicates whether Internet access is enabled.
        # 
        # Valid values:
        # 
        # *   Creating: Internet access is being enabled.
        # *   Failed: Internet access failed to be enabled or deleted.
        # *   Running: Internet access is running.
        # *   Deleted: Internet access is deleted.
        # *   Deleting: Internet access is being deleted.
        self.internet_status = internet_status
        # The internal endpoint.
        self.intranet_domain = intranet_domain
        self.intranet_enabled = intranet_enabled
        # Indicates whether it is the default private gateway.
        self.is_default = is_default
        self.labels = labels
        # The number of nodes in the private gateway.
        self.replicas = replicas
        # The request ID.
        self.request_id = request_id
        # Indicates whether the HTTP to HTTPS redirection is enabled.
        self.sslredirection_enabled = sslredirection_enabled
        # The status of the private gateway.
        # 
        # Valid values:
        # 
        # *   Creating
        # *   Stopped
        # *   Failed
        # *   Running
        # *   Deleted
        # *   Deleting
        # *   Waiting
        self.status = status
        # The time when the private gateway was updated. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.external_cluster_id is not None:
            result['ExternalClusterId'] = self.external_cluster_id

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain

        if self.internet_enabled is not None:
            result['InternetEnabled'] = self.internet_enabled

        if self.internet_status is not None:
            result['InternetStatus'] = self.internet_status

        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain

        if self.intranet_enabled is not None:
            result['IntranetEnabled'] = self.intranet_enabled

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sslredirection_enabled is not None:
            result['SSLRedirectionEnabled'] = self.sslredirection_enabled

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExternalClusterId') is not None:
            self.external_cluster_id = m.get('ExternalClusterId')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')

        if m.get('InternetEnabled') is not None:
            self.internet_enabled = m.get('InternetEnabled')

        if m.get('InternetStatus') is not None:
            self.internet_status = m.get('InternetStatus')

        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')

        if m.get('IntranetEnabled') is not None:
            self.intranet_enabled = m.get('IntranetEnabled')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.DescribeGatewayResponseBodyLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SSLRedirectionEnabled') is not None:
            self.sslredirection_enabled = m.get('SSLRedirectionEnabled')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeGatewayResponseBodyLabels(DaraModel):
    def __init__(
        self,
        label_key: str = None,
        label_value: str = None,
    ):
        self.label_key = label_key
        self.label_value = label_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label_key is not None:
            result['LabelKey'] = self.label_key

        if self.label_value is not None:
            result['LabelValue'] = self.label_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LabelKey') is not None:
            self.label_key = m.get('LabelKey')

        if m.get('LabelValue') is not None:
            self.label_value = m.get('LabelValue')

        return self

