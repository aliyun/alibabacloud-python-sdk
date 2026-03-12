# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class DescribeConfigHistoryResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[main_models.DescribeConfigHistoryResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeConfigHistoryResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeConfigHistoryResponseBodyData(DaraModel):
    def __init__(
        self,
        config_history_effect_details: List[main_models.DescribeConfigHistoryResponseBodyDataConfigHistoryEffectDetails] = None,
        config_history_id: str = None,
        config_mementos: List[main_models.DescribeConfigHistoryResponseBodyDataConfigMementos] = None,
        effect_status: str = None,
        effected: bool = None,
        gmt_create: int = None,
        operator_id: str = None,
        reason: str = None,
        rollback: bool = None,
    ):
        self.config_history_effect_details = config_history_effect_details
        self.config_history_id = config_history_id
        self.config_mementos = config_mementos
        self.effect_status = effect_status
        self.effected = effected
        self.gmt_create = gmt_create
        self.operator_id = operator_id
        self.reason = reason
        self.rollback = rollback

    def validate(self):
        if self.config_history_effect_details:
            for v1 in self.config_history_effect_details:
                 if v1:
                    v1.validate()
        if self.config_mementos:
            for v1 in self.config_mementos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigHistoryEffectDetails'] = []
        if self.config_history_effect_details is not None:
            for k1 in self.config_history_effect_details:
                result['ConfigHistoryEffectDetails'].append(k1.to_map() if k1 else None)

        if self.config_history_id is not None:
            result['ConfigHistoryId'] = self.config_history_id

        result['ConfigMementos'] = []
        if self.config_mementos is not None:
            for k1 in self.config_mementos:
                result['ConfigMementos'].append(k1.to_map() if k1 else None)

        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status

        if self.effected is not None:
            result['Effected'] = self.effected

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.rollback is not None:
            result['Rollback'] = self.rollback

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_history_effect_details = []
        if m.get('ConfigHistoryEffectDetails') is not None:
            for k1 in m.get('ConfigHistoryEffectDetails'):
                temp_model = main_models.DescribeConfigHistoryResponseBodyDataConfigHistoryEffectDetails()
                self.config_history_effect_details.append(temp_model.from_map(k1))

        if m.get('ConfigHistoryId') is not None:
            self.config_history_id = m.get('ConfigHistoryId')

        self.config_mementos = []
        if m.get('ConfigMementos') is not None:
            for k1 in m.get('ConfigMementos'):
                temp_model = main_models.DescribeConfigHistoryResponseBodyDataConfigMementos()
                self.config_mementos.append(temp_model.from_map(k1))

        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')

        if m.get('Effected') is not None:
            self.effected = m.get('Effected')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Rollback') is not None:
            self.rollback = m.get('Rollback')

        return self

class DescribeConfigHistoryResponseBodyDataConfigMementos(DaraModel):
    def __init__(
        self,
        action: str = None,
        after: str = None,
        before: str = None,
        config_key: str = None,
        config_type: str = None,
    ):
        self.action = action
        self.after = after
        self.before = before
        self.config_key = config_key
        self.config_type = config_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.after is not None:
            result['After'] = self.after

        if self.before is not None:
            result['Before'] = self.before

        if self.config_key is not None:
            result['ConfigKey'] = self.config_key

        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('After') is not None:
            self.after = m.get('After')

        if m.get('Before') is not None:
            self.before = m.get('Before')

        if m.get('ConfigKey') is not None:
            self.config_key = m.get('ConfigKey')

        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        return self

class DescribeConfigHistoryResponseBodyDataConfigHistoryEffectDetails(DaraModel):
    def __init__(
        self,
        effect_status: str = None,
        node_group_id: str = None,
        node_id: str = None,
    ):
        self.effect_status = effect_status
        self.node_group_id = node_group_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effect_status is not None:
            result['EffectStatus'] = self.effect_status

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectStatus') is not None:
            self.effect_status = m.get('EffectStatus')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

