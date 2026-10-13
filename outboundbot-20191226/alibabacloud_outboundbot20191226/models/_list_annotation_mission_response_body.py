# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ListAnnotationMissionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListAnnotationMissionResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The additional information. If the request is successful, success is returned. If the request fails, a specific error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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

        if m.get('Data') is not None:
            temp_model = main_models.ListAnnotationMissionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAnnotationMissionResponseBodyData(DaraModel):
    def __init__(
        self,
        annotation_mission_list: List[main_models.ListAnnotationMissionResponseBodyDataAnnotationMissionList] = None,
        message: str = None,
        page_index: int = None,
        page_size: int = None,
        success: bool = None,
        total_count: int = None,
        total_page_count: int = None,
    ):
        # The list of annotation tasks.
        self.annotation_mission_list = annotation_mission_list
        # The additional information. If the request is successful, success is returned. If the request fails, a specific error code is returned.
        self.message = message
        # The page number.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size
        # Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed.
        self.success = success
        # The total count.
        self.total_count = total_count
        # The total number of pages.
        self.total_page_count = total_page_count

    def validate(self):
        if self.annotation_mission_list:
            for v1 in self.annotation_mission_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AnnotationMissionList'] = []
        if self.annotation_mission_list is not None:
            for k1 in self.annotation_mission_list:
                result['AnnotationMissionList'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.annotation_mission_list = []
        if m.get('AnnotationMissionList') is not None:
            for k1 in m.get('AnnotationMissionList'):
                temp_model = main_models.ListAnnotationMissionResponseBodyDataAnnotationMissionList()
                self.annotation_mission_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')

        return self

class ListAnnotationMissionResponseBodyDataAnnotationMissionList(DaraModel):
    def __init__(
        self,
        annotation_mission_data_source_type: int = None,
        annotation_mission_debug_data_source_list: List[int] = None,
        annotation_mission_id: str = None,
        annotation_mission_name: str = None,
        annotation_status: int = None,
        conversation_time_end_filter: int = None,
        conversation_time_start_filter: int = None,
        create_time: int = None,
        exclude_other_mission_session: bool = None,
        finish_time: int = None,
        instance_id: str = None,
        sampling_count: int = None,
        sampling_description: str = None,
        sampling_rate: int = None,
        sampling_type: int = None,
        session_end_reason_filter_list: List[int] = None,
        session_finish_count: int = None,
        session_total_count: int = None,
    ):
        # The data source of the annotation task. Valid values: 1: Outbound call. 2: Navigation.
        self.annotation_mission_data_source_type = annotation_mission_data_source_type
        # The list of debug data sources for the annotation task.
        # 
        # > Note: An additional 0 is included in the response. The return values are [0,1], [0,2], or [0,1,2].
        self.annotation_mission_debug_data_source_list = annotation_mission_debug_data_source_list
        # The task ID.
        self.annotation_mission_id = annotation_mission_id
        # The task name.
        self.annotation_mission_name = annotation_mission_name
        # The annotation status. Valid values:
        # - 1: In progress.
        # - 2: Completed.
        # - 3: Closed.
        self.annotation_status = annotation_status
        # The end time of the conversation time query condition for the annotation task.
        self.conversation_time_end_filter = conversation_time_end_filter
        # The start time of the conversation time query condition for the annotation task.
        self.conversation_time_start_filter = conversation_time_start_filter
        # The creation time. The value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # Indicates whether to exclude call records that have been annotated in other tasks.
        self.exclude_other_mission_session = exclude_other_mission_session
        # The completion time of the annotation task. The value is a UNIX timestamp in milliseconds.
        self.finish_time = finish_time
        # The instance ID.
        self.instance_id = instance_id
        # The maximum limit for the sampling count.
        self.sampling_count = sampling_count
        # The sampling description.
        self.sampling_description = sampling_description
        # The sampling rate.
        self.sampling_rate = sampling_rate
        # The sampling type.
        self.sampling_type = sampling_type
        # The list of call end reasons used to create the task. Valid values:
        # - 1: Normal completion.
        # - 2: Hang up by the robot after unrecognized input.
        # - 3: Hang up due to silence timeout.
        # - 4: Hang up by the user after unrecognized input.
        # - 5: Hang up by the user without a reason.
        # - 6: Transfer to a human agent due to intent match.
        # - 7: Transfer to a human agent after unrecognized input.
        # - 8: No interaction on the user side.
        # - 9: Interruption due to a system exception.
        # - 10: Transfer to IVR due to intent match.
        # - 11: Transfer to IVR after unrecognized input.
        self.session_end_reason_filter_list = session_end_reason_filter_list
        # The number of completed sessions in the annotation task.
        self.session_finish_count = session_finish_count
        # The total number of sessions in the annotation task.
        self.session_total_count = session_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_mission_data_source_type is not None:
            result['AnnotationMissionDataSourceType'] = self.annotation_mission_data_source_type

        if self.annotation_mission_debug_data_source_list is not None:
            result['AnnotationMissionDebugDataSourceList'] = self.annotation_mission_debug_data_source_list

        if self.annotation_mission_id is not None:
            result['AnnotationMissionId'] = self.annotation_mission_id

        if self.annotation_mission_name is not None:
            result['AnnotationMissionName'] = self.annotation_mission_name

        if self.annotation_status is not None:
            result['AnnotationStatus'] = self.annotation_status

        if self.conversation_time_end_filter is not None:
            result['ConversationTimeEndFilter'] = self.conversation_time_end_filter

        if self.conversation_time_start_filter is not None:
            result['ConversationTimeStartFilter'] = self.conversation_time_start_filter

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.exclude_other_mission_session is not None:
            result['ExcludeOtherMissionSession'] = self.exclude_other_mission_session

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.sampling_count is not None:
            result['SamplingCount'] = self.sampling_count

        if self.sampling_description is not None:
            result['SamplingDescription'] = self.sampling_description

        if self.sampling_rate is not None:
            result['SamplingRate'] = self.sampling_rate

        if self.sampling_type is not None:
            result['SamplingType'] = self.sampling_type

        if self.session_end_reason_filter_list is not None:
            result['SessionEndReasonFilterList'] = self.session_end_reason_filter_list

        if self.session_finish_count is not None:
            result['SessionFinishCount'] = self.session_finish_count

        if self.session_total_count is not None:
            result['SessionTotalCount'] = self.session_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotationMissionDataSourceType') is not None:
            self.annotation_mission_data_source_type = m.get('AnnotationMissionDataSourceType')

        if m.get('AnnotationMissionDebugDataSourceList') is not None:
            self.annotation_mission_debug_data_source_list = m.get('AnnotationMissionDebugDataSourceList')

        if m.get('AnnotationMissionId') is not None:
            self.annotation_mission_id = m.get('AnnotationMissionId')

        if m.get('AnnotationMissionName') is not None:
            self.annotation_mission_name = m.get('AnnotationMissionName')

        if m.get('AnnotationStatus') is not None:
            self.annotation_status = m.get('AnnotationStatus')

        if m.get('ConversationTimeEndFilter') is not None:
            self.conversation_time_end_filter = m.get('ConversationTimeEndFilter')

        if m.get('ConversationTimeStartFilter') is not None:
            self.conversation_time_start_filter = m.get('ConversationTimeStartFilter')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExcludeOtherMissionSession') is not None:
            self.exclude_other_mission_session = m.get('ExcludeOtherMissionSession')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SamplingCount') is not None:
            self.sampling_count = m.get('SamplingCount')

        if m.get('SamplingDescription') is not None:
            self.sampling_description = m.get('SamplingDescription')

        if m.get('SamplingRate') is not None:
            self.sampling_rate = m.get('SamplingRate')

        if m.get('SamplingType') is not None:
            self.sampling_type = m.get('SamplingType')

        if m.get('SessionEndReasonFilterList') is not None:
            self.session_end_reason_filter_list = m.get('SessionEndReasonFilterList')

        if m.get('SessionFinishCount') is not None:
            self.session_finish_count = m.get('SessionFinishCount')

        if m.get('SessionTotalCount') is not None:
            self.session_total_count = m.get('SessionTotalCount')

        return self

