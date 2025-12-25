# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetDataTrackOrderDetailResponseBody(DaraModel):
    def __init__(
        self,
        data_track_order_detail: main_models.GetDataTrackOrderDetailResponseBodyDataTrackOrderDetail = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the ticket.
        self.data_track_order_detail = data_track_order_detail
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data_track_order_detail:
            self.data_track_order_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_track_order_detail is not None:
            result['DataTrackOrderDetail'] = self.data_track_order_detail.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataTrackOrderDetail') is not None:
            temp_model = main_models.GetDataTrackOrderDetailResponseBodyDataTrackOrderDetail()
            self.data_track_order_detail = temp_model.from_map(m.get('DataTrackOrderDetail'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataTrackOrderDetailResponseBodyDataTrackOrderDetail(DaraModel):
    def __init__(
        self,
        database_search_name: str = None,
        db_id: int = None,
        job_end_time: str = None,
        job_start_time: str = None,
        job_status: str = None,
        logic: bool = None,
        schema_name: str = None,
        status_desc: str = None,
        table_names: List[str] = None,
        track_types: List[str] = None,
    ):
        # The name that is used to search for the database.
        self.database_search_name = database_search_name
        # The ID of the database.
        self.db_id = db_id
        # The end time of the time range in which data operations are tracked. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.job_end_time = job_end_time
        # The start time of the time range in which data operations are tracked. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.job_start_time = job_start_time
        # The status of the data tracking task. Valid values:
        # 
        # *   **INIT**: The task is being initialized.
        # *   **LISTING**: The binary logs are being obtained.
        # *   **LIST_SUCCESS**: The binary logs are successfully obtained.
        # *   **DOWNLOADING**: The binary logs are being downloaded.
        # *   **DOWNLOAD_FAIL**: The binary logs failed to be downloaded.
        # *   **DOWNLOAD_SUCCESS**: The binary logs are successfully downloaded.
        # *   **FILTERING**: The binary logs are being parsed.
        # *   **FILTER_FAIL**: The binary logs failed to be parsed.
        # *   **FILTER_SUCCESS**: The binary logs are successfully parsed.
        self.job_status = job_status
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.logic = logic
        # The name of the database.
        self.schema_name = schema_name
        # The description of the task status.
        self.status_desc = status_desc
        # The names of the tables for which data operations are tracked.
        self.table_names = table_names
        # The types of data operations that are tracked.
        self.track_types = track_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_search_name is not None:
            result['DatabaseSearchName'] = self.database_search_name

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.job_end_time is not None:
            result['JobEndTime'] = self.job_end_time

        if self.job_start_time is not None:
            result['JobStartTime'] = self.job_start_time

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.table_names is not None:
            result['TableNames'] = self.table_names

        if self.track_types is not None:
            result['TrackTypes'] = self.track_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseSearchName') is not None:
            self.database_search_name = m.get('DatabaseSearchName')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('JobEndTime') is not None:
            self.job_end_time = m.get('JobEndTime')

        if m.get('JobStartTime') is not None:
            self.job_start_time = m.get('JobStartTime')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')

        if m.get('TrackTypes') is not None:
            self.track_types = m.get('TrackTypes')

        return self

