# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class AddUnknownThreatDetectProcessResponseBody(DaraModel):
    def __init__(
        self,
        id_list: List[main_models.AddUnknownThreatDetectProcessResponseBodyIdList] = None,
        request_id: str = None,
    ):
        # A list of results for the added processes.
        self.id_list = id_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.id_list:
            for v1 in self.id_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IdList'] = []
        if self.id_list is not None:
            for k1 in self.id_list:
                result['IdList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.id_list = []
        if m.get('IdList') is not None:
            for k1 in m.get('IdList'):
                temp_model = main_models.AddUnknownThreatDetectProcessResponseBodyIdList()
                self.id_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AddUnknownThreatDetectProcessResponseBodyIdList(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The ID generated for the added process.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

