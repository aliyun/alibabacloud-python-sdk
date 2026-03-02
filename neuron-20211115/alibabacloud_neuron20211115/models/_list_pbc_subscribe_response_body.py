# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class ListPbcSubscribeResponseBody(DaraModel):
    def __init__(
        self,
        pbc_list_result: main_models.PbcListResult = None,
        request_id: str = None,
    ):
        self.pbc_list_result = pbc_list_result
        self.request_id = request_id

    def validate(self):
        if self.pbc_list_result:
            self.pbc_list_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pbc_list_result is not None:
            result['pbcListResult'] = self.pbc_list_result.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pbcListResult') is not None:
            temp_model = main_models.PbcListResult()
            self.pbc_list_result = temp_model.from_map(m.get('pbcListResult'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

