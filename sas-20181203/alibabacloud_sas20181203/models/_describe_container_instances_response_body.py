# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeContainerInstancesResponseBody(DaraModel):
    def __init__(
        self,
        container_instance_list: List[main_models.DescribeContainerInstancesResponseBodyContainerInstanceList] = None,
        page_info: main_models.DescribeContainerInstancesResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The details of the container asset.
        self.container_instance_list = container_instance_list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.container_instance_list:
            for v1 in self.container_instance_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContainerInstanceList'] = []
        if self.container_instance_list is not None:
            for k1 in self.container_instance_list:
                result['ContainerInstanceList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.container_instance_list = []
        if m.get('ContainerInstanceList') is not None:
            for k1 in m.get('ContainerInstanceList'):
                temp_model = main_models.DescribeContainerInstancesResponseBodyContainerInstanceList()
                self.container_instance_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeContainerInstancesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeContainerInstancesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
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

class DescribeContainerInstancesResponseBodyContainerInstanceList(DaraModel):
    def __init__(
        self,
        alarm_count: int = None,
        alarm_status: str = None,
        app_name: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        container_id: str = None,
        create_timestamp: int = None,
        exposed: int = None,
        exposed_detail: str = None,
        hc_count: int = None,
        hc_status: str = None,
        host_ip: str = None,
        image: str = None,
        image_digest: str = None,
        image_id: str = None,
        image_repo_name: str = None,
        image_repo_namespace: str = None,
        image_repo_tag: str = None,
        image_uuid: str = None,
        instance_id: str = None,
        namespace: str = None,
        node_info: str = None,
        node_name: str = None,
        pod: str = None,
        pod_ip: str = None,
        region_id: str = None,
        risk_count: str = None,
        risk_status: str = None,
        update_mark: str = None,
        vul_count: int = None,
        vul_status: str = None,
    ):
        # The number of alerts.
        self.alarm_count = alarm_count
        # Indicates whether alerts are generated for the container. Valid values:
        # 
        # *   **YES**
        # *   **NO**
        self.alarm_status = alarm_status
        # The name of the application.
        self.app_name = app_name
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The ID of the container.
        self.container_id = container_id
        # The timestamp when the cluster was created. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # Indicates whether the asset is exposed to the Internet.
        # 
        # *   **1**: exposed
        # *   **0**: not exposed
        self.exposed = exposed
        # The exposure details. The value is a JSON string.
        self.exposed_detail = exposed_detail
        # The number of baseline risks.
        self.hc_count = hc_count
        # Indicates whether baseline risks are detected. Valid values:
        # 
        # *   **NO**
        # *   **YES**
        self.hc_status = hc_status
        # The IP address of the host.
        self.host_ip = host_ip
        # The image of the container.
        self.image = image
        # The digest value of the image.
        self.image_digest = image_digest
        # The image ID.
        self.image_id = image_id
        # The name of the image repository.
        self.image_repo_name = image_repo_name
        # The namespace of the image repository.
        self.image_repo_namespace = image_repo_namespace
        # The tag that is added to the image.
        self.image_repo_tag = image_repo_tag
        # The UUID of the image.
        self.image_uuid = image_uuid
        # The instance ID of the asset.
        self.instance_id = instance_id
        # The namespace.
        self.namespace = namespace
        # The node information.
        self.node_info = node_info
        # The name of the node.
        self.node_name = node_name
        # The pod.
        self.pod = pod
        # The IP address of the pod.
        self.pod_ip = pod_ip
        # The region ID of the container.
        self.region_id = region_id
        # The number of risks.
        self.risk_count = risk_count
        # Indicates whether risks exist. Valid values:
        # 
        # *   **NO**
        # *   **YES**
        self.risk_status = risk_status
        # The update identifier of the container.
        self.update_mark = update_mark
        # The number of vulnerabilities that are detected in the container cluster.
        self.vul_count = vul_count
        # Indicates whether vulnerabilities are detected in the container. Valid values:
        # 
        # *   **YES**
        # *   **NO**
        self.vul_status = vul_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_count is not None:
            result['AlarmCount'] = self.alarm_count

        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.exposed is not None:
            result['Exposed'] = self.exposed

        if self.exposed_detail is not None:
            result['ExposedDetail'] = self.exposed_detail

        if self.hc_count is not None:
            result['HcCount'] = self.hc_count

        if self.hc_status is not None:
            result['HcStatus'] = self.hc_status

        if self.host_ip is not None:
            result['HostIp'] = self.host_ip

        if self.image is not None:
            result['Image'] = self.image

        if self.image_digest is not None:
            result['ImageDigest'] = self.image_digest

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_repo_name is not None:
            result['ImageRepoName'] = self.image_repo_name

        if self.image_repo_namespace is not None:
            result['ImageRepoNamespace'] = self.image_repo_namespace

        if self.image_repo_tag is not None:
            result['ImageRepoTag'] = self.image_repo_tag

        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.node_info is not None:
            result['NodeInfo'] = self.node_info

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.pod is not None:
            result['Pod'] = self.pod

        if self.pod_ip is not None:
            result['PodIp'] = self.pod_ip

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.risk_status is not None:
            result['RiskStatus'] = self.risk_status

        if self.update_mark is not None:
            result['UpdateMark'] = self.update_mark

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        if self.vul_status is not None:
            result['VulStatus'] = self.vul_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmCount') is not None:
            self.alarm_count = m.get('AlarmCount')

        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Exposed') is not None:
            self.exposed = m.get('Exposed')

        if m.get('ExposedDetail') is not None:
            self.exposed_detail = m.get('ExposedDetail')

        if m.get('HcCount') is not None:
            self.hc_count = m.get('HcCount')

        if m.get('HcStatus') is not None:
            self.hc_status = m.get('HcStatus')

        if m.get('HostIp') is not None:
            self.host_ip = m.get('HostIp')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImageDigest') is not None:
            self.image_digest = m.get('ImageDigest')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageRepoName') is not None:
            self.image_repo_name = m.get('ImageRepoName')

        if m.get('ImageRepoNamespace') is not None:
            self.image_repo_namespace = m.get('ImageRepoNamespace')

        if m.get('ImageRepoTag') is not None:
            self.image_repo_tag = m.get('ImageRepoTag')

        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NodeInfo') is not None:
            self.node_info = m.get('NodeInfo')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Pod') is not None:
            self.pod = m.get('Pod')

        if m.get('PodIp') is not None:
            self.pod_ip = m.get('PodIp')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('RiskStatus') is not None:
            self.risk_status = m.get('RiskStatus')

        if m.get('UpdateMark') is not None:
            self.update_mark = m.get('UpdateMark')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        if m.get('VulStatus') is not None:
            self.vul_status = m.get('VulStatus')

        return self

