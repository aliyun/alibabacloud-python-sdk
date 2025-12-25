# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_foasconsole20190601 import models as main_models
from darabonba.model import DaraModel

class ConvertPrepayInstanceRequest(DaraModel):
    def __init__(
        self,
        convert_prepay_instance_request: main_models.ConvertPrepayInstanceRequestConvertPrepayInstanceRequest = None,
    ):
        # This parameter is required.
        self.convert_prepay_instance_request = convert_prepay_instance_request

    def validate(self):
        if self.convert_prepay_instance_request:
            self.convert_prepay_instance_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.convert_prepay_instance_request is not None:
            result['ConvertPrepayInstanceRequest'] = self.convert_prepay_instance_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConvertPrepayInstanceRequest') is not None:
            temp_model = main_models.ConvertPrepayInstanceRequestConvertPrepayInstanceRequest()
            self.convert_prepay_instance_request = temp_model.from_map(m.get('ConvertPrepayInstanceRequest'))

        return self

class ConvertPrepayInstanceRequestConvertPrepayInstanceRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

