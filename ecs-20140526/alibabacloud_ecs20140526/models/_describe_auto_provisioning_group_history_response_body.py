# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoProvisioningGroupHistoryResponseBody(DaraModel):
    def __init__(
        self,
        auto_provisioning_group_histories: main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistories = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array of scheduled task history records.
        self.auto_provisioning_group_histories = auto_provisioning_group_histories
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of scheduled tasks.
        self.total_count = total_count

    def validate(self):
        if self.auto_provisioning_group_histories:
            self.auto_provisioning_group_histories.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_provisioning_group_histories is not None:
            result['AutoProvisioningGroupHistories'] = self.auto_provisioning_group_histories.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoProvisioningGroupHistories') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistories()
            self.auto_provisioning_group_histories = temp_model.from_map(m.get('AutoProvisioningGroupHistories'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistories(DaraModel):
    def __init__(
        self,
        auto_provisioning_group_history: List[main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistory] = None,
    ):
        self.auto_provisioning_group_history = auto_provisioning_group_history

    def validate(self):
        if self.auto_provisioning_group_history:
            for v1 in self.auto_provisioning_group_history:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoProvisioningGroupHistory'] = []
        if self.auto_provisioning_group_history is not None:
            for k1 in self.auto_provisioning_group_history:
                result['AutoProvisioningGroupHistory'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_provisioning_group_history = []
        if m.get('AutoProvisioningGroupHistory') is not None:
            for k1 in m.get('AutoProvisioningGroupHistory'):
                temp_model = main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistory()
                self.auto_provisioning_group_history.append(temp_model.from_map(k1))

        return self

class DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistory(DaraModel):
    def __init__(
        self,
        activity_details: main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetails = None,
        last_event_time: str = None,
        start_time: str = None,
        status: str = None,
        task_id: str = None,
    ):
        self.activity_details = activity_details
        self.last_event_time = last_event_time
        self.start_time = start_time
        self.status = status
        self.task_id = task_id

    def validate(self):
        if self.activity_details:
            self.activity_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_details is not None:
            result['ActivityDetails'] = self.activity_details.to_map()

        if self.last_event_time is not None:
            result['LastEventTime'] = self.last_event_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityDetails') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetails()
            self.activity_details = temp_model.from_map(m.get('ActivityDetails'))

        if m.get('LastEventTime') is not None:
            self.last_event_time = m.get('LastEventTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetails(DaraModel):
    def __init__(
        self,
        activity_detail: List[main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetail] = None,
    ):
        self.activity_detail = activity_detail

    def validate(self):
        if self.activity_detail:
            for v1 in self.activity_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ActivityDetail'] = []
        if self.activity_detail is not None:
            for k1 in self.activity_detail:
                result['ActivityDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activity_detail = []
        if m.get('ActivityDetail') is not None:
            for k1 in m.get('ActivityDetail'):
                temp_model = main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetail()
                self.activity_detail.append(temp_model.from_map(k1))

        return self

class DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetail(DaraModel):
    def __init__(
        self,
        created_instance_ids: main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailCreatedInstanceIds = None,
        destroyed_instance_ids: main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailDestroyedInstanceIds = None,
        detail: str = None,
        error_messages: main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailErrorMessages = None,
        status: str = None,
    ):
        self.created_instance_ids = created_instance_ids
        self.destroyed_instance_ids = destroyed_instance_ids
        self.detail = detail
        self.error_messages = error_messages
        self.status = status

    def validate(self):
        if self.created_instance_ids:
            self.created_instance_ids.validate()
        if self.destroyed_instance_ids:
            self.destroyed_instance_ids.validate()
        if self.error_messages:
            self.error_messages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_instance_ids is not None:
            result['CreatedInstanceIds'] = self.created_instance_ids.to_map()

        if self.destroyed_instance_ids is not None:
            result['DestroyedInstanceIds'] = self.destroyed_instance_ids.to_map()

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.error_messages is not None:
            result['ErrorMessages'] = self.error_messages.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedInstanceIds') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailCreatedInstanceIds()
            self.created_instance_ids = temp_model.from_map(m.get('CreatedInstanceIds'))

        if m.get('DestroyedInstanceIds') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailDestroyedInstanceIds()
            self.destroyed_instance_ids = temp_model.from_map(m.get('DestroyedInstanceIds'))

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('ErrorMessages') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailErrorMessages()
            self.error_messages = temp_model.from_map(m.get('ErrorMessages'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailErrorMessages(DaraModel):
    def __init__(
        self,
        error_message: List[main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailErrorMessagesErrorMessage] = None,
    ):
        self.error_message = error_message

    def validate(self):
        if self.error_message:
            for v1 in self.error_message:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ErrorMessage'] = []
        if self.error_message is not None:
            for k1 in self.error_message:
                result['ErrorMessage'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_message = []
        if m.get('ErrorMessage') is not None:
            for k1 in m.get('ErrorMessage'):
                temp_model = main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailErrorMessagesErrorMessage()
                self.error_message.append(temp_model.from_map(k1))

        return self

class DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailErrorMessagesErrorMessage(DaraModel):
    def __init__(
        self,
        code: str = None,
        failed_instance_ids: main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailErrorMessagesErrorMessageFailedInstanceIds = None,
        message: str = None,
    ):
        self.code = code
        self.failed_instance_ids = failed_instance_ids
        self.message = message

    def validate(self):
        if self.failed_instance_ids:
            self.failed_instance_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.failed_instance_ids is not None:
            result['FailedInstanceIds'] = self.failed_instance_ids.to_map()

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('FailedInstanceIds') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailErrorMessagesErrorMessageFailedInstanceIds()
            self.failed_instance_ids = temp_model.from_map(m.get('FailedInstanceIds'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

class DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailErrorMessagesErrorMessageFailedInstanceIds(DaraModel):
    def __init__(
        self,
        failed_instance_id: List[str] = None,
    ):
        self.failed_instance_id = failed_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_instance_id is not None:
            result['FailedInstanceId'] = self.failed_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedInstanceId') is not None:
            self.failed_instance_id = m.get('FailedInstanceId')

        return self

class DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailDestroyedInstanceIds(DaraModel):
    def __init__(
        self,
        destroyed_instance_id: List[str] = None,
    ):
        self.destroyed_instance_id = destroyed_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destroyed_instance_id is not None:
            result['DestroyedInstanceId'] = self.destroyed_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestroyedInstanceId') is not None:
            self.destroyed_instance_id = m.get('DestroyedInstanceId')

        return self

class DescribeAutoProvisioningGroupHistoryResponseBodyAutoProvisioningGroupHistoriesAutoProvisioningGroupHistoryActivityDetailsActivityDetailCreatedInstanceIds(DaraModel):
    def __init__(
        self,
        created_instance_id: List[str] = None,
    ):
        self.created_instance_id = created_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_instance_id is not None:
            result['CreatedInstanceId'] = self.created_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedInstanceId') is not None:
            self.created_instance_id = m.get('CreatedInstanceId')

        return self

