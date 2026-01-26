# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetPrometheusInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetPrometheusInstanceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code. The status code 200 indicates that the request was successful. If another status code is returned, the request failed.
        self.code = code
        # The response parameters.
        self.data = data
        # The message returned.
        self.message = message
        # Id of the request
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetPrometheusInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPrometheusInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        access_type: str = None,
        archive_duration: int = None,
        auth_free_read_policy: str = None,
        auth_free_write_policy: str = None,
        auth_token: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        db_instance_status: str = None,
        enable_auth_free_read: bool = None,
        enable_auth_free_write: bool = None,
        enable_auth_token: str = None,
        extra_info: Dict[str, str] = None,
        grafana_instance_id: str = None,
        http_api_inter_url: str = None,
        http_api_intra_url: str = None,
        open_telemetry_inter_url: str = None,
        open_telemetry_intra_url: str = None,
        payment_type: str = None,
        payment_type_update_time: str = None,
        product: str = None,
        push_gateway_inter_url: str = None,
        push_gateway_intra_url: str = None,
        region_id: str = None,
        remote_read_inter_url: str = None,
        remote_read_intra_url: str = None,
        remote_write_inter_url: str = None,
        remote_write_intra_url: str = None,
        resource_group_id: str = None,
        resource_type: str = None,
        security_group_id: str = None,
        storage_duration: int = None,
        sub_clusters_json: str = None,
        support_auth_types: List[str] = None,
        tags: List[main_models.GetPrometheusInstanceResponseBodyDataTags] = None,
        user_id: str = None,
        v_switch_id: str = None,
        version: str = None,
        vpc_id: str = None,
    ):
        # The permission type. Valid values: readWrite, readOnly, and httpReadOnly
        self.access_type = access_type
        # The number of days for which data is automatically archived after the storage duration expires. Valid values: 60, 90, 180, and 365. 0 indicates that the data is not archived.
        self.archive_duration = archive_duration
        # The whitelist of IP addresses for which password-free read is enabled.
        self.auth_free_read_policy = auth_free_read_policy
        # The whitelist of IP addresses for which password-free write is enabled.
        self.auth_free_write_policy = auth_free_write_policy
        # The authorization token.
        self.auth_token = auth_token
        # The ID of the Prometheus instance.
        self.cluster_id = cluster_id
        # The name of the monitoring object.
        self.cluster_name = cluster_name
        # *   remote-write: general-purpose Prometheus instance
        # *   ecs: Prometheus instances for ECS
        # *   cloud-monitor: Prometheus instance for Alibaba Cloud services in the Chinese mainland
        # *   cloud-product: Prometheus instance for Alibaba Cloud services outside the Chinese mainland
        # *   global-view: global aggregation instance
        # *   aliyun-cs: Prometheus instance for Container Service
        self.cluster_type = cluster_type
        # The data storage status at the backend.
        self.db_instance_status = db_instance_status
        # Indicates whether password-free read is enabled.
        self.enable_auth_free_read = enable_auth_free_read
        # Indicates whether password-free write is enabled.
        self.enable_auth_free_write = enable_auth_free_write
        # Indicates whether access token authentication is enabled.
        self.enable_auth_token = enable_auth_token
        # The extra information. This parameter is returned only for console requests.
        self.extra_info = extra_info
        # The ID of the Grafana workspace.
        self.grafana_instance_id = grafana_instance_id
        # The public URL for the HTTP API.
        self.http_api_inter_url = http_api_inter_url
        # The internal URL for the HTTP API.
        self.http_api_intra_url = http_api_intra_url
        self.open_telemetry_inter_url = open_telemetry_inter_url
        self.open_telemetry_intra_url = open_telemetry_intra_url
        # The billing method. Valid values:
        # 
        # *   PREPAY: subscription
        # *   POSTPAY: pay-as-you-go
        self.payment_type = payment_type
        # The time when the billing method was modified.
        self.payment_type_update_time = payment_type_update_time
        # The product to which the Prometheus instance belongs. Valid values: arms and cms.
        self.product = product
        # The public URL for Pushgateway.
        self.push_gateway_inter_url = push_gateway_inter_url
        # The internal URL for Pushgateway.
        self.push_gateway_intra_url = push_gateway_intra_url
        # The region ID.
        self.region_id = region_id
        # The public URL for remote read.
        self.remote_read_inter_url = remote_read_inter_url
        # The internal URL for remote read.
        self.remote_read_intra_url = remote_read_intra_url
        # The public URL for remote write.
        self.remote_write_inter_url = remote_write_inter_url
        # The internal URL for remote write.
        self.remote_write_intra_url = remote_write_intra_url
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The type of the resource. Set the value to PROMETHEUS.
        self.resource_type = resource_type
        # The ID of the security group. This parameter is returned only for Prometheus instances for ECS.
        self.security_group_id = security_group_id
        # The data storage duration. Unit: days.
        self.storage_duration = storage_duration
        # The child instances of the global aggregation instance. The value is a JSON string.
        self.sub_clusters_json = sub_clusters_json
        # The supported authentication types.
        self.support_auth_types = support_auth_types
        # The tags of the instance.
        self.tags = tags
        # The user ID.
        self.user_id = user_id
        # The vSwitch ID. This parameter is returned only for Prometheus instances for ECS.
        self.v_switch_id = v_switch_id
        # Version
        self.version = version
        # The VPC ID. This parameter is returned only for Prometheus instances for ECS.
        self.vpc_id = vpc_id

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
            result['AccessType'] = self.access_type

        if self.archive_duration is not None:
            result['ArchiveDuration'] = self.archive_duration

        if self.auth_free_read_policy is not None:
            result['AuthFreeReadPolicy'] = self.auth_free_read_policy

        if self.auth_free_write_policy is not None:
            result['AuthFreeWritePolicy'] = self.auth_free_write_policy

        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.db_instance_status is not None:
            result['DbInstanceStatus'] = self.db_instance_status

        if self.enable_auth_free_read is not None:
            result['EnableAuthFreeRead'] = self.enable_auth_free_read

        if self.enable_auth_free_write is not None:
            result['EnableAuthFreeWrite'] = self.enable_auth_free_write

        if self.enable_auth_token is not None:
            result['EnableAuthToken'] = self.enable_auth_token

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.grafana_instance_id is not None:
            result['GrafanaInstanceId'] = self.grafana_instance_id

        if self.http_api_inter_url is not None:
            result['HttpApiInterUrl'] = self.http_api_inter_url

        if self.http_api_intra_url is not None:
            result['HttpApiIntraUrl'] = self.http_api_intra_url

        if self.open_telemetry_inter_url is not None:
            result['OpenTelemetryInterUrl'] = self.open_telemetry_inter_url

        if self.open_telemetry_intra_url is not None:
            result['OpenTelemetryIntraUrl'] = self.open_telemetry_intra_url

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.payment_type_update_time is not None:
            result['PaymentTypeUpdateTime'] = self.payment_type_update_time

        if self.product is not None:
            result['Product'] = self.product

        if self.push_gateway_inter_url is not None:
            result['PushGatewayInterUrl'] = self.push_gateway_inter_url

        if self.push_gateway_intra_url is not None:
            result['PushGatewayIntraUrl'] = self.push_gateway_intra_url

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.remote_read_inter_url is not None:
            result['RemoteReadInterUrl'] = self.remote_read_inter_url

        if self.remote_read_intra_url is not None:
            result['RemoteReadIntraUrl'] = self.remote_read_intra_url

        if self.remote_write_inter_url is not None:
            result['RemoteWriteInterUrl'] = self.remote_write_inter_url

        if self.remote_write_intra_url is not None:
            result['RemoteWriteIntraUrl'] = self.remote_write_intra_url

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.storage_duration is not None:
            result['StorageDuration'] = self.storage_duration

        if self.sub_clusters_json is not None:
            result['SubClustersJson'] = self.sub_clusters_json

        if self.support_auth_types is not None:
            result['SupportAuthTypes'] = self.support_auth_types

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.version is not None:
            result['Version'] = self.version

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')

        if m.get('ArchiveDuration') is not None:
            self.archive_duration = m.get('ArchiveDuration')

        if m.get('AuthFreeReadPolicy') is not None:
            self.auth_free_read_policy = m.get('AuthFreeReadPolicy')

        if m.get('AuthFreeWritePolicy') is not None:
            self.auth_free_write_policy = m.get('AuthFreeWritePolicy')

        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('DbInstanceStatus') is not None:
            self.db_instance_status = m.get('DbInstanceStatus')

        if m.get('EnableAuthFreeRead') is not None:
            self.enable_auth_free_read = m.get('EnableAuthFreeRead')

        if m.get('EnableAuthFreeWrite') is not None:
            self.enable_auth_free_write = m.get('EnableAuthFreeWrite')

        if m.get('EnableAuthToken') is not None:
            self.enable_auth_token = m.get('EnableAuthToken')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('GrafanaInstanceId') is not None:
            self.grafana_instance_id = m.get('GrafanaInstanceId')

        if m.get('HttpApiInterUrl') is not None:
            self.http_api_inter_url = m.get('HttpApiInterUrl')

        if m.get('HttpApiIntraUrl') is not None:
            self.http_api_intra_url = m.get('HttpApiIntraUrl')

        if m.get('OpenTelemetryInterUrl') is not None:
            self.open_telemetry_inter_url = m.get('OpenTelemetryInterUrl')

        if m.get('OpenTelemetryIntraUrl') is not None:
            self.open_telemetry_intra_url = m.get('OpenTelemetryIntraUrl')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('PaymentTypeUpdateTime') is not None:
            self.payment_type_update_time = m.get('PaymentTypeUpdateTime')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('PushGatewayInterUrl') is not None:
            self.push_gateway_inter_url = m.get('PushGatewayInterUrl')

        if m.get('PushGatewayIntraUrl') is not None:
            self.push_gateway_intra_url = m.get('PushGatewayIntraUrl')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemoteReadInterUrl') is not None:
            self.remote_read_inter_url = m.get('RemoteReadInterUrl')

        if m.get('RemoteReadIntraUrl') is not None:
            self.remote_read_intra_url = m.get('RemoteReadIntraUrl')

        if m.get('RemoteWriteInterUrl') is not None:
            self.remote_write_inter_url = m.get('RemoteWriteInterUrl')

        if m.get('RemoteWriteIntraUrl') is not None:
            self.remote_write_intra_url = m.get('RemoteWriteIntraUrl')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('StorageDuration') is not None:
            self.storage_duration = m.get('StorageDuration')

        if m.get('SubClustersJson') is not None:
            self.sub_clusters_json = m.get('SubClustersJson')

        if m.get('SupportAuthTypes') is not None:
            self.support_auth_types = m.get('SupportAuthTypes')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetPrometheusInstanceResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class GetPrometheusInstanceResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

