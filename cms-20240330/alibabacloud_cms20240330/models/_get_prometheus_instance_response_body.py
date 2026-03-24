# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetPrometheusInstanceResponseBody(DaraModel):
    def __init__(
        self,
        prometheus_instance: main_models.GetPrometheusInstanceResponseBodyPrometheusInstance = None,
        request_id: str = None,
    ):
        # The details of the Prometheus instance.
        self.prometheus_instance = prometheus_instance
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.prometheus_instance:
            self.prometheus_instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prometheus_instance is not None:
            result['prometheusInstance'] = self.prometheus_instance.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('prometheusInstance') is not None:
            temp_model = main_models.GetPrometheusInstanceResponseBodyPrometheusInstance()
            self.prometheus_instance = temp_model.from_map(m.get('prometheusInstance'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetPrometheusInstanceResponseBodyPrometheusInstance(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        archive_duration: int = None,
        auth_free_read_policy: str = None,
        auth_free_write_policy: str = None,
        auth_token: str = None,
        create_time: str = None,
        enable_auth_free_read: bool = None,
        enable_auth_free_write: bool = None,
        enable_auth_token: bool = None,
        extra_info: Dict[str, str] = None,
        folder_url: str = None,
        grafana_instance_id: str = None,
        grafana_instance_name: str = None,
        http_api_inter_url: str = None,
        http_api_intra_url: str = None,
        instance_type: str = None,
        payment_type: str = None,
        payment_type_update_time: str = None,
        product: str = None,
        prometheus_instance_id: str = None,
        prometheus_instance_name: str = None,
        push_gateway_inter_url: str = None,
        push_gateway_intra_url: str = None,
        region_id: str = None,
        remote_read_inter_url: str = None,
        remote_read_intra_url: str = None,
        remote_write_inter_url: str = None,
        remote_write_intra_url: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        status: str = None,
        storage_duration: int = None,
        support_auth_types: List[str] = None,
        tags: List[main_models.GetPrometheusInstanceResponseBodyPrometheusInstanceTags] = None,
        user_id: str = None,
        version: str = None,
        workspace: str = None,
    ):
        # The permission type. Valid values: \\`readWrite\\`, \\`readOnly\\`, and \\`httpReadOnly\\`.
        self.access_type = access_type
        # The number of days to archive data after the storage duration ends. A value of 0 means data is not archived. A value of 3650 means data is permanently archived.
        self.archive_duration = archive_duration
        # The password-free read policy. IP address ranges and VPC IDs are supported.
        self.auth_free_read_policy = auth_free_read_policy
        # The password-free write policy. IP address ranges and VPC IDs are supported.
        self.auth_free_write_policy = auth_free_write_policy
        # The authentication token.
        self.auth_token = auth_token
        # The time when the instance was created. The time is in UTC and follows the yyyy-MM-ddTHH:mmZ format.
        self.create_time = create_time
        # Indicates whether password-free read is enabled.
        self.enable_auth_free_read = enable_auth_free_read
        # Indicates whether password-free write is enabled.
        self.enable_auth_free_write = enable_auth_free_write
        # Indicates whether the authentication token is enabled.
        self.enable_auth_token = enable_auth_token
        # The extra information.
        self.extra_info = extra_info
        # The URL of the visualization dashboard folder.
        self.folder_url = folder_url
        # The ID of the attached Grafana instance.
        self.grafana_instance_id = grafana_instance_id
        # The name of the attached Grafana instance.
        self.grafana_instance_name = grafana_instance_name
        # The HTTP endpoint for the Internet.
        self.http_api_inter_url = http_api_inter_url
        # The HTTP endpoint for the internal network.
        self.http_api_intra_url = http_api_intra_url
        # The type of the Prometheus instance.
        self.instance_type = instance_type
        # The billing method. Valid values:
        # \\`POSTPAY\\`: pay-as-you-go based on the number of reported metrics.
        # \\`POSTPAY_GB\\`: pay-as-you-go based on the volume of data written.
        self.payment_type = payment_type
        # The time when the billing method of the instance was last modified.
        self.payment_type_update_time = payment_type_update_time
        # The Alibaba Cloud service to which the instance belongs. Valid values: \\`arms\\` and \\`cms\\`.
        self.product = product
        # The instance ID.
        self.prometheus_instance_id = prometheus_instance_id
        # The instance name.
        self.prometheus_instance_name = prometheus_instance_name
        # The Pushgateway endpoint for the Internet.
        self.push_gateway_inter_url = push_gateway_inter_url
        # The Pushgateway endpoint for the internal network.
        self.push_gateway_intra_url = push_gateway_intra_url
        # The region ID.
        self.region_id = region_id
        # The read endpoint for the Internet.
        self.remote_read_inter_url = remote_read_inter_url
        # The read endpoint for the internal network.
        self.remote_read_intra_url = remote_read_intra_url
        # The write endpoint for the Internet.
        self.remote_write_inter_url = remote_write_inter_url
        # The write endpoint for the internal network.
        self.remote_write_intra_url = remote_write_intra_url
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # A static field. The value is \\`PrometheusInstance\\`.
        self.resource_type = resource_type
        # The instance status.
        self.status = status
        # The storage duration in days.
        self.storage_duration = storage_duration
        # The supported authentication and authorization types.
        self.support_auth_types = support_auth_types
        # The list of tags.
        self.tags = tags
        # The user ID.
        self.user_id = user_id
        # The version.
        self.version = version
        # The workspace to which the Prometheus instance belongs.
        self.workspace = workspace

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_type is not None:
            result['accessType'] = self.access_type

        if self.archive_duration is not None:
            result['archiveDuration'] = self.archive_duration

        if self.auth_free_read_policy is not None:
            result['authFreeReadPolicy'] = self.auth_free_read_policy

        if self.auth_free_write_policy is not None:
            result['authFreeWritePolicy'] = self.auth_free_write_policy

        if self.auth_token is not None:
            result['authToken'] = self.auth_token

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.enable_auth_free_read is not None:
            result['enableAuthFreeRead'] = self.enable_auth_free_read

        if self.enable_auth_free_write is not None:
            result['enableAuthFreeWrite'] = self.enable_auth_free_write

        if self.enable_auth_token is not None:
            result['enableAuthToken'] = self.enable_auth_token

        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info

        if self.folder_url is not None:
            result['folderUrl'] = self.folder_url

        if self.grafana_instance_id is not None:
            result['grafanaInstanceId'] = self.grafana_instance_id

        if self.grafana_instance_name is not None:
            result['grafanaInstanceName'] = self.grafana_instance_name

        if self.http_api_inter_url is not None:
            result['httpApiInterUrl'] = self.http_api_inter_url

        if self.http_api_intra_url is not None:
            result['httpApiIntraUrl'] = self.http_api_intra_url

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.payment_type is not None:
            result['paymentType'] = self.payment_type

        if self.payment_type_update_time is not None:
            result['paymentTypeUpdateTime'] = self.payment_type_update_time

        if self.product is not None:
            result['product'] = self.product

        if self.prometheus_instance_id is not None:
            result['prometheusInstanceId'] = self.prometheus_instance_id

        if self.prometheus_instance_name is not None:
            result['prometheusInstanceName'] = self.prometheus_instance_name

        if self.push_gateway_inter_url is not None:
            result['pushGatewayInterUrl'] = self.push_gateway_inter_url

        if self.push_gateway_intra_url is not None:
            result['pushGatewayIntraUrl'] = self.push_gateway_intra_url

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.remote_read_inter_url is not None:
            result['remoteReadInterUrl'] = self.remote_read_inter_url

        if self.remote_read_intra_url is not None:
            result['remoteReadIntraUrl'] = self.remote_read_intra_url

        if self.remote_write_inter_url is not None:
            result['remoteWriteInterUrl'] = self.remote_write_inter_url

        if self.remote_write_intra_url is not None:
            result['remoteWriteIntraUrl'] = self.remote_write_intra_url

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.status is not None:
            result['status'] = self.status

        if self.storage_duration is not None:
            result['storageDuration'] = self.storage_duration

        if self.support_auth_types is not None:
            result['supportAuthTypes'] = self.support_auth_types

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.version is not None:
            result['version'] = self.version

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessType') is not None:
            self.access_type = m.get('accessType')

        if m.get('archiveDuration') is not None:
            self.archive_duration = m.get('archiveDuration')

        if m.get('authFreeReadPolicy') is not None:
            self.auth_free_read_policy = m.get('authFreeReadPolicy')

        if m.get('authFreeWritePolicy') is not None:
            self.auth_free_write_policy = m.get('authFreeWritePolicy')

        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('enableAuthFreeRead') is not None:
            self.enable_auth_free_read = m.get('enableAuthFreeRead')

        if m.get('enableAuthFreeWrite') is not None:
            self.enable_auth_free_write = m.get('enableAuthFreeWrite')

        if m.get('enableAuthToken') is not None:
            self.enable_auth_token = m.get('enableAuthToken')

        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')

        if m.get('folderUrl') is not None:
            self.folder_url = m.get('folderUrl')

        if m.get('grafanaInstanceId') is not None:
            self.grafana_instance_id = m.get('grafanaInstanceId')

        if m.get('grafanaInstanceName') is not None:
            self.grafana_instance_name = m.get('grafanaInstanceName')

        if m.get('httpApiInterUrl') is not None:
            self.http_api_inter_url = m.get('httpApiInterUrl')

        if m.get('httpApiIntraUrl') is not None:
            self.http_api_intra_url = m.get('httpApiIntraUrl')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')

        if m.get('paymentTypeUpdateTime') is not None:
            self.payment_type_update_time = m.get('paymentTypeUpdateTime')

        if m.get('product') is not None:
            self.product = m.get('product')

        if m.get('prometheusInstanceId') is not None:
            self.prometheus_instance_id = m.get('prometheusInstanceId')

        if m.get('prometheusInstanceName') is not None:
            self.prometheus_instance_name = m.get('prometheusInstanceName')

        if m.get('pushGatewayInterUrl') is not None:
            self.push_gateway_inter_url = m.get('pushGatewayInterUrl')

        if m.get('pushGatewayIntraUrl') is not None:
            self.push_gateway_intra_url = m.get('pushGatewayIntraUrl')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('remoteReadInterUrl') is not None:
            self.remote_read_inter_url = m.get('remoteReadInterUrl')

        if m.get('remoteReadIntraUrl') is not None:
            self.remote_read_intra_url = m.get('remoteReadIntraUrl')

        if m.get('remoteWriteInterUrl') is not None:
            self.remote_write_inter_url = m.get('remoteWriteInterUrl')

        if m.get('remoteWriteIntraUrl') is not None:
            self.remote_write_intra_url = m.get('remoteWriteIntraUrl')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('storageDuration') is not None:
            self.storage_duration = m.get('storageDuration')

        if m.get('supportAuthTypes') is not None:
            self.support_auth_types = m.get('supportAuthTypes')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.GetPrometheusInstanceResponseBodyPrometheusInstanceTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class GetPrometheusInstanceResponseBodyPrometheusInstanceTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

