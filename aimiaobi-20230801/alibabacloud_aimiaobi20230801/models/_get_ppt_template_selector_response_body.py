# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetPptTemplateSelectorResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPptTemplateSelectorResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
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

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

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
            temp_model = main_models.GetPptTemplateSelectorResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPptTemplateSelectorResponseBodyData(DaraModel):
    def __init__(
        self,
        career: List[main_models.GetPptTemplateSelectorResponseBodyDataCareer] = None,
        colour: List[main_models.GetPptTemplateSelectorResponseBodyDataColour] = None,
        suit_scene: List[main_models.GetPptTemplateSelectorResponseBodyDataSuitScene] = None,
        suit_style: List[main_models.GetPptTemplateSelectorResponseBodyDataSuitStyle] = None,
    ):
        self.career = career
        self.colour = colour
        self.suit_scene = suit_scene
        self.suit_style = suit_style

    def validate(self):
        if self.career:
            for v1 in self.career:
                 if v1:
                    v1.validate()
        if self.colour:
            for v1 in self.colour:
                 if v1:
                    v1.validate()
        if self.suit_scene:
            for v1 in self.suit_scene:
                 if v1:
                    v1.validate()
        if self.suit_style:
            for v1 in self.suit_style:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Career'] = []
        if self.career is not None:
            for k1 in self.career:
                result['Career'].append(k1.to_map() if k1 else None)

        result['Colour'] = []
        if self.colour is not None:
            for k1 in self.colour:
                result['Colour'].append(k1.to_map() if k1 else None)

        result['SuitScene'] = []
        if self.suit_scene is not None:
            for k1 in self.suit_scene:
                result['SuitScene'].append(k1.to_map() if k1 else None)

        result['SuitStyle'] = []
        if self.suit_style is not None:
            for k1 in self.suit_style:
                result['SuitStyle'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.career = []
        if m.get('Career') is not None:
            for k1 in m.get('Career'):
                temp_model = main_models.GetPptTemplateSelectorResponseBodyDataCareer()
                self.career.append(temp_model.from_map(k1))

        self.colour = []
        if m.get('Colour') is not None:
            for k1 in m.get('Colour'):
                temp_model = main_models.GetPptTemplateSelectorResponseBodyDataColour()
                self.colour.append(temp_model.from_map(k1))

        self.suit_scene = []
        if m.get('SuitScene') is not None:
            for k1 in m.get('SuitScene'):
                temp_model = main_models.GetPptTemplateSelectorResponseBodyDataSuitScene()
                self.suit_scene.append(temp_model.from_map(k1))

        self.suit_style = []
        if m.get('SuitStyle') is not None:
            for k1 in m.get('SuitStyle'):
                temp_model = main_models.GetPptTemplateSelectorResponseBodyDataSuitStyle()
                self.suit_style.append(temp_model.from_map(k1))

        return self

class GetPptTemplateSelectorResponseBodyDataSuitStyle(DaraModel):
    def __init__(
        self,
        id: int = None,
        title: str = None,
    ):
        self.id = id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetPptTemplateSelectorResponseBodyDataSuitScene(DaraModel):
    def __init__(
        self,
        id: int = None,
        title: str = None,
    ):
        self.id = id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class GetPptTemplateSelectorResponseBodyDataColour(DaraModel):
    def __init__(
        self,
        code: str = None,
        id: int = None,
        name: str = None,
    ):
        self.code = code
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetPptTemplateSelectorResponseBodyDataCareer(DaraModel):
    def __init__(
        self,
        id: int = None,
        is_hot: int = None,
        name: str = None,
    ):
        self.id = id
        self.is_hot = is_hot
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.is_hot is not None:
            result['IsHot'] = self.is_hot

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsHot') is not None:
            self.is_hot = m.get('IsHot')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

