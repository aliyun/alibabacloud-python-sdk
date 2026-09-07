# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class CreatePrometheusInstanceRequest(DaraModel):
    def __init__(
        self,
        all_sub_clusters_success: bool = None,
        archive_duration: int = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        duration: int = None,
        grafana_instance_id: str = None,
        payment_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        sub_clusters_json: str = None,
        tags: List[main_models.CreatePrometheusInstanceRequestTags] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # Specifies whether all sub-instances must pass validation before the GlobalView instance is created. Default value: false, which indicates that partial success is allowed.
        self.all_sub_clusters_success = all_sub_clusters_success
        # The number of days to automatically archive data after the storage period expires. Valid values: 60, 90, 180, and 365. A value of 0 indicates that data is not archived.
        self.archive_duration = archive_duration
        # The Container Service cluster ID. This parameter is required when ClusterType is set to aliyun-cs.
        self.cluster_id = cluster_id
        # The name of the cluster to create. This parameter is required when ClusterType is set to remote-write, ecs, or global-view.
        # 
        # For ecs instances, the ClusterName must follow the format "name-vpc-id", and the name part cannot exceed 24 characters. Example: "mytest1-vpc-xxxxxxxxxxx".
        self.cluster_name = cluster_name
        # The instance type. Valid values: 
        # -  remote-write: Prometheus for Remote Write.
        # -  ecs (no longer supported): Prometheus for ECS.
        # -  global-view: Prometheus for GlobalView.
        # -  aliyun-cs (no longer supported): Prometheus for Container Service.
        # - cloud-product (no longer supported): Prometheus for Cloud Service.
        # - cloud-monitor (no longer supported): Prometheus for Hybrid Cloud Monitoring.
        # - flink (no longer supported): Prometheus for Flink.
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # The data storage duration, in days.
        self.duration = duration
        # The ID of the bound Grafana workspace. Set this parameter to "free" when you use the shared Grafana edition.
        self.grafana_instance_id = grafana_instance_id
        # The Billable methods. Valid values:
        # POSTPAY: pay-as-you-go based on the number of reported metrics.
        # POSTPAY_GB: pay-as-you-go based on the volume of written metrics.
        # Empty: uses the default billing method configured by the user. If no default is configured, the system defaults to billing based on the number of reported metrics.
        self.payment_type = payment_type
        # The actual region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The Network Security group ID. This parameter is required when ClusterType is set to ecs or aliyun-cs for a managed ASK cluster.
        self.security_group_id = security_group_id
        # The JSON string of sub-instances for the GlobalView instance.
        self.sub_clusters_json = sub_clusters_json
        # The custom tags.
        self.tags = tags
        # The vSwitch ID. This parameter is required when ClusterType is set to ecs or aliyun-cs for a managed ASK cluster.
        self.v_switch_id = v_switch_id
        # The VPC ID. This parameter is required when ClusterType is set to ecs or aliyun-cs for a managed ASK cluster.
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
        if self.all_sub_clusters_success is not None:
            result['AllSubClustersSuccess'] = self.all_sub_clusters_success

        if self.archive_duration is not None:
            result['ArchiveDuration'] = self.archive_duration

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.grafana_instance_id is not None:
            result['GrafanaInstanceId'] = self.grafana_instance_id

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.sub_clusters_json is not None:
            result['SubClustersJson'] = self.sub_clusters_json

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllSubClustersSuccess') is not None:
            self.all_sub_clusters_success = m.get('AllSubClustersSuccess')

        if m.get('ArchiveDuration') is not None:
            self.archive_duration = m.get('ArchiveDuration')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('GrafanaInstanceId') is not None:
            self.grafana_instance_id = m.get('GrafanaInstanceId')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SubClustersJson') is not None:
            self.sub_clusters_json = m.get('SubClustersJson')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreatePrometheusInstanceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreatePrometheusInstanceRequestTags(DaraModel):
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
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

