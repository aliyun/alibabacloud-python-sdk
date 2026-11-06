# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationAvailableVersionRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_type: str = None,
        components: List[main_models.DescribeApplicationAvailableVersionRequestComponents] = None,
        region_id: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The application type.
        self.application_type = application_type
        # The list of application subcomponents.
        self.components = components
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.DescribeApplicationAvailableVersionRequestComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class DescribeApplicationAvailableVersionRequestComponents(DaraModel):
    def __init__(
        self,
        component_class: str = None,
        component_max_replica: int = None,
        component_replica: int = None,
        component_type: str = None,
    ):
        # The specifications of the application subcomponent.
        self.component_class = component_class
        # The maximum number of application subcomponents of the same specifications. Default value: the value of ComponentReplica. This parameter is supported only for raycluster applications.
        self.component_max_replica = component_max_replica
        # The number of replicas for the application subcomponent. Default value: 1.
        self.component_replica = component_replica
        # The type of the application subcomponent.
        self.component_type = component_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_class is not None:
            result['ComponentClass'] = self.component_class

        if self.component_max_replica is not None:
            result['ComponentMaxReplica'] = self.component_max_replica

        if self.component_replica is not None:
            result['ComponentReplica'] = self.component_replica

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentClass') is not None:
            self.component_class = m.get('ComponentClass')

        if m.get('ComponentMaxReplica') is not None:
            self.component_max_replica = m.get('ComponentMaxReplica')

        if m.get('ComponentReplica') is not None:
            self.component_replica = m.get('ComponentReplica')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        return self

