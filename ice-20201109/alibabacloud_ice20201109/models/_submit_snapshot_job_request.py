# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitSnapshotJobRequest(DaraModel):
    def __init__(
        self,
        input: main_models.SubmitSnapshotJobRequestInput = None,
        name: str = None,
        output: main_models.SubmitSnapshotJobRequestOutput = None,
        schedule_config: main_models.SubmitSnapshotJobRequestScheduleConfig = None,
        template_config: main_models.SubmitSnapshotJobRequestTemplateConfig = None,
        user_data: str = None,
    ):
        # The snapshot input.
        # 
        # This parameter is required.
        self.input = input
        # The name of the job.
        self.name = name
        # The snapshot output.
        # 
        # This parameter is required.
        self.output = output
        # The scheduling settings.
        self.schedule_config = schedule_config
        # The snapshot template configuration.
        # 
        # This parameter is required.
        self.template_config = template_config
        # The user-defined data.
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()
        if self.output:
            self.output.validate()
        if self.schedule_config:
            self.schedule_config.validate()
        if self.template_config:
            self.template_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config.to_map()

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            temp_model = main_models.SubmitSnapshotJobRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Output') is not None:
            temp_model = main_models.SubmitSnapshotJobRequestOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('ScheduleConfig') is not None:
            temp_model = main_models.SubmitSnapshotJobRequestScheduleConfig()
            self.schedule_config = temp_model.from_map(m.get('ScheduleConfig'))

        if m.get('TemplateConfig') is not None:
            temp_model = main_models.SubmitSnapshotJobRequestTemplateConfig()
            self.template_config = temp_model.from_map(m.get('TemplateConfig'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitSnapshotJobRequestTemplateConfig(DaraModel):
    def __init__(
        self,
        overwrite_params: main_models.SubmitSnapshotJobRequestTemplateConfigOverwriteParams = None,
        template_id: str = None,
    ):
        # The parameters that are used to overwrite the corresponding parameters.
        self.overwrite_params = overwrite_params
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        if self.overwrite_params:
            self.overwrite_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overwrite_params is not None:
            result['OverwriteParams'] = self.overwrite_params.to_map()

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverwriteParams') is not None:
            temp_model = main_models.SubmitSnapshotJobRequestTemplateConfigOverwriteParams()
            self.overwrite_params = temp_model.from_map(m.get('OverwriteParams'))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class SubmitSnapshotJobRequestTemplateConfigOverwriteParams(DaraModel):
    def __init__(
        self,
        black_level: int = None,
        count: int = None,
        frame_type: str = None,
        height: int = None,
        interval: int = None,
        is_spt_frag: bool = None,
        pixel_black_threshold: int = None,
        sprite_snapshot_config: main_models.SubmitSnapshotJobRequestTemplateConfigOverwriteParamsSpriteSnapshotConfig = None,
        time: int = None,
        type: str = None,
        width: int = None,
    ):
        # The threshold that is used to filter out black frames for the first snapshot to be captured. This feature is available if you request the system to capture multiple snapshots.
        self.black_level = black_level
        # The number of snapshots.
        self.count = count
        # The type of the frame.
        self.frame_type = frame_type
        # The height of a captured snapshot.
        self.height = height
        # The interval at which snapshots are captured.
        self.interval = interval
        # The WebVTT snapshot configuration that specifies whether to merge the output snapshots.
        self.is_spt_frag = is_spt_frag
        # The color value threshold that determines whether a pixel is black.
        self.pixel_black_threshold = pixel_black_threshold
        # The configuration of the sprite snapshot.
        self.sprite_snapshot_config = sprite_snapshot_config
        # The point in time at which the system starts to capture snapshots in the input video.
        self.time = time
        # The snapshot type. Valid values:
        self.type = type
        # The width of a captured snapshot.
        self.width = width

    def validate(self):
        if self.sprite_snapshot_config:
            self.sprite_snapshot_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.black_level is not None:
            result['BlackLevel'] = self.black_level

        if self.count is not None:
            result['Count'] = self.count

        if self.frame_type is not None:
            result['FrameType'] = self.frame_type

        if self.height is not None:
            result['Height'] = self.height

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.is_spt_frag is not None:
            result['IsSptFrag'] = self.is_spt_frag

        if self.pixel_black_threshold is not None:
            result['PixelBlackThreshold'] = self.pixel_black_threshold

        if self.sprite_snapshot_config is not None:
            result['SpriteSnapshotConfig'] = self.sprite_snapshot_config.to_map()

        if self.time is not None:
            result['Time'] = self.time

        if self.type is not None:
            result['Type'] = self.type

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackLevel') is not None:
            self.black_level = m.get('BlackLevel')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('FrameType') is not None:
            self.frame_type = m.get('FrameType')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IsSptFrag') is not None:
            self.is_spt_frag = m.get('IsSptFrag')

        if m.get('PixelBlackThreshold') is not None:
            self.pixel_black_threshold = m.get('PixelBlackThreshold')

        if m.get('SpriteSnapshotConfig') is not None:
            temp_model = main_models.SubmitSnapshotJobRequestTemplateConfigOverwriteParamsSpriteSnapshotConfig()
            self.sprite_snapshot_config = temp_model.from_map(m.get('SpriteSnapshotConfig'))

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class SubmitSnapshotJobRequestTemplateConfigOverwriteParamsSpriteSnapshotConfig(DaraModel):
    def __init__(
        self,
        cell_height: int = None,
        cell_width: int = None,
        color: str = None,
        columns: int = None,
        lines: int = None,
        margin: int = None,
        padding: int = None,
    ):
        # The height of a single snapshot before tiling. The default value is the height of the output snapshot.
        self.cell_height = cell_height
        # The width of a single snapshot before tiling. The default value is the width of the output snapshot.
        self.cell_width = cell_width
        # The background color.
        self.color = color
        # The number of columns that the image sprite contains.
        self.columns = columns
        # The number of rows that the image sprite contains.
        self.lines = lines
        # The width of the frame. Default value: 0. Unit: pixels.
        self.margin = margin
        # The spacing between two adjacent snapshots. Default value: 0. Unit: pixels.
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

        if self.cell_width is not None:
            result['CellWidth'] = self.cell_width

        if self.color is not None:
            result['Color'] = self.color

        if self.columns is not None:
            result['Columns'] = self.columns

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

        if m.get('CellWidth') is not None:
            self.cell_width = m.get('CellWidth')

        if m.get('Color') is not None:
            self.color = m.get('Color')

        if m.get('Columns') is not None:
            self.columns = m.get('Columns')

        if m.get('Lines') is not None:
            self.lines = m.get('Lines')

        if m.get('Margin') is not None:
            self.margin = m.get('Margin')

        if m.get('Padding') is not None:
            self.padding = m.get('Padding')

        return self

class SubmitSnapshotJobRequestScheduleConfig(DaraModel):
    def __init__(
        self,
        pipeline_id: str = None,
    ):
        # The ID of the ApsaraVideo Media Processing (MPS) queue that is used to run the job.
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        return self

class SubmitSnapshotJobRequestOutput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The output file. If Type is set to OSS, the URL of an OSS object is returned. If Type is set to Media, the ID of a media asset is returned. The URL of an OSS object can be in one of the following formats:
        # 
        # 1.  oss://bucket/object
        # 2.  http(s)://bucket.oss-[RegionId].aliyuncs.com/object
        # 
        # In the URL, bucket specifies an OSS bucket that resides in the same region as the job, and object specifies the object URL in OSS. If multiple static snapshots were captured, the object must contain the "{Count}" placeholder. In the case of a sprite, the object must contain the "{TileCount}" placeholder. The suffix of the WebVTT snapshot objects must be ".vtt".
        # 
        # >  Before you use the OSS bucket in the URL, you must add the bucket on the [Storage Management](https://help.aliyun.com/document_detail/609918.html) page of the IMS console.
        # 
        # This parameter is required.
        self.media = media
        # The type of the output file. Valid values:
        # 
        # 1.  OSS: an OSS object.
        # 2.  Media: a media asset.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class SubmitSnapshotJobRequestInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The input file. If Type is set to OSS, the URL of an OSS object is returned. If Type is set to Media, the ID of a media asset is returned. The URL of an OSS object can be in one of the following formats:
        # 
        # 1.  oss://bucket/object
        # 2.  http(s)://bucket.oss-[RegionId].aliyuncs.com/object In the URL, bucket specifies an OSS bucket that resides in the same region as the job, and object specifies the object URL in OSS.
        # 
        # >  Before you use the OSS bucket in the URL, you must add the bucket on the [Storage Management](https://help.aliyun.com/document_detail/609918.html) page of the Intelligent Media Services (IMS) console.
        # 
        # This parameter is required.
        self.media = media
        # The type of the input file. Valid values:
        # 
        # 1.  OSS: an Object Storage Service (OSS) object.
        # 2.  Media: a media asset.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

