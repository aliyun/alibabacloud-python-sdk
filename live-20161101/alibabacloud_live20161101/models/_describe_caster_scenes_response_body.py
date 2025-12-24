# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeCasterScenesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scene_list: main_models.DescribeCasterScenesResponseBodySceneList = None,
        total: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The scenes.
        self.scene_list = scene_list
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.scene_list:
            self.scene_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scene_list is not None:
            result['SceneList'] = self.scene_list.to_map()

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SceneList') is not None:
            temp_model = main_models.DescribeCasterScenesResponseBodySceneList()
            self.scene_list = temp_model.from_map(m.get('SceneList'))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeCasterScenesResponseBodySceneList(DaraModel):
    def __init__(
        self,
        scene: List[main_models.DescribeCasterScenesResponseBodySceneListScene] = None,
    ):
        self.scene = scene

    def validate(self):
        if self.scene:
            for v1 in self.scene:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Scene'] = []
        if self.scene is not None:
            for k1 in self.scene:
                result['Scene'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scene = []
        if m.get('Scene') is not None:
            for k1 in m.get('Scene'):
                temp_model = main_models.DescribeCasterScenesResponseBodySceneListScene()
                self.scene.append(temp_model.from_map(k1))

        return self

class DescribeCasterScenesResponseBodySceneListScene(DaraModel):
    def __init__(
        self,
        component_ids: main_models.DescribeCasterScenesResponseBodySceneListSceneComponentIds = None,
        layout_id: str = None,
        output_type: str = None,
        scene_id: str = None,
        scene_name: str = None,
        status: int = None,
        stream_infos: main_models.DescribeCasterScenesResponseBodySceneListSceneStreamInfos = None,
        stream_url: str = None,
    ):
        # The components.
        self.component_ids = component_ids
        # The ID of the layout.
        self.layout_id = layout_id
        # Indicates whether the output video is in PVW mode or PGM mode. Valid values:
        # 
        # *   **0**: in PVW mode.
        # *   **1**: in PGM mode.
        self.output_type = output_type
        # The ID of the scene. You can use the ID as a request parameter in the API operation that is used to modify the audio configurations of the scene, query the audio configurations of the scene, start the scene, or stop the scene.
        self.scene_id = scene_id
        # The name of the scene.
        self.scene_name = scene_name
        # The status of the scene. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.status = status
        # The information about the stream.
        self.stream_infos = stream_infos
        # The URL of the output stream.
        self.stream_url = stream_url

    def validate(self):
        if self.component_ids:
            self.component_ids.validate()
        if self.stream_infos:
            self.stream_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_ids is not None:
            result['ComponentIds'] = self.component_ids.to_map()

        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id

        if self.output_type is not None:
            result['OutputType'] = self.output_type

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.status is not None:
            result['Status'] = self.status

        if self.stream_infos is not None:
            result['StreamInfos'] = self.stream_infos.to_map()

        if self.stream_url is not None:
            result['StreamUrl'] = self.stream_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentIds') is not None:
            temp_model = main_models.DescribeCasterScenesResponseBodySceneListSceneComponentIds()
            self.component_ids = temp_model.from_map(m.get('ComponentIds'))

        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')

        if m.get('OutputType') is not None:
            self.output_type = m.get('OutputType')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StreamInfos') is not None:
            temp_model = main_models.DescribeCasterScenesResponseBodySceneListSceneStreamInfos()
            self.stream_infos = temp_model.from_map(m.get('StreamInfos'))

        if m.get('StreamUrl') is not None:
            self.stream_url = m.get('StreamUrl')

        return self

class DescribeCasterScenesResponseBodySceneListSceneStreamInfos(DaraModel):
    def __init__(
        self,
        stream_info: List[main_models.DescribeCasterScenesResponseBodySceneListSceneStreamInfosStreamInfo] = None,
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
                temp_model = main_models.DescribeCasterScenesResponseBodySceneListSceneStreamInfosStreamInfo()
                self.stream_info.append(temp_model.from_map(k1))

        return self

class DescribeCasterScenesResponseBodySceneListSceneStreamInfosStreamInfo(DaraModel):
    def __init__(
        self,
        output_stream_url: str = None,
        transcode_config: str = None,
        video_format: str = None,
    ):
        # The streaming URL.
        self.output_stream_url = output_stream_url
        # The transcoding configuration. Valid values:
        # 
        # *   **sd**: standard definition
        # *   **lld**: low definition
        # *   **lud**: ultra-high definition
        # *   **lhd**: high definition
        self.transcode_config = transcode_config
        # The format. Valid values:
        # 
        # *   **flv**
        # *   **mp4**
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

class DescribeCasterScenesResponseBodySceneListSceneComponentIds(DaraModel):
    def __init__(
        self,
        component_id: List[str] = None,
    ):
        self.component_id = component_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_id is not None:
            result['componentId'] = self.component_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentId') is not None:
            self.component_id = m.get('componentId')

        return self

