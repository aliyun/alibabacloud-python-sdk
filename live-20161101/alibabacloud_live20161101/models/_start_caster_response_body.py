# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class StartCasterResponseBody(DaraModel):
    def __init__(
        self,
        pgm_scene_infos: main_models.StartCasterResponseBodyPgmSceneInfos = None,
        pvw_scene_infos: main_models.StartCasterResponseBodyPvwSceneInfos = None,
        request_id: str = None,
    ):
        # The PGM scenes.
        self.pgm_scene_infos = pgm_scene_infos
        # The PVW scenes.
        self.pvw_scene_infos = pvw_scene_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.pgm_scene_infos:
            self.pgm_scene_infos.validate()
        if self.pvw_scene_infos:
            self.pvw_scene_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pgm_scene_infos is not None:
            result['PgmSceneInfos'] = self.pgm_scene_infos.to_map()

        if self.pvw_scene_infos is not None:
            result['PvwSceneInfos'] = self.pvw_scene_infos.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PgmSceneInfos') is not None:
            temp_model = main_models.StartCasterResponseBodyPgmSceneInfos()
            self.pgm_scene_infos = temp_model.from_map(m.get('PgmSceneInfos'))

        if m.get('PvwSceneInfos') is not None:
            temp_model = main_models.StartCasterResponseBodyPvwSceneInfos()
            self.pvw_scene_infos = temp_model.from_map(m.get('PvwSceneInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class StartCasterResponseBodyPvwSceneInfos(DaraModel):
    def __init__(
        self,
        scene_info: List[main_models.StartCasterResponseBodyPvwSceneInfosSceneInfo] = None,
    ):
        self.scene_info = scene_info

    def validate(self):
        if self.scene_info:
            for v1 in self.scene_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SceneInfo'] = []
        if self.scene_info is not None:
            for k1 in self.scene_info:
                result['SceneInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scene_info = []
        if m.get('SceneInfo') is not None:
            for k1 in m.get('SceneInfo'):
                temp_model = main_models.StartCasterResponseBodyPvwSceneInfosSceneInfo()
                self.scene_info.append(temp_model.from_map(k1))

        return self

class StartCasterResponseBodyPvwSceneInfosSceneInfo(DaraModel):
    def __init__(
        self,
        scene_id: str = None,
        stream_url: str = None,
    ):
        # The ID of the scene.
        self.scene_id = scene_id
        # The streaming URL of the PVW scene in the production studio. The value is not a stream relay URL.
        self.stream_url = stream_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.stream_url is not None:
            result['StreamUrl'] = self.stream_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('StreamUrl') is not None:
            self.stream_url = m.get('StreamUrl')

        return self

class StartCasterResponseBodyPgmSceneInfos(DaraModel):
    def __init__(
        self,
        scene_info: List[main_models.StartCasterResponseBodyPgmSceneInfosSceneInfo] = None,
    ):
        self.scene_info = scene_info

    def validate(self):
        if self.scene_info:
            for v1 in self.scene_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SceneInfo'] = []
        if self.scene_info is not None:
            for k1 in self.scene_info:
                result['SceneInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scene_info = []
        if m.get('SceneInfo') is not None:
            for k1 in m.get('SceneInfo'):
                temp_model = main_models.StartCasterResponseBodyPgmSceneInfosSceneInfo()
                self.scene_info.append(temp_model.from_map(k1))

        return self

class StartCasterResponseBodyPgmSceneInfosSceneInfo(DaraModel):
    def __init__(
        self,
        scene_id: str = None,
        stream_infos: main_models.StartCasterResponseBodyPgmSceneInfosSceneInfoStreamInfos = None,
        stream_url: str = None,
    ):
        # The ID of the scene.
        self.scene_id = scene_id
        # The stream relay URLs.
        self.stream_infos = stream_infos
        # The streaming URL of the PGM scene in the production studio. The value is not a stream relay URL.
        self.stream_url = stream_url

    def validate(self):
        if self.stream_infos:
            self.stream_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.stream_infos is not None:
            result['StreamInfos'] = self.stream_infos.to_map()

        if self.stream_url is not None:
            result['StreamUrl'] = self.stream_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('StreamInfos') is not None:
            temp_model = main_models.StartCasterResponseBodyPgmSceneInfosSceneInfoStreamInfos()
            self.stream_infos = temp_model.from_map(m.get('StreamInfos'))

        if m.get('StreamUrl') is not None:
            self.stream_url = m.get('StreamUrl')

        return self

class StartCasterResponseBodyPgmSceneInfosSceneInfoStreamInfos(DaraModel):
    def __init__(
        self,
        stream_info: List[main_models.StartCasterResponseBodyPgmSceneInfosSceneInfoStreamInfosStreamInfo] = None,
    ):
        self.stream_info = stream_info

    def validate(self):
        if self.stream_info:
            for v1 in self.stream_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StreamInfo'] = []
        if self.stream_info is not None:
            for k1 in self.stream_info:
                result['StreamInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stream_info = []
        if m.get('StreamInfo') is not None:
            for k1 in m.get('StreamInfo'):
                temp_model = main_models.StartCasterResponseBodyPgmSceneInfosSceneInfoStreamInfosStreamInfo()
                self.stream_info.append(temp_model.from_map(k1))

        return self

class StartCasterResponseBodyPgmSceneInfosSceneInfoStreamInfosStreamInfo(DaraModel):
    def __init__(
        self,
        output_stream_url: str = None,
        transcode_config: str = None,
        video_format: str = None,
    ):
        # The URL.
        self.output_stream_url = output_stream_url
        # The transcoding configuration. Valid values:
        # 
        # *   **lsd**: standard definition
        # *   **lld**: low definition
        # *   **lud**: ultra-high definition
        # *   **lhd**: high definition
        self.transcode_config = transcode_config
        # The format. Valid values:
        # 
        # *   **flv**
        # *   **rtmp**
        # *   **m3u8**
        self.video_format = video_format

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output_stream_url is not None:
            result['OutputStreamUrl'] = self.output_stream_url

        if self.transcode_config is not None:
            result['TranscodeConfig'] = self.transcode_config

        if self.video_format is not None:
            result['VideoFormat'] = self.video_format

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutputStreamUrl') is not None:
            self.output_stream_url = m.get('OutputStreamUrl')

        if m.get('TranscodeConfig') is not None:
            self.transcode_config = m.get('TranscodeConfig')

        if m.get('VideoFormat') is not None:
            self.video_format = m.get('VideoFormat')

        return self

