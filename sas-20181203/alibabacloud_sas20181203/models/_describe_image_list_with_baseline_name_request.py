# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeImageListWithBaselineNameRequest(DaraModel):
    def __init__(
        self,
        baseline_name_key: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        container_id: str = None,
        criteria: str = None,
        criteria_type: str = None,
        current_page: int = None,
        image: str = None,
        image_digest: str = None,
        lang: str = None,
        namespace: str = None,
        page_size: int = None,
        pod: str = None,
        repo_instance_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        scan_range: List[str] = None,
    ):
        # The name of the image baseline.
        # 
        # This parameter is required.
        self.baseline_name_key = baseline_name_key
        # The ID of the container cluster.
        # 
        # >  You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the IDs of container clusters.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The ID of the container.
        self.container_id = container_id
        # The search condition for the image baseline.
        self.criteria = criteria
        # The type of the search condition. Valid values:
        # 
        # *   **BaselineNameAlias**: baseline name
        # *   **BaselineClassAlias**: baseline category
        self.criteria_type = criteria_type
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The name of the image to which the container belongs.
        self.image = image
        # The SHA-256 value of the image digest.
        self.image_digest = image_digest
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The namespace.
        self.namespace = namespace
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size
        # The pod.
        self.pod = pod
        # The instance ID of the image repository.
        self.repo_instance_id = repo_instance_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The namespace to which the image repository belongs.
        self.repo_namespace = repo_namespace
        # The types of the assets that you want to scan.
        self.scan_range = scan_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_name_key is not None:
            result['BaselineNameKey'] = self.baseline_name_key

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.criteria_type is not None:
            result['CriteriaType'] = self.criteria_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.image is not None:
            result['Image'] = self.image

        if self.image_digest is not None:
            result['ImageDigest'] = self.image_digest

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pod is not None:
            result['Pod'] = self.pod

        if self.repo_instance_id is not None:
            result['RepoInstanceId'] = self.repo_instance_id

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineNameKey') is not None:
            self.baseline_name_key = m.get('BaselineNameKey')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('CriteriaType') is not None:
            self.criteria_type = m.get('CriteriaType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImageDigest') is not None:
            self.image_digest = m.get('ImageDigest')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Pod') is not None:
            self.pod = m.get('Pod')

        if m.get('RepoInstanceId') is not None:
            self.repo_instance_id = m.get('RepoInstanceId')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        return self

