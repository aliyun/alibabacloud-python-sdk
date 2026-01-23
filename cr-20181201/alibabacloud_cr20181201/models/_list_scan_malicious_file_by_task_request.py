# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListScanMaliciousFileByTaskRequest(DaraModel):
    def __init__(
        self,
        digest: str = None,
        instance_id: str = None,
        level: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_id: str = None,
        scan_task_id: str = None,
        tag: str = None,
    ):
        # The image digest.
        self.digest = digest
        # The instance ID.
        self.instance_id = instance_id
        # The severity of the malicious file.
        self.level = level
        # The page number.
        self.page_no = page_no
        # The number of entries per page. Maximum value: 100. If you specify a value greater than 100 for this parameter, the system reports a parameter error or uses 100 as the maximum value.
        self.page_size = page_size
        # The image repository ID.
        self.repo_id = repo_id
        # The ID of the image scan task.
        self.scan_task_id = scan_task_id
        # The image tag.
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

        if self.level is not None:
            result['Level'] = self.level

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

