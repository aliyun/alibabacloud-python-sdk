# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class CreateDataTrackOrderRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        param: main_models.CreateDataTrackOrderRequestParam = None,
        related_user_list: List[str] = None,
        tid: int = None,
    ):
        # The purpose or objective of the data tracking ticket. This parameter is used to help reduce unnecessary communication.
        # 
        # This parameter is required.
        self.comment = comment
        # The parameters of the ticket.
        # 
        # This parameter is required.
        self.param = param
        # The IDs of the operators that are related to the ticket.
        self.related_user_list = related_user_list
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.param is not None:
            result['Param'] = self.param.to_map()

        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Param') is not None:
            temp_model = main_models.CreateDataTrackOrderRequestParam()
            self.param = temp_model.from_map(m.get('Param'))

        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class CreateDataTrackOrderRequestParam(DaraModel):
    def __init__(
        self,
        db_id: str = None,
        job_end_time: str = None,
        job_start_time: str = None,
        table_names: List[str] = None,
        track_types: List[str] = None,
    ):
        # The ID of the database. You can call the [SearchDatabases](https://help.aliyun.com/document_detail/141876.html) operation to query the ID of the database.
        # 
        # > You can call this operation to create a data tracking ticket for only physical databases. This operation is not applicable to logical databases.
        # 
        # This parameter is required.
        self.db_id = db_id
        # The end time of the time range in which you want to track data operations. The time must be in the yyyy-MM-dd HH:mm:ss format.
        # 
        # This parameter is required.
        self.job_end_time = job_end_time
        # The start time of the time range in which you want to track data operations. The time must be in the yyyy-MM-dd HH:mm:ss format.
        # 
        # This parameter is required.
        self.job_start_time = job_start_time
        # The names of the tables for which you want to track data operations.
        # 
        # This parameter is required.
        self.table_names = table_names
        # The types of data operations that you want to track.
        # 
        # This parameter is required.
        self.track_types = track_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.job_end_time is not None:
            result['JobEndTime'] = self.job_end_time

        if self.job_start_time is not None:
            result['JobStartTime'] = self.job_start_time

        if self.table_names is not None:
            result['TableNames'] = self.table_names

        if self.track_types is not None:
            result['TrackTypes'] = self.track_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('JobEndTime') is not None:
            self.job_end_time = m.get('JobEndTime')

        if m.get('JobStartTime') is not None:
            self.job_start_time = m.get('JobStartTime')

        if m.get('TableNames') is not None:
            self.table_names = m.get('TableNames')

        if m.get('TrackTypes') is not None:
            self.track_types = m.get('TrackTypes')

        return self

