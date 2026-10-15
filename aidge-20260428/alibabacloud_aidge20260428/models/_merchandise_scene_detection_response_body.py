# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class MerchandiseSceneDetectionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.MerchandiseSceneDetectionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The display scene detection result.
        self.data = data
        # The response message or failure description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful.
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
            temp_model = main_models.MerchandiseSceneDetectionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class MerchandiseSceneDetectionResponseBodyData(DaraModel):
    def __init__(
        self,
        result: main_models.MerchandiseSceneDetectionResponseBodyDataResult = None,
        usage_map: Dict[str, int] = None,
    ):
        # The details of the display scene detection result.
        self.result = result
        # The usage information.
        self.usage_map = usage_map

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            temp_model = main_models.MerchandiseSceneDetectionResponseBodyDataResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('UsageMap') is not None:
            self.usage_map = m.get('UsageMap')

        return self

class MerchandiseSceneDetectionResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        grounding: main_models.MerchandiseSceneDetectionResponseBodyDataResultGrounding = None,
        scenes: List[main_models.MerchandiseSceneDetectionResponseBodyDataResultScenes] = None,
        type: str = None,
    ):
        # The positioning information.
        self.grounding = grounding
        # The list of recognized scenes.
        self.scenes = scenes
        # Fixed value: scene.
        self.type = type

    def validate(self):
        if self.grounding:
            self.grounding.validate()
        if self.scenes:
            for v1 in self.scenes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grounding is not None:
            result['Grounding'] = self.grounding.to_map()

        result['Scenes'] = []
        if self.scenes is not None:
            for k1 in self.scenes:
                result['Scenes'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Grounding') is not None:
            temp_model = main_models.MerchandiseSceneDetectionResponseBodyDataResultGrounding()
            self.grounding = temp_model.from_map(m.get('Grounding'))

        self.scenes = []
        if m.get('Scenes') is not None:
            for k1 in m.get('Scenes'):
                temp_model = main_models.MerchandiseSceneDetectionResponseBodyDataResultScenes()
                self.scenes.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class MerchandiseSceneDetectionResponseBodyDataResultScenes(DaraModel):
    def __init__(
        self,
        area_rate: float = None,
        own_purity: float = None,
        plumpness: float = None,
        scene_actual_name: str = None,
        scene_center: List[float] = None,
        scene_location: List[main_models.MerchandiseSceneDetectionResponseBodyDataResultScenesSceneLocation] = None,
        scene_name: str = None,
        shelf_distribution_rate: float = None,
    ):
        # Optional. The area proportion.
        self.area_rate = area_rate
        # Optional. The purity metric for proprietary products. The specific business criteria are subject to the recognition service.
        self.own_purity = own_purity
        # Optional. The display plumpness metric.
        self.plumpness = plumpness
        # The display name of the scene. If omitted, the value is an empty string.
        self.scene_actual_name = scene_actual_name
        # The center point of the scene, which retains the original normalized coordinates. If omitted, the value is an empty array.
        self.scene_center = scene_center
        # The list of region points. Each item is in the {x,y} format and retains the original normalized coordinates. If omitted, the value is an empty array.
        self.scene_location = scene_location
        # The scene identifier. This parameter is required and cannot be empty.
        self.scene_name = scene_name
        # Optional. The shelf distribution proportion metric. The specific business criteria are subject to the recognition service.
        self.shelf_distribution_rate = shelf_distribution_rate

    def validate(self):
        if self.scene_location:
            for v1 in self.scene_location:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_rate is not None:
            result['AreaRate'] = self.area_rate

        if self.own_purity is not None:
            result['OwnPurity'] = self.own_purity

        if self.plumpness is not None:
            result['Plumpness'] = self.plumpness

        if self.scene_actual_name is not None:
            result['SceneActualName'] = self.scene_actual_name

        if self.scene_center is not None:
            result['SceneCenter'] = self.scene_center

        result['SceneLocation'] = []
        if self.scene_location is not None:
            for k1 in self.scene_location:
                result['SceneLocation'].append(k1.to_map() if k1 else None)

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.shelf_distribution_rate is not None:
            result['ShelfDistributionRate'] = self.shelf_distribution_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaRate') is not None:
            self.area_rate = m.get('AreaRate')

        if m.get('OwnPurity') is not None:
            self.own_purity = m.get('OwnPurity')

        if m.get('Plumpness') is not None:
            self.plumpness = m.get('Plumpness')

        if m.get('SceneActualName') is not None:
            self.scene_actual_name = m.get('SceneActualName')

        if m.get('SceneCenter') is not None:
            self.scene_center = m.get('SceneCenter')

        self.scene_location = []
        if m.get('SceneLocation') is not None:
            for k1 in m.get('SceneLocation'):
                temp_model = main_models.MerchandiseSceneDetectionResponseBodyDataResultScenesSceneLocation()
                self.scene_location.append(temp_model.from_map(k1))

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('ShelfDistributionRate') is not None:
            self.shelf_distribution_rate = m.get('ShelfDistributionRate')

        return self

class MerchandiseSceneDetectionResponseBodyDataResultScenesSceneLocation(DaraModel):
    def __init__(
        self,
        x: float = None,
        y: float = None,
    ):
        # The x-coordinate of the region point.
        self.x = x
        # The y-coordinate of the region point.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class MerchandiseSceneDetectionResponseBodyDataResultGrounding(DaraModel):
    def __init__(
        self,
        coverage: str = None,
        regions: List[main_models.MerchandiseSceneDetectionResponseBodyDataResultGroundingRegions] = None,
    ):
        # The coverage.
        self.coverage = coverage
        # The list of regions.
        self.regions = regions

    def validate(self):
        if self.regions:
            for v1 in self.regions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coverage is not None:
            result['Coverage'] = self.coverage

        result['Regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['Regions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Coverage') is not None:
            self.coverage = m.get('Coverage')

        self.regions = []
        if m.get('Regions') is not None:
            for k1 in m.get('Regions'):
                temp_model = main_models.MerchandiseSceneDetectionResponseBodyDataResultGroundingRegions()
                self.regions.append(temp_model.from_map(k1))

        return self

class MerchandiseSceneDetectionResponseBodyDataResultGroundingRegions(DaraModel):
    def __init__(
        self,
        bbox_2d: List[float] = None,
        label: str = None,
        text: str = None,
    ):
        # The 2D bounding box in the format of [top-left x, top-left y, bottom-right x, bottom-right y]. Valid values: 0 to 1000. The left coordinate must be less than the right coordinate, and the top coordinate must be less than the bottom coordinate.
        self.bbox_2d = bbox_2d
        # The label.
        self.label = label
        # The recognized text.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bbox_2d is not None:
            result['Bbox_2d'] = self.bbox_2d

        if self.label is not None:
            result['Label'] = self.label

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bbox_2d') is not None:
            self.bbox_2d = m.get('Bbox_2d')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

