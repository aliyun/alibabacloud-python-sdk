# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeVerifyDeviceRiskStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeVerifyDeviceRiskStatisticsResponseBodyResultObject = None,
    ):
        # ID of this request.
        self.request_id = request_id
        # Authentication result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DescribeVerifyDeviceRiskStatisticsResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class DescribeVerifyDeviceRiskStatisticsResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        face_attack_rate: str = None,
        id_fake_rate: str = None,
        items: List[main_models.DescribeVerifyDeviceRiskStatisticsResponseBodyResultObjectItems] = None,
        risk_count: int = None,
        root_rate: str = None,
        simulator_rate: str = None,
        virtual_video_rate: str = None,
    ):
        # Suspected fake face percentage: total number of suspected fake faces / total number of risks.
        self.face_attack_rate = face_attack_rate
        # Total number of suspected fake identities.
        self.id_fake_rate = id_fake_rate
        # Data items in the response.
        self.items = items
        # Number of risks.
        self.risk_count = risk_count
        # Root percentage: total number of root / total number of risks.
        self.root_rate = root_rate
        # Simulator percentage: total number of simulators / total number of risks.
        self.simulator_rate = simulator_rate
        # Virtual video percentage: total number of virtual videos / total number of risks.
        self.virtual_video_rate = virtual_video_rate

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_attack_rate is not None:
            result['FaceAttackRate'] = self.face_attack_rate

        if self.id_fake_rate is not None:
            result['IdFakeRate'] = self.id_fake_rate

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.root_rate is not None:
            result['RootRate'] = self.root_rate

        if self.simulator_rate is not None:
            result['SimulatorRate'] = self.simulator_rate

        if self.virtual_video_rate is not None:
            result['VirtualVideoRate'] = self.virtual_video_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceAttackRate') is not None:
            self.face_attack_rate = m.get('FaceAttackRate')

        if m.get('IdFakeRate') is not None:
            self.id_fake_rate = m.get('IdFakeRate')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeVerifyDeviceRiskStatisticsResponseBodyResultObjectItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('RootRate') is not None:
            self.root_rate = m.get('RootRate')

        if m.get('SimulatorRate') is not None:
            self.simulator_rate = m.get('SimulatorRate')

        if m.get('VirtualVideoRate') is not None:
            self.virtual_video_rate = m.get('VirtualVideoRate')

        return self

class DescribeVerifyDeviceRiskStatisticsResponseBodyResultObjectItems(DaraModel):
    def __init__(
        self,
        daily_call_count: int = None,
        date: str = None,
        device_risk_rate: str = None,
        identity_risk_rate: str = None,
    ):
        # Daily call count.
        self.daily_call_count = daily_call_count
        # Date.
        self.date = date
        # Abnormal device risk ratio.
        self.device_risk_rate = device_risk_rate
        # Abnormal identity risk ratio.
        self.identity_risk_rate = identity_risk_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.daily_call_count is not None:
            result['DailyCallCount'] = self.daily_call_count

        if self.date is not None:
            result['Date'] = self.date

        if self.device_risk_rate is not None:
            result['DeviceRiskRate'] = self.device_risk_rate

        if self.identity_risk_rate is not None:
            result['IdentityRiskRate'] = self.identity_risk_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DailyCallCount') is not None:
            self.daily_call_count = m.get('DailyCallCount')

        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('DeviceRiskRate') is not None:
            self.device_risk_rate = m.get('DeviceRiskRate')

        if m.get('IdentityRiskRate') is not None:
            self.identity_risk_rate = m.get('IdentityRiskRate')

        return self

