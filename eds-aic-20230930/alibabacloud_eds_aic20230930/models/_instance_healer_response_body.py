# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class InstanceHealerResponseBody(DaraModel):
    def __init__(
        self,
        instance_healer_model: main_models.InstanceHealerResponseBodyInstanceHealerModel = None,
        request_id: str = None,
    ):
        self.instance_healer_model = instance_healer_model
        self.request_id = request_id

    def validate(self):
        if self.instance_healer_model:
            self.instance_healer_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_healer_model is not None:
            result['InstanceHealerModel'] = self.instance_healer_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceHealerModel') is not None:
            temp_model = main_models.InstanceHealerResponseBodyInstanceHealerModel()
            self.instance_healer_model = temp_model.from_map(m.get('InstanceHealerModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class InstanceHealerResponseBodyInstanceHealerModel(DaraModel):
    def __init__(
        self,
        result: str = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

