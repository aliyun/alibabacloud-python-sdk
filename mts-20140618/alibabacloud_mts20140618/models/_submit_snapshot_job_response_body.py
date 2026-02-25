# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class SubmitSnapshotJobResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        snapshot_job: main_models.SubmitSnapshotJobResponseBodySnapshotJob = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the snapshot job.
        self.snapshot_job = snapshot_job

    def validate(self):
        if self.snapshot_job:
            self.snapshot_job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshot_job is not None:
            result['SnapshotJob'] = self.snapshot_job.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnapshotJob') is not None:
            temp_model = main_models.SubmitSnapshotJobResponseBodySnapshotJob()
            self.snapshot_job = temp_model.from_map(m.get('SnapshotJob'))

        return self

class SubmitSnapshotJobResponseBodySnapshotJob(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: str = None,
        creation_time: str = None,
        id: str = None,
        input: main_models.SubmitSnapshotJobResponseBodySnapshotJobInput = None,
        mnsmessage_result: main_models.SubmitSnapshotJobResponseBodySnapshotJobMNSMessageResult = None,
        message: str = None,
        pipeline_id: str = None,
        snapshot_config: main_models.SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfig = None,
        state: str = None,
        tile_count: str = None,
        user_data: str = None,
    ):
        # The error code returned if the job fails. This parameter is not returned if the job is successful.
        self.code = code
        # The number of snapshots that are captured.
        self.count = count
        # The time when the job was created.
        self.creation_time = creation_time
        # The ID of the snapshot job.
        self.id = id
        # The information about the job input.
        self.input = input
        # The message sent by MNS to notify the user of the job result.
        self.mnsmessage_result = mnsmessage_result
        # The error message returned if the job fails. This parameter is not returned if the job is successful.
        self.message = message
        # The ID of the MPS queue to which the snapshot job is submitted.
        self.pipeline_id = pipeline_id
        # The snapshot configurations.
        self.snapshot_config = snapshot_config
        # The status of the snapshot job. Valid values:
        # 
        # *   **Submitted**: The job is submitted.
        # *   **Snapshoting**: The job is being processed.
        # *   **Success**: The job is successful.
        # *   **Fail**: The job fails.
        self.state = state
        # The number of single images that are contained in the tiled image.
        self.tile_count = tile_count
        # The custom data.
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
            temp_model = main_models.SubmitSnapshotJobResponseBodySnapshotJobInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('MNSMessageResult') is not None:
            temp_model = main_models.SubmitSnapshotJobResponseBodySnapshotJobMNSMessageResult()
            self.mnsmessage_result = temp_model.from_map(m.get('MNSMessageResult'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('SnapshotConfig') is not None:
            temp_model = main_models.SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfig()
            self.snapshot_config = temp_model.from_map(m.get('SnapshotConfig'))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TileCount') is not None:
            self.tile_count = m.get('TileCount')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfig(DaraModel):
    def __init__(
        self,
        frame_type: str = None,
        height: str = None,
        interval: str = None,
        num: str = None,
        output_file: main_models.SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfigOutputFile = None,
        tile_out: main_models.SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfigTileOut = None,
        tile_output_file: main_models.SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfigTileOutputFile = None,
        time: str = None,
        time_array: main_models.SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfigTimeArray = None,
        width: str = None,
    ):
        # The type of the snapshot. Default value: **Normal**. Valid values:
        # 
        # *   **normal**: normal frames.
        # *   **intra**: I-frames (keyframes).
        # 
        # > If the FrameType parameter is set to intra in the request, only keyframes are captured. If no keyframe is found at the specified point in time, the keyframe closest to the specified point in time is captured. Keyframes are captured faster than normal frames if the same snapshot rules are applied.
        self.frame_type = frame_type
        # The height of the output snapshot.
        self.height = height
        # The interval for capturing snapshots.
        # 
        # *   If this parameter is specified in the request, snapshots are captured at intervals. The value must be greater than 0 in the request.
        # *   Unit: seconds.
        # *   Default value: **10**.
        self.interval = interval
        # The number of snapshots. If the Num parameter is set in the request, snapshots are captured at intervals.
        self.num = num
        # The information about the output file of the snapshot job.
        self.output_file = output_file
        # The tiling configurations.
        self.tile_out = tile_out
        # The information about the output file of the tiling job.
        self.tile_output_file = tile_output_file
        # The start time for capturing snapshots. Unit: milliseconds.
        self.time = time
        self.time_array = time_array
        # The width of the output snapshot.
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
            temp_model = main_models.SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfigOutputFile()
            self.output_file = temp_model.from_map(m.get('OutputFile'))

        if m.get('TileOut') is not None:
            temp_model = main_models.SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfigTileOut()
            self.tile_out = temp_model.from_map(m.get('TileOut'))

        if m.get('TileOutputFile') is not None:
            temp_model = main_models.SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfigTileOutputFile()
            self.tile_output_file = temp_model.from_map(m.get('TileOutputFile'))

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TimeArray') is not None:
            temp_model = main_models.SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfigTimeArray()
            self.time_array = temp_model.from_map(m.get('TimeArray'))

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfigTimeArray(DaraModel):
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

class SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfigTileOutputFile(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
        role_arn: str = None,
    ):
        # The OSS bucket that stores the object.
        self.bucket = bucket
        # The ID of the region in which the OSS bucket that stores the object is located.
        self.location = location
        # The OSS object that is generated as the output file of the tiling job.
        self.object = object
        # The ARN of the specified RAM role. Format: acs:ram::$accountID:role/$roleName.
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

class SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfigTileOut(DaraModel):
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
        # The height of a single image. The default value is the height of the output snapshot.
        self.cell_height = cell_height
        # The step for selecting a single image.
        self.cell_sel_step = cell_sel_step
        # The width of a single image. The default value is the width of the output snapshot.
        self.cell_width = cell_width
        # The background color.
        # 
        # *   Default value: **black**.
        # *   You can set the Color parameter to a **color keyword** or **random** in the request.
        # 
        # > If you want to set the background color to black, you can specify the color keyword in one of the following three formats: Black, black, and #000000.
        self.color = color
        # The number of columns that the tiled image contains. Default value: **10**.
        self.columns = columns
        # Indicates whether the single images are retained. Valid values:
        # 
        # *   **true**: The single images are retained.
        # *   **false**: The single images are not retained.
        # *   Default value: **true**.
        self.is_keep_cell_pic = is_keep_cell_pic
        # The number of rows that the tiled image contains. Default value: **10**.
        self.lines = lines
        # The margin width of the tiled image.
        # 
        # *   Default value: **0**.
        # *   Unit: pixel.
        self.margin = margin
        # The distance between two consecutive single images in the tiled image.
        # 
        # *   Default value: **0**.
        # *   Unit: pixel.
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

class SubmitSnapshotJobResponseBodySnapshotJobSnapshotConfigOutputFile(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
        role_arn: str = None,
    ):
        # The OSS bucket that stores the output snapshot.
        self.bucket = bucket
        # The OSS region in which the OSS bucket for storing the output snapshot resides.
        self.location = location
        # The OSS object that is generated as the output file of the snapshot job.
        self.object = object
        # The Alibaba Cloud Resource Name (ARN) of the specified RAM role. Format: acs:ram::$accountID:role/$roleName.
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

class SubmitSnapshotJobResponseBodySnapshotJobMNSMessageResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        message_id: str = None,
    ):
        # The error code returned if the job fails. This parameter is not returned if the job is successful.
        self.error_code = error_code
        # The error message returned if the job fails. This parameter is not returned if the job is successful.
        self.error_message = error_message
        # The ID of the message. This parameter is not returned if the job fails.
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

class SubmitSnapshotJobResponseBodySnapshotJobInput(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        location: str = None,
        object: str = None,
        role_arn: str = None,
    ):
        # The OSS bucket that stores the object.
        self.bucket = bucket
        # The region in which the OSS bucket resides.
        self.location = location
        # The OSS object that is used as the input file.
        self.object = object
        # The ARN of the specified RAM role. Format: acs:ram::$accountID:role/$roleName.
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

