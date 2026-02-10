# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeImageGroupedVulListRequest(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        cluster_id: str = None,
        current_page: int = None,
        cve_id: str = None,
        group_id: str = None,
        image_digest: str = None,
        image_layer: str = None,
        image_tag: str = None,
        is_latest: int = None,
        lang: str = None,
        name: str = None,
        necessity: str = None,
        page_size: int = None,
        patch_id: int = None,
        repo_id: str = None,
        repo_instance_id: str = None,
        repo_name: str = None,
        repo_namespace: str = None,
        repo_region_id: str = None,
        rule_tag: str = None,
        scan_range: List[str] = None,
        type: str = None,
        uuids: str = None,
    ):
        # The alias of the vulnerability.
        self.alias_name = alias_name
        # The ID of the container cluster.
        # 
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to query the ID of the container cluster.
        self.cluster_id = cluster_id
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The Common Vulnerabilities and Exposures (CVE) ID of the vulnerability.
        self.cve_id = cve_id
        # The ID of the asset group.
        self.group_id = group_id
        # The SHA-256 value of the image digest.
        self.image_digest = image_digest
        # The layer of the image.
        self.image_layer = image_layer
        # The tag of the image.
        self.image_tag = image_tag
        # Specifies whether to query the vulnerabilities in the latest images. If you do not specify this parameter, the vulnerabilities in all images are queried. Valid values:
        # 
        # *   **0**: does not query the vulnerabilities in the latest images.
        # *   **1**: queries the vulnerabilities in the latest images.
        self.is_latest = is_latest
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The name of the vulnerability.
        self.name = name
        # The priority to fix the vulnerability. Valid values:
        # 
        # *   **asap**: high. You must fix the vulnerability at the earliest opportunity.
        # *   **later**: medium. You can fix the vulnerability based on your business requirements.
        # *   **nntf**: low. You can ignore the vulnerability.
        self.necessity = necessity
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # The ID of the patch that is used to fix the vulnerability.
        self.patch_id = patch_id
        # The ID of the image repository.
        self.repo_id = repo_id
        # The instance ID of the image repository.
        self.repo_instance_id = repo_instance_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The namespace to which the image repository belongs.
        self.repo_namespace = repo_namespace
        # The region ID of the image repository.
        self.repo_region_id = repo_region_id
        # The tag of this vulnerability. Valid values:
        # 
        # *   **AI**: AI-related components.
        self.rule_tag = rule_tag
        # An array consisting of the types of the assets that you want to scan.
        self.scan_range = scan_range
        # The type of the vulnerability that you want to query. Valid values:
        # 
        # *   **cve**: image system vulnerability
        # *   **sca**: image application vulnerability
        self.type = type
        # The UUID of the asset. Separate multiple UUIDs with commas (,).
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.cve_id is not None:
            result['CveId'] = self.cve_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.image_digest is not None:
            result['ImageDigest'] = self.image_digest

        if self.image_layer is not None:
            result['ImageLayer'] = self.image_layer

        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag

        if self.is_latest is not None:
            result['IsLatest'] = self.is_latest

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.necessity is not None:
            result['Necessity'] = self.necessity

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.patch_id is not None:
            result['PatchId'] = self.patch_id

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

        if self.rule_tag is not None:
            result['RuleTag'] = self.rule_tag

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        if self.type is not None:
            result['Type'] = self.type

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ImageDigest') is not None:
            self.image_digest = m.get('ImageDigest')

        if m.get('ImageLayer') is not None:
            self.image_layer = m.get('ImageLayer')

        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')

        if m.get('IsLatest') is not None:
            self.is_latest = m.get('IsLatest')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Necessity') is not None:
            self.necessity = m.get('Necessity')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PatchId') is not None:
            self.patch_id = m.get('PatchId')

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

        if m.get('RuleTag') is not None:
            self.rule_tag = m.get('RuleTag')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

