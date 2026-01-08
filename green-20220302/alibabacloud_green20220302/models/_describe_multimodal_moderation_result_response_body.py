# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220302 import models as main_models
from darabonba.model import DaraModel

class DescribeMultimodalModerationResultResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.DescribeMultimodalModerationResultResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id

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

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeMultimodalModerationResultResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMultimodalModerationResultResponseBodyData(DaraModel):
    def __init__(
        self,
        comment_datas: List[main_models.DescribeMultimodalModerationResultResponseBodyDataCommentDatas] = None,
        data_id: str = None,
        main_data: main_models.DescribeMultimodalModerationResultResponseBodyDataMainData = None,
        req_id: str = None,
        risk_level: str = None,
    ):
        self.comment_datas = comment_datas
        self.data_id = data_id
        self.main_data = main_data
        self.req_id = req_id
        self.risk_level = risk_level

    def validate(self):
        if self.comment_datas:
            for v1 in self.comment_datas:
                 if v1:
                    v1.validate()
        if self.main_data:
            self.main_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CommentDatas'] = []
        if self.comment_datas is not None:
            for k1 in self.comment_datas:
                result['CommentDatas'].append(k1.to_map() if k1 else None)

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.main_data is not None:
            result['MainData'] = self.main_data.to_map()

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.comment_datas = []
        if m.get('CommentDatas') is not None:
            for k1 in m.get('CommentDatas'):
                temp_model = main_models.DescribeMultimodalModerationResultResponseBodyDataCommentDatas()
                self.comment_datas.append(temp_model.from_map(k1))

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('MainData') is not None:
            temp_model = main_models.DescribeMultimodalModerationResultResponseBodyDataMainData()
            self.main_data = temp_model.from_map(m.get('MainData'))

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class DescribeMultimodalModerationResultResponseBodyDataMainData(DaraModel):
    def __init__(
        self,
        results: List[main_models.DescribeMultimodalModerationResultResponseBodyDataMainDataResults] = None,
    ):
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.DescribeMultimodalModerationResultResponseBodyDataMainDataResults()
                self.results.append(temp_model.from_map(k1))

        return self

class DescribeMultimodalModerationResultResponseBodyDataMainDataResults(DaraModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
    ):
        self.description = description
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class DescribeMultimodalModerationResultResponseBodyDataCommentDatas(DaraModel):
    def __init__(
        self,
        comment_datas: List[main_models.DescribeMultimodalModerationResultResponseBodyDataCommentDatasCommentDatas] = None,
        results: List[main_models.DescribeMultimodalModerationResultResponseBodyDataCommentDatasResults] = None,
    ):
        self.comment_datas = comment_datas
        self.results = results

    def validate(self):
        if self.comment_datas:
            for v1 in self.comment_datas:
                 if v1:
                    v1.validate()
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CommentDatas'] = []
        if self.comment_datas is not None:
            for k1 in self.comment_datas:
                result['CommentDatas'].append(k1.to_map() if k1 else None)

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.comment_datas = []
        if m.get('CommentDatas') is not None:
            for k1 in m.get('CommentDatas'):
                temp_model = main_models.DescribeMultimodalModerationResultResponseBodyDataCommentDatasCommentDatas()
                self.comment_datas.append(temp_model.from_map(k1))

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.DescribeMultimodalModerationResultResponseBodyDataCommentDatasResults()
                self.results.append(temp_model.from_map(k1))

        return self

class DescribeMultimodalModerationResultResponseBodyDataCommentDatasResults(DaraModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
    ):
        self.description = description
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

class DescribeMultimodalModerationResultResponseBodyDataCommentDatasCommentDatas(DaraModel):
    def __init__(
        self,
        results: List[main_models.DescribeMultimodalModerationResultResponseBodyDataCommentDatasCommentDatasResults] = None,
    ):
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.DescribeMultimodalModerationResultResponseBodyDataCommentDatasCommentDatasResults()
                self.results.append(temp_model.from_map(k1))

        return self

class DescribeMultimodalModerationResultResponseBodyDataCommentDatasCommentDatasResults(DaraModel):
    def __init__(
        self,
        description: str = None,
        label: str = None,
    ):
        self.description = description
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.label is not None:
            result['Label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        return self

