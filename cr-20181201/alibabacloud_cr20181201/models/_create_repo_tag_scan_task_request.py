# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRepoTagScanTaskRequest(DaraModel):
    def __init__(
        self,
        digest: str = None,
        instance_id: str = None,
        repo_id: str = None,
        scan_service: str = None,
        scan_type: str = None,
        tag: str = None,
    ):
        # The digest of the image.
        self.digest = digest
        # The ID of the Container Registry instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
        self.repo_id = repo_id
        # The type of the scanning engine.
        # 
        # *   `SAS_SCAN_SERVICE`: Security Center scan engine (paid service)
        # *   `ACR_SCAN_SERVICE`: Container Registry scan engine
        self.scan_service = scan_service
        self.scan_type = scan_type
        # The image version.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.digest is not None:
            result['Digest'] = self.digest

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.scan_service is not None:
            result['ScanService'] = self.scan_service

        if self.scan_type is not None:
            result['ScanType'] = self.scan_type

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('ScanService') is not None:
            self.scan_service = m.get('ScanService')

        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

