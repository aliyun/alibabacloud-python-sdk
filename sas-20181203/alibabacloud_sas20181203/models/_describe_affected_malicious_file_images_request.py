# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAffectedMaliciousFileImagesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        container_id: str = None,
        current_page: int = None,
        image: str = None,
        image_digest: str = None,
        image_layer: str = None,
        image_tag: str = None,
        lang: str = None,
        levels: str = None,
        malicious_md_5: str = None,
        namespace: str = None,
        page_size: str = None,
        pod: str = None,
        repo_id: str = None,
        repo_instance_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        repo_region_id: str = None,
        scan_range: List[str] = None,
        status: str = None,
    ):
        # The ID of the container cluster to query.
        # > Call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to obtain this parameter.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The ID of the container.
        self.container_id = container_id
        # The page number of the current page when using paging. Minimum value: **1**. Default value: **1**.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The name of the container image.
        self.image = image
        # The digest of the image.
        self.image_digest = image_digest
        # The layer of the image.
        self.image_layer = image_layer
        # The tag of the image.
        self.image_tag = image_tag
        # The language type of the request and response. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The severity levels. Separate multiple values with commas (,). Valid values:
        # * **serious**: urgent
        # * **suspicious**: suspicious
        # * **remind**: reminder.
        self.levels = levels
        # The MD5 hash of the malicious file.
        # > Call the [DescribeGroupedMaliciousFiles](~~DescribeGroupedMaliciousFiles~~) operation to obtain the MD5 hash of the malicious file.
        self.malicious_md_5 = malicious_md_5
        # The namespace.
        self.namespace = namespace
        # The maximum number of entries per page when using paging. Default value: **20**.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The pod.
        self.pod = pod
        # The ID of the image repository.
        # > Call the [ListRepository](https://help.aliyun.com/document_detail/145293.html) operation of Container Registry. You can obtain the image repository ID from the **RepoId** response parameter.
        self.repo_id = repo_id
        # The ID of the container image instance.
        # > Call the [ListRepository](https://help.aliyun.com/document_detail/145293.html) operation of Container Registry. You can obtain the container image instance ID from the **InstanceId** response parameter.
        self.repo_instance_id = repo_instance_id
        # The name of the image repository.
        # > Fuzzy match is supported.
        self.repo_name = repo_name
        # The namespace of the image repository.
        # > Fuzzy match is supported.
        self.repo_namespace = repo_namespace
        # The region ID of the image repository. Valid values:
        # - **cn-beijing**: China (Beijing)
        # - **cn-zhangjiakou**: China (Zhangjiakou)
        # - **cn-hangzhou**: China (Hangzhou)
        # - **cn-shanghai**: China (Shanghai)
        # - **cn-shenzhen**: China (Shenzhen)
        # - **cn-hongkong**: Hong Kong (China)
        # - **ap-southeast-1**: Singapore
        # - **ap-southeast-5**: Indonesia (Jakarta)
        # - **us-east-1**: US (Virginia)
        # - **us-west-1**: US (Silicon Valley)
        # - **eu-central-1**: Germany (Frankfurt)
        # - **eu-west-1**: UK (London).
        self.repo_region_id = repo_region_id
        # The collection of scan ranges.
        self.scan_range = scan_range
        # The processing status of the malicious image sample. Valid values:
        # - **0**: unhandled
        # - **1**: handled
        # - **2**: verifying
        # - **3**: added to whitelist.
        self.status = status

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

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.image is not None:
            result['Image'] = self.image

        if self.image_digest is not None:
            result['ImageDigest'] = self.image_digest

        if self.image_layer is not None:
            result['ImageLayer'] = self.image_layer

        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.levels is not None:
            result['Levels'] = self.levels

        if self.malicious_md_5 is not None:
            result['MaliciousMd5'] = self.malicious_md_5

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pod is not None:
            result['Pod'] = self.pod

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_instance_id is not None:
            result['RepoInstanceId'] = self.repo_instance_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.repo_region_id is not None:
            result['RepoRegionId'] = self.repo_region_id

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImageDigest') is not None:
            self.image_digest = m.get('ImageDigest')

        if m.get('ImageLayer') is not None:
            self.image_layer = m.get('ImageLayer')

        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Levels') is not None:
            self.levels = m.get('Levels')

        if m.get('MaliciousMd5') is not None:
            self.malicious_md_5 = m.get('MaliciousMd5')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pod') is not None:
            self.pod = m.get('Pod')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoInstanceId') is not None:
            self.repo_instance_id = m.get('RepoInstanceId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('RepoRegionId') is not None:
            self.repo_region_id = m.get('RepoRegionId')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

