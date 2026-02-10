# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupedContainerInstancesResponseBody(DaraModel):
    def __init__(
        self,
        grouped_container_instance_list: List[main_models.DescribeGroupedContainerInstancesResponseBodyGroupedContainerInstanceList] = None,
        page_info: main_models.DescribeGroupedContainerInstancesResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The information about the container.
        self.grouped_container_instance_list = grouped_container_instance_list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.grouped_container_instance_list:
            for v1 in self.grouped_container_instance_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GroupedContainerInstanceList'] = []
        if self.grouped_container_instance_list is not None:
            for k1 in self.grouped_container_instance_list:
                result['GroupedContainerInstanceList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grouped_container_instance_list = []
        if m.get('GroupedContainerInstanceList') is not None:
            for k1 in m.get('GroupedContainerInstanceList'):
                temp_model = main_models.DescribeGroupedContainerInstancesResponseBodyGroupedContainerInstanceList()
                self.grouped_container_instance_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeGroupedContainerInstancesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeGroupedContainerInstancesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of container assets returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **20**.
        self.page_size = page_size
        # The total number of container assets returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeGroupedContainerInstancesResponseBodyGroupedContainerInstanceList(DaraModel):
    def __init__(
        self,
        alarm_count: int = None,
        app_name: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        create_time: int = None,
        custer_state: str = None,
        hc_count: int = None,
        host_ip: str = None,
        image: str = None,
        image_digest: str = None,
        image_repo_name: str = None,
        image_repo_namespace: str = None,
        image_repo_tag: str = None,
        image_uuid: str = None,
        instance_count: int = None,
        instance_id: str = None,
        namespace: str = None,
        pod: str = None,
        pod_ip: str = None,
        region_id: str = None,
        risk_instance_count: int = None,
        risk_level: str = None,
        risk_status: str = None,
        sync_open: int = None,
        sync_status: int = None,
        vul_count: int = None,
    ):
        # The number of alerts that are detected for the current pod, application, namespace, or cluster.
        self.alarm_count = alarm_count
        # The name of the application.
        self.app_name = app_name
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The type of the cluster. Valid values:
        # 
        # *   **Kubernetes**: dedicated Kubernetes cluster.
        # *   **ManagedKubernetes**: standard managed cluster (edge cluster).
        # *   **Ask**: serverless Kubernetes (ASK) cluster.
        self.cluster_type = cluster_type
        # The timestamp when the cluster was created. Unit: milliseconds.
        self.create_time = create_time
        # The status of the cluster. Valid values:
        # 
        # *   **running**: The cluster is running.
        # *   **stopped**: The cluster is stopped.
        # *   **deleted**: The cluster is deleted.
        # *   **delete_failed**: The cluster failed to be deleted.
        # *   **failed**: The cluster failed to be created.
        self.custer_state = custer_state
        # The number of baseline risks that are detected for the current pod, application, namespace, or cluster.
        self.hc_count = hc_count
        # The IP address of the host in the container cluster.
        self.host_ip = host_ip
        # The container image.
        self.image = image
        # The digest value of the image.
        self.image_digest = image_digest
        # The name of the image repository.
        self.image_repo_name = image_repo_name
        # The namespace of the image repository.
        self.image_repo_namespace = image_repo_namespace
        # The tag that is added to the image repository.
        self.image_repo_tag = image_repo_tag
        # The UUID of the image.
        self.image_uuid = image_uuid
        # The number of pods, applications, clusters, or namespaces.
        self.instance_count = instance_count
        # The ID of the server.
        self.instance_id = instance_id
        # The namespace of the cluster.
        self.namespace = namespace
        # The name of the pod.
        self.pod = pod
        # The IP address of the pod.
        self.pod_ip = pod_ip
        # The region ID of the instance.
        self.region_id = region_id
        # The number of at-risk instances.
        self.risk_instance_count = risk_instance_count
        # The risk level. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.risk_level = risk_level
        # Indicates whether risks were detected. Valid values:
        # 
        # *   **NO**
        # *   **YES**
        self.risk_status = risk_status
        # Indicates whether the synchronization of cluster audit logs is enabled. Valid values:
        # 
        # *   **0**: disabled.
        # *   **1**: enabled.
        self.sync_open = sync_open
        # The status of the synchronization of cluster audit logs. Valid values:
        # 
        # *   **0**: The synchronization failed.
        # *   **1**: The synchronization is successful.
        self.sync_status = sync_status
        # The number of vulnerabilities that are detected for the current pod, application, namespace, or cluster.
        self.vul_count = vul_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_count is not None:
            result['AlarmCount'] = self.alarm_count

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.custer_state is not None:
            result['CusterState'] = self.custer_state

        if self.hc_count is not None:
            result['HcCount'] = self.hc_count

        if self.host_ip is not None:
            result['HostIp'] = self.host_ip

        if self.image is not None:
            result['Image'] = self.image

        if self.image_digest is not None:
            result['ImageDigest'] = self.image_digest

        if self.image_repo_name is not None:
            result['ImageRepoName'] = self.image_repo_name

        if self.image_repo_namespace is not None:
            result['ImageRepoNamespace'] = self.image_repo_namespace

        if self.image_repo_tag is not None:
            result['ImageRepoTag'] = self.image_repo_tag

        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.pod is not None:
            result['Pod'] = self.pod

        if self.pod_ip is not None:
            result['PodIp'] = self.pod_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.risk_instance_count is not None:
            result['RiskInstanceCount'] = self.risk_instance_count

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_status is not None:
            result['RiskStatus'] = self.risk_status

        if self.sync_open is not None:
            result['SyncOpen'] = self.sync_open

        if self.sync_status is not None:
            result['SyncStatus'] = self.sync_status

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmCount') is not None:
            self.alarm_count = m.get('AlarmCount')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CusterState') is not None:
            self.custer_state = m.get('CusterState')

        if m.get('HcCount') is not None:
            self.hc_count = m.get('HcCount')

        if m.get('HostIp') is not None:
            self.host_ip = m.get('HostIp')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImageDigest') is not None:
            self.image_digest = m.get('ImageDigest')

        if m.get('ImageRepoName') is not None:
            self.image_repo_name = m.get('ImageRepoName')

        if m.get('ImageRepoNamespace') is not None:
            self.image_repo_namespace = m.get('ImageRepoNamespace')

        if m.get('ImageRepoTag') is not None:
            self.image_repo_tag = m.get('ImageRepoTag')

        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Pod') is not None:
            self.pod = m.get('Pod')

        if m.get('PodIp') is not None:
            self.pod_ip = m.get('PodIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RiskInstanceCount') is not None:
            self.risk_instance_count = m.get('RiskInstanceCount')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskStatus') is not None:
            self.risk_status = m.get('RiskStatus')

        if m.get('SyncOpen') is not None:
            self.sync_open = m.get('SyncOpen')

        if m.get('SyncStatus') is not None:
            self.sync_status = m.get('SyncStatus')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        return self

