# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeDiagnoseReportsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        reports: List[main_models.DescribeDiagnoseReportsResponseBodyReports] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The diagnostic reports.
        self.reports = reports
        # The ID of the request.
        self.request_id = request_id
        # The total number of diagnostic reports.
        self.total_count = total_count

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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Reports'] = []
        if self.reports is not None:
            for k1 in self.reports:
                result['Reports'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.reports = []
        if m.get('Reports') is not None:
            for k1 in m.get('Reports'):
                temp_model = main_models.DescribeDiagnoseReportsResponseBodyReports()
                self.reports.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDiagnoseReportsResponseBodyReports(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        details: List[main_models.DescribeDiagnoseReportsResponseBodyReportsDetails] = None,
        diagnose_status: str = None,
        process_status: str = None,
        region_id: str = None,
        report_id: str = None,
        scaling_group_id: str = None,
        user_id: str = None,
    ):
        # The time when the diagnostic report was created.
        self.creation_time = creation_time
        # The details of the diagnostic report.
        self.details = details
        # The status of the diagnostic item. Only the severe status is displayed in the diagnostic report. Valid values:
        # 
        # *   Normal: The diagnostic result is normal.
        # *   Warn: The diagnostic result is warning.
        # *   Critical: The diagnostic result is critical.
        self.diagnose_status = diagnose_status
        # The status of the diagnostic report. Valid values:
        # 
        # *   processing: The diagnosis is in progress.
        # *   Finished: The diagnosis is complete.
        self.process_status = process_status
        # The ID of the region.
        self.region_id = region_id
        # The ID of the diagnostic report.
        self.report_id = report_id
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The user ID of the scaling group.
        self.user_id = user_id

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.diagnose_status is not None:
            result['DiagnoseStatus'] = self.diagnose_status

        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.report_id is not None:
            result['ReportId'] = self.report_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.DescribeDiagnoseReportsResponseBodyReportsDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('DiagnoseStatus') is not None:
            self.diagnose_status = m.get('DiagnoseStatus')

        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReportId') is not None:
            self.report_id = m.get('ReportId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeDiagnoseReportsResponseBodyReportsDetails(DaraModel):
    def __init__(
        self,
        diagnose_type: str = None,
        error_code: str = None,
        resource_id: str = None,
        status: str = None,
    ):
        # The type of the diagnostic item. Valid values:
        # 
        # *   AccountArrearage: Checks whether your Alibaba Cloud account has overdue payments.
        # *   AccountNotEnoughBalance: Checks whether the balance of your Alibaba Cloud account at the China site (aliyun.com) is greater than or equal to CNY 100.
        # *   ElasticStrength: Checks whether the instance types that are specified in the scaling configuration are sufficient.
        # *   VSwitch: Checks whether a specific vSwitch can work as expected. For example, if a vSwitch is deleted, the vSwitch cannot provide services and an exception occurs.
        # *   SecurityGroup: Checks whether a specific security group can work as expected. For example, if a security group is deleted, the security group cannot provide services and an exception occurs.
        # *   KeyPair: Checks whether the key pair is available. If the specified key pair is deleted, specify another key pair for the scaling group.
        # *   SlbBackendServerQuota: Checks whether the number of ECS instances that are added to the default server group and the vServer groups of the SLB instances associated with the scaling group has reached the upper limit.
        # *   AlbBackendServerQuota: Checks whether the number of ECS instances that are added to the backend server groups of the ALB instances associated with the scaling group has reached the upper limit.
        # *   NlbBackendServerQuota: Checks whether the number of ECS instances that are added to the backend server groups of the NLB instances associated with the scaling group has reached the upper limit.
        self.diagnose_type = diagnose_type
        # The error code of the diagnostic item. Valid values:
        # 
        # *   VSwitchIdNotFound: The vSwitch does not exist.
        # *   SecurityGroupNotFound: The security group does not exist.
        # *   KeyPairNotFound: The key pair does not exist.
        # *   SlbBackendServerQuotaExceeded: The number of ECS instances that are added to the default server group and the vServer groups of the SLB instances associated with the scaling group has reached the upper limit.
        # *   AlbBackendServerQuotaExceeded: The number of ECS instances that are attached to the ALB instances of the scaling group has reached the upper limit.
        # *   NlbBackendServerQuotaExceeded: The number of ECS instances that are attached to the NLB instances of the scaling group has reached the upper limit.
        # *   AccountArrearage: Your account has overdue payments.
        # *   AccountNotEnoughBalance: The balance of your Alibaba Cloud account is less than CNY 100.
        # *   ElasticStrengthAlert: The inventory levels are lower than expected.
        self.error_code = error_code
        # The ID of the resource.
        self.resource_id = resource_id
        # The status of the diagnostic item. Valid values:
        # 
        # *   Normal: The diagnostic result is normal.
        # *   Warn: The diagnostic result is warning.
        # *   Critical: The diagnostic result is critical.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diagnose_type is not None:
            result['DiagnoseType'] = self.diagnose_type

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnoseType') is not None:
            self.diagnose_type = m.get('DiagnoseType')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

