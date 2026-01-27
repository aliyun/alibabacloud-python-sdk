# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWmEmbedTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        audio_control_shrink: str = None,
        csv_control_shrink: str = None,
        document_control_shrink: str = None,
        file_url: str = None,
        filename: str = None,
        image_control_shrink: str = None,
        image_embed_jpeg_quality: int = None,
        image_embed_level: int = None,
        invisible_enable: bool = None,
        video_bitrate: str = None,
        video_control_shrink: str = None,
        video_is_long: bool = None,
        wm_info_bytes_b64: str = None,
        wm_info_size: int = None,
        wm_info_uint: str = None,
        wm_type: str = None,
    ):
        self.audio_control_shrink = audio_control_shrink
        self.csv_control_shrink = csv_control_shrink
        self.document_control_shrink = document_control_shrink
        # This parameter is required.
        self.file_url = file_url
        # This parameter is required.
        self.filename = filename
        self.image_control_shrink = image_control_shrink
        self.image_embed_jpeg_quality = image_embed_jpeg_quality
        self.image_embed_level = image_embed_level
        self.invisible_enable = invisible_enable
        self.video_bitrate = video_bitrate
        self.video_control_shrink = video_control_shrink
        self.video_is_long = video_is_long
        self.wm_info_bytes_b64 = wm_info_bytes_b64
        self.wm_info_size = wm_info_size
        self.wm_info_uint = wm_info_uint
        # This parameter is required.
        self.wm_type = wm_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_control_shrink is not None:
            result['AudioControl'] = self.audio_control_shrink

        if self.csv_control_shrink is not None:
            result['CsvControl'] = self.csv_control_shrink

        if self.document_control_shrink is not None:
            result['DocumentControl'] = self.document_control_shrink

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.filename is not None:
            result['Filename'] = self.filename

        if self.image_control_shrink is not None:
            result['ImageControl'] = self.image_control_shrink

        if self.image_embed_jpeg_quality is not None:
            result['ImageEmbedJpegQuality'] = self.image_embed_jpeg_quality

        if self.image_embed_level is not None:
            result['ImageEmbedLevel'] = self.image_embed_level

        if self.invisible_enable is not None:
            result['InvisibleEnable'] = self.invisible_enable

        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate

        if self.video_control_shrink is not None:
            result['VideoControl'] = self.video_control_shrink

        if self.video_is_long is not None:
            result['VideoIsLong'] = self.video_is_long

        if self.wm_info_bytes_b64 is not None:
            result['WmInfoBytesB64'] = self.wm_info_bytes_b64

        if self.wm_info_size is not None:
            result['WmInfoSize'] = self.wm_info_size

        if self.wm_info_uint is not None:
            result['WmInfoUint'] = self.wm_info_uint

        if self.wm_type is not None:
            result['WmType'] = self.wm_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioControl') is not None:
            self.audio_control_shrink = m.get('AudioControl')

        if m.get('CsvControl') is not None:
            self.csv_control_shrink = m.get('CsvControl')

        if m.get('DocumentControl') is not None:
            self.document_control_shrink = m.get('DocumentControl')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Filename') is not None:
            self.filename = m.get('Filename')

        if m.get('ImageControl') is not None:
            self.image_control_shrink = m.get('ImageControl')

        if m.get('ImageEmbedJpegQuality') is not None:
            self.image_embed_jpeg_quality = m.get('ImageEmbedJpegQuality')

        if m.get('ImageEmbedLevel') is not None:
            self.image_embed_level = m.get('ImageEmbedLevel')

        if m.get('InvisibleEnable') is not None:
            self.invisible_enable = m.get('InvisibleEnable')

        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')

        if m.get('VideoControl') is not None:
            self.video_control_shrink = m.get('VideoControl')

        if m.get('VideoIsLong') is not None:
            self.video_is_long = m.get('VideoIsLong')

        if m.get('WmInfoBytesB64') is not None:
            self.wm_info_bytes_b64 = m.get('WmInfoBytesB64')

        if m.get('WmInfoSize') is not None:
            self.wm_info_size = m.get('WmInfoSize')

        if m.get('WmInfoUint') is not None:
            self.wm_info_uint = m.get('WmInfoUint')

        if m.get('WmType') is not None:
            self.wm_type = m.get('WmType')

        return self

