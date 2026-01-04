# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetSynchronizationJobResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        synchronization_job: main_models.GetSynchronizationJobResponseBodySynchronizationJob = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the synchronization job.
        self.synchronization_job = synchronization_job

    def validate(self):
        if self.synchronization_job:
            self.synchronization_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.synchronization_job is not None:
            result['SynchronizationJob'] = self.synchronization_job.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SynchronizationJob') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJob()
            self.synchronization_job = temp_model.from_map(m.get('SynchronizationJob'))

        return self

class GetSynchronizationJobResponseBodySynchronizationJob(DaraModel):
    def __init__(
        self,
        direction: str = None,
        end_time: int = None,
        result: main_models.GetSynchronizationJobResponseBodySynchronizationJobResult = None,
        start_time: int = None,
        status: str = None,
        synchronization_job_id: str = None,
        target_id: str = None,
        target_type: str = None,
        trigger_type: str = None,
    ):
        # The direction of the synchronization job. Valid values:
        # 
        # *   ingress
        # *   egress
        self.direction = direction
        # The end time of the synchronization. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_time = end_time
        # The result of the synchronization job.
        self.result = result
        # The start time of the synchronization. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The status of the synchronization job. Valid values:
        # 
        # *   pending
        # *   running
        # *   failed
        # *   partial_success
        # *   success
        self.status = status
        # The ID of the synchronization job.
        self.synchronization_job_id = synchronization_job_id
        # The ID of the synchronization destination.
        self.target_id = target_id
        # The type of the synchronization destination. Valid values:
        # 
        # *   identity_provider
        # *   application
        self.target_type = target_type
        # The trigger type of the synchronization. Valid values:
        # 
        # *   auto
        # *   manual
        self.trigger_type = trigger_type

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Result') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResult()
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

class GetSynchronizationJobResponseBodySynchronizationJobResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        group_member_statistics: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatistics = None,
        group_statistics: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatistics = None,
        organizational_unit_statistics: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatistics = None,
        user_statistics: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultUserStatistics = None,
    ):
        # The error code corresponding to the error message.
        self.error_code = error_code
        # The error message returned in the case of an error.
        self.error_message = error_message
        # The group member synchronization result statistics.
        self.group_member_statistics = group_member_statistics
        # The group synchronization result statistics.
        self.group_statistics = group_statistics
        # The organization synchronization result statistics.
        self.organizational_unit_statistics = organizational_unit_statistics
        # The user synchronization result statistics.
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
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatistics()
            self.group_member_statistics = temp_model.from_map(m.get('GroupMemberStatistics'))

        if m.get('GroupStatistics') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatistics()
            self.group_statistics = temp_model.from_map(m.get('GroupStatistics'))

        if m.get('OrganizationalUnitStatistics') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatistics()
            self.organizational_unit_statistics = temp_model.from_map(m.get('OrganizationalUnitStatistics'))

        if m.get('UserStatistics') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultUserStatistics()
            self.user_statistics = temp_model.from_map(m.get('UserStatistics'))

        return self

class GetSynchronizationJobResponseBodySynchronizationJobResultUserStatistics(DaraModel):
    def __init__(
        self,
        binded: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsBinded = None,
        created: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsCreated = None,
        deleted: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsDeleted = None,
        pushed: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsPushed = None,
        same: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsSame = None,
        updated: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsUpdated = None,
    ):
        # The binding result statistics.
        self.binded = binded
        # The creation result statistics.
        self.created = created
        # The deletion result statistics.
        self.deleted = deleted
        # The notification result statistics.
        self.pushed = pushed
        # The result statistics about identical users.
        self.same = same
        # The update result statistics.
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
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsBinded()
            self.binded = temp_model.from_map(m.get('Binded'))

        if m.get('Created') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsCreated()
            self.created = temp_model.from_map(m.get('Created'))

        if m.get('Deleted') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsDeleted()
            self.deleted = temp_model.from_map(m.get('Deleted'))

        if m.get('Pushed') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsPushed()
            self.pushed = temp_model.from_map(m.get('Pushed'))

        if m.get('Same') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsSame()
            self.same = temp_model.from_map(m.get('Same'))

        if m.get('Updated') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsUpdated()
            self.updated = temp_model.from_map(m.get('Updated'))

        return self

class GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsUpdated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsSame(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsPushed(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsDeleted(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsCreated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultUserStatisticsBinded(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatistics(DaraModel):
    def __init__(
        self,
        binded: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsBinded = None,
        created: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsCreated = None,
        deleted: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsDeleted = None,
        pushed: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsPushed = None,
        same: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsSame = None,
        updated: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsUpdated = None,
    ):
        # The binding result statistics.
        self.binded = binded
        # The creation result statistics.
        self.created = created
        # The deletion result statistics.
        self.deleted = deleted
        # The notification result statistics.
        self.pushed = pushed
        # The result statistics about identical organizations.
        self.same = same
        # The update result statistics.
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
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsBinded()
            self.binded = temp_model.from_map(m.get('Binded'))

        if m.get('Created') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsCreated()
            self.created = temp_model.from_map(m.get('Created'))

        if m.get('Deleted') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsDeleted()
            self.deleted = temp_model.from_map(m.get('Deleted'))

        if m.get('Pushed') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsPushed()
            self.pushed = temp_model.from_map(m.get('Pushed'))

        if m.get('Same') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsSame()
            self.same = temp_model.from_map(m.get('Same'))

        if m.get('Updated') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsUpdated()
            self.updated = temp_model.from_map(m.get('Updated'))

        return self

class GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsUpdated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsSame(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsPushed(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsDeleted(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsCreated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultOrganizationalUnitStatisticsBinded(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatistics(DaraModel):
    def __init__(
        self,
        binded: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsBinded = None,
        created: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsCreated = None,
        deleted: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsDeleted = None,
        pushed: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsPushed = None,
        same: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsSame = None,
        updated: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsUpdated = None,
    ):
        # The binding result statistics.
        self.binded = binded
        # The creation result statistics.
        self.created = created
        # The deletion result statistics.
        self.deleted = deleted
        # The notification result statistics.
        self.pushed = pushed
        # The result statistics about identical groups.
        self.same = same
        # The update result statistics.
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
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsBinded()
            self.binded = temp_model.from_map(m.get('Binded'))

        if m.get('Created') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsCreated()
            self.created = temp_model.from_map(m.get('Created'))

        if m.get('Deleted') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsDeleted()
            self.deleted = temp_model.from_map(m.get('Deleted'))

        if m.get('Pushed') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsPushed()
            self.pushed = temp_model.from_map(m.get('Pushed'))

        if m.get('Same') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsSame()
            self.same = temp_model.from_map(m.get('Same'))

        if m.get('Updated') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsUpdated()
            self.updated = temp_model.from_map(m.get('Updated'))

        return self

class GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsUpdated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsSame(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsPushed(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsDeleted(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsCreated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultGroupStatisticsBinded(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatistics(DaraModel):
    def __init__(
        self,
        binded: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsBinded = None,
        created: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsCreated = None,
        deleted: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsDeleted = None,
        pushed: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsPushed = None,
        same: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsSame = None,
        updated: main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsUpdated = None,
    ):
        # The binding result statistics.
        self.binded = binded
        # The creation result statistics.
        self.created = created
        # The deletion result statistics.
        self.deleted = deleted
        # The notification result statistics.
        self.pushed = pushed
        # The result statistics about identical group members.
        self.same = same
        # The update result statistics.
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
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsBinded()
            self.binded = temp_model.from_map(m.get('Binded'))

        if m.get('Created') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsCreated()
            self.created = temp_model.from_map(m.get('Created'))

        if m.get('Deleted') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsDeleted()
            self.deleted = temp_model.from_map(m.get('Deleted'))

        if m.get('Pushed') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsPushed()
            self.pushed = temp_model.from_map(m.get('Pushed'))

        if m.get('Same') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsSame()
            self.same = temp_model.from_map(m.get('Same'))

        if m.get('Updated') is not None:
            temp_model = main_models.GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsUpdated()
            self.updated = temp_model.from_map(m.get('Updated'))

        return self

class GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsUpdated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsSame(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsPushed(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsDeleted(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsCreated(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

class GetSynchronizationJobResponseBodySynchronizationJobResultGroupMemberStatisticsBinded(DaraModel):
    def __init__(
        self,
        failed: int = None,
        skipped: int = None,
        success: int = None,
        total: int = None,
    ):
        # The number of failed items.
        self.failed = failed
        # The number of skipped items.
        self.skipped = skipped
        # The number of successful items.
        self.success = success
        # The total number of items.
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

