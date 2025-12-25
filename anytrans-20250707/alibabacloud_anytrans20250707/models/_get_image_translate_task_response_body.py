# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_anytrans20250707 import models as main_models
from darabonba.model import DaraModel

class GetImageTranslateTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetImageTranslateTaskResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        synchro: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.synchro = synchro

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.synchro is not None:
            result['synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetImageTranslateTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('synchro') is not None:
            self.synchro = m.get('synchro')

        return self

class GetImageTranslateTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        trace_id: str = None,
        translation: main_models.GetImageTranslateTaskResponseBodyDataTranslation = None,
    ):
        self.trace_id = trace_id
        self.translation = translation

    def validate(self):
        if self.translation:
            self.translation.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        if self.translation is not None:
            result['translation'] = self.translation.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        if m.get('translation') is not None:
            temp_model = main_models.GetImageTranslateTaskResponseBodyDataTranslation()
            self.translation = temp_model.from_map(m.get('translation'))

        return self

class GetImageTranslateTaskResponseBodyDataTranslation(DaraModel):
    def __init__(
        self,
        angle: int = None,
        bounding_boxes: List[main_models.GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxes] = None,
        boxes_count: int = None,
        height: int = None,
        org_height: int = None,
        org_width: int = None,
        table_infos: List[main_models.GetImageTranslateTaskResponseBodyDataTranslationTableInfos] = None,
        width: int = None,
    ):
        self.angle = angle
        self.bounding_boxes = bounding_boxes
        self.boxes_count = boxes_count
        self.height = height
        self.org_height = org_height
        self.org_width = org_width
        self.table_infos = table_infos
        self.width = width

    def validate(self):
        if self.bounding_boxes:
            for v1 in self.bounding_boxes:
                 if v1:
                    v1.validate()
        if self.table_infos:
            for v1 in self.table_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.angle is not None:
            result['angle'] = self.angle

        result['boundingBoxes'] = []
        if self.bounding_boxes is not None:
            for k1 in self.bounding_boxes:
                result['boundingBoxes'].append(k1.to_map() if k1 else None)

        if self.boxes_count is not None:
            result['boxesCount'] = self.boxes_count

        if self.height is not None:
            result['height'] = self.height

        if self.org_height is not None:
            result['orgHeight'] = self.org_height

        if self.org_width is not None:
            result['orgWidth'] = self.org_width

        result['tableInfos'] = []
        if self.table_infos is not None:
            for k1 in self.table_infos:
                result['tableInfos'].append(k1.to_map() if k1 else None)

        if self.width is not None:
            result['width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('angle') is not None:
            self.angle = m.get('angle')

        self.bounding_boxes = []
        if m.get('boundingBoxes') is not None:
            for k1 in m.get('boundingBoxes'):
                temp_model = main_models.GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxes()
                self.bounding_boxes.append(temp_model.from_map(k1))

        if m.get('boxesCount') is not None:
            self.boxes_count = m.get('boxesCount')

        if m.get('height') is not None:
            self.height = m.get('height')

        if m.get('orgHeight') is not None:
            self.org_height = m.get('orgHeight')

        if m.get('orgWidth') is not None:
            self.org_width = m.get('orgWidth')

        self.table_infos = []
        if m.get('tableInfos') is not None:
            for k1 in m.get('tableInfos'):
                temp_model = main_models.GetImageTranslateTaskResponseBodyDataTranslationTableInfos()
                self.table_infos.append(temp_model.from_map(k1))

        if m.get('width') is not None:
            self.width = m.get('width')

        return self

class GetImageTranslateTaskResponseBodyDataTranslationTableInfos(DaraModel):
    def __init__(
        self,
        cell_infos: List[main_models.GetImageTranslateTaskResponseBodyDataTranslationTableInfosCellInfos] = None,
        table_id: int = None,
        x_cell_size: int = None,
        y_cell_size: int = None,
    ):
        self.cell_infos = cell_infos
        self.table_id = table_id
        self.x_cell_size = x_cell_size
        self.y_cell_size = y_cell_size

    def validate(self):
        if self.cell_infos:
            for v1 in self.cell_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['cellInfos'] = []
        if self.cell_infos is not None:
            for k1 in self.cell_infos:
                result['cellInfos'].append(k1.to_map() if k1 else None)

        if self.table_id is not None:
            result['tableId'] = self.table_id

        if self.x_cell_size is not None:
            result['xCellSize'] = self.x_cell_size

        if self.y_cell_size is not None:
            result['yCellSize'] = self.y_cell_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cell_infos = []
        if m.get('cellInfos') is not None:
            for k1 in m.get('cellInfos'):
                temp_model = main_models.GetImageTranslateTaskResponseBodyDataTranslationTableInfosCellInfos()
                self.cell_infos.append(temp_model.from_map(k1))

        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')

        if m.get('xCellSize') is not None:
            self.x_cell_size = m.get('xCellSize')

        if m.get('yCellSize') is not None:
            self.y_cell_size = m.get('yCellSize')

        return self

class GetImageTranslateTaskResponseBodyDataTranslationTableInfosCellInfos(DaraModel):
    def __init__(
        self,
        pos: List[main_models.GetImageTranslateTaskResponseBodyDataTranslationTableInfosCellInfosPos] = None,
        table_cell_id: int = None,
        text: str = None,
        xec: int = None,
        xsc: int = None,
        yec: int = None,
        ysc: int = None,
    ):
        self.pos = pos
        self.table_cell_id = table_cell_id
        self.text = text
        self.xec = xec
        self.xsc = xsc
        self.yec = yec
        self.ysc = ysc

    def validate(self):
        if self.pos:
            for v1 in self.pos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['pos'] = []
        if self.pos is not None:
            for k1 in self.pos:
                result['pos'].append(k1.to_map() if k1 else None)

        if self.table_cell_id is not None:
            result['tableCellId'] = self.table_cell_id

        if self.text is not None:
            result['text'] = self.text

        if self.xec is not None:
            result['xec'] = self.xec

        if self.xsc is not None:
            result['xsc'] = self.xsc

        if self.yec is not None:
            result['yec'] = self.yec

        if self.ysc is not None:
            result['ysc'] = self.ysc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pos = []
        if m.get('pos') is not None:
            for k1 in m.get('pos'):
                temp_model = main_models.GetImageTranslateTaskResponseBodyDataTranslationTableInfosCellInfosPos()
                self.pos.append(temp_model.from_map(k1))

        if m.get('tableCellId') is not None:
            self.table_cell_id = m.get('tableCellId')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('xec') is not None:
            self.xec = m.get('xec')

        if m.get('xsc') is not None:
            self.xsc = m.get('xsc')

        if m.get('yec') is not None:
            self.yec = m.get('yec')

        if m.get('ysc') is not None:
            self.ysc = m.get('ysc')

        return self

class GetImageTranslateTaskResponseBodyDataTranslationTableInfosCellInfosPos(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['x'] = self.x

        if self.y is not None:
            result['y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')

        if m.get('y') is not None:
            self.y = m.get('y')

        return self

class GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxes(DaraModel):
    def __init__(
        self,
        confidence: float = None,
        direction: int = None,
        down_left: main_models.GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesDownLeft = None,
        down_right: main_models.GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesDownRight = None,
        table_cell_id: int = None,
        table_id: int = None,
        text: str = None,
        translation: Dict[str, Any] = None,
        up_left: main_models.GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesUpLeft = None,
        up_right: main_models.GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesUpRight = None,
    ):
        self.confidence = confidence
        self.direction = direction
        self.down_left = down_left
        self.down_right = down_right
        self.table_cell_id = table_cell_id
        self.table_id = table_id
        self.text = text
        self.translation = translation
        self.up_left = up_left
        self.up_right = up_right

    def validate(self):
        if self.down_left:
            self.down_left.validate()
        if self.down_right:
            self.down_right.validate()
        if self.up_left:
            self.up_left.validate()
        if self.up_right:
            self.up_right.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['confidence'] = self.confidence

        if self.direction is not None:
            result['direction'] = self.direction

        if self.down_left is not None:
            result['downLeft'] = self.down_left.to_map()

        if self.down_right is not None:
            result['downRight'] = self.down_right.to_map()

        if self.table_cell_id is not None:
            result['tableCellId'] = self.table_cell_id

        if self.table_id is not None:
            result['tableId'] = self.table_id

        if self.text is not None:
            result['text'] = self.text

        if self.translation is not None:
            result['translation'] = self.translation

        if self.up_left is not None:
            result['upLeft'] = self.up_left.to_map()

        if self.up_right is not None:
            result['upRight'] = self.up_right.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('confidence') is not None:
            self.confidence = m.get('confidence')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('downLeft') is not None:
            temp_model = main_models.GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesDownLeft()
            self.down_left = temp_model.from_map(m.get('downLeft'))

        if m.get('downRight') is not None:
            temp_model = main_models.GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesDownRight()
            self.down_right = temp_model.from_map(m.get('downRight'))

        if m.get('tableCellId') is not None:
            self.table_cell_id = m.get('tableCellId')

        if m.get('tableId') is not None:
            self.table_id = m.get('tableId')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('translation') is not None:
            self.translation = m.get('translation')

        if m.get('upLeft') is not None:
            temp_model = main_models.GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesUpLeft()
            self.up_left = temp_model.from_map(m.get('upLeft'))

        if m.get('upRight') is not None:
            temp_model = main_models.GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesUpRight()
            self.up_right = temp_model.from_map(m.get('upRight'))

        return self

class GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesUpRight(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['x'] = self.x

        if self.y is not None:
            result['y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')

        if m.get('y') is not None:
            self.y = m.get('y')

        return self

class GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesUpLeft(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['x'] = self.x

        if self.y is not None:
            result['y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')

        if m.get('y') is not None:
            self.y = m.get('y')

        return self

class GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesDownRight(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['x'] = self.x

        if self.y is not None:
            result['y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')

        if m.get('y') is not None:
            self.y = m.get('y')

        return self

class GetImageTranslateTaskResponseBodyDataTranslationBoundingBoxesDownLeft(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
    ):
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['x'] = self.x

        if self.y is not None:
            result['y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('x') is not None:
            self.x = m.get('x')

        if m.get('y') is not None:
            self.y = m.get('y')

        return self

