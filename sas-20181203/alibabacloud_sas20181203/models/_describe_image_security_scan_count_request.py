# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeImageSecurityScanCountRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        dealed: str = None,
        image_digest: str = None,
        image_tag: str = None,
        image_uuid: str = None,
        repo_id: str = None,
        repo_instance_id: str = None,
        repo_region_id: str = None,
        scan_range: List[str] = None,
        uuids: List[str] = None,
    ):
        # The ID of the cluster that you want to scan.
        self.cluster_id = cluster_id
        # The handling status. Valid values:
        # 
        # *   **Y**: handled.
        # *   **N**: unhandled.
        # *   **A**: all.
        self.dealed = dealed
        # The SHA-256 value of the image digest.
        self.image_digest = image_digest
        # The tag of the image.
        self.image_tag = image_tag
        # The UUID of the image.
        self.image_uuid = image_uuid
        # The ID of the Container Registry repository.
        self.repo_id = repo_id
        # The ID of the Container Registry instance.
        # 
        # >  You can call the [DescribeImageInstances](~~DescribeImageInstances~~) operation to obtain the ID.
        self.repo_instance_id = repo_instance_id
        # The region ID of the Container Registry repository.
        self.repo_region_id = repo_region_id
        # The assets that you want to scan.
        self.scan_range = scan_range
        # The IDs of the instances that you want to scan.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.dealed is not None:
            result['Dealed'] = self.dealed

        if self.image_digest is not None:
            result['ImageDigest'] = self.image_digest

        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag

        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.repo_instance_id is not None:
            result['RepoInstanceId'] = self.repo_instance_id

        if self.repo_region_id is not None:
            result['RepoRegionId'] = self.repo_region_id

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Dealed') is not None:
            self.dealed = m.get('Dealed')

        if m.get('ImageDigest') is not None:
            self.image_digest = m.get('ImageDigest')

        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')

        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RepoInstanceId') is not None:
            self.repo_instance_id = m.get('RepoInstanceId')

        if m.get('RepoRegionId') is not None:
            self.repo_region_id = m.get('RepoRegionId')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

