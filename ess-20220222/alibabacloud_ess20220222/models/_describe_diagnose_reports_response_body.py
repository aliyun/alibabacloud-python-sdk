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
        # The list of diagnostic reports.
        self.reports = reports
        # Id of the request
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
        # The time when the diagnostic report was created. The time is displayed in UTC and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format.
        self.creation_time = creation_time
        # The details of the diagnostic report.
        self.details = details
        # The diagnostic status. The value is the most severe status among the diagnostic details. Valid values:
        # 
        # - Normal: the diagnostic result is normal.
        # 
        # - Warn: the diagnostic result is a warning.
        # 
        # - Critical: the diagnostic result is critical.
        self.diagnose_status = diagnose_status
        # The status of the diagnostic report. Valid values:
        # 
        # - Processing: in progress.
        # 
        # - Finished: completed.
        self.process_status = process_status
        # The region ID.
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
        # - AccountArrearage: account overdue payment. Checks whether the user account has overdue payments.
        # 
        # - AccountNotEnoughBalance: insufficient account balance. Checks whether the balance of a user account on the China site is greater than or equal to CNY 100.
        # 
        # - ElasticStrength: inventory health. Checks the inventory health of the instance type configured for the scaling group.
        # 
        # - VSwitch: vSwitch status. Checks whether the vSwitch is active, such as whether it is deleted.
        # 
        # - SecurityGroup: security group status. Checks whether the security group is active, such as whether it is deleted.
        # 
        # - KeyPair: key pair status. Checks whether the key pair is active, such as whether it is deleted.
        # 
        # - SlbBackendServerQuota: number of instances mounted to the SLB instance in the scaling group. Checks whether the number of ECS instances mounted to the default server group and virtual service groups of the SLB instance exceeds the quota.
        # 
        # - AlbBackendServerQuota: number of instances mounted to the ALB instance in the scaling group. Checks whether the number of ECS instances mounted to the server groups of the ALB instance exceeds the quota.
        # 
        # - NlbBackendServerQuota: number of instances mounted to the NLB instance in the scaling group. Checks whether the number of ECS instances mounted to the server groups of the NLB instance exceeds the quota.
        self.diagnose_type = diagnose_type
        # The error code of the diagnostic item. Valid values:
        # 
        # - VSwitchIdNotFound: the vSwitch does not exist.
        # 
        # - SecurityGroupNotFound: the security group does not exist.
        # 
        # - KeyPairNotFound: the key pair does not exist.
        # 
        # - SlbBackendServerQuotaExceeded: the number of ECS instances mounted to the default server group and virtual service groups of the SLB instance exceeds the quota.
        # 
        # - AlbBackendServerQuotaExceeded: the number of ECS instances mounted to the server groups of the ALB instance exceeds the quota.
        # 
        # - NlbBackendServerQuotaExceeded: the number of ECS instances mounted to the server groups of the NLB instance exceeds the quota.
        # 
        # - AccountArrearage: the account has overdue payments.
        # 
        # - AccountNotEnoughBalance: the account balance is insufficient (less than CNY 100).
        # 
        # - ElasticStrengthAlert: the inventory health is poor.
        self.error_code = error_code
        # The resource ID.
        self.resource_id = resource_id
        # The diagnostic status of the diagnostic item. Valid values:
        # 
        # - Normal: the diagnostic result is normal.
        # 
        # - Warn: the diagnostic result is a warning.
        # 
        # - Critical: the diagnostic result is critical.
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

