# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class QuerySnapshotJobListResponseBody(DaraModel):
    def __init__(
        self,
        next_page_token: str = None,
        non_exist_snapshot_job_ids: main_models.QuerySnapshotJobListResponseBodyNonExistSnapshotJobIds = None,
        request_id: str = None,
        snapshot_job_list: main_models.QuerySnapshotJobListResponseBodySnapshotJobList = None,
    ):
        # The OSS object that is used as the input file.
        self.next_page_token = next_page_token
        self.non_exist_snapshot_job_ids = non_exist_snapshot_job_ids
        # The ID of the snapshot job.
        self.request_id = request_id
        self.snapshot_job_list = snapshot_job_list

    def validate(self):
        if self.non_exist_snapshot_job_ids:
            self.non_exist_snapshot_job_ids.validate()
        if self.snapshot_job_list:
            self.snapshot_job_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.non_exist_snapshot_job_ids is not None:
            result['NonExistSnapshotJobIds'] = self.non_exist_snapshot_job_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshot_job_list is not None:
            result['SnapshotJobList'] = self.snapshot_job_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('NonExistSnapshotJobIds') is not None:
            temp_model = main_models.QuerySnapshotJobListResponseBodyNonExistSnapshotJobIds()
            self.non_exist_snapshot_job_ids = temp_model.from_map(m.get('NonExistSnapshotJobIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnapshotJobList') is not None:
            temp_model = main_models.QuerySnapshotJobListResponseBodySnapshotJobList()
            self.snapshot_job_list = temp_model.from_map(m.get('SnapshotJobList'))

        return self

class QuerySnapshotJobListResponseBodySnapshotJobList(DaraModel):
    def __init__(
        self,
        snapshot_job: List[main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJob] = None,
    ):
        self.snapshot_job = snapshot_job

    def validate(self):
        if self.snapshot_job:
            for v1 in self.snapshot_job:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SnapshotJob'] = []
        if self.snapshot_job is not None:
            for k1 in self.snapshot_job:
                result['SnapshotJob'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshot_job = []
        if m.get('SnapshotJob') is not None:
            for k1 in m.get('SnapshotJob'):
                temp_model = main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJob()
                self.snapshot_job.append(temp_model.from_map(k1))

        return self

class QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJob(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: str = None,
        creation_time: str = None,
        id: str = None,
        input: main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobInput = None,
        mnsmessage_result: main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobMNSMessageResult = None,
        message: str = None,
        pipeline_id: str = None,
        snapshot_config: main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfig = None,
        state: str = None,
        tile_count: str = None,
        user_data: str = None,
    ):
        self.code = code
        self.count = count
        self.creation_time = creation_time
        self.id = id
        self.input = input
        self.mnsmessage_result = mnsmessage_result
        self.message = message
        self.pipeline_id = pipeline_id
        self.snapshot_config = snapshot_config
        self.state = state
        self.tile_count = tile_count
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()
        if self.mnsmessage_result:
            self.mnsmessage_result.validate()
        if self.snapshot_config:
            self.snapshot_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.id is not None:
            result['Id'] = self.id

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.mnsmessage_result is not None:
            result['MNSMessageResult'] = self.mnsmessage_result.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.snapshot_config is not None:
            result['SnapshotConfig'] = self.snapshot_config.to_map()

        if self.state is not None:
            result['State'] = self.state

        if self.tile_count is not None:
            result['TileCount'] = self.tile_count

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Input') is not None:
            temp_model = main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('MNSMessageResult') is not None:
            temp_model = main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobMNSMessageResult()
            self.mnsmessage_result = temp_model.from_map(m.get('MNSMessageResult'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('SnapshotConfig') is not None:
            temp_model = main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfig()
            self.snapshot_config = temp_model.from_map(m.get('SnapshotConfig'))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TileCount') is not None:
            self.tile_count = m.get('TileCount')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfig(DaraModel):
    def __init__(
        self,
        frame_type: str = None,
        height: str = None,
        interval: str = None,
        num: str = None,
        output_file: main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfigOutputFile = None,
        tile_out: main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfigTileOut = None,
        tile_output_file: main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfigTileOutputFile = None,
        time: str = None,
        time_array: main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfigTimeArray = None,
        width: str = None,
    ):
        self.frame_type = frame_type
        self.height = height
        self.interval = interval
        self.num = num
        self.output_file = output_file
        self.tile_out = tile_out
        self.tile_output_file = tile_output_file
        self.time = time
        self.time_array = time_array
        self.width = width

    def validate(self):
        if self.output_file:
            self.output_file.validate()
        if self.tile_out:
            self.tile_out.validate()
        if self.tile_output_file:
            self.tile_output_file.validate()
        if self.time_array:
            self.time_array.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.frame_type is not None:
            result['FrameType'] = self.frame_type

        if self.height is not None:
            result['Height'] = self.height

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.num is not None:
            result['Num'] = self.num

        if self.output_file is not None:
            result['OutputFile'] = self.output_file.to_map()

        if self.tile_out is not None:
            result['TileOut'] = self.tile_out.to_map()

        if self.tile_output_file is not None:
            result['TileOutputFile'] = self.tile_output_file.to_map()

        if self.time is not None:
            result['Time'] = self.time

        if self.time_array is not None:
            result['TimeArray'] = self.time_array.to_map()

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrameType') is not None:
            self.frame_type = m.get('FrameType')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        if m.get('OutputFile') is not None:
            temp_model = main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfigOutputFile()
            self.output_file = temp_model.from_map(m.get('OutputFile'))

        if m.get('TileOut') is not None:
            temp_model = main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfigTileOut()
            self.tile_out = temp_model.from_map(m.get('TileOut'))

        if m.get('TileOutputFile') is not None:
            temp_model = main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfigTileOutputFile()
            self.tile_output_file = temp_model.from_map(m.get('TileOutputFile'))

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TimeArray') is not None:
            temp_model = main_models.QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfigTimeArray()
            self.time_array = temp_model.from_map(m.get('TimeArray'))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfigTimeArray(DaraModel):
    def __init__(
        self,
        time_point_list: List[int] = None,
    ):
        self.time_point_list = time_point_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time_point_list is not None:
            result['TimePointList'] = self.time_point_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimePointList') is not None:
            self.time_point_list = m.get('TimePointList')

        return self

class QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfigTileOutputFile(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
        role_arn: str = None,
    ):
        self.bucket = bucket
        self.location = location
        self.object = object
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.location is not None:
            result['Location'] = self.location

        if self.object is not None:
            result['Object'] = self.object

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        return self

class QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfigTileOut(DaraModel):
    def __init__(
        self,
        cell_height: str = None,
        cell_sel_step: str = None,
        cell_width: str = None,
        color: str = None,
        columns: str = None,
        is_keep_cell_pic: str = None,
        lines: str = None,
        margin: str = None,
        padding: str = None,
    ):
        self.cell_height = cell_height
        self.cell_sel_step = cell_sel_step
        self.cell_width = cell_width
        self.color = color
        self.columns = columns
        self.is_keep_cell_pic = is_keep_cell_pic
        self.lines = lines
        self.margin = margin
        self.padding = padding

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cell_height is not None:
            result['CellHeight'] = self.cell_height

        if self.cell_sel_step is not None:
            result['CellSelStep'] = self.cell_sel_step

        if self.cell_width is not None:
            result['CellWidth'] = self.cell_width

        if self.color is not None:
            result['Color'] = self.color

        if self.columns is not None:
            result['Columns'] = self.columns

        if self.is_keep_cell_pic is not None:
            result['IsKeepCellPic'] = self.is_keep_cell_pic

        if self.lines is not None:
            result['Lines'] = self.lines

        if self.margin is not None:
            result['Margin'] = self.margin

        if self.padding is not None:
            result['Padding'] = self.padding

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CellHeight') is not None:
            self.cell_height = m.get('CellHeight')

        if m.get('CellSelStep') is not None:
            self.cell_sel_step = m.get('CellSelStep')

        if m.get('CellWidth') is not None:
            self.cell_width = m.get('CellWidth')

        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('Columns') is not None:
            self.columns = m.get('Columns')

        if m.get('IsKeepCellPic') is not None:
            self.is_keep_cell_pic = m.get('IsKeepCellPic')

        if m.get('Lines') is not None:
            self.lines = m.get('Lines')

        if m.get('Margin') is not None:
            self.margin = m.get('Margin')

        if m.get('Padding') is not None:
            self.padding = m.get('Padding')

        return self

class QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobSnapshotConfigOutputFile(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
        role_arn: str = None,
    ):
        self.bucket = bucket
        self.location = location
        self.object = object
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.location is not None:
            result['Location'] = self.location

        if self.object is not None:
            result['Object'] = self.object

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        return self

class QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobMNSMessageResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        message_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        return self

class QuerySnapshotJobListResponseBodySnapshotJobListSnapshotJobInput(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
        role_arn: str = None,
    ):
        self.bucket = bucket
        self.location = location
        self.object = object
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.location is not None:
            result['Location'] = self.location

        if self.object is not None:
            result['Object'] = self.object

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Object') is not None:
            self.object = m.get('Object')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        return self

class QuerySnapshotJobListResponseBodyNonExistSnapshotJobIds(DaraModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.string is not None:
            result['String'] = self.string

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')

        return self

