# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class CreateGadInstanceMemberResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.CreateGadInstanceMemberResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # An array that consists of the information returned.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.CreateGadInstanceMemberResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class CreateGadInstanceMemberResponseBodyResult(DaraModel):
    def __init__(
        self,
        create_count: str = None,
        gad_instance_name: str = None,
    ):
        # The number of unit nodes that are created by calling this operation.
        self.create_count = create_count
        # The ID of the global active database cluster.
        self.gad_instance_name = gad_instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_count is not None:
            result['CreateCount'] = self.create_count

        if self.gad_instance_name is not None:
            result['GadInstanceName'] = self.gad_instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCount') is not None:
            self.create_count = m.get('CreateCount')

        if m.get('GadInstanceName') is not None:
            self.gad_instance_name = m.get('GadInstanceName')

        return self

