# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeVulDesktopsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        vul_desktops: List[main_models.DescribeVulDesktopsResponseBodyVulDesktops] = None,
    ):
        # The number of entries per page in a paged query.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token for the next query. An empty value indicates that no more results exist.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # The list of cloud computers affected by the vulnerability.
        self.vul_desktops = vul_desktops

    def validate(self):
        if self.vul_desktops:
            for v1 in self.vul_desktops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VulDesktops'] = []
        if self.vul_desktops is not None:
            for k1 in self.vul_desktops:
                result['VulDesktops'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vul_desktops = []
        if m.get('VulDesktops') is not None:
            for k1 in m.get('VulDesktops'):
                temp_model = main_models.DescribeVulDesktopsResponseBodyVulDesktops()
                self.vul_desktops.append(temp_model.from_map(k1))

        return self

class DescribeVulDesktopsResponseBodyVulDesktops(DaraModel):
    def __init__(
        self,
        config_group_id: str = None,
        cve_count: int = None,
        cves: List[main_models.DescribeVulDesktopsResponseBodyVulDesktopsCves] = None,
        desktop_id: str = None,
        disabled: bool = None,
        first_found_time: str = None,
        fix_records: List[main_models.DescribeVulDesktopsResponseBodyVulDesktopsFixRecords] = None,
        patch_ids: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        vul_level: str = None,
    ):
        # The configuration task ID.
        self.config_group_id = config_group_id
        # The number of vulnerabilities.
        self.cve_count = cve_count
        # The list of vulnerability details.
        self.cves = cves
        # The ID of the cloud computer affected by the vulnerability.
        self.desktop_id = desktop_id
        # Indicates whether the activation code is disabled.
        self.disabled = disabled
        # The time when the vulnerability was first discovered.
        self.first_found_time = first_found_time
        # The list of fix records for the cloud computer.
        self.fix_records = fix_records
        # The list of patch IDs.
        self.patch_ids = patch_ids
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by WUYING Workspace.
        self.region_id = region_id
        # The enterprise resource group ID.
        self.resource_group_id = resource_group_id
        # The fix status of the patch.
        self.status = status
        # The patch level.
        self.vul_level = vul_level

    def validate(self):
        if self.cves:
            for v1 in self.cves:
                 if v1:
                    v1.validate()
        if self.fix_records:
            for v1 in self.fix_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_group_id is not None:
            result['ConfigGroupId'] = self.config_group_id

        if self.cve_count is not None:
            result['CveCount'] = self.cve_count

        result['Cves'] = []
        if self.cves is not None:
            for k1 in self.cves:
                result['Cves'].append(k1.to_map() if k1 else None)

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.first_found_time is not None:
            result['FirstFoundTime'] = self.first_found_time

        result['FixRecords'] = []
        if self.fix_records is not None:
            for k1 in self.fix_records:
                result['FixRecords'].append(k1.to_map() if k1 else None)

        if self.patch_ids is not None:
            result['PatchIds'] = self.patch_ids

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigGroupId') is not None:
            self.config_group_id = m.get('ConfigGroupId')

        if m.get('CveCount') is not None:
            self.cve_count = m.get('CveCount')

        self.cves = []
        if m.get('Cves') is not None:
            for k1 in m.get('Cves'):
                temp_model = main_models.DescribeVulDesktopsResponseBodyVulDesktopsCves()
                self.cves.append(temp_model.from_map(k1))

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('FirstFoundTime') is not None:
            self.first_found_time = m.get('FirstFoundTime')

        self.fix_records = []
        if m.get('FixRecords') is not None:
            for k1 in m.get('FixRecords'):
                temp_model = main_models.DescribeVulDesktopsResponseBodyVulDesktopsFixRecords()
                self.fix_records.append(temp_model.from_map(k1))

        if m.get('PatchIds') is not None:
            self.patch_ids = m.get('PatchIds')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')

        return self

class DescribeVulDesktopsResponseBodyVulDesktopsFixRecords(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        fix_failure_reason: str = None,
        fix_result: str = None,
        fix_time: str = None,
        fix_type: str = None,
    ):
        # The batch ID of the scheduled task execution.
        self.batch_id = batch_id
        # The failure reason.
        self.fix_failure_reason = fix_failure_reason
        # The fix result.
        self.fix_result = fix_result
        # The timestamp when the fix task ended, in milliseconds.
        self.fix_time = fix_time
        # The fix type.
        self.fix_type = fix_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.fix_failure_reason is not None:
            result['FixFailureReason'] = self.fix_failure_reason

        if self.fix_result is not None:
            result['FixResult'] = self.fix_result

        if self.fix_time is not None:
            result['FixTime'] = self.fix_time

        if self.fix_type is not None:
            result['FixType'] = self.fix_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('FixFailureReason') is not None:
            self.fix_failure_reason = m.get('FixFailureReason')

        if m.get('FixResult') is not None:
            self.fix_result = m.get('FixResult')

        if m.get('FixTime') is not None:
            self.fix_time = m.get('FixTime')

        if m.get('FixType') is not None:
            self.fix_type = m.get('FixType')

        return self

class DescribeVulDesktopsResponseBodyVulDesktopsCves(DaraModel):
    def __init__(
        self,
        cve_id: str = None,
        cve_level: str = None,
        cve_title: str = None,
        cve_url: str = None,
        impact_score: str = None,
        reference_url: str = None,
        release_time: str = None,
    ):
        # The CVE ID.
        self.cve_id = cve_id
        # The vulnerability level.
        self.cve_level = cve_level
        # The vulnerability name.
        self.cve_title = cve_title
        # The CVE URL.
        self.cve_url = cve_url
        # The vulnerability score.
        self.impact_score = impact_score
        # The reference URL.
        self.reference_url = reference_url
        # The release time. The time follows the ISO 8601 standard in UTC: yyyy-MM-ddTHH:mm:ssZ.
        self.release_time = release_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cve_id is not None:
            result['CveId'] = self.cve_id

        if self.cve_level is not None:
            result['CveLevel'] = self.cve_level

        if self.cve_title is not None:
            result['CveTitle'] = self.cve_title

        if self.cve_url is not None:
            result['CveUrl'] = self.cve_url

        if self.impact_score is not None:
            result['ImpactScore'] = self.impact_score

        if self.reference_url is not None:
            result['ReferenceUrl'] = self.reference_url

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')

        if m.get('CveLevel') is not None:
            self.cve_level = m.get('CveLevel')

        if m.get('CveTitle') is not None:
            self.cve_title = m.get('CveTitle')

        if m.get('CveUrl') is not None:
            self.cve_url = m.get('CveUrl')

        if m.get('ImpactScore') is not None:
            self.impact_score = m.get('ImpactScore')

        if m.get('ReferenceUrl') is not None:
            self.reference_url = m.get('ReferenceUrl')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        return self

