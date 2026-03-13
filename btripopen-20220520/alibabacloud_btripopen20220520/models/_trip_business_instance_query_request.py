# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TripBusinessInstanceQueryRequest(DaraModel):
    def __init__(
        self,
        business_instance_id: str = None,
        third_business_id: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.business_instance_id = business_instance_id
        self.third_business_id = third_business_id
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_instance_id is not None:
            result['business_instance_id'] = self.business_instance_id

        if self.third_business_id is not None:
            result['third_business_id'] = self.third_business_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_name is not None:
            result['user_name'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('business_instance_id') is not None:
            self.business_instance_id = m.get('business_instance_id')

        if m.get('third_business_id') is not None:
            self.third_business_id = m.get('third_business_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')

        return self

