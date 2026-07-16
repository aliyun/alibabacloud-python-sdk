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
        # The input for the snapshot job.
        # 
        # This parameter is required.
        self.input = input
        # The name of the snapshot job.
        self.name = name
        # The output destination for the snapshot job.
        # 
        # This parameter is required.
        self.output = output
        # The scheduling configuration.
        self.schedule_config = schedule_config
        # The snapshot template configuration.
        # 
        # This parameter is required.
        self.template_config = template_config
        # Custom user data, passed as a JSON-formatted string.
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
        # Parameters used to override settings in the specified template.
        self.overwrite_params = overwrite_params
        # The snapshot template ID.
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
        # The threshold for detecting and filtering black content in the first frame. This applies only to multi-frame snapshots.
        self.black_level = black_level
        # The number of snapshots to capture.
        self.count = count
        # The frame type.
        self.frame_type = frame_type
        # The output image height.
        self.height = height
        # The interval between snapshots.
        self.interval = interval
        # Specifies whether to stitch snapshots into a single sprite. This applies only to WebVTT snapshots.
        self.is_spt_frag = is_spt_frag
        # The threshold for determining whether a pixel is black.
        self.pixel_black_threshold = pixel_black_threshold
        # The sprite configuration.
        self.sprite_snapshot_config = sprite_snapshot_config
        # The start time for capturing snapshots.
        self.time = time
        # The snapshot type.
        self.type = type
        # The output image width.
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
        # The height of each tile. Default: the height of the output snapshot.
        self.cell_height = cell_height
        # The width of each tile. Default: the width of the output snapshot.
        self.cell_width = cell_width
        # The background color.
        self.color = color
        # The number of columns in the sprite grid.
        self.columns = columns
        # The number of rows in the sprite grid.
        self.lines = lines
        # The margin around the sprite, in pixels. Default value: 0.
        self.margin = margin
        # The padding between tiles, in pixels. Default value: 0.
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
        # The pipeline ID.
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
        # The output media asset.
        # 
        # - If `Type` is `OSS`, specify the OSS URL for the output file.
        # 
        # - If `Type` is `Media`, specify the ID of the output media asset.
        # 
        # The OSS URL must be in one of the following formats:
        # 
        # 1. `oss://bucket/object`
        # 
        # 2. `http(s)://bucket.oss-[RegionId].aliyuncs.com/object`
        # 
        # In these formats, `bucket` is the name of an OSS bucket located in the same region as the current project, and `object` is the file path.
        # 
        # - When capturing multiple static snapshots, the `object` must contain the `{Count}` placeholder.
        # 
        # - When capturing a sprite, the `object` must contain the `{TileCount}` placeholder.
        # 
        # - For WebVTT snapshots, the filename in the `object` path must end with `.vtt`.
        # 
        # > The OSS bucket specified in the URL must be added to IMS [storage management](https://help.aliyun.com/document_detail/609918.html) before use.
        # 
        # This parameter is required.
        self.media = media
        # The type of the output. Valid values:
        # 
        # - `OSS`: an OSS file URL.
        # 
        # - `Media`: a media asset ID.
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
        # The input media asset.
        # 
        # - If `Type` is `OSS`, specify the OSS URL of the input file.
        # 
        # - If `Type` is `Media`, specify the ID of the media asset.
        # 
        # The OSS URL must be in one of the following formats:
        # 
        # 1. `oss://bucket/object`
        # 
        # 2. `http(s)://bucket.oss-[RegionId].aliyuncs.com/object`
        #    <br>In these formats, `bucket` is the name of an OSS bucket located in the same region as the current project, and `object` is the file path.<br>
        # 
        # > The OSS bucket specified in the URL must be added to IMS [storage management](https://help.aliyun.com/document_detail/609918.html) before use.
        # 
        # This parameter is required.
        self.media = media
        # The type of the input. Valid values:
        # 
        # - `OSS`: an OSS file URL.
        # 
        # - `Media`: a media asset ID.
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

