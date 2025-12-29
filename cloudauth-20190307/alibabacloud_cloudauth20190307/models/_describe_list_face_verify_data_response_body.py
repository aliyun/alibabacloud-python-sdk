# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeListFaceVerifyDataResponseBody(DaraModel):
    def __init__(
        self,
        monitor_data: main_models.DescribeListFaceVerifyDataResponseBodyMonitorData = None,
        request_id: str = None,
    ):
        # Returned data.
        self.monitor_data = monitor_data
        # ID of this request.
        self.request_id = request_id

    def validate(self):
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorData') is not None:
            temp_model = main_models.DescribeListFaceVerifyDataResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m.get('MonitorData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeListFaceVerifyDataResponseBodyMonitorData(DaraModel):
    def __init__(
        self,
        face_verify_data: List[main_models.DescribeListFaceVerifyDataResponseBodyMonitorDataFaceVerifyData] = None,
    ):
        # Face verification data.
        self.face_verify_data = face_verify_data

    def validate(self):
        if self.face_verify_data:
            for v1 in self.face_verify_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FaceVerifyData'] = []
        if self.face_verify_data is not None:
            for k1 in self.face_verify_data:
                result['FaceVerifyData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.face_verify_data = []
        if m.get('FaceVerifyData') is not None:
            for k1 in m.get('FaceVerifyData'):
                temp_model = main_models.DescribeListFaceVerifyDataResponseBodyMonitorDataFaceVerifyData()
                self.face_verify_data.append(temp_model.from_map(k1))

        return self

class DescribeListFaceVerifyDataResponseBodyMonitorDataFaceVerifyData(DaraModel):
    def __init__(
        self,
        con_date: str = None,
        fail_cnt: str = None,
        name: str = None,
        scene_id: str = None,
        succ_cnt: str = None,
        total_cnt: str = None,
    ):
        # Verification statistics time.
        self.con_date = con_date
        # Number of failed verifications.
        self.fail_cnt = fail_cnt
        # Verification scheme.
        self.name = name
        # Scene ID.
        self.scene_id = scene_id
        # Number of successful verifications.
        self.succ_cnt = succ_cnt
        # Total number of verifications.
        self.total_cnt = total_cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.con_date is not None:
            result['ConDate'] = self.con_date

        if self.fail_cnt is not None:
            result['FailCnt'] = self.fail_cnt

        if self.name is not None:
            result['Name'] = self.name

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.succ_cnt is not None:
            result['SuccCnt'] = self.succ_cnt

        if self.total_cnt is not None:
            result['TotalCnt'] = self.total_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConDate') is not None:
            self.con_date = m.get('ConDate')

        if m.get('FailCnt') is not None:
            self.fail_cnt = m.get('FailCnt')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SuccCnt') is not None:
            self.succ_cnt = m.get('SuccCnt')

        if m.get('TotalCnt') is not None:
            self.total_cnt = m.get('TotalCnt')

        return self

