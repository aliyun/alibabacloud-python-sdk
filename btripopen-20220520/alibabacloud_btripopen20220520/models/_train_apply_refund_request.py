# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TrainApplyRefundRequest(DaraModel):
    def __init__(
        self,
        order_id: str = None,
        out_order_id: str = None,
        out_refund_id: str = None,
        refund_train_infos: List[main_models.TrainApplyRefundRequestRefundTrainInfos] = None,
    ):
        # This parameter is required.
        self.order_id = order_id
        # This parameter is required.
        self.out_order_id = out_order_id
        # This parameter is required.
        self.out_refund_id = out_refund_id
        # This parameter is required.
        self.refund_train_infos = refund_train_infos

    def validate(self):
        if self.refund_train_infos:
            for v1 in self.refund_train_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.out_refund_id is not None:
            result['out_refund_id'] = self.out_refund_id

        result['refund_train_infos'] = []
        if self.refund_train_infos is not None:
            for k1 in self.refund_train_infos:
                result['refund_train_infos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('out_refund_id') is not None:
            self.out_refund_id = m.get('out_refund_id')

        self.refund_train_infos = []
        if m.get('refund_train_infos') is not None:
            for k1 in m.get('refund_train_infos'):
                temp_model = main_models.TrainApplyRefundRequestRefundTrainInfos()
                self.refund_train_infos.append(temp_model.from_map(k1))

        return self

class TrainApplyRefundRequestRefundTrainInfos(DaraModel):
    def __init__(
        self,
        dep_time: str = None,
        refund_passenger_infos: List[main_models.TrainApplyRefundRequestRefundTrainInfosRefundPassengerInfos] = None,
        train_no: str = None,
    ):
        # This parameter is required.
        self.dep_time = dep_time
        # This parameter is required.
        self.refund_passenger_infos = refund_passenger_infos
        # This parameter is required.
        self.train_no = train_no

    def validate(self):
        if self.refund_passenger_infos:
            for v1 in self.refund_passenger_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        result['refund_passenger_infos'] = []
        if self.refund_passenger_infos is not None:
            for k1 in self.refund_passenger_infos:
                result['refund_passenger_infos'].append(k1.to_map() if k1 else None)

        if self.train_no is not None:
            result['train_no'] = self.train_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        self.refund_passenger_infos = []
        if m.get('refund_passenger_infos') is not None:
            for k1 in m.get('refund_passenger_infos'):
                temp_model = main_models.TrainApplyRefundRequestRefundTrainInfosRefundPassengerInfos()
                self.refund_passenger_infos.append(temp_model.from_map(k1))

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        return self

class TrainApplyRefundRequestRefundTrainInfosRefundPassengerInfos(DaraModel):
    def __init__(
        self,
        passenger_cert_no: str = None,
        passenger_cert_type: str = None,
        passenger_id: str = None,
        passenger_name: str = None,
    ):
        # This parameter is required.
        self.passenger_cert_no = passenger_cert_no
        # This parameter is required.
        self.passenger_cert_type = passenger_cert_type
        # This parameter is required.
        self.passenger_id = passenger_id
        # This parameter is required.
        self.passenger_name = passenger_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_cert_no is not None:
            result['passenger_cert_no'] = self.passenger_cert_no

        if self.passenger_cert_type is not None:
            result['passenger_cert_type'] = self.passenger_cert_type

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_cert_no') is not None:
            self.passenger_cert_no = m.get('passenger_cert_no')

        if m.get('passenger_cert_type') is not None:
            self.passenger_cert_type = m.get('passenger_cert_type')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        return self

