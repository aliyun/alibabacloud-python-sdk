# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationServerlessConfResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        request_id: str = None,
        serverless_conf_items: List[main_models.DescribeApplicationServerlessConfResponseBodyServerlessConfItems] = None,
    ):
        self.application_id = application_id
        self.request_id = request_id
        self.serverless_conf_items = serverless_conf_items

    def validate(self):
        if self.serverless_conf_items:
            for v1 in self.serverless_conf_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ServerlessConfItems'] = []
        if self.serverless_conf_items is not None:
            for k1 in self.serverless_conf_items:
                result['ServerlessConfItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.serverless_conf_items = []
        if m.get('ServerlessConfItems') is not None:
            for k1 in m.get('ServerlessConfItems'):
                temp_model = main_models.DescribeApplicationServerlessConfResponseBodyServerlessConfItems()
                self.serverless_conf_items.append(temp_model.from_map(k1))

        return self

class DescribeApplicationServerlessConfResponseBodyServerlessConfItems(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        scale_max: str = None,
        scale_min: str = None,
    ):
        self.component_type = component_type
        self.scale_max = scale_max
        self.scale_min = scale_min

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.scale_max is not None:
            result['ScaleMax'] = self.scale_max

        if self.scale_min is not None:
            result['ScaleMin'] = self.scale_min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('ScaleMax') is not None:
            self.scale_max = m.get('ScaleMax')

        if m.get('ScaleMin') is not None:
            self.scale_min = m.get('ScaleMin')

        return self

