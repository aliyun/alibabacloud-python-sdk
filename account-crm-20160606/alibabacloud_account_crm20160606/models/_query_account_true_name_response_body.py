# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_account_crm20160606 import models as main_models
from darabonba.model import DaraModel

class QueryAccountTrueNameResponseBody(DaraModel):
    def __init__(
        self,
        profile_info: main_models.QueryAccountTrueNameResponseBodyProfileInfo = None,
        request_id: str = None,
    ):
        self.profile_info = profile_info
        self.request_id = request_id

    def validate(self):
        if self.profile_info:
            self.profile_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.profile_info is not None:
            result['ProfileInfo'] = self.profile_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProfileInfo') is not None:
            temp_model = main_models.QueryAccountTrueNameResponseBodyProfileInfo()
            self.profile_info = temp_model.from_map(m.get('ProfileInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryAccountTrueNameResponseBodyProfileInfo(DaraModel):
    def __init__(
        self,
        true_name: str = None,
    ):
        self.true_name = true_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.true_name is not None:
            result['TrueName'] = self.true_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrueName') is not None:
            self.true_name = m.get('TrueName')

        return self

