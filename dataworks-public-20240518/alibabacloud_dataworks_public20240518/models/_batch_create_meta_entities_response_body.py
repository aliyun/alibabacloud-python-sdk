# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class BatchCreateMetaEntitiesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.MetaEntityWriteResult] = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # A list of results for the batch creation operation. This list provides the success status and any error messages for each individual entity in the request.
        self.results = results
        # Indicates whether the request was successful. This parameter returns `true` even if creating some entities fails. To determine the outcome for each entity, check the `Success` and `ErrorMessage` fields in the `Results` array.
        self.success = success

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.MetaEntityWriteResult()
                self.results.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

