# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupExecutingInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        executing_info: main_models.DescribeGroupExecutingInfoResponseBodyExecutingInfo = None,
        group_id: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.executing_info = executing_info
        self.group_id = group_id
        self.http_status_code = http_status_code
        self.instance_id = instance_id
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.executing_info:
            self.executing_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.executing_info is not None:
            result['ExecutingInfo'] = self.executing_info.to_map()

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ExecutingInfo') is not None:
            temp_model = main_models.DescribeGroupExecutingInfoResponseBodyExecutingInfo()
            self.executing_info = temp_model.from_map(m.get('ExecutingInfo'))

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeGroupExecutingInfoResponseBodyExecutingInfo(DaraModel):
    def __init__(
        self,
        avg_talk_time: int = None,
        call_failed_num: int = None,
        call_num: int = None,
        creator_name: str = None,
        duration_distribution: str = None,
        end_time: int = None,
        finished_num: int = None,
        hang_up_by_client_num: int = None,
        jobs_progress: main_models.DescribeGroupExecutingInfoResponseBodyExecutingInfoJobsProgress = None,
        no_interaction_num: int = None,
        start_time: int = None,
        talk_turns_distribution: str = None,
        transfer_by_intent_num: int = None,
        transfer_by_no_answer: int = None,
    ):
        self.avg_talk_time = avg_talk_time
        self.call_failed_num = call_failed_num
        self.call_num = call_num
        self.creator_name = creator_name
        self.duration_distribution = duration_distribution
        self.end_time = end_time
        self.finished_num = finished_num
        self.hang_up_by_client_num = hang_up_by_client_num
        self.jobs_progress = jobs_progress
        self.no_interaction_num = no_interaction_num
        self.start_time = start_time
        self.talk_turns_distribution = talk_turns_distribution
        self.transfer_by_intent_num = transfer_by_intent_num
        self.transfer_by_no_answer = transfer_by_no_answer

    def validate(self):
        if self.jobs_progress:
            self.jobs_progress.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_talk_time is not None:
            result['AvgTalkTime'] = self.avg_talk_time

        if self.call_failed_num is not None:
            result['CallFailedNum'] = self.call_failed_num

        if self.call_num is not None:
            result['CallNum'] = self.call_num

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.duration_distribution is not None:
            result['DurationDistribution'] = self.duration_distribution

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.finished_num is not None:
            result['FinishedNum'] = self.finished_num

        if self.hang_up_by_client_num is not None:
            result['HangUpByClientNum'] = self.hang_up_by_client_num

        if self.jobs_progress is not None:
            result['JobsProgress'] = self.jobs_progress.to_map()

        if self.no_interaction_num is not None:
            result['NoInteractionNum'] = self.no_interaction_num

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.talk_turns_distribution is not None:
            result['TalkTurnsDistribution'] = self.talk_turns_distribution

        if self.transfer_by_intent_num is not None:
            result['TransferByIntentNum'] = self.transfer_by_intent_num

        if self.transfer_by_no_answer is not None:
            result['TransferByNoAnswer'] = self.transfer_by_no_answer

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgTalkTime') is not None:
            self.avg_talk_time = m.get('AvgTalkTime')

        if m.get('CallFailedNum') is not None:
            self.call_failed_num = m.get('CallFailedNum')

        if m.get('CallNum') is not None:
            self.call_num = m.get('CallNum')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('DurationDistribution') is not None:
            self.duration_distribution = m.get('DurationDistribution')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FinishedNum') is not None:
            self.finished_num = m.get('FinishedNum')

        if m.get('HangUpByClientNum') is not None:
            self.hang_up_by_client_num = m.get('HangUpByClientNum')

        if m.get('JobsProgress') is not None:
            temp_model = main_models.DescribeGroupExecutingInfoResponseBodyExecutingInfoJobsProgress()
            self.jobs_progress = temp_model.from_map(m.get('JobsProgress'))

        if m.get('NoInteractionNum') is not None:
            self.no_interaction_num = m.get('NoInteractionNum')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TalkTurnsDistribution') is not None:
            self.talk_turns_distribution = m.get('TalkTurnsDistribution')

        if m.get('TransferByIntentNum') is not None:
            self.transfer_by_intent_num = m.get('TransferByIntentNum')

        if m.get('TransferByNoAnswer') is not None:
            self.transfer_by_no_answer = m.get('TransferByNoAnswer')

        return self

class DescribeGroupExecutingInfoResponseBodyExecutingInfoJobsProgress(DaraModel):
    def __init__(
        self,
        cancelled_num: int = None,
        executing_num: int = None,
        failed_num: int = None,
        paused_num: int = None,
        scheduling_num: int = None,
        total_completed_num: int = None,
        total_jobs: int = None,
        total_not_answered_num: int = None,
    ):
        self.cancelled_num = cancelled_num
        self.executing_num = executing_num
        self.failed_num = failed_num
        self.paused_num = paused_num
        self.scheduling_num = scheduling_num
        self.total_completed_num = total_completed_num
        self.total_jobs = total_jobs
        self.total_not_answered_num = total_not_answered_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancelled_num is not None:
            result['CancelledNum'] = self.cancelled_num

        if self.executing_num is not None:
            result['ExecutingNum'] = self.executing_num

        if self.failed_num is not None:
            result['FailedNum'] = self.failed_num

        if self.paused_num is not None:
            result['PausedNum'] = self.paused_num

        if self.scheduling_num is not None:
            result['SchedulingNum'] = self.scheduling_num

        if self.total_completed_num is not None:
            result['TotalCompletedNum'] = self.total_completed_num

        if self.total_jobs is not None:
            result['TotalJobs'] = self.total_jobs

        if self.total_not_answered_num is not None:
            result['TotalNotAnsweredNum'] = self.total_not_answered_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CancelledNum') is not None:
            self.cancelled_num = m.get('CancelledNum')

        if m.get('ExecutingNum') is not None:
            self.executing_num = m.get('ExecutingNum')

        if m.get('FailedNum') is not None:
            self.failed_num = m.get('FailedNum')

        if m.get('PausedNum') is not None:
            self.paused_num = m.get('PausedNum')

        if m.get('SchedulingNum') is not None:
            self.scheduling_num = m.get('SchedulingNum')

        if m.get('TotalCompletedNum') is not None:
            self.total_completed_num = m.get('TotalCompletedNum')

        if m.get('TotalJobs') is not None:
            self.total_jobs = m.get('TotalJobs')

        if m.get('TotalNotAnsweredNum') is not None:
            self.total_not_answered_num = m.get('TotalNotAnsweredNum')

        return self

