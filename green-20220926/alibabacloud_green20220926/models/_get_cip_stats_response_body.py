# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetCipStatsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetCipStatsResponseBodyData = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.msg = msg
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

        if self.msg is not None:
            result['Msg'] = self.msg

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
            temp_model = main_models.GetCipStatsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCipStatsResponseBodyData(DaraModel):
    def __init__(
        self,
        label_stat_chart: List[main_models.GetCipStatsResponseBodyDataLabelStatChart] = None,
        total_stat: Dict[str, dict] = None,
        uids: List[str] = None,
        x: List[str] = None,
        y: List[main_models.GetCipStatsResponseBodyDataY] = None,
        z: List[main_models.GetCipStatsResponseBodyDataZ] = None,
    ):
        self.label_stat_chart = label_stat_chart
        self.total_stat = total_stat
        self.uids = uids
        self.x = x
        self.y = y
        self.z = z

    def validate(self):
        if self.label_stat_chart:
            for v1 in self.label_stat_chart:
                 if v1:
                    v1.validate()
        if self.y:
            for v1 in self.y:
                 if v1:
                    v1.validate()
        if self.z:
            for v1 in self.z:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LabelStatChart'] = []
        if self.label_stat_chart is not None:
            for k1 in self.label_stat_chart:
                result['LabelStatChart'].append(k1.to_map() if k1 else None)

        if self.total_stat is not None:
            result['TotalStat'] = self.total_stat

        if self.uids is not None:
            result['Uids'] = self.uids

        if self.x is not None:
            result['X'] = self.x

        result['Y'] = []
        if self.y is not None:
            for k1 in self.y:
                result['Y'].append(k1.to_map() if k1 else None)

        result['Z'] = []
        if self.z is not None:
            for k1 in self.z:
                result['Z'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.label_stat_chart = []
        if m.get('LabelStatChart') is not None:
            for k1 in m.get('LabelStatChart'):
                temp_model = main_models.GetCipStatsResponseBodyDataLabelStatChart()
                self.label_stat_chart.append(temp_model.from_map(k1))

        if m.get('TotalStat') is not None:
            self.total_stat = m.get('TotalStat')

        if m.get('Uids') is not None:
            self.uids = m.get('Uids')

        if m.get('X') is not None:
            self.x = m.get('X')

        self.y = []
        if m.get('Y') is not None:
            for k1 in m.get('Y'):
                temp_model = main_models.GetCipStatsResponseBodyDataY()
                self.y.append(temp_model.from_map(k1))

        self.z = []
        if m.get('Z') is not None:
            for k1 in m.get('Z'):
                temp_model = main_models.GetCipStatsResponseBodyDataZ()
                self.z.append(temp_model.from_map(k1))

        return self

class GetCipStatsResponseBodyDataZ(DaraModel):
    def __init__(
        self,
        data: List[int] = None,
        name: str = None,
    ):
        self.data = data
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetCipStatsResponseBodyDataY(DaraModel):
    def __init__(
        self,
        data: List[int] = None,
        name: str = None,
    ):
        self.data = data
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetCipStatsResponseBodyDataLabelStatChart(DaraModel):
    def __init__(
        self,
        image_tree_char: List[main_models.GetCipStatsResponseBodyDataLabelStatChartImageTreeChar] = None,
        service_code: str = None,
        text_tree_chart: List[main_models.GetCipStatsResponseBodyDataLabelStatChartTextTreeChart] = None,
        total_count: int = None,
        tree_chart: List[main_models.GetCipStatsResponseBodyDataLabelStatChartTreeChart] = None,
        voice_tree_chart: List[main_models.GetCipStatsResponseBodyDataLabelStatChartVoiceTreeChart] = None,
        x: List[str] = None,
        y: List[main_models.GetCipStatsResponseBodyDataLabelStatChartY] = None,
    ):
        self.image_tree_char = image_tree_char
        self.service_code = service_code
        self.text_tree_chart = text_tree_chart
        self.total_count = total_count
        self.tree_chart = tree_chart
        self.voice_tree_chart = voice_tree_chart
        self.x = x
        self.y = y

    def validate(self):
        if self.image_tree_char:
            for v1 in self.image_tree_char:
                 if v1:
                    v1.validate()
        if self.text_tree_chart:
            for v1 in self.text_tree_chart:
                 if v1:
                    v1.validate()
        if self.tree_chart:
            for v1 in self.tree_chart:
                 if v1:
                    v1.validate()
        if self.voice_tree_chart:
            for v1 in self.voice_tree_chart:
                 if v1:
                    v1.validate()
        if self.y:
            for v1 in self.y:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageTreeChar'] = []
        if self.image_tree_char is not None:
            for k1 in self.image_tree_char:
                result['ImageTreeChar'].append(k1.to_map() if k1 else None)

        if self.service_code is not None:
            result['ServiceCode'] = self.service_code

        result['TextTreeChart'] = []
        if self.text_tree_chart is not None:
            for k1 in self.text_tree_chart:
                result['TextTreeChart'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TreeChart'] = []
        if self.tree_chart is not None:
            for k1 in self.tree_chart:
                result['TreeChart'].append(k1.to_map() if k1 else None)

        result['VoiceTreeChart'] = []
        if self.voice_tree_chart is not None:
            for k1 in self.voice_tree_chart:
                result['VoiceTreeChart'].append(k1.to_map() if k1 else None)

        if self.x is not None:
            result['X'] = self.x

        result['Y'] = []
        if self.y is not None:
            for k1 in self.y:
                result['Y'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_tree_char = []
        if m.get('ImageTreeChar') is not None:
            for k1 in m.get('ImageTreeChar'):
                temp_model = main_models.GetCipStatsResponseBodyDataLabelStatChartImageTreeChar()
                self.image_tree_char.append(temp_model.from_map(k1))

        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')

        self.text_tree_chart = []
        if m.get('TextTreeChart') is not None:
            for k1 in m.get('TextTreeChart'):
                temp_model = main_models.GetCipStatsResponseBodyDataLabelStatChartTextTreeChart()
                self.text_tree_chart.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.tree_chart = []
        if m.get('TreeChart') is not None:
            for k1 in m.get('TreeChart'):
                temp_model = main_models.GetCipStatsResponseBodyDataLabelStatChartTreeChart()
                self.tree_chart.append(temp_model.from_map(k1))

        self.voice_tree_chart = []
        if m.get('VoiceTreeChart') is not None:
            for k1 in m.get('VoiceTreeChart'):
                temp_model = main_models.GetCipStatsResponseBodyDataLabelStatChartVoiceTreeChart()
                self.voice_tree_chart.append(temp_model.from_map(k1))

        if m.get('X') is not None:
            self.x = m.get('X')

        self.y = []
        if m.get('Y') is not None:
            for k1 in m.get('Y'):
                temp_model = main_models.GetCipStatsResponseBodyDataLabelStatChartY()
                self.y.append(temp_model.from_map(k1))

        return self

class GetCipStatsResponseBodyDataLabelStatChartY(DaraModel):
    def __init__(
        self,
        data: List[int] = None,
        name: str = None,
    ):
        self.data = data
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetCipStatsResponseBodyDataLabelStatChartVoiceTreeChart(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetCipStatsResponseBodyDataLabelStatChartTreeChart(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetCipStatsResponseBodyDataLabelStatChartTextTreeChart(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetCipStatsResponseBodyDataLabelStatChartImageTreeChar(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

