# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRepoTagScanResultRequest(DaraModel):
    def __init__(
        self,
        digest: str = None,
        filter_value: str = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_id: str = None,
        scan_task_id: str = None,
        scan_type: str = None,
        severity: str = None,
        tag: str = None,
        vul_query_key: str = None,
    ):
        # The image digest.
        self.digest = digest
        # The query filter parameter. If the value is `FixCmd`, only the `FixCmd` result is returned, and other fields are not returned.
        self.filter_value = filter_value
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number of the scan result list.
        self.page_no = page_no
        # The number of entries per page in the scan result list.
        self.page_size = page_size
        # The image repository ID.
        self.repo_id = repo_id
        # The image scan task ID.
        self.scan_task_id = scan_task_id
        # The vulnerability type. Valid values:
        # 
        # - `cve`: Image system vulnerability
        # - `sca`: Image application vulnerability
        self.scan_type = scan_type
        # The severity level of the scanned vulnerability. Valid values:
        # 
        # - `High`: High
        # 
        # - `Medium`: Medium
        # 
        # - `Low`: Low
        # 
        # - `Unknown`: Unknown
        self.severity = severity
        # The image version name.
        self.tag = tag
        # The fuzzy search keyword for scanning. Fuzzy match by CVE name is supported.
        self.vul_query_key = vul_query_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.digest is not None:
            result['Digest'] = self.digest

        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id

        if self.scan_type is not None:
            result['ScanType'] = self.scan_type

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.vul_query_key is not None:
            result['VulQueryKey'] = self.vul_query_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')

        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('VulQueryKey') is not None:
            self.vul_query_key = m.get('VulQueryKey')

        return self

