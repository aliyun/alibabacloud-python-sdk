# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeGroupedMaliciousFilesRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        current_page: int = None,
        fuzzy_malicious_name: str = None,
        image_digest: str = None,
        image_layer: str = None,
        image_tag: str = None,
        lang: str = None,
        levels: str = None,
        malicious_md_5: str = None,
        page_size: str = None,
        repo_id: str = None,
        repo_instance_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        repo_region_id: str = None,
        scan_range: List[str] = None,
    ):
        # The cluster ID of the container on which the malicious image sample is detected.
        self.cluster_id = cluster_id
        # The number of the page to return. Pages start from page **1**. Default value: **1**.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The name of the malicious image sample that you want to query.
        # 
        # >  Fuzzy match is supported.
        self.fuzzy_malicious_name = fuzzy_malicious_name
        # The image digest.
        self.image_digest = image_digest
        # The image layer.
        self.image_layer = image_layer
        # The image tag.
        self.image_tag = image_tag
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The severity of the malicious image sample that you want to query. You can enter multiple severities. Separate the severities with commas (,). Valid values:
        # 
        # *   **serious**
        # *   **suspicious**
        # *   **remind**
        self.levels = levels
        # The MD5 hash value of the malicious image sample.
        self.malicious_md_5 = malicious_md_5
        # The number of entries to return on each page. Default value: **20**.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the image repository.
        # 
        # >  You can call the [ListRepository](https://help.aliyun.com/document_detail/145293.html) operation to query the IDs of image repositories from the value of the **RepoId** response parameter.
        self.repo_id = repo_id
        # The ID of the container image.
        # 
        # >  You can call the [ListRepository](https://help.aliyun.com/document_detail/145293.html) operation to query the IDs of container images from the value of the **InstanceId** response parameter.
        self.repo_instance_id = repo_instance_id
        # The name of the image repository.
        # 
        # >  Fuzzy match is supported.
        self.repo_name = repo_name
        # The namespace to which the image repository belongs.
        # 
        # >  Fuzzy match is supported.
        self.repo_namespace = repo_namespace
        # The region ID of the image repository. Valid values:
        # 
        # *   **cn-beijing**: China (Beijing)
        # *   **cn-zhangjiakou**: China (Zhangjiakou)
        # *   **cn-hangzhou**: China (Hangzhou)
        # *   **cn-shanghai**: China (Shanghai)
        # *   **cn-shenzhen**: China (Shenzhen)
        # *   **cn-hongkong**: China (Hong Kong)
        # *   **ap-southeast-1**: Singapore
        # *   **ap-southeast-5**: Indonesia (Jakarta)
        # *   **us-east-1**: US (Virginia)
        # *   **us-west-1**: US (Silicon Valley)
        # *   **eu-central-1**: Germany (Frankfurt)
        # *   **eu-west-1**: UK (London)
        self.repo_region_id = repo_region_id
        # The types of the assets that you want to scan.
        self.scan_range = scan_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.fuzzy_malicious_name is not None:
            result['FuzzyMaliciousName'] = self.fuzzy_malicious_name

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

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FuzzyMaliciousName') is not None:
            self.fuzzy_malicious_name = m.get('FuzzyMaliciousName')

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

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

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

        return self

