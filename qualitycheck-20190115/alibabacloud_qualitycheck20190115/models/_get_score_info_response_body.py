# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetScoreInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetScoreInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = main_models.GetScoreInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetScoreInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        score_po: List[main_models.GetScoreInfoResponseBodyDataScorePo] = None,
    ):
        self.score_po = score_po

    def validate(self):
        if self.score_po:
            for v1 in self.score_po:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ScorePo'] = []
        if self.score_po is not None:
            for k1 in self.score_po:
                result['ScorePo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.score_po = []
        if m.get('ScorePo') is not None:
            for k1 in m.get('ScorePo'):
                temp_model = main_models.GetScoreInfoResponseBodyDataScorePo()
                self.score_po.append(temp_model.from_map(k1))

        return self

class GetScoreInfoResponseBodyDataScorePo(DaraModel):
    def __init__(
        self,
        score_id: int = None,
        score_infos: main_models.GetScoreInfoResponseBodyDataScorePoScoreInfos = None,
        score_name: str = None,
    ):
        self.score_id = score_id
        self.score_infos = score_infos
        self.score_name = score_name

    def validate(self):
        if self.score_infos:
            self.score_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.score_id is not None:
            result['ScoreId'] = self.score_id

        if self.score_infos is not None:
            result['ScoreInfos'] = self.score_infos.to_map()

        if self.score_name is not None:
            result['ScoreName'] = self.score_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScoreId') is not None:
            self.score_id = m.get('ScoreId')

        if m.get('ScoreInfos') is not None:
            temp_model = main_models.GetScoreInfoResponseBodyDataScorePoScoreInfos()
            self.score_infos = temp_model.from_map(m.get('ScoreInfos'))

        if m.get('ScoreName') is not None:
            self.score_name = m.get('ScoreName')

        return self

class GetScoreInfoResponseBodyDataScorePoScoreInfos(DaraModel):
    def __init__(
        self,
        score_param: List[main_models.GetScoreInfoResponseBodyDataScorePoScoreInfosScoreParam] = None,
    ):
        self.score_param = score_param

    def validate(self):
        if self.score_param:
            for v1 in self.score_param:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ScoreParam'] = []
        if self.score_param is not None:
            for k1 in self.score_param:
                result['ScoreParam'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.score_param = []
        if m.get('ScoreParam') is not None:
            for k1 in m.get('ScoreParam'):
                temp_model = main_models.GetScoreInfoResponseBodyDataScorePoScoreInfosScoreParam()
                self.score_param.append(temp_model.from_map(k1))

        return self

class GetScoreInfoResponseBodyDataScorePoScoreInfosScoreParam(DaraModel):
    def __init__(
        self,
        score_num: int = None,
        score_sub_id: int = None,
        score_sub_name: str = None,
        score_type: int = None,
    ):
        self.score_num = score_num
        self.score_sub_id = score_sub_id
        self.score_sub_name = score_sub_name
        self.score_type = score_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.score_num is not None:
            result['ScoreNum'] = self.score_num

        if self.score_sub_id is not None:
            result['ScoreSubId'] = self.score_sub_id

        if self.score_sub_name is not None:
            result['ScoreSubName'] = self.score_sub_name

        if self.score_type is not None:
            result['ScoreType'] = self.score_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScoreNum') is not None:
            self.score_num = m.get('ScoreNum')

        if m.get('ScoreSubId') is not None:
            self.score_sub_id = m.get('ScoreSubId')

        if m.get('ScoreSubName') is not None:
            self.score_sub_name = m.get('ScoreSubName')

        if m.get('ScoreType') is not None:
            self.score_type = m.get('ScoreType')

        return self

