# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListInstanceRiskNumResponseBody(DaraModel):
    def __init__(
        self,
        instance_risk_num: List[main_models.ListInstanceRiskNumResponseBodyInstanceRiskNum] = None,
        request_id: str = None,
    ):
        # The information about the risks in the instance.
        self.instance_risk_num = instance_risk_num
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_risk_num:
            for v1 in self.instance_risk_num:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceRiskNum'] = []
        if self.instance_risk_num is not None:
            for k1 in self.instance_risk_num:
                result['InstanceRiskNum'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_risk_num = []
        if m.get('InstanceRiskNum') is not None:
            for k1 in m.get('InstanceRiskNum'):
                temp_model = main_models.ListInstanceRiskNumResponseBodyInstanceRiskNum()
                self.instance_risk_num.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListInstanceRiskNumResponseBodyInstanceRiskNum(DaraModel):
    def __init__(
        self,
        instance_item: main_models.ListInstanceRiskNumResponseBodyInstanceRiskNumInstanceItem = None,
        risk_num_entity: main_models.ListInstanceRiskNumResponseBodyInstanceRiskNumRiskNumEntity = None,
    ):
        # The information about the instance.
        self.instance_item = instance_item
        # The statistics about the risks.
        self.risk_num_entity = risk_num_entity

    def validate(self):
        if self.instance_item:
            self.instance_item.validate()
        if self.risk_num_entity:
            self.risk_num_entity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_item is not None:
            result['InstanceItem'] = self.instance_item.to_map()

        if self.risk_num_entity is not None:
            result['RiskNumEntity'] = self.risk_num_entity.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceItem') is not None:
            temp_model = main_models.ListInstanceRiskNumResponseBodyInstanceRiskNumInstanceItem()
            self.instance_item = temp_model.from_map(m.get('InstanceItem'))

        if m.get('RiskNumEntity') is not None:
            temp_model = main_models.ListInstanceRiskNumResponseBodyInstanceRiskNumRiskNumEntity()
            self.risk_num_entity = temp_model.from_map(m.get('RiskNumEntity'))

        return self

class ListInstanceRiskNumResponseBodyInstanceRiskNumRiskNumEntity(DaraModel):
    def __init__(
        self,
        suspicious_high_count: int = None,
        suspicious_low_count: int = None,
        suspicious_medium_count: int = None,
        vul_high_count: int = None,
        vul_low_count: int = None,
        vul_medium_count: int = None,
        weak_pass_word_count: int = None,
    ):
        # The number of high-risk alerts.
        self.suspicious_high_count = suspicious_high_count
        # The number of low-risk alerts.
        self.suspicious_low_count = suspicious_low_count
        # The number of medium-risk alerts.
        self.suspicious_medium_count = suspicious_medium_count
        # The number of high-risk vulnerabilities.
        self.vul_high_count = vul_high_count
        # The number of low-risk vulnerabilities.
        self.vul_low_count = vul_low_count
        # The number of medium-risk vulnerabilities.
        self.vul_medium_count = vul_medium_count
        # The number of weak passwords exposed on the Internet.
        self.weak_pass_word_count = weak_pass_word_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.suspicious_high_count is not None:
            result['SuspiciousHighCount'] = self.suspicious_high_count

        if self.suspicious_low_count is not None:
            result['SuspiciousLowCount'] = self.suspicious_low_count

        if self.suspicious_medium_count is not None:
            result['SuspiciousMediumCount'] = self.suspicious_medium_count

        if self.vul_high_count is not None:
            result['VulHighCount'] = self.vul_high_count

        if self.vul_low_count is not None:
            result['VulLowCount'] = self.vul_low_count

        if self.vul_medium_count is not None:
            result['VulMediumCount'] = self.vul_medium_count

        if self.weak_pass_word_count is not None:
            result['WeakPassWordCount'] = self.weak_pass_word_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SuspiciousHighCount') is not None:
            self.suspicious_high_count = m.get('SuspiciousHighCount')

        if m.get('SuspiciousLowCount') is not None:
            self.suspicious_low_count = m.get('SuspiciousLowCount')

        if m.get('SuspiciousMediumCount') is not None:
            self.suspicious_medium_count = m.get('SuspiciousMediumCount')

        if m.get('VulHighCount') is not None:
            self.vul_high_count = m.get('VulHighCount')

        if m.get('VulLowCount') is not None:
            self.vul_low_count = m.get('VulLowCount')

        if m.get('VulMediumCount') is not None:
            self.vul_medium_count = m.get('VulMediumCount')

        if m.get('WeakPassWordCount') is not None:
            self.weak_pass_word_count = m.get('WeakPassWordCount')

        return self

class ListInstanceRiskNumResponseBodyInstanceRiskNumInstanceItem(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        uuid: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The UUID of the instance.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

