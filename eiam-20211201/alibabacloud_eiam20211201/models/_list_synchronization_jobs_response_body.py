# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListSynchronizationJobsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        synchronization_jobs: List[main_models.ListSynchronizationJobsResponseBodySynchronizationJobs] = None,
        total_count: int = None,
    ):
        # The token to retrieve the next page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # A list of sync task information.
        self.synchronization_jobs = synchronization_jobs
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.synchronization_jobs:
            for v1 in self.synchronization_jobs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SynchronizationJobs'] = []
        if self.synchronization_jobs is not None:
            for k1 in self.synchronization_jobs:
                result['SynchronizationJobs'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.synchronization_jobs = []
        if m.get('SynchronizationJobs') is not None:
            for k1 in m.get('SynchronizationJobs'):
                temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobs()
                self.synchronization_jobs.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobs(DaraModel):
    def __init__(
        self,
        description: str = None,
        direction: str = None,
        end_time: int = None,
        result: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResult = None,
        start_time: int = None,
        status: str = None,
        synchronization_job_id: str = None,
        target_id: str = None,
        target_type: str = None,
        trigger_type: str = None,
    ):
        # The description of the sync task.
        self.description = description
        # The direction of the sync task. Valid values:
        # 
        # - ingress: Inbound.
        # 
        # - egress: Outbound.
        self.direction = direction
        # The synchronization end time. The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The result of the sync task.
        self.result = result
        # The synchronization start time. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time
        # The status of the sync task. Valid values:
        # 
        # - pending: The task is pending.
        # 
        # - running: The task is running.
        # 
        # - failed: The task failed.
        # 
        # - partial_success: The task is partially successful.
        # 
        # - success: The task is successful.
        self.status = status
        # The sync task ID.
        self.synchronization_job_id = synchronization_job_id
        # The synchronization target ID.
        self.target_id = target_id
        # The type of the synchronization target. Valid values:
        # 
        # - identity_provider: Identity provider.
        # 
        # - application: Application.
        self.target_type = target_type
        # The trigger type of the synchronization. Valid values:
        # 
        # - auto: Automatic.
        # 
        # - manual: Manual.
        self.trigger_type = trigger_type

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.synchronization_job_id is not None:
            result['SynchronizationJobId'] = self.synchronization_job_id

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Result') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SynchronizationJobId') is not None:
            self.synchronization_job_id = m.get('SynchronizationJobId')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        group_member_statistics: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatistics = None,
        group_statistics: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatistics = None,
        organizational_unit_statistics: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatistics = None,
        user_statistics: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatistics = None,
    ):
        # The error code for the synchronization result.
        self.error_code = error_code
        # The error message for the synchronization result.
        self.error_message = error_message
        # The statistics of group member synchronization results.
        self.group_member_statistics = group_member_statistics
        # The statistics of group synchronization results.
        self.group_statistics = group_statistics
        # The statistics of organization synchronization results.
        self.organizational_unit_statistics = organizational_unit_statistics
        # The statistics of user synchronization results.
        self.user_statistics = user_statistics

    def validate(self):
        if self.group_member_statistics:
            self.group_member_statistics.validate()
        if self.group_statistics:
            self.group_statistics.validate()
        if self.organizational_unit_statistics:
            self.organizational_unit_statistics.validate()
        if self.user_statistics:
            self.user_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.group_member_statistics is not None:
            result['GroupMemberStatistics'] = self.group_member_statistics.to_map()

        if self.group_statistics is not None:
            result['GroupStatistics'] = self.group_statistics.to_map()

        if self.organizational_unit_statistics is not None:
            result['OrganizationalUnitStatistics'] = self.organizational_unit_statistics.to_map()

        if self.user_statistics is not None:
            result['UserStatistics'] = self.user_statistics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('GroupMemberStatistics') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatistics()
            self.group_member_statistics = temp_model.from_map(m.get('GroupMemberStatistics'))

        if m.get('GroupStatistics') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatistics()
            self.group_statistics = temp_model.from_map(m.get('GroupStatistics'))

        if m.get('OrganizationalUnitStatistics') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatistics()
            self.organizational_unit_statistics = temp_model.from_map(m.get('OrganizationalUnitStatistics'))

        if m.get('UserStatistics') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatistics()
            self.user_statistics = temp_model.from_map(m.get('UserStatistics'))

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatistics(DaraModel):
    def __init__(
        self,
        binded: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsBinded = None,
        created: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsCreated = None,
        deleted: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsDeleted = None,
        exported: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsExported = None,
        pushed: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsPushed = None,
        same: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsSame = None,
        updated: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsUpdated = None,
    ):
        # The statistics of binding results.
        self.binded = binded
        # The statistics of creation results.
        self.created = created
        # The statistics of deletion results.
        self.deleted = deleted
        # The statistics of export results.
        self.exported = exported
        # The statistics of push results.
        self.pushed = pushed
        # The statistics of identical entries.
        self.same = same
        # The statistics of update results.
        self.updated = updated

    def validate(self):
        if self.binded:
            self.binded.validate()
        if self.created:
            self.created.validate()
        if self.deleted:
            self.deleted.validate()
        if self.exported:
            self.exported.validate()
        if self.pushed:
            self.pushed.validate()
        if self.same:
            self.same.validate()
        if self.updated:
            self.updated.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binded is not None:
            result['Binded'] = self.binded.to_map()

        if self.created is not None:
            result['Created'] = self.created.to_map()

        if self.deleted is not None:
            result['Deleted'] = self.deleted.to_map()

        if self.exported is not None:
            result['Exported'] = self.exported.to_map()

        if self.pushed is not None:
            result['Pushed'] = self.pushed.to_map()

        if self.same is not None:
            result['Same'] = self.same.to_map()

        if self.updated is not None:
            result['Updated'] = self.updated.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Binded') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsBinded()
            self.binded = temp_model.from_map(m.get('Binded'))

        if m.get('Created') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsCreated()
            self.created = temp_model.from_map(m.get('Created'))

        if m.get('Deleted') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsDeleted()
            self.deleted = temp_model.from_map(m.get('Deleted'))

        if m.get('Exported') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsExported()
            self.exported = temp_model.from_map(m.get('Exported'))

        if m.get('Pushed') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsPushed()
            self.pushed = temp_model.from_map(m.get('Pushed'))

        if m.get('Same') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsSame()
            self.same = temp_model.from_map(m.get('Same'))

        if m.get('Updated') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsUpdated()
            self.updated = temp_model.from_map(m.get('Updated'))

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsUpdated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsSame(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsPushed(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsExported(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsDeleted(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsCreated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultUserStatisticsBinded(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatistics(DaraModel):
    def __init__(
        self,
        binded: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsBinded = None,
        created: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsCreated = None,
        deleted: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsDeleted = None,
        pushed: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsPushed = None,
        same: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsSame = None,
        updated: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsUpdated = None,
    ):
        # The statistics of binding results.
        self.binded = binded
        # The statistics of creation results.
        self.created = created
        # The statistics of deletion results.
        self.deleted = deleted
        # The statistics of push results.
        self.pushed = pushed
        # The statistics of identical entries.
        self.same = same
        # The statistics of update results.
        self.updated = updated

    def validate(self):
        if self.binded:
            self.binded.validate()
        if self.created:
            self.created.validate()
        if self.deleted:
            self.deleted.validate()
        if self.pushed:
            self.pushed.validate()
        if self.same:
            self.same.validate()
        if self.updated:
            self.updated.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binded is not None:
            result['Binded'] = self.binded.to_map()

        if self.created is not None:
            result['Created'] = self.created.to_map()

        if self.deleted is not None:
            result['Deleted'] = self.deleted.to_map()

        if self.pushed is not None:
            result['Pushed'] = self.pushed.to_map()

        if self.same is not None:
            result['Same'] = self.same.to_map()

        if self.updated is not None:
            result['Updated'] = self.updated.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Binded') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsBinded()
            self.binded = temp_model.from_map(m.get('Binded'))

        if m.get('Created') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsCreated()
            self.created = temp_model.from_map(m.get('Created'))

        if m.get('Deleted') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsDeleted()
            self.deleted = temp_model.from_map(m.get('Deleted'))

        if m.get('Pushed') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsPushed()
            self.pushed = temp_model.from_map(m.get('Pushed'))

        if m.get('Same') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsSame()
            self.same = temp_model.from_map(m.get('Same'))

        if m.get('Updated') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsUpdated()
            self.updated = temp_model.from_map(m.get('Updated'))

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsUpdated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsSame(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsPushed(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsDeleted(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsCreated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultOrganizationalUnitStatisticsBinded(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatistics(DaraModel):
    def __init__(
        self,
        binded: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsBinded = None,
        created: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsCreated = None,
        deleted: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsDeleted = None,
        pushed: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsPushed = None,
        same: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsSame = None,
        updated: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsUpdated = None,
    ):
        # The statistics of binding results.
        self.binded = binded
        # The statistics of creation results.
        self.created = created
        # The statistics of deletion results.
        self.deleted = deleted
        # The statistics of push results.
        self.pushed = pushed
        # The statistics of identical entries.
        self.same = same
        # The statistics of update results.
        self.updated = updated

    def validate(self):
        if self.binded:
            self.binded.validate()
        if self.created:
            self.created.validate()
        if self.deleted:
            self.deleted.validate()
        if self.pushed:
            self.pushed.validate()
        if self.same:
            self.same.validate()
        if self.updated:
            self.updated.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binded is not None:
            result['Binded'] = self.binded.to_map()

        if self.created is not None:
            result['Created'] = self.created.to_map()

        if self.deleted is not None:
            result['Deleted'] = self.deleted.to_map()

        if self.pushed is not None:
            result['Pushed'] = self.pushed.to_map()

        if self.same is not None:
            result['Same'] = self.same.to_map()

        if self.updated is not None:
            result['Updated'] = self.updated.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Binded') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsBinded()
            self.binded = temp_model.from_map(m.get('Binded'))

        if m.get('Created') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsCreated()
            self.created = temp_model.from_map(m.get('Created'))

        if m.get('Deleted') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsDeleted()
            self.deleted = temp_model.from_map(m.get('Deleted'))

        if m.get('Pushed') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsPushed()
            self.pushed = temp_model.from_map(m.get('Pushed'))

        if m.get('Same') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsSame()
            self.same = temp_model.from_map(m.get('Same'))

        if m.get('Updated') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsUpdated()
            self.updated = temp_model.from_map(m.get('Updated'))

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsUpdated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsSame(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsPushed(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsDeleted(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsCreated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupStatisticsBinded(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatistics(DaraModel):
    def __init__(
        self,
        binded: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsBinded = None,
        created: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsCreated = None,
        deleted: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsDeleted = None,
        pushed: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsPushed = None,
        same: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsSame = None,
        updated: main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsUpdated = None,
    ):
        # The statistics of binding results.
        self.binded = binded
        # The statistics of creation results.
        self.created = created
        # The statistics of deletion results.
        self.deleted = deleted
        # The statistics of push results.
        self.pushed = pushed
        # The statistics of identical entries.
        self.same = same
        # The statistics of update results.
        self.updated = updated

    def validate(self):
        if self.binded:
            self.binded.validate()
        if self.created:
            self.created.validate()
        if self.deleted:
            self.deleted.validate()
        if self.pushed:
            self.pushed.validate()
        if self.same:
            self.same.validate()
        if self.updated:
            self.updated.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binded is not None:
            result['Binded'] = self.binded.to_map()

        if self.created is not None:
            result['Created'] = self.created.to_map()

        if self.deleted is not None:
            result['Deleted'] = self.deleted.to_map()

        if self.pushed is not None:
            result['Pushed'] = self.pushed.to_map()

        if self.same is not None:
            result['Same'] = self.same.to_map()

        if self.updated is not None:
            result['Updated'] = self.updated.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Binded') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsBinded()
            self.binded = temp_model.from_map(m.get('Binded'))

        if m.get('Created') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsCreated()
            self.created = temp_model.from_map(m.get('Created'))

        if m.get('Deleted') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsDeleted()
            self.deleted = temp_model.from_map(m.get('Deleted'))

        if m.get('Pushed') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsPushed()
            self.pushed = temp_model.from_map(m.get('Pushed'))

        if m.get('Same') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsSame()
            self.same = temp_model.from_map(m.get('Same'))

        if m.get('Updated') is not None:
            temp_model = main_models.ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsUpdated()
            self.updated = temp_model.from_map(m.get('Updated'))

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsUpdated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsSame(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsPushed(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsDeleted(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsCreated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListSynchronizationJobsResponseBodySynchronizationJobsResultGroupMemberStatisticsBinded(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed operations.
        self.failed = failed
        # The number of skipped operations.
        self.skipped = skipped
        # The number of successful operations.
        self.success = success
        # The total number.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed is not None:
            result['Failed'] = self.failed

        if self.skipped is not None:
            result['Skipped'] = self.skipped

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Skipped') is not None:
            self.skipped = m.get('Skipped')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

