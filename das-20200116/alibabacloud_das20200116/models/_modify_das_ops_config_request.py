# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class ModifyDasOpsConfigRequest(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        filters: List[main_models.ModifyDasOpsConfigRequestFilters] = None,
        instance_id: str = None,
    ):
        # Specifies whether to enable DAS Alibaba Cloud Managed Services. Valid values:
        # 
        # - **true**: Enable.
        # - **false**: Disable. Shutdown only turns off the feature but does not unsubscribe from the service. To unsubscribe, go to the unsubscription management page.
        self.enable = enable
        # A reserved parameter.
        self.filters = filters
        # The database instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.ModifyDasOpsConfigRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class ModifyDasOpsConfigRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The filter parameter.
        # 
        # > For supported filter parameters and their values, see **Supplementary description of request parameters**.
        self.key = key
        # A reserved parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

