# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class ModifyApplicationServerlessConfRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        serverless_conf_list: List[main_models.ModifyApplicationServerlessConfRequestServerlessConfList] = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # The list of Serverless configurations.
        # 
        # This parameter is required.
        self.serverless_conf_list = serverless_conf_list

    def validate(self):
        if self.serverless_conf_list:
            for v1 in self.serverless_conf_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        result['ServerlessConfList'] = []
        if self.serverless_conf_list is not None:
            for k1 in self.serverless_conf_list:
                result['ServerlessConfList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        self.serverless_conf_list = []
        if m.get('ServerlessConfList') is not None:
            for k1 in m.get('ServerlessConfList'):
                temp_model = main_models.ModifyApplicationServerlessConfRequestServerlessConfList()
                self.serverless_conf_list.append(temp_model.from_map(k1))

        return self

class ModifyApplicationServerlessConfRequestServerlessConfList(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        scale_max: str = None,
        scale_min: str = None,
    ):
        # The type of the application sub-component.
        # 
        # For Supabase, valid values are:
        # 
        # - gateway
        # 
        # - backend
        self.component_type = component_type
        # The maximum number of PCUs for a single node. Valid values: 0 to 16.
        self.scale_max = scale_max
        # The minimum number of PolarDB Capacity Units (PCUs) for a single node. Valid values: 0 to 16.
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

