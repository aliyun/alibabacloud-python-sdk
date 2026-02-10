# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAffectedMaliciousFileImagesResponseBody(DaraModel):
    def __init__(
        self,
        affected_malicious_file_images_response: List[main_models.DescribeAffectedMaliciousFileImagesResponseBodyAffectedMaliciousFileImagesResponse] = None,
        page_info: main_models.DescribeAffectedMaliciousFileImagesResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # An array consisting of the images that have malicious image samples.
        self.affected_malicious_file_images_response = affected_malicious_file_images_response
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.affected_malicious_file_images_response:
            for v1 in self.affected_malicious_file_images_response:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AffectedMaliciousFileImagesResponse'] = []
        if self.affected_malicious_file_images_response is not None:
            for k1 in self.affected_malicious_file_images_response:
                result['AffectedMaliciousFileImagesResponse'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.affected_malicious_file_images_response = []
        if m.get('AffectedMaliciousFileImagesResponse') is not None:
            for k1 in m.get('AffectedMaliciousFileImagesResponse'):
                temp_model = main_models.DescribeAffectedMaliciousFileImagesResponseBodyAffectedMaliciousFileImagesResponse()
                self.affected_malicious_file_images_response.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeAffectedMaliciousFileImagesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAffectedMaliciousFileImagesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of images that have malicious image samples returned on the current page.
        self.count = count
        # The page number of the returned page. Pages start from page **1**. Default value: **1**.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **20**.
        self.page_size = page_size
        # The total number of images that have malicious image samples.
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

class DescribeAffectedMaliciousFileImagesResponseBodyAffectedMaliciousFileImagesResponse(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        container_id: str = None,
        digest: str = None,
        download_url: str = None,
        file_path: str = None,
        first_scan_timestamp: int = None,
        high_light: str = None,
        id: int = None,
        image: str = None,
        image_uuid: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        latest_scan_timestamp: int = None,
        latest_verify_timestamp: int = None,
        layer: str = None,
        level: str = None,
        malicious_md_5: str = None,
        namespace: str = None,
        pod: str = None,
        repo_id: str = None,
        repo_instance_id: str = None,
        repo_name: str = None,
        repo_region_id: str = None,
        status: int = None,
        tag: str = None,
        target_id: str = None,
        target_name: str = None,
        target_type: str = None,
        uuid: str = None,
    ):
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The ID of the container.
        self.container_id = container_id
        # The image digest.
        self.digest = digest
        # The URL to download the malicious image sample.
        self.download_url = download_url
        # The path to the image file.
        self.file_path = file_path
        # The timestamp of the first scan.
        self.first_scan_timestamp = first_scan_timestamp
        # The text that is highlighted.
        self.high_light = high_light
        # The ID of alert event.
        self.id = id
        # The name of the image.
        self.image = image
        # The UUID of the image.
        self.image_uuid = image_uuid
        # The name of the ECS instance.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The timestamp of the last scan.
        self.latest_scan_timestamp = latest_scan_timestamp
        # The timestamp of the last verification.
        self.latest_verify_timestamp = latest_verify_timestamp
        # The image layer.
        self.layer = layer
        # The severity of the malicious image sample. Valid values:
        # 
        # *   **serious**
        # *   **suspicious**
        # *   **remind**
        self.level = level
        # The MD5 hash value of the malicious image sample.
        self.malicious_md_5 = malicious_md_5
        # The namespace to which the image repository belongs.
        self.namespace = namespace
        # The pod.
        self.pod = pod
        # The ID of the image repository.
        self.repo_id = repo_id
        # The ID of the container image.
        self.repo_instance_id = repo_instance_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The region ID of the image repository.
        self.repo_region_id = repo_region_id
        # The handling status of the malicious image sample. Valid values:
        # 
        # *   **0**: unhandled
        # *   **1**: handled
        # *   **2**: verifying
        # *   **3**: added to the whitelist
        self.status = status
        # The tag that is added to the image.
        self.tag = tag
        # The ID of the task object.
        self.target_id = target_id
        # The name of the task object.
        self.target_name = target_name
        # The object type. Valid value:
        # 
        # *   **ECS_IMAGE**
        # *   **ECS_SNAPSHOT**
        self.target_type = target_type
        # The UUID of the server.
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

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.first_scan_timestamp is not None:
            result['FirstScanTimestamp'] = self.first_scan_timestamp

        if self.high_light is not None:
            result['HighLight'] = self.high_light

        if self.id is not None:
            result['Id'] = self.id

        if self.image is not None:
            result['Image'] = self.image

        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.latest_scan_timestamp is not None:
            result['LatestScanTimestamp'] = self.latest_scan_timestamp

        if self.latest_verify_timestamp is not None:
            result['LatestVerifyTimestamp'] = self.latest_verify_timestamp

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.level is not None:
            result['Level'] = self.level

        if self.malicious_md_5 is not None:
            result['MaliciousMd5'] = self.malicious_md_5

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.pod is not None:
            result['Pod'] = self.pod

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_instance_id is not None:
            result['RepoInstanceId'] = self.repo_instance_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_region_id is not None:
            result['RepoRegionId'] = self.repo_region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

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

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('FirstScanTimestamp') is not None:
            self.first_scan_timestamp = m.get('FirstScanTimestamp')

        if m.get('HighLight') is not None:
            self.high_light = m.get('HighLight')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('LatestScanTimestamp') is not None:
            self.latest_scan_timestamp = m.get('LatestScanTimestamp')

        if m.get('LatestVerifyTimestamp') is not None:
            self.latest_verify_timestamp = m.get('LatestVerifyTimestamp')

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MaliciousMd5') is not None:
            self.malicious_md_5 = m.get('MaliciousMd5')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Pod') is not None:
            self.pod = m.get('Pod')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoInstanceId') is not None:
            self.repo_instance_id = m.get('RepoInstanceId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoRegionId') is not None:
            self.repo_region_id = m.get('RepoRegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

