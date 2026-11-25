# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListRepoTagScanResultResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vulnerabilities: List[main_models.ListRepoTagScanResultResponseBodyVulnerabilities] = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # - `true`: Success
        # 
        # - `false`: Failure
        self.is_success = is_success
        # The page number of the scan result list.
        self.page_no = page_no
        # The number of entries per page in the scan result list.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of scanned vulnerabilities.
        self.total_count = total_count
        # The array of scanned vulnerabilities.
        self.vulnerabilities = vulnerabilities

    def validate(self):
        if self.vulnerabilities:
            for v1 in self.vulnerabilities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Vulnerabilities'] = []
        if self.vulnerabilities is not None:
            for k1 in self.vulnerabilities:
                result['Vulnerabilities'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vulnerabilities = []
        if m.get('Vulnerabilities') is not None:
            for k1 in m.get('Vulnerabilities'):
                temp_model = main_models.ListRepoTagScanResultResponseBodyVulnerabilities()
                self.vulnerabilities.append(temp_model.from_map(k1))

        return self

class ListRepoTagScanResultResponseBodyVulnerabilities(DaraModel):
    def __init__(
        self,
        added_by: str = None,
        alias_name: str = None,
        cve_link: str = None,
        cve_location: str = None,
        cve_name: str = None,
        description: str = None,
        feature: str = None,
        fix_cmd: str = None,
        scan_type: str = None,
        severity: str = None,
        version: str = None,
        version_fixed: str = None,
        version_format: str = None,
    ):
        # The image layer that introduced the vulnerability.
        self.added_by = added_by
        # The vulnerability name.
        self.alias_name = alias_name
        # The vulnerability link.
        self.cve_link = cve_link
        # The vulnerability location.
        self.cve_location = cve_location
        # The vulnerability name.
        self.cve_name = cve_name
        # The vulnerability description.
        self.description = description
        # The feature that introduced the vulnerability.
        self.feature = feature
        # The vulnerability fix command.
        self.fix_cmd = fix_cmd
        # The vulnerability type. Valid values:
        # 
        # - `cve`: System vulnerability
        # 
        # - `sca`: Application vulnerability
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
        # The vulnerability version.
        self.version = version
        # The version that fixes the vulnerability.
        self.version_fixed = version_fixed
        # The version format.
        self.version_format = version_format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.added_by is not None:
            result['AddedBy'] = self.added_by

        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.cve_link is not None:
            result['CveLink'] = self.cve_link

        if self.cve_location is not None:
            result['CveLocation'] = self.cve_location

        if self.cve_name is not None:
            result['CveName'] = self.cve_name

        if self.description is not None:
            result['Description'] = self.description

        if self.feature is not None:
            result['Feature'] = self.feature

        if self.fix_cmd is not None:
            result['FixCmd'] = self.fix_cmd

        if self.scan_type is not None:
            result['ScanType'] = self.scan_type

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.version is not None:
            result['Version'] = self.version

        if self.version_fixed is not None:
            result['VersionFixed'] = self.version_fixed

        if self.version_format is not None:
            result['VersionFormat'] = self.version_format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddedBy') is not None:
            self.added_by = m.get('AddedBy')

        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('CveLink') is not None:
            self.cve_link = m.get('CveLink')

        if m.get('CveLocation') is not None:
            self.cve_location = m.get('CveLocation')

        if m.get('CveName') is not None:
            self.cve_name = m.get('CveName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Feature') is not None:
            self.feature = m.get('Feature')

        if m.get('FixCmd') is not None:
            self.fix_cmd = m.get('FixCmd')

        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionFixed') is not None:
            self.version_fixed = m.get('VersionFixed')

        if m.get('VersionFormat') is not None:
            self.version_format = m.get('VersionFormat')

        return self

