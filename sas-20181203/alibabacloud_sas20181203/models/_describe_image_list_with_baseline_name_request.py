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
        # The name of the image baseline check result.
        # 
        # This parameter is required.
        self.baseline_name_key = baseline_name_key
        # The ID of the container cluster to query.
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to obtain this parameter.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The container ID.
        self.container_id = container_id
        # The query condition for the baseline.
        self.criteria = criteria
        # The query type for the baseline. Valid values:
        # 
        # - **BaselineNameAlias**: baseline name
        # - **BaselineClassAlias**: baseline category.
        self.criteria_type = criteria_type
        # The page number of the page to return. Default value: **1**, which indicates that the first page is returned.
        self.current_page = current_page
        # The container image name.
        self.image = image
        # The SHA256 value of the image digest.
        self.image_digest = image_digest
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The namespace.
        self.namespace = namespace
        # Settings for paged query paging. The number of image baseline check result details to display per page. Default value: **10**, which indicates that 10 image baseline check result details are displayed per page.
        self.page_size = page_size
        # The pod.
        self.pod = pod
        # The instance ID of the image repository.
        self.repo_instance_id = repo_instance_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The namespace of the image repository.
        self.repo_namespace = repo_namespace
        # The collection of scan ranges.
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

