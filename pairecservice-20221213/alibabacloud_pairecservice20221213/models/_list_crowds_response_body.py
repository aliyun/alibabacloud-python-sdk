# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListCrowdsResponseBody(DaraModel):
    def __init__(
        self,
        crowds: List[main_models.ListCrowdsResponseBodyCrowds] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.crowds = crowds
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.crowds:
            for v1 in self.crowds:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Crowds'] = []
        if self.crowds is not None:
            for k1 in self.crowds:
                result['Crowds'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.crowds = []
        if m.get('Crowds') is not None:
            for k1 in m.get('Crowds'):
                temp_model = main_models.ListCrowdsResponseBodyCrowds()
                self.crowds.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCrowdsResponseBodyCrowds(DaraModel):
    def __init__(
        self,
        crowd_id: str = None,
        description: str = None,
        gmt_create_time: str = None,
        label: str = None,
        name: str = None,
        quantity: str = None,
        source: str = None,
        users: str = None,
    ):
        self.crowd_id = crowd_id
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.label = label
        self.name = name
        self.quantity = quantity
        self.source = source
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crowd_id is not None:
            result['CrowdId'] = self.crowd_id

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.source is not None:
            result['Source'] = self.source

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrowdId') is not None:
            self.crowd_id = m.get('CrowdId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

