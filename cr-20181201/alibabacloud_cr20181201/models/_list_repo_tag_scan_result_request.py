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
        # The digest of the image.
        self.digest = digest
        # The parameter whose value that you want to query. Fox example, if the value is `FixCmd`, only the `FixCmd` parameter is returned.
        self.filter_value = filter_value
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        self.page_no = page_no
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the image repository.
        self.repo_id = repo_id
        # The ID of the security scan task.
        self.scan_task_id = scan_task_id
        # The type of the vulnerability. Valid values:
        # 
        # *   `cve`: image system vulnerability
        # *   `sca`: image application vulnerability
        self.scan_type = scan_type
        # The severity of the vulnerability. Valid values:
        # 
        # *   `High`
        # *   `Medium`
        # *   `Low`
        # *   `Unknown`
        self.severity = severity
        # The name of the image tag.
        self.tag = tag
        # The keyword for fuzzy search used in scanning. The value can be a CVE name.
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

