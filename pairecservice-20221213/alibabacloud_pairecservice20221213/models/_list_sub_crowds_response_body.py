# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListSubCrowdsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sub_crowds: List[main_models.ListSubCrowdsResponseBodySubCrowds] = None,
        total_count: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.sub_crowds = sub_crowds
        self.total_count = total_count

    def validate(self):
        if self.sub_crowds:
            for v1 in self.sub_crowds:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SubCrowds'] = []
        if self.sub_crowds is not None:
            for k1 in self.sub_crowds:
                result['SubCrowds'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sub_crowds = []
        if m.get('SubCrowds') is not None:
            for k1 in m.get('SubCrowds'):
                temp_model = main_models.ListSubCrowdsResponseBodySubCrowds()
                self.sub_crowds.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSubCrowdsResponseBodySubCrowds(DaraModel):
    def __init__(
        self,
        gmt_create_time: str = None,
        quantity: int = None,
        source: str = None,
        sub_crowd_id: str = None,
        users: str = None,
    ):
        self.gmt_create_time = gmt_create_time
        self.quantity = quantity
        self.source = source
        self.sub_crowd_id = sub_crowd_id
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.source is not None:
            result['Source'] = self.source

        if self.sub_crowd_id is not None:
            result['SubCrowdId'] = self.sub_crowd_id

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SubCrowdId') is not None:
            self.sub_crowd_id = m.get('SubCrowdId')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

