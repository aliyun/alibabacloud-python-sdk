# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListPrometheusInstanceByTagAndResourceGroupIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListPrometheusInstanceByTagAndResourceGroupIdResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed.
        self.code = code
        # The returned struct.
        self.data = data
        # The returned message.
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
            temp_model = main_models.ListPrometheusInstanceByTagAndResourceGroupIdResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPrometheusInstanceByTagAndResourceGroupIdResponseBodyData(DaraModel):
    def __init__(
        self,
        prometheus_instances: List[main_models.ListPrometheusInstanceByTagAndResourceGroupIdResponseBodyDataPrometheusInstances] = None,
    ):
        # The queried Prometheus instances.
        self.prometheus_instances = prometheus_instances

    def validate(self):
        if self.prometheus_instances:
            for v1 in self.prometheus_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PrometheusInstances'] = []
        if self.prometheus_instances is not None:
            for k1 in self.prometheus_instances:
                result['PrometheusInstances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prometheus_instances = []
        if m.get('PrometheusInstances') is not None:
            for k1 in m.get('PrometheusInstances'):
                temp_model = main_models.ListPrometheusInstanceByTagAndResourceGroupIdResponseBodyDataPrometheusInstances()
                self.prometheus_instances.append(temp_model.from_map(k1))

        return self

class ListPrometheusInstanceByTagAndResourceGroupIdResponseBodyDataPrometheusInstances(DaraModel):
    def __init__(
        self,
        auth_token: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        grafana_instance_id: str = None,
        http_api_inter_url: str = None,
        http_api_intra_url: str = None,
        payment_type: str = None,
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
        sub_clusters_json: str = None,
        tags: List[main_models.ListPrometheusInstanceByTagAndResourceGroupIdResponseBodyDataPrometheusInstancesTags] = None,
        user_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The authorization token.
        self.auth_token = auth_token
        # The ID of the Prometheus instance.
        self.cluster_id = cluster_id
        # The name of the Prometheus instance.
        self.cluster_name = cluster_name
        # The instance type. Valid values:
        # 
        # *   remote-write: Prometheus instance for Remote Write
        # *   ecs: Prometheus instances for ECS
        # *   cloud-monitor: Prometheus instance for Alibaba Cloud services in the Chinese mainland
        # *   cloud-product: Prometheus instance for Alibaba Cloud services outside the Chinese mainland
        # *   global-view: global aggregation instance
        # *   aliyun-cs: Prometheus instance for Container Service
        self.cluster_type = cluster_type
        # The ID of the Grafana workspace.
        self.grafana_instance_id = grafana_instance_id
        # The public URL for the HTTP API.
        self.http_api_inter_url = http_api_inter_url
        # The internal URL for the HTTP API.
        self.http_api_intra_url = http_api_intra_url
        # The billing method. Valid values:
        # 
        # *   PREPAY: subscription
        # *   POSTPAY: pay-as-you-go
        self.payment_type = payment_type
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
        # The ID of the resource group to which the Prometheus instance belongs.
        self.resource_group_id = resource_group_id
        # The resource type.
        self.resource_type = resource_type
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The child instances of the global aggregation instance. The value is a JSON string.
        self.sub_clusters_json = sub_clusters_json
        # The list of tags.
        self.tags = tags
        # The ID of the user.
        self.user_id = user_id
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
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
        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.grafana_instance_id is not None:
            result['GrafanaInstanceId'] = self.grafana_instance_id

        if self.http_api_inter_url is not None:
            result['HttpApiInterUrl'] = self.http_api_inter_url

        if self.http_api_intra_url is not None:
            result['HttpApiIntraUrl'] = self.http_api_intra_url

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

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

        if self.sub_clusters_json is not None:
            result['SubClustersJson'] = self.sub_clusters_json

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('GrafanaInstanceId') is not None:
            self.grafana_instance_id = m.get('GrafanaInstanceId')

        if m.get('HttpApiInterUrl') is not None:
            self.http_api_inter_url = m.get('HttpApiInterUrl')

        if m.get('HttpApiIntraUrl') is not None:
            self.http_api_intra_url = m.get('HttpApiIntraUrl')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

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

        if m.get('SubClustersJson') is not None:
            self.sub_clusters_json = m.get('SubClustersJson')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListPrometheusInstanceByTagAndResourceGroupIdResponseBodyDataPrometheusInstancesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListPrometheusInstanceByTagAndResourceGroupIdResponseBodyDataPrometheusInstancesTags(DaraModel):
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

