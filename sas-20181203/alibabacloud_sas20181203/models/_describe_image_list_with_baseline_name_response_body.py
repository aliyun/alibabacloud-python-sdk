# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageListWithBaselineNameResponseBody(DaraModel):
    def __init__(
        self,
        image_infos: List[main_models.DescribeImageListWithBaselineNameResponseBodyImageInfos] = None,
        page_info: main_models.DescribeImageListWithBaselineNameResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The information about the images.
        self.image_infos = image_infos
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.image_infos:
            for v1 in self.image_infos:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageInfos'] = []
        if self.image_infos is not None:
            for k1 in self.image_infos:
                result['ImageInfos'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_infos = []
        if m.get('ImageInfos') is not None:
            for k1 in m.get('ImageInfos'):
                temp_model = main_models.DescribeImageListWithBaselineNameResponseBodyImageInfos()
                self.image_infos.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeImageListWithBaselineNameResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageListWithBaselineNameResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of the images returned on the current page.
        self.count = count
        # The page number of the returned page. Default value: **1**.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **10**.
        self.page_size = page_size
        # The total number of images on which baseline risks are detected.
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

class DescribeImageListWithBaselineNameResponseBodyImageInfos(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        container_id: str = None,
        digest: str = None,
        first_scan_time: int = None,
        high_risk_image: int = None,
        image: str = None,
        image_create: int = None,
        image_id: str = None,
        image_size: int = None,
        image_update: int = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        last_scan_time: int = None,
        low_risk_image: int = None,
        middle_risk_image: int = None,
        namespace: str = None,
        no_risk_image: int = None,
        pod: str = None,
        region_id: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        repo_type: str = None,
        risk_status: str = None,
        tag: str = None,
        target_id: str = None,
        target_name: str = None,
        target_type: str = None,
        total_item_count: int = None,
        uuid: str = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The ID of the container.
        self.container_id = container_id
        # The SHA-256 value of the image digest.
        self.digest = digest
        # The timestamp generated when the first scan was performed. Unit: milliseconds.
        self.first_scan_time = first_scan_time
        # The number of images on which **high** baseline risks are detected.
        self.high_risk_image = high_risk_image
        # The name of the image.
        self.image = image
        # The timestamp when the image was created. Unit: milliseconds.
        self.image_create = image_create
        # The ID of the image.
        self.image_id = image_id
        # The size of the image.
        self.image_size = image_size
        # The timestamp when the image was updated. Unit: milliseconds.
        self.image_update = image_update
        # The ID of the image instance.
        self.instance_id = instance_id
        # The instance name of the server.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The timestamp when the last baseline check was performed. Unit: milliseconds.
        self.last_scan_time = last_scan_time
        # The number of images on which **low** baseline risks are detected.
        self.low_risk_image = low_risk_image
        # The number of images on which **medium** baseline risks are detected.
        self.middle_risk_image = middle_risk_image
        # The namespace.
        self.namespace = namespace
        # The number of images that do not have baseline risks.
        self.no_risk_image = no_risk_image
        # The pod.
        self.pod = pod
        # The region ID of the image instance.
        self.region_id = region_id
        # The ID of the image repository.
        self.repo_id = repo_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The namespace to which the image repository belongs.
        self.repo_namespace = repo_namespace
        # The type of the image repository.
        self.repo_type = repo_type
        # Indicates whether the image is at risk. Valid values:
        # 
        # *   **YES**
        # *   **NO**
        self.risk_status = risk_status
        # The version of the image.
        self.tag = tag
        # The ID of the asset on which the baseline check is performed.
        self.target_id = target_id
        # The name of the asset on which the baseline check is performed.
        self.target_name = target_name
        # The type of the asset on which the baseline check is performed. Valid values:
        # 
        # *   ECS_IMAGE
        # *   ECS_SNAPSHOT
        self.target_type = target_type
        # The total number of risk items that are detected on the image by using the baseline.
        self.total_item_count = total_item_count
        # The UUID of the image.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.digest is not None:
            result['Digest'] = self.digest

        if self.first_scan_time is not None:
            result['FirstScanTime'] = self.first_scan_time

        if self.high_risk_image is not None:
            result['HighRiskImage'] = self.high_risk_image

        if self.image is not None:
            result['Image'] = self.image

        if self.image_create is not None:
            result['ImageCreate'] = self.image_create

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_size is not None:
            result['ImageSize'] = self.image_size

        if self.image_update is not None:
            result['ImageUpdate'] = self.image_update

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time

        if self.low_risk_image is not None:
            result['LowRiskImage'] = self.low_risk_image

        if self.middle_risk_image is not None:
            result['MiddleRiskImage'] = self.middle_risk_image

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.no_risk_image is not None:
            result['NoRiskImage'] = self.no_risk_image

        if self.pod is not None:
            result['Pod'] = self.pod

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.repo_type is not None:
            result['RepoType'] = self.repo_type

        if self.risk_status is not None:
            result['RiskStatus'] = self.risk_status

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.total_item_count is not None:
            result['TotalItemCount'] = self.total_item_count

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('FirstScanTime') is not None:
            self.first_scan_time = m.get('FirstScanTime')

        if m.get('HighRiskImage') is not None:
            self.high_risk_image = m.get('HighRiskImage')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImageCreate') is not None:
            self.image_create = m.get('ImageCreate')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')

        if m.get('ImageUpdate') is not None:
            self.image_update = m.get('ImageUpdate')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')

        if m.get('LowRiskImage') is not None:
            self.low_risk_image = m.get('LowRiskImage')

        if m.get('MiddleRiskImage') is not None:
            self.middle_risk_image = m.get('MiddleRiskImage')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NoRiskImage') is not None:
            self.no_risk_image = m.get('NoRiskImage')

        if m.get('Pod') is not None:
            self.pod = m.get('Pod')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')

        if m.get('RiskStatus') is not None:
            self.risk_status = m.get('RiskStatus')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TotalItemCount') is not None:
            self.total_item_count = m.get('TotalItemCount')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

