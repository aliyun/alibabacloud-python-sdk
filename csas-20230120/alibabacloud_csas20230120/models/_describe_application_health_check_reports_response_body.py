# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationHealthCheckReportsResponseBody(DaraModel):
    def __init__(
        self,
        reports: List[main_models.DescribeApplicationHealthCheckReportsResponseBodyReports] = None,
        request_id: str = None,
    ):
        # The list of health check reports.
        self.reports = reports
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.reports:
            for v1 in self.reports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Reports'] = []
        if self.reports is not None:
            for k1 in self.reports:
                result['Reports'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.reports = []
        if m.get('Reports') is not None:
            for k1 in m.get('Reports'):
                temp_model = main_models.DescribeApplicationHealthCheckReportsResponseBodyReports()
                self.reports.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeApplicationHealthCheckReportsResponseBodyReports(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        failed_addresses: List[str] = None,
        failed_regions: List[str] = None,
        failure_count: int = None,
        failure_reasons: List[str] = None,
        health_check_status: str = None,
        mode: str = None,
        success_count: int = None,
    ):
        # The ID of the internal-facing application.
        self.application_id = application_id
        # The list of addresses where health checks failed.
        self.failed_addresses = failed_addresses
        # The list of regions where health checks failed.
        self.failed_regions = failed_regions
        # The number of failed health checks within the query time range.
        self.failure_count = failure_count
        # The list of reasons for health check failures.
        self.failure_reasons = failure_reasons
        # The status calculated based on the latest check result. Valid values:
        # * normal: The success rate of the latest check is greater than or equal to 95%.
        # * partialError: The success rate of the latest check is greater than 0 and less than 95%.
        # * error: The success rate of the latest check is 0.
        # * uncompleted: No check results are available.
        self.health_check_status = health_check_status
        # The health check mode. Valid values:
        # * OnAccess: on-access check
        # * Continuous: continuous check
        self.mode = mode
        # The number of successful health checks within the query time range.
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.failed_addresses is not None:
            result['FailedAddresses'] = self.failed_addresses

        if self.failed_regions is not None:
            result['FailedRegions'] = self.failed_regions

        if self.failure_count is not None:
            result['FailureCount'] = self.failure_count

        if self.failure_reasons is not None:
            result['FailureReasons'] = self.failure_reasons

        if self.health_check_status is not None:
            result['HealthCheckStatus'] = self.health_check_status

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('FailedAddresses') is not None:
            self.failed_addresses = m.get('FailedAddresses')

        if m.get('FailedRegions') is not None:
            self.failed_regions = m.get('FailedRegions')

        if m.get('FailureCount') is not None:
            self.failure_count = m.get('FailureCount')

        if m.get('FailureReasons') is not None:
            self.failure_reasons = m.get('FailureReasons')

        if m.get('HealthCheckStatus') is not None:
            self.health_check_status = m.get('HealthCheckStatus')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        return self

