# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeApplicationParametersRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        component_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.component_id_list = component_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.component_id_list is not None:
            result['ComponentIdList'] = self.component_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ComponentIdList') is not None:
            self.component_id_list = m.get('ComponentIdList')

        return self

