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
        # Does it require all child instances to be verified successfully before creating a GlobalView instance. The default is false, which means partial success is possible.
        self.all_sub_clusters_success = all_sub_clusters_success
        # The number of days for which data is automatically archived after the storage expires. Valid values: 60, 90, 180, and 365. 0 indicates that the data is not archived.
        self.archive_duration = archive_duration
        # The ID of the ACK cluster. This parameter is required if you set the ClusterType parameter to aliyun-cs.
        self.cluster_id = cluster_id
        # The name of the created cluster. This parameter is required if you set the ClusterType parameter to remote-write or ecs.
        self.cluster_name = cluster_name
        # The type of the Prometheus instance. Valid values:
        # 
        # *   remote-write: Prometheus instance for Remote Write
        # *   ecs (unavailable): Prometheus instance for ECS
        # *   global-view: Prometheus instance for GlobalView
        # *   aliyun-cs: Prometheus instance for Container Service
        # *   cloud-product (unavailable): Prometheus instance for Alibaba Cloud services
        # *   cloud-monitor (unavailable): Prometheus instance for Hybrid Cloud Monitoring
        # *   flink (unavailable): Prometheus instance for Flink
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        # The data storage duration. Unit: days.
        self.duration = duration
        # The ID of the Grafana dedicated instance. This parameter is available if you set the ClusterType parameter to ecs.
        self.grafana_instance_id = grafana_instance_id
        # The billing mode. Valid values: POSTPAY: charges fees based on the amount of reported metric data. POSTPAY_GB: charges fees based on the amount of written metric data. Empty: The user-defined default billing mode is used. If you do not specify a default value, you are charged based on the amount of reported metric data.
        self.payment_type = payment_type
        # The ID of the region. If you use a Prometheus instance to monitor an Alibaba Cloud service in China, this parameter must be set to cn-shanghai.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the custom resource group. You can configure this parameter to bind the instance to the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the security group. This parameter is required if you set the ClusterType parameter to ecs.
        self.security_group_id = security_group_id
        # JSON string for child instances of the globalView instance.
        self.sub_clusters_json = sub_clusters_json
        # The tags of the instance. You can configure this parameter to manage tags for the instance.
        self.tags = tags
        # The ID of the vSwitch. This parameter is required if you set the ClusterType parameter to ecs.
        self.v_switch_id = v_switch_id
        # The ID of virtual private cloud (VPC). This parameter is required if you set the ClusterType parameter to ecs.
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
        self.key = key
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

